#!/usr/bin/env python3
"""Gate test for docs-site/dist.

Launches headless Brave against file://dist/index.html, clicks through several
internal links, and fails the run if there are any console errors or network
failures. Uses a throwaway --user-data-dir so the user's real Brave profile is
untouched. Kills the Brave PID on exit.

Usage:  python3 scripts/verify.py
"""
from __future__ import annotations

import asyncio
import json
import os
import re
import signal
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from urllib.request import urlopen

import websockets

BRAVE = "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
HERE = Path(__file__).resolve().parent
DIST = HERE.parent / "dist"
INDEX = DIST / "index.html"
CDP_PORT = 9335  # matches the prototype's port
PAGE_TIMEOUT_S = 6
CLICK_PAGES = 3  # number of internal pages to click through


def start_brave() -> tuple[subprocess.Popen, str, str]:
    if not INDEX.exists():
        sys.exit(f"FAIL: {INDEX} does not exist. Run `pnpm build` first.")
    profile = tempfile.mkdtemp(prefix="brave-docs-verify-")
    stderr_path = Path(profile) / "brave.stderr.log"
    stderr_fh = open(stderr_path, "wb")
    args = [
        BRAVE,
        "--headless=new",
        f"--remote-debugging-port={CDP_PORT}",
        f"--user-data-dir={profile}",
        "--no-first-run",
        "--no-default-browser-check",
        "--disable-features=BraveRewards,BraveWallet,BraveVPN",
        f"file://{INDEX}",
    ]
    proc = subprocess.Popen(args, stdout=subprocess.DEVNULL, stderr=stderr_fh)
    # Poll /json/version until Brave is up
    for _ in range(40):
        try:
            with urlopen(f"http://127.0.0.1:{CDP_PORT}/json/version", timeout=0.25) as r:
                data = json.loads(r.read())
                return proc, data["webSocketDebuggerUrl"], profile
        except Exception:
            time.sleep(0.1)
    proc.terminate()
    sys.exit(f"FAIL: Brave did not expose CDP on port {CDP_PORT} within 4s")


async def open_target(ws, target_type="page"):
    """Attach to the first page target; return a session-wrapped call()."""
    targets = await ws_call(ws, "Target.getTargets")
    page = next(t for t in targets["targetInfos"] if t["type"] == target_type)
    sess = await ws_call(ws, "Target.attachToTarget", {"targetId": page["targetId"], "flatten": True})
    return sess["sessionId"]


_msg_id = 0


async def ws_call(ws, method, params=None, session_id=None):
    global _msg_id
    _msg_id += 1
    mid = _msg_id
    msg = {"id": mid, "method": method, "params": params or {}}
    if session_id:
        msg["sessionId"] = session_id
    await ws.send(json.dumps(msg))
    while True:
        raw = await ws.recv()
        m = json.loads(raw)
        if m.get("id") == mid:
            if "error" in m:
                raise RuntimeError(f"CDP error on {method}: {m['error']}")
            return m.get("result", {})
        # Drop unrelated events at setup time.


class Collector:
    def __init__(self):
        self.console = []
        self.network_fail = []
        self.req_urls = {}  # requestId -> url

    def handle(self, msg):
        m = msg.get("method")
        p = msg.get("params", {})
        if m == "Runtime.consoleAPICalled":
            args = [a.get("value") or a.get("description") for a in p.get("args", [])]
            self.console.append({"level": p.get("type"), "text": " ".join(str(a) for a in args)})
        elif m == "Log.entryAdded":
            e = p.get("entry", {})
            self.console.append(
                {"level": e.get("level"), "text": e.get("text"), "src": e.get("source"), "url": e.get("url")}
            )
        elif m == "Runtime.exceptionThrown":
            ex = p.get("exceptionDetails", {})
            self.console.append({"level": "exception", "text": ex.get("text"), "url": ex.get("url")})
        elif m == "Network.requestWillBeSent":
            self.req_urls[p.get("requestId")] = p.get("request", {}).get("url")
        elif m == "Network.loadingFailed":
            self.network_fail.append(
                {"url": self.req_urls.get(p.get("requestId")), "error": p.get("errorText"), "type": p.get("type")}
            )


async def pump(ws, collector: Collector, seconds: float, session_id: str):
    end = asyncio.get_event_loop().time() + seconds
    while asyncio.get_event_loop().time() < end:
        try:
            raw = await asyncio.wait_for(ws.recv(), timeout=0.25)
        except asyncio.TimeoutError:
            continue
        m = json.loads(raw)
        if m.get("sessionId") == session_id:
            collector.handle(m)


async def navigate(ws, session_id, url, collector: Collector):
    await ws_call(ws, "Page.navigate", {"url": url}, session_id)
    await pump(ws, collector, PAGE_TIMEOUT_S, session_id)


async def internal_links(ws, session_id) -> list[str]:
    res = await ws_call(
        ws,
        "Runtime.evaluate",
        {
            "expression": (
                "Array.from(document.querySelectorAll('a[href]'))"
                ".map(a => a.href)"
                ".filter(h => h.startsWith('file://') && !h.includes('#') && !h.endsWith(location.pathname))"
            ),
            "returnByValue": True,
        },
        session_id,
    )
    links = res.get("result", {}).get("value", []) or []
    # Dedupe while preserving order, strip self-refs
    seen = set()
    out = []
    for l in links:
        if l in seen:
            continue
        seen.add(l)
        out.append(l)
    return out


def summarize(label: str, collector: Collector):
    errs = [c for c in collector.console if c.get("level") in ("error", "exception", "severe")]
    print(f"--- {label}: {len(collector.network_fail)} net-fail, {len(errs)} console-err")
    for f in collector.network_fail:
        print("  NET-FAIL:", f)
    for e in errs:
        print("  CONSOLE:", e)
    return errs


async def run():
    proc, ws_url, profile = start_brave()
    print(f"[verify] Brave up on port {CDP_PORT}, profile={profile}, pid={proc.pid}")
    exit_code = 0
    try:
        async with websockets.connect(ws_url, max_size=20_000_000) as ws:
            session_id = await open_target(ws)
            for m in ("Page.enable", "Runtime.enable", "Network.enable", "Log.enable"):
                await ws_call(ws, m, session_id=session_id)

            # Visit 1: landing
            landing = Collector()
            await navigate(ws, session_id, f"file://{INDEX}", landing)
            errs = summarize("landing", landing)
            if errs or landing.network_fail:
                exit_code = 2

            # Collect internal links from landing
            links = await internal_links(ws, session_id)
            print(f"[verify] {len(links)} internal links from landing")
            for l in links[:10]:
                print("   ·", l)

            if len(links) < CLICK_PAGES:
                print(f"FAIL: expected at least {CLICK_PAGES} internal links, got {len(links)}")
                exit_code = 3

            # Visit CLICK_PAGES more pages
            for i, target in enumerate(links[:CLICK_PAGES]):
                c = Collector()
                await navigate(ws, session_id, target, c)
                errs = summarize(f"page{i + 1} {target}", c)
                if errs or c.network_fail:
                    exit_code = 2
    finally:
        try:
            proc.send_signal(signal.SIGTERM)
            proc.wait(timeout=5)
        except Exception:
            proc.kill()
        print(f"[verify] Brave pid {proc.pid} stopped")

    if exit_code == 0:
        print("\nPASS — docs-site/dist renders cleanly from file://")
    else:
        print(f"\nFAIL — exit {exit_code}")
    sys.exit(exit_code)


if __name__ == "__main__":
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        sys.exit(130)
