---
title: "Reverse Engineering — Transport & Anti-Bot"
description: "How to get a response from a server that doesn't want to talk to you."
---

How to get a response from a server that doesn't want to talk to you.

## HTTP Client — `agentos.client` Routes Through the Engine

### The short answer

```python
from agentos import client, connection

# Public JSON API — no cookies, no browser bundle
connection("api", base_url="https://api.example.com",
           auth={"type": "api_key", "header": {"x-api-key": ".auth.key"}})

@connection("api")
async def list_things(**params):
    return await client.get("/things")

# Behind CloudFront/Cloudflare — connection says client="fetch" (XHR bundle)
connection("service", base_url="https://service.example.com",
           client="fetch",
           auth={"type": "cookies", "domain": ".example.com"})

# Full page navigation (Amazon, Goodreads) — client="browser"
connection("web", base_url="https://www.example.com",
           client="browser",
           auth={"type": "cookies", "domain": ".example.com"})

@connection("web")
async def get_page(**params):
    resp = await client.get("/some/path")
    return resp["body"]
```

All HTTP goes through the Rust engine via `agentos.client`. The engine handles transport mechanics (HTTP/2 via wreq+BoringSSL, decompression, timeouts, logging). **Headers come from the connection's `client=` kind** — the SDK composes the browser/fetch/api bundle per call, layering any caller `headers={...}` on top.

> **Default rule: pick the right `client=` kind once, per connection.** `"browser"` for
> navigate-style pages, `"fetch"` for XHR/API endpoints that still need browser identity,
> `"api"` for bare REST with key-in-header auth. Cookies ride the ambient Jar — the skill
> never threads them.
>
> ```python
> # WRONG — api connection on a page that needs Sec-Fetch-*; Amazon will reject
> connection("web", base_url=..., client="api", auth={"type": "cookies", ...})
>
> # RIGHT — browser bundle rides automatically; add service-specific headers only
> connection("web", base_url=..., client="browser", auth={"type": "cookies", ...})
>
> @connection("web")
> async def post_thing(**params):
>     return await client.post("/thing", json=body,
>                              headers={"x-csrf-token": "x"})
> ```

### TLS fingerprinting — why the engine uses wreq with BoringSSL

AWS WAF, Cloudflare, and other CDNs compute a **JA3/JA4 fingerprint** from every TLS ClientHello and compare it to the claimed User-Agent. If the UA says "Chrome 131" but the TLS fingerprint says "rustls" or "urllib3," the request gets flagged as a bot. Sensitive pages (Amazon orders, Chase banking, account settings) have higher anomaly thresholds than product pages — so the homepage works but the orders page redirects to login.

The engine uses **wreq** (a reqwest fork) backed by **BoringSSL** — the same TLS library Chrome uses. With `Emulation::Chrome131`, every request produces an authentic Chrome JA4 fingerprint (`t13d1516h2_8daaf6152771`), including correct HTTP/2 SETTINGS frames, pseudo-header order, and WINDOW_UPDATE values. This is not string-matching — wreq constructs the same ClientHello Chrome would, using the same library, and the fingerprint falls out naturally.

**Verified (2026-04-01):** Same cookies from Brave Browser. reqwest (rustls) → Amazon redirects to signin. wreq (BoringSSL, Chrome 131) → Amazon returns 7 orders. The only difference was the TLS fingerprint.

Python clients (`requests`, `httpx`) have similar issues — `requests`/urllib3 has a blocklisted JA3 hash (`8d9f7747675e24454cd9b7ed35c58707`). Skills don't hit this because all HTTP goes through the engine's wreq client, not Python libraries directly.

### When to use `http2=False` (Vercel)

**Vercel Security Checkpoint** blocks HTTP/2 clients outright — every request
returns `429` with a JS challenge page, regardless of cookies or headers. But
HTTP/1.1 passes cleanly.

Per-call `http2=False` is how a skill opts out of HTTP/2 for a specific
request or helper:

```python
# CloudFront / Cloudflare — HTTP/2 is the default, nothing to do
resp = await client.get(url)

# Vercel Security Checkpoint — force HTTP/1.1
resp = await client.get(url, http2=False)
```

