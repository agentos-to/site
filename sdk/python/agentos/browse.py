"""Reverse-engineering helper: drive a real Brave tab via CDP.

**Authoring-time only.** Use this to walk through a service's login
or any multi-step flow once, capture the real HTTP sequence, then
replay it in your skill with ``agentos.client``. The shipped skill
must never import ``agentos.browse`` — at runtime, all I/O goes
through ``agentos.client``.

Prereqs:
    # Launch Brave with CDP on port 9222 (or any port you pass)
    open -a 'Brave Browser' --args --remote-debugging-port=9222

Typical use:

    import asyncio
    from agentos.browse import Session

    async def main():
        async with Session.launch() as b:
            await b.clear_cookies()
            await b.goto("https://www.amazon.com/")
            await b.click("#nav-link-accountList")
            await b.fill("#ap_email", "joe@example.com")
            await b.click("#continue")
            await b.fill("#ap_password", "...")
            await b.click("#signInSubmit")
            # inspect state
            print(await b.url())
            # dump captured network
            b.save_network_log("/tmp/amazon_capture.json")
            # pull cookies for replay
            cookies = await b.cookies_for(".amazon.com")

    asyncio.run(main())

The session opens a new tab you can see in Brave (not headless,
not a hidden target), drives it step-by-step with live stderr
progress, and records every HTTP request/response for later
analysis. When the block exits, the tab is closed.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
import time
import urllib.request

try:
    import websocket  # type: ignore
except ImportError as e:  # pragma: no cover
    raise ImportError(
        "agentos.browse requires `websocket-client`. Install with: "
        "pip install websocket-client"
    ) from e


__all__ = ["Session"]


# ---------------------------------------------------------------------------
# CDP endpoint discovery
# ---------------------------------------------------------------------------


def _browser_ws(port: int) -> str:
    """Return the browser-level CDP WebSocket URL for a given port."""
    data = json.loads(
        urllib.request.urlopen(
            f"http://127.0.0.1:{port}/json/version", timeout=3
        ).read()
    )
    return data["webSocketDebuggerUrl"]


def _open_tab(port: int, url: str = "about:blank") -> tuple[str, str]:
    """Create a new tab via Target.createTarget. Returns (target_id, ws_url)."""
    browser_ws = _browser_ws(port)
    ws = websocket.create_connection(browser_ws, timeout=10)
    target_id = None
    try:
        ws.send(
            json.dumps(
                {"id": 1, "method": "Target.createTarget", "params": {"url": url}}
            )
        )
        deadline = time.time() + 10
        while time.time() < deadline:
            msg = json.loads(ws.recv())
            if msg.get("id") == 1:
                target_id = msg["result"]["targetId"]
                break
    finally:
        ws.close()

    if not target_id:
        raise RuntimeError("Target.createTarget returned no target id")

    # Look up the page-level WS for the new tab
    time.sleep(0.3)
    tabs = json.loads(
        urllib.request.urlopen(f"http://127.0.0.1:{port}/json", timeout=3).read()
    )
    for t in tabs:
        if t.get("id") == target_id:
            return target_id, t["webSocketDebuggerUrl"]
    raise RuntimeError(f"new tab {target_id} not found in /json")


def _close_tab(port: int, target_id: str) -> None:
    """Close a tab via the browser-level WS."""
    try:
        browser_ws = _browser_ws(port)
        ws = websocket.create_connection(browser_ws, timeout=5)
        try:
            ws.send(
                json.dumps(
                    {
                        "id": 1,
                        "method": "Target.closeTarget",
                        "params": {"targetId": target_id},
                    }
                )
            )
        finally:
            ws.close()
    except Exception as e:
        print(f"  [warn] failed to close tab {target_id[:8]}: {e}", file=sys.stderr)


# ---------------------------------------------------------------------------
# Session
# ---------------------------------------------------------------------------


def _log(step: str, msg: str = "") -> None:
    """Live progress marker. Unbuffered so tail -f sees it."""
    line = f"  [browse] {step}" + (f"  {msg}" if msg else "")
    print(line, file=sys.stderr, flush=True)


class Session:
    """A live Brave tab driven via CDP. Records every HTTP event.

    Use ``Session.launch(...)`` to open a fresh tab and ``await
    session.close()`` when done, or use ``async with`` for auto-cleanup.
    """

    def __init__(self, port: int, target_id: str, ws_url: str):
        self.port = port
        self.target_id = target_id
        self.ws = websocket.create_connection(ws_url, timeout=30)
        self._msg_id = 0
        self._events: list[dict] = []
        self._closed = False

    # ---- Lifecycle -------------------------------------------------------

    @classmethod
    async def launch(cls, *, port: int = 9222, url: str = "about:blank") -> "Session":
        """Open a new visible tab in Brave. Returns the Session.

        Brave must be running with ``--remote-debugging-port=<port>``.
        The tab is foregrounded so you can watch the automation run.
        """
        target_id, ws_url = _open_tab(port, url)
        s = cls(port, target_id, ws_url)
        await s._enable_domains()
        # Bring the tab to the front so the user can see it
        try:
            await s._cdp("Page.bringToFront")
        except Exception:
            pass
        _log("launch", f"tab={target_id[:8]} url={url}")
        return s

    async def __aenter__(self) -> "Session":
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.close()

    async def close(self) -> None:
        if self._closed:
            return
        self._closed = True
        try:
            self.ws.close()
        except Exception:
            pass
        _close_tab(self.port, self.target_id)
        _log("close", f"tab={self.target_id[:8]}")

    # ---- CDP primitives --------------------------------------------------

    async def _cdp(self, method: str, params: dict | None = None, timeout: float = 15.0) -> dict:
        """Send a CDP command, return the response. Collects events along the way."""
        self._msg_id += 1
        mid = self._msg_id
        msg = {"id": mid, "method": method}
        if params:
            msg["params"] = params

        # The websocket-client API is sync; run the send+recv loop in a
        # thread executor so asyncio consumers don't block the event loop.
        def _blocking() -> dict:
            self.ws.send(json.dumps(msg))
            deadline = time.time() + timeout
            while time.time() < deadline:
                try:
                    raw = self.ws.recv()
                except Exception:
                    continue
                if not raw:
                    continue
                m = json.loads(raw)
                if m.get("id") == mid:
                    return m
                if "method" in m:
                    self._events.append(m)
            raise TimeoutError(f"Timeout on CDP {method} (id={mid})")

        return await asyncio.get_event_loop().run_in_executor(None, _blocking)

    async def _enable_domains(self) -> None:
        await self._cdp("Network.enable")
        await self._cdp("Page.enable")
        await self._cdp("Runtime.enable")

    async def _wait_for_load(self, timeout: float = 20.0) -> bool:
        """Drain events until Page.loadEventFired."""
        def _blocking() -> bool:
            deadline = time.time() + timeout
            while time.time() < deadline:
                try:
                    raw = self.ws.recv()
                except Exception:
                    continue
                if not raw:
                    continue
                m = json.loads(raw)
                if "method" in m:
                    self._events.append(m)
                    if m["method"] == "Page.loadEventFired":
                        return True
            return False

        return await asyncio.get_event_loop().run_in_executor(None, _blocking)

    # ---- Navigation ------------------------------------------------------

    async def goto(self, url: str, *, wait: bool = True) -> None:
        """Navigate the tab to ``url``. Waits for the load event by default."""
        _log("goto", url)
        await self._cdp("Page.navigate", {"url": url})
        if wait:
            loaded = await self._wait_for_load()
            _log("goto", f"{'loaded' if loaded else 'timeout'}")

    async def url(self) -> str:
        """Current ``location.href``."""
        r = await self._cdp(
            "Runtime.evaluate",
            {"expression": "location.href", "returnByValue": True},
        )
        return r.get("result", {}).get("result", {}).get("value", "")

    async def html(self) -> str:
        """Full ``document.documentElement.outerHTML``."""
        r = await self._cdp(
            "Runtime.evaluate",
            {
                "expression": "document.documentElement.outerHTML",
                "returnByValue": True,
            },
        )
        return r.get("result", {}).get("result", {}).get("value", "")

    async def eval(self, expression: str) -> object:
        """Evaluate a JS expression and return ``result.value``.

        The expression must be a single expression (use an IIFE for
        multi-statement code). Values are returned via ``returnByValue``,
        so only JSON-serialisable shapes come back.
        """
        r = await self._cdp(
            "Runtime.evaluate",
            {"expression": expression, "returnByValue": True},
        )
        return r.get("result", {}).get("result", {}).get("value")

    # ---- DOM actions -----------------------------------------------------

    async def fill(self, selector: str, value: str) -> None:
        """Set an input's value and fire the ``input`` event.

        Handles ``<input>``, ``<textarea>``, and contenteditable. The
        ``input`` event is fired so frameworks (React, etc.) pick up
        the change.
        """
        _log("fill", selector)
        js = f"""
            (() => {{
                const el = document.querySelector({json.dumps(selector)});
                if (!el) return 'not-found';
                const setter = Object.getOwnPropertyDescriptor(
                    el.__proto__, 'value'
                ) && Object.getOwnPropertyDescriptor(el.__proto__, 'value').set;
                if (setter) setter.call(el, {json.dumps(value)});
                else el.value = {json.dumps(value)};
                el.dispatchEvent(new Event('input', {{bubbles: true}}));
                el.dispatchEvent(new Event('change', {{bubbles: true}}));
                return 'ok';
            }})()
        """
        result = await self.eval(js)
        if result != "ok":
            raise RuntimeError(f"fill({selector!r}): element {result}")

    async def click(self, selector: str, *, wait_for_load: bool = True) -> None:
        """Click an element. Waits for page load by default (forms submit)."""
        _log("click", selector)
        js = f"""
            (() => {{
                const el = document.querySelector({json.dumps(selector)});
                if (!el) return 'not-found';
                el.click();
                return 'ok';
            }})()
        """
        result = await self.eval(js)
        if result != "ok":
            raise RuntimeError(f"click({selector!r}): element {result}")
        if wait_for_load:
            loaded = await self._wait_for_load()
            _log("click", f"{'loaded' if loaded else 'timeout'}")

    async def exists(self, selector: str) -> bool:
        """``True`` if a selector matches any element."""
        return bool(await self.eval(
            f"!!document.querySelector({json.dumps(selector)})"
        ))

    async def text(self, selector: str) -> str:
        """Return ``element.innerText`` or empty string if not found."""
        js = f"""
            (() => {{
                const el = document.querySelector({json.dumps(selector)});
                return el ? el.innerText : '';
            }})()
        """
        return str(await self.eval(js) or "")

    # ---- Cookies ---------------------------------------------------------

    async def clear_cookies(self) -> None:
        """Wipe all browser cookies."""
        _log("clear_cookies")
        await self._cdp("Network.clearBrowserCookies")

    async def cookies_for(self, domain: str) -> list[dict]:
        """Return all cookies where ``cookie.domain`` contains ``domain``.

        Cookies are raw CDP cookie records — ``name``, ``value``,
        ``domain``, ``path``, ``expires``, etc. Useful for inspecting
        the session post-login.
        """
        r = await self._cdp("Network.getAllCookies")
        cookies = r.get("result", {}).get("cookies", [])
        dom = domain.lstrip(".").lower()
        return [
            c for c in cookies
            if dom in (c.get("domain") or "").lower()
        ]

    # ---- Network log -----------------------------------------------------

    def network_log(self, *, domain: str | None = None) -> list[dict]:
        """Return captured network events, optionally filtered by host.

        Each event is a raw CDP ``Network.*`` message. The useful ones:

        * ``Network.requestWillBeSent`` — outbound request. ``params.request``
          has ``url``, ``method``, ``headers``, ``postData``.
        * ``Network.responseReceived`` — inbound response. ``params.response``
          has ``status``, ``url``, ``headers`` (lower-cased).

        When ``domain`` is passed, only events whose URL contains it
        are returned. Handy for trimming noise.
        """
        events = [e for e in self._events if e.get("method", "").startswith("Network.")]
        if domain:
            dom = domain.lstrip(".").lower()
            def _has_dom(e: dict) -> bool:
                p = e.get("params", {})
                url = (p.get("request") or p.get("response") or {}).get("url", "")
                return dom in url.lower()
            events = [e for e in events if _has_dom(e)]
        return events

    def save_network_log(self, path: str, *, domain: str | None = None) -> None:
        """Dump the network log to a JSON file for offline analysis."""
        events = self.network_log(domain=domain)
        with open(path, "w") as f:
            json.dump(events, f, indent=2)
        _log("save_network_log", f"{len(events)} events → {path}")
