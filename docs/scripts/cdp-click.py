#!/usr/bin/env python3
"""Navigate to a file:// page, click an internal doc link, check the new page loads."""
import asyncio, json, sys
import websockets

async def main(url, ws_url):
    msg_id = 0
    console, network_fail, request_urls = [], [], []

    async with websockets.connect(ws_url, max_size=10_000_000) as ws:
        async def call(method, params=None, wait=False):
            nonlocal msg_id
            msg_id += 1; mid = msg_id
            await ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
            if wait:
                while True:
                    msg = json.loads(await ws.recv())
                    if msg.get("id") == mid: return msg.get("result", {})
                    _handle(msg)

        def _handle(msg):
            m = msg.get("method"); p = msg.get("params", {})
            if m == "Runtime.consoleAPICalled":
                args = [a.get("value") or a.get("description") for a in p.get("args", [])]
                console.append({"level": p.get("type"), "text": " ".join(str(a) for a in args)})
            elif m == "Log.entryAdded":
                e = p.get("entry", {})
                console.append({"level": e.get("level"), "text": e.get("text"), "src": e.get("source")})
            elif m == "Runtime.exceptionThrown":
                ex = p.get("exceptionDetails", {})
                console.append({"level": "exception", "text": ex.get("text")})
            elif m == "Network.loadingFailed":
                network_fail.append({"requestId": p.get("requestId"), "error": p.get("errorText")})
            elif m == "Network.requestWillBeSent":
                request_urls.append(p.get("request", {}).get("url"))

        for m in ["Page.enable", "Runtime.enable", "Network.enable", "Log.enable"]:
            await call(m)
        await call("Page.navigate", {"url": url})

        # Wait for load
        end = asyncio.get_event_loop().time() + 5
        while asyncio.get_event_loop().time() < end:
            try: _handle(json.loads(await asyncio.wait_for(ws.recv(), 0.3)))
            except asyncio.TimeoutError: continue

        # Find all in-page anchors
        res = await call("Runtime.evaluate",
                         {"expression": "Array.from(document.querySelectorAll('a[href]')).map(a => a.href).filter(h => h.startsWith('file://') && !h.includes(location.pathname)).slice(0, 5)",
                          "returnByValue": True}, wait=True)
        links = res.get("result", {}).get("value", [])
        print("=== ANCHORS FOUND ===")
        for l in links: print(" ", l)

        if not links:
            print("FAIL: no internal file:// anchors found")
            sys.exit(3)

        # Click the first one via JS navigation (simulates user click)
        target = links[0]
        console.clear(); network_fail.clear(); request_urls.clear()
        print(f"\n=== NAVIGATING to {target} ===")
        await call("Page.navigate", {"url": target})

        end = asyncio.get_event_loop().time() + 5
        while asyncio.get_event_loop().time() < end:
            try: _handle(json.loads(await asyncio.wait_for(ws.recv(), 0.3)))
            except asyncio.TimeoutError: continue

        res = await call("Runtime.evaluate",
                         {"expression": "(document.title || 'NO-TITLE') + '||' + (document.body ? document.body.innerText.slice(0, 400) : 'NO-BODY')"},
                         wait=True)
        body = res.get("result", {}).get("result", {}).get("value", "")

        print("=== NETWORK FAILURES on 2nd page ===", len(network_fail))
        for f in network_fail: print(" ", f)
        print("=== CONSOLE (errors only) ===")
        errs = [c for c in console if c.get("level") in ("error", "exception")]
        for e in errs: print(" ", e)
        print("=== RENDERED ===")
        print(body[:600])

        if network_fail or errs:
            print("\nFAIL")
            sys.exit(2)
        print("\nPASS")

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