Usually you wrap it once: a per-skill `_get`/`_post` helper that
pins `http2=False` for every call on a Vercel-hosted service (see
greptile, claude-web). The engine's TLS fingerprint still emulates
Chrome either way.

Not every Vercel-hosted endpoint enables the checkpoint. During Exa testing,
`auth.exa.ai` (Vercel, no checkpoint) accepted h2; `dashboard.exa.ai`
(Vercel, checkpoint enabled) rejected it. The checkpoint is a per-project
Vercel Firewall setting — you have to test each subdomain.

**Tested against `dashboard.exa.ai` (Vercel + Cloudflare):**

| | `http2=True` | `http2=False` |
|---|---|---|
| session + cf_clearance | 429 | 200 |
| session only | 429 | 200 |
| no cookies at all | 429 | 200 (empty session) |

Cookies and headers are irrelevant — the checkpoint triggers purely on
the HTTP/2 TLS fingerprint.

**Rule of thumb:** use `waf="cf"` for CloudFront/Cloudflare, `waf="vercel"` for Vercel. If you get `429` from Vercel, it's the HTTP/2 fingerprint. If you get `403` from CloudFront, you need HTTP/2 + client hints.

### Diagnostic protocol: isolating the variable

When a request fails, don't guess — isolate. Test each transport variable
independently to find the one that matters:

```
Step 1: Try httpx http2=True (default)
  → Works?     Done.
  → 429/403?   Continue.

Step 2: Try httpx http2=False
  → Works?     Vercel Security Checkpoint. Use http2=False, done.
  → Still 403? Continue.

Step 3: Try with full browser-like headers (Sec-Fetch-*, Sec-CH-UA, etc.)
  → Works?     WAF header check. Add headers, done.
  → Still 403? Continue.

Step 4: Try with valid session cookies
  → Works?     Auth required. Handle login first.
  → Still 403? It's TLS fingerprint-level.

Step 5: Use curl_cffi with Chrome impersonation
  → Works?     Strict JA3/JA4 enforcement. Use curl_cffi.
  → Still 403? Something non-standard (CAPTCHA, IP block).
```

The key insight from the Exa reverse engineering session: **test one variable
at a time.** During Exa testing, we created a matrix of `http2=True/False` x
`cookies/no-cookies` x `headers/no-headers` and discovered that ONLY the h2
setting mattered. Cookies and headers were completely irrelevant to the
Vercel checkpoint. This prevented unnecessary complexity in the skill code.

### You don't need `curl_cffi` or `httpx`

The engine's wreq client already emits Chrome's exact TLS cipher suites, GREASE values, extension ordering, ALPN, and HTTP/2 SETTINGS frames. Skills should never use `httpx`, `requests`, or `curl_cffi` directly — `agentos.http` handles all of this automatically.

### All I/O through SDK modules

Skills must use `agentos.http` for all HTTP — never `urllib`, `requests`, `httpx`, or `subprocess` directly. All I/O goes through SDK modules (`client.get/post`, `shell.run`, `sql.query`) so the engine can log, gate, and manage requests.

---

## Browser-Like Headers — the `client=` kind picks the bundle

There's no per-request header composer. The connection's `client=`
value picks one of three sealed header bundles, and every
`client.get/post/…` call inside a tool bound to that connection
inherits it.

```python
from agentos import client, connection

connection("web",
    base_url="https://www.example.com",
    client="browser",                  # full Chrome navigate bundle
    auth={"type": "cookies", "domain": ".example.com"})

@connection("web")
async def scrape(**params):
    return await client.get("/path")   # bundle rides automatically
```

### Three bundles

| `client=` | Headers | Use for |
|-----------|---------|---------|
| `"browser"` | UA + `Sec-CH-UA*` + `Sec-Fetch-Dest: document` + `Sec-Fetch-Mode: navigate` + `Sec-Fetch-Site: none` + `Sec-Fetch-User: ?1` + `Upgrade-Insecure-Requests: 1` + `Cache-Control: max-age=0` + full device hints (`Sec-CH-Device-Memory`, `Sec-CH-DPR`, `Sec-CH-UA-Full-Version-List`) + `Accept: text/html,application/xhtml+xml,…` | Page loads, form POSTs, top-level navigation (Amazon, Goodreads pages) |
| `"fetch"` | UA + `Sec-CH-UA*` + `Sec-Fetch-Dest: empty` + `Sec-Fetch-Mode: cors` + `Sec-Fetch-Site: same-origin` + `Accept: application/json` | AJAX/fetch from within a page (Claude.ai /api, Greptile tRPC) |
| `"api"` (default) | Nothing — caller supplies all headers | Bare REST with key-in-header auth (Anthropic, OpenRouter, Linear) |

