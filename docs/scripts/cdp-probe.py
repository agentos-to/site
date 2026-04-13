#!/usr/bin/env python3
"""CDP console + network capture for a file:// page."""
import asyncio, json, sys
import websockets

async def main(url, ws_url):
    msg_id = 0
    console = []
    network_fail = []
    request_urls = []

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        async def call(method, params=None, wait_result=False):
            nonlocal msg_id
            msg_id += 1
            mid = msg_id
            await ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
            if wait_result:
                while True:
                    raw = await ws.recv()
                    msg = json.loads(raw)
                    if msg.get("id") == mid:
                        return msg.get("result", {})
                    # stash events as we wait
                    _handle(msg)
            return None

        def _handle(msg):
            m = msg.get("method"); p = msg.get("params", {})
            if m == "Runtime.consoleAPICalled":
                args = [a.get("value") or a.get("description") for a in p.get("args", [])]
                console.append({"level": p.get("type"), "text": " ".join(str(a) for a in args)})
            elif m == "Log.entryAdded":
                e = p.get("entry", {})
                console.append({"level": e.get("level"), "text": e.get("text"), "src": e.get("source"), "url": e.get("url")})
            elif m == "Runtime.exceptionThrown":
                ex = p.get("exceptionDetails", {})
                console.append({"level": "exception", "text": ex.get("text"), "url": ex.get("url")})
            elif m == "Network.loadingFailed":
                network_fail.append({"url": getattr(_handle, "_req_urls", {}).get(p.get("requestId")),
                                     "error": p.get("errorText"), "type": p.get("type")})
            elif m == "Network.requestWillBeSent":
                u = p.get("request", {}).get("url")
                request_urls.append(u)
                _handle.__dict__.setdefault("_req_urls", {})[p.get("requestId")] = u

        await call("Page.enable")
        await call("Runtime.enable")
        await call("Network.enable")
        await call("Log.enable")
        await call("Page.navigate", {"url": url})

        # Pump events for N seconds
        end_at = asyncio.get_event_loop().time() + 6
        while asyncio.get_event_loop().time() < end_at:
            try:
                raw = await asyncio.wait_for(ws.recv(), timeout=0.5)
                _handle(json.loads(raw))
            except asyncio.TimeoutError:
                continue

        res = await call("Runtime.evaluate",
                         {"expression": "document.title + '||' + (document.body ? document.body.innerText.slice(0, 600) : '[no body]')"},
                         wait_result=True)
        body_text = res.get("result", {}).get("value", "")

    print("=== URL ===", url)
    print("=== REQUESTS ===", len(request_urls))
    for u in request_urls[:8]:
        print("  ", u)
    print("=== NETWORK FAILURES ===", len(network_fail))
    for f in network_fail:
        print(" FAIL:", f)
    print("=== CONSOLE ===", len(console))
    for c in console:
        print(" ", c)
    print("=== RENDERED (title || body excerpt) ===")
    print(body_text[:800])

    errors = [c for c in console if c.get("level") in ("error", "exception")]
    if network_fail or errors:
        print(f"\nFAIL: {len(errors)} console errors, {len(network_fail)} network failures")
        sys.exit(2)
    print("\nPASS")

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