The SDK's Python client hints and the engine's TLS emulation (Chrome
via wreq+BoringSSL) are byte-matched on purpose — a request from
AgentOS looks like a real Brave/Chrome tab at every layer.

### Per-request overrides (rare)

```python
# One call inside a "browser" connection wants XHR behavior
await client.get(url, client="fetch")

# Force HTTP/1.1 (Vercel checkpoint, Cloudflare JA4 edge cases)
await client.get(url, http2=False)

# Add service-specific headers (CSRF token, Authorization,
# Referer) — merge on top of the bundle, caller wins.
await client.post(url, json=body,
                  headers={"x-csrf-token": "x"})

# Strip cookies from the outbound Cookie: header (Amazon's
# csd-key / csm-hit / aws-waf-token — see Cookie Stripping below)
await client.get(url, skip_cookies=_SKIP_COOKIES)

# Bypass the ambient Jar entirely (third-party fetch that shouldn't
# carry the authed session's cookies)
await client.get(external_url, incognito=True)
```

### Version drift

The Chrome version in client hints is pinned in
`sdk-skills/agentos/client.py::_CHROME_VERSION` and must stay in
sync with `crates/exec-executors/src/http.rs::CHROME_EMULATION`. If
you start getting unexpected 403s months later, bump both together
to match the current stable Chrome release.

### How to discover the right headers

Use the Playwright skill's `capture_network` or the fetch interceptor
to see exactly what headers a real browser sends on the same request.
Compare with what the `browser` / `fetch` bundle produces; if
something specific is missing (auth token, CSRF, Referer, Origin),
add it via `headers={...}` on the call.

---

## Cookie Stripping — Disabling Client-Side Features

Some sites inject JavaScript-driven features via cookies. When you're scraping
with HTTPX (no JS engine), these features produce unusable output. The fix:
**strip the trigger cookies** so the server falls back to plain HTML.

### Amazon's Siege Encryption

Amazon uses a system called `SiegeClientSideDecryption` to encrypt page content
client-side. When the `csd-key` cookie is present, Amazon sends encrypted HTML
blobs instead of readable content. The browser decrypts them with JavaScript;
HTTPX gets unreadable garbage.

**Solution:** strip the trigger cookies per call via `skip_cookies=`:

```python
_SKIP_COOKIES = ["csd-key", "csm-hit", "aws-waf-token"]

@connection("web")    # client="browser"
async def list_orders(**params):
    resp = await client.get(url, skip_cookies=_SKIP_COOKIES)
    return resp["body"]
```

The SDK filters these names out of the outbound `Cookie:` header
before dispatch (the jar still stores them — the filter is
send-only). With `csd-key` stripped, Amazon serves plain, parseable
HTML. `csm-hit` and `aws-waf-token` are telemetry/WAF cookies that
trigger additional client-side behavior; strip them for the same
reason. See `skills/logistics/amazon/amazon.py` for the `_get` /
`_post` / `_warm_session` wrappers that pin `skip_cookies` on every
authed call.

### Diagnosing encryption

If your HTML responses contain garbled content, long base64 strings, or empty
containers where data should be, check for client-side decryption:

1. Compare the page source in the browser (View Source, not DevTools Elements)
   with your HTTPX response
2. Search for keywords like `decrypt`, `Siege`, `clientSide` in the page JS
3. Try stripping cookies one at a time to find which one triggers encryption

Reference: `skills/amazon/amazon.py` `SKIP_COOKIES`.

---

## Response Decompression — You Must Handle What You Advertise

When you send `Accept-Encoding: gzip, deflate, br, zstd` (as all browser-like profiles do), the server will compress its response. **Your HTTP client must decompress it.** If it doesn't, you get raw binary garbage instead of HTML — and every parser returns zero results.

This is a silent failure. The HTTP status is 200, the headers look normal, and `Content-Length` is reasonable. But `resp.text` is garbled bytes. It looks like client-side encryption (see above), but the cause is much simpler: the response is compressed and you're not decompressing it.

### How `agentos.http` handles it

The Rust HTTP engine uses wreq with `gzip`, `brotli`, `deflate`, and `zstd` feature flags enabled. Decompression is automatic and transparent — `resp["body"]` is always plaintext.

### Why this matters

**Brotli** (RFC 7932) is a compression algorithm designed by Google for the web. It compresses 20-26% better than gzip on HTML/CSS/JS. Every modern browser supports it, and servers aggressively use it for large pages. Amazon's order history page, for example, returns ~168KB of brotli-compressed HTML. Without decompression, you get 168KB of binary noise and zero order cards.

**The trap:** small pages (homepages, API endpoints) may not be compressed or may use gzip which some clients handle by default. Large pages (order history, dashboards, search results) almost always use brotli. So your skill works on simple endpoints and silently fails on the important ones.

### Diagnostic

If your response body contains non-UTF-8 bytes, starts with garbled characters, or contains no recognizable HTML despite a 200 status:

1. Check the response `Content-Encoding` header — if it says `br`, `gzip`, or `zstd`, the body is compressed
2. Verify your HTTP client has decompression enabled
3. In agentOS: `agentos.http` handles this automatically. If you're using raw `urllib.request`, it does NOT decompress brotli

Reference: `Cargo.toml` wreq features — `gzip`, `brotli`, `deflate`, `zstd`.

---

## Session Warming

Some services track request patterns and flag direct deep-links from an unknown
session as bot traffic. The fix: **warm the session** by visiting the homepage
first, then navigate to the target page.

```python
def _warm_session(client) -> None:
    """Visit homepage first to provision session cookies."""
    client.get("https://www.amazon.com/", headers={"Sec-Fetch-Site": "none"})
```

This establishes the session context (cookies, CSRF tokens, tracking state)
before hitting authenticated pages. Without it, Amazon redirects order history
and account pages to the login page even with valid session cookies.

**When to warm:**
- Before any authenticated page fetch (order history, account settings)
- When the first request to a deep URL returns a login redirect despite valid cookies
- When you see WAF-level blocks only on direct navigation

**When warming isn't needed:**
- API endpoints (JSON responses) — they don't use page-level session tracking
- Public pages without authentication
- Sites where direct deep-links work fine (test first)

Reference: `skills/amazon/amazon.py` `_warm_session()`.

---

## Headless Browser Stealth

Default Playwright/Chromium gets blocked by many sites (Goodreads returns 403,
Cloudflare serves challenge pages). The fix is a set of anti-fingerprinting settings.

### Minimum stealth settings

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(
        headless=True,
        args=["--disable-blink-features=AutomationControlled"],
    )
    context = browser.new_context(
        user_agent=(
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/131.0.0.0 Safari/537.36"
        ),
        viewport={"width": 1440, "height": 900},
        locale="en-US",
        timezone_id="America/New_York",
    )
    page = context.new_page()
    page.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => false });
    """)
```

### What each setting does

| Setting | Why |
|---|---|
| `--disable-blink-features=AutomationControlled` | Removes the `navigator.webdriver=true` flag that Chromium sets in automation mode |
| Custom `user_agent` | Default headless UA contains `HeadlessChrome` which is trivially blocked |
| `viewport` | Default headless viewport is 800x600, which no real user has |
| `locale` / `timezone_id` | Some bot detectors check for mismatches between locale and timezone |
| `navigator.webdriver = false` | Belt-and-suspenders override in case the flag leaks through other paths |

### Real example: Goodreads

Default Playwright against `goodreads.com/book/show/4934` returns HTTP 403 with
one network request. With stealth settings, the page loads fully with 1400+ requests
including 4 AppSync GraphQL calls. See `skills/goodreads/public_graph.py`
`discover_via_browser()` for the implementation.

---

## CDP Detection Signals — Why Playwright Gets Caught

Even with the stealth settings above, Playwright is still detectable at the
**Chrome DevTools Protocol (CDP) layer**. These signals are invisible in
DevTools and unrelated to headers, cookies, or user-agent strings. They matter
most during reverse engineering sessions — if a site behaves differently under
Playwright than in your real browser, CDP leaks are likely the cause.

### Runtime.Enable leak

Playwright calls `Runtime.Enable` on every CDP session to receive execution
context events. Anti-bot systems (Cloudflare, DataDome) detect this with a few
lines of in-page JavaScript that only fire when `Runtime.Enable` is active.
This is the single most devastating detection vector — it works regardless of
all other stealth measures.

### sourceURL leak

Playwright appends `//# sourceURL=__playwright_evaluation_script__` to every
`page.evaluate()` call. Any page script can inspect error stack traces and see
these telltale URLs. This means your `__NEXT_DATA__` extraction, DOM inspection,
or any other `evaluate()` call leaves a fingerprint.

### Utility world name

Playwright creates an isolated world named `__playwright_utility_world__` that
is visible in Chrome's internal state and potentially to detection scripts.

### What to do about it

These leaks are baked into Playwright's source code — no launch flag or init
script fixes them. Two options:

1. **For most RE work:** The stealth settings above (flags, UA, viewport,
   webdriver override) are enough. Most sites don't check CDP-level signals.
   If a site seems to behave differently under Playwright, check for these
   leaks before adding complexity.

2. **For strict sites (Cloudflare Bot Management, DataDome):** Use
   [`rebrowser-playwright`](https://github.com/rebrowser/rebrowser-patches)
   as a drop-in replacement. It patches Playwright's source to eliminate
   `Runtime.Enable` calls, randomize sourceURLs, and rename the utility
   world. Install: `npm install rebrowser-playwright` and change your import.

**This doesn't affect production skills.** Our architecture uses Playwright
only for discovery — production calls go through `surf()` / HTTPX, which has
zero CDP surface. The CDP leaks only matter during reverse engineering sessions
where you're using the browser to investigate a protected site.

---

## Cookie Domain Filtering — RFC 6265

When a cookie provider (brave-browser, firefox) extracts cookies for a domain like `.uber.com`, it returns cookies from ALL subdomains: `.uber.com`, `.riders.uber.com`, `.auth.uber.com`, `.www.uber.com`. If the skill's `base_url` is `https://riders.uber.com`, sending cookies from `.auth.uber.com` is wrong — the server picks the wrong `csid` and redirects to login.

The engine implements **RFC 6265 domain matching**: when resolving cookies, it extracts the host from `connection.base_url` and passes it to the cookie provider. The provider filters cookies so only matching ones are returned:

```
host = "riders.uber.com"

.uber.com          → riders.uber.com ends with .uber.com   → KEEP (parent domain)
.riders.uber.com   → riders.uber.com matches exactly        → KEEP (exact match)
.auth.uber.com     → riders.uber.com doesn't match          → DROP (sibling)
.www.uber.com      → riders.uber.com doesn't match          → DROP (sibling)
```

This is automatic — skills don't need to do anything. The filtering happens in the cookie provider (`brave-browser/get-cookie.py`, `firefox/firefox.py`) based on the `host` parameter the engine passes from `connection.base_url`.

**When it matters:** Only when a domain has cookies on multiple subdomains with the same cookie name. Most skills are unaffected — Amazon, Goodreads, Chase all have cookies on a single domain. Uber is the first case where it matters.

**The old workaround:** Before RFC 6265 filtering, the Uber skill had a `_filter_cookies()` function that deduplicated by cookie name (last occurrence wins). This has been removed — the provider handles it correctly now.

---

## Cookie Resolution — `http.cookies()`

Skills don't resolve cookies manually — they declare a
`connection(..., auth={"type": "cookies", "domain": ".uber.com"})`
and the engine runs provider discovery, picks the freshest session,
and seeds the ambient Jar automatically:

```python
from agentos import client, connection

connection("web",
    base_url="https://riders.uber.com",
    client="fetch",
    auth={"type": "cookies", "domain": ".uber.com",
          "account": {"check": "check_session"}})

@connection("web")
async def list_trips(**params):
    # Ambient Jar has the freshest cookies from brave-browser /
    # firefox / wherever. No resolver call in skill code.
    return await client.post("/graphql", json={...})
```

For a skill that needs to reach a second domain one-off (rare), use
`client.get(url, incognito=True)` for unauthed third-party fetches
or declare a second connection — don't reintroduce manual cookie
resolving.

### Playwright integration

`capture_network` accepts a `cookie_domain` param that resolves cookies automatically:

```python
# One step — no manual cookie extraction needed
run(skill="playwright", tool="capture_network", params={
    "url": "https://riders.uber.com/trips",
    "cookie_domain": ".uber.com",
    "pattern": "**graphql**",
})
```

This replaces the old 3-step flow (extract from provider → reformat → inject).

---

## Debugging 400/403 Errors

| Symptom | Likely cause | Fix |
|---|---|---|
| `403` from CloudFront with a bot-detection HTML page | JA3/JA4 fingerprint blocked | Shouldn't happen with wreq — if it does, check that the engine is running the wreq build |
| `400` from CloudFront, body is `"Forbidden"` or short string | WAF rule triggered (header order, ALPN) | Use `waf="cf"` + check `mode=` |
| `400`, body looks like `"404"` | API Gateway can't route the request — usually a missing tenant/auth header | Find and add the missing header via `extra=` |
| `403` for a same-origin API (e.g. `claude.ai`) | Missing `Sec-Fetch-*` headers | Use `waf="cf"` — sets Sec-Fetch-* automatically |
| `403` from headless Playwright | Default Chromium automation fingerprint | Add stealth settings (see Headless Browser Stealth above) |
| `429` with "Vercel Security Checkpoint" HTML | Vercel blocks HTTP/2 fingerprint | Use `waf="vercel"` (sets http2=False) |
| Works in browser, fails in Python regardless | Check for authorization that's not a JWT | Look for short `Authorization` values in the bundle (namespace, env name, etc.) |

### Using Playwright to capture exact headers

When you're stuck, use Playwright to intercept the actual XHR and log all headers
(including those added by axios interceptors that aren't visible in DevTools):

```python
from playwright.sync_api import sync_playwright

def capture_request_headers(url_pattern: str, trigger_url: str) -> dict:
    """Navigate to trigger_url and capture headers from the first request matching url_pattern."""
    captured = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.on("request", lambda req: captured.update(req.headers)
                if url_pattern in req.url else None)
        page.goto(trigger_url)
        page.wait_for_timeout(3000)
        browser.close()
    return captured
```

---

## Skill File Layout

```
skills/<skill-name>/
  readme.md            <- agentOS skill descriptor (operations, adapters, etc.)
  requirements.md      <- reverse engineering notes, API docs, findings log
  <skill>.py           <- Python module with all API functions
  icon.svg             <- skill icon
```

Keep `requirements.md` as a living document — update it every time you discover
a new endpoint, figure out a new header, or resolve a mystery.

---

## Real-World Examples in This Repo

| Skill | Service | Transport config | Key learnings |
|---|---|---|---|
| `skills/amazon/` | Amazon (Lightsaber) | `waf="cf", mode="navigate", accept="html"` | Full device hints required, `skip_cookies=` for Siege encryption, session warming. Chrome TLS fingerprint (wreq) required for orders page — Amazon's WAF uses JA4 + OpenID `max_auth_age=0` per-feature auth gates. |
| `skills/austin-boulder-project/` | Tilefive / approach.app | `accept="json"` + auth header | CloudFront, `Authorization` = namespace string |
| `skills/claude/` | claude.ai (Cloudflare) | `waf="cf", accept="json"`, http2=False override | Custom Sec-CH-UA (Brave v146), Cloudflare bypass needs Sec-Fetch-* |
| `skills/exa/` | dashboard.exa.ai (Vercel) | `waf="vercel", accept="json"` | Vercel checkpoint is purely TLS — cookies and headers irrelevant |
| `skills/goodreads/` | Goodreads (CloudFront) | `waf="cf", accept="html"` | Public GraphQL via CloudFront, headless Playwright needs stealth settings |
| `skills/uber/` | Uber (CloudFront) | `accept="json"` + custom headers | RFC 6265 cookie domain filtering — first skill where sibling subdomain cookies caused bugs |
