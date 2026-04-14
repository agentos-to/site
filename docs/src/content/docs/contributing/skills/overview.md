---
title: "Skills"
description: "A skill connects agentOS to an external service. Read this once, build a skill."
---A skill connects agentOS to an external service. Read this once, build a skill.

A skill is a directory with a `readme.md` (identity + config) and one or more `*.py` files (tools).

```
skills/my-skill/
  readme.md        # identity + config (YAML frontmatter)
  my_skill.py      # tools (decorated Python functions)
```

The engine reads both at boot:
- `readme.md` frontmatter → identity, connections, test config
- `*.py` files → tools (via AST parsing, never executed at boot)

## How tool discovery works

There is **no manifest listing tools**. The engine walks every `*.py` file in the skill directory, parses it as AST (without importing it), and treats any top-level function carrying an SDK decorator (`@returns`, `@provides`, `@connection`, `@timeout`) as a tool. The tool name is the **Python function name** — the filename is irrelevant to routing. A request to `run({skill:"my-skill", tool:"list_items"})` resolves to whichever file defines `def list_items(...)` with a decorator.

Because AST discovery happens before import, decorators are **no-ops at runtime** — they're markers the engine greps for, not logic that runs. Undecorated functions (including underscore-prefixed helpers) are invisible to the engine regardless of their name.

## Multi-file skills

A skill with several logical surfaces can split them across files. Claude has an API connector, a CLI connector, and a web connector — all under skill id `claude`:

```
skills/ai/claude/
  readme.md           # id: claude
  claude_api.py       # @returns tools for the HTTP API
  claude_code.py      # @returns tools for the local CLI + JSONL state
  claude_web.py       # @returns tools for claude.ai web scraping
```

All three files contribute to a single flat tool namespace keyed on function name. `list_models` in `claude_api.py` and `list_sessions` in `claude_code.py` are both reachable as `tool: "list_models"` / `tool: "list_sessions"` on skill `claude`. **Tool names must be globally unique within the skill** — duplicates are a bug, caught by `agent-sdk validate`.

Helper functions (any name starting with `_`) and imports are not tools, so you can share `_flatten_content` or `_parse_row` across files without worrying about collisions.

## Skill anatomy

### readme.md — identity and config

```markdown
---
id: my-skill
name: My Skill
description: What this skill does in one line
color: "#4A90D9"
website: https://example.com

connections:
  api:
    base_url: https://api.example.com
    auth:
      type: api_key
      header:
        x-api-key: .auth.key
    label: API Key
    help_url: https://example.com/api-keys

test:
  list_items: { params: { query: "test" } }
  get_item: { params: { id: "123" } }
---

# My Skill

Description of what this skill connects to and what data it provides.
```

**Required frontmatter fields:** `id`, `name`

**Connection auth types:**
- `api_key` — API key in a header or query param
- `cookies` — browser session cookies (domain required)
- `oauth` — OAuth2 refresh token flow
- `none` — no auth needed (omit the connections block entirely)

See [connections.md](connections.md) for the full reference.

### Python module — tools

```python
"""My Skill — connects to Example API for items and searches."""

from agentos import http, returns

@returns("product[]")
def list_items(query: str = None, limit: int = 10, **params) -> list[dict]:
    """List items matching a query.

    Args:
        query: Search query to filter items
        limit: Max results to return (default 10)
    """
    resp = http.get("https://api.example.com/items",
                    params={"q": query, "limit": limit},
                    headers={"x-api-key": params["auth"]["key"]})
    return [{"id": str(item["id"]),
             "name": item["title"],
             "url": f"https://example.com/items/{item['id']}",
             "price": item.get("price"),
             "currency": item.get("currency", "USD")}
            for item in resp["json"]["items"]]
```

**Rules:**
- A function becomes a tool when it carries at least one SDK decorator (`@returns`, `@provides`, `@connection`, `@timeout`). Undecorated functions and `_underscore_prefixed` helpers are invisible to the engine.
- Every tool MUST have `@returns("shape")` or `@returns("shape[]")` — the decorator the engine reads to know what the tool produces.
- Every tool MUST accept `**params` — the engine injects auth, context, and session state there.
- First line of docstring = tool description (shown in MCP tool schema).
- `Args:` section (Google style) = parameter descriptions.
- Type hints on params = schema types (`str`, `int`, `bool`, `float`).
- Default values = optional params; no default = required.
- The tool name is the function name. Keep function names globally unique **within the skill**, even across multiple `.py` files.

## Decorators

```python
from agentos import returns, provides, connection, timeout
```

### @returns(shape) — required on every tool

```python
@returns("event[]")          # returns list of events
def list_events(...): ...

@returns("event")            # returns single event
def get_event(...): ...

@returns({"ok": "boolean"})  # inline schema (no shape reference)
def delete_item(...): ...
```

The engine reads this via AST at boot — it's a no-op at runtime, and its mere presence is what marks a function as a tool.

### @provides(tool) — register as a standard capability

```python
from agentos import provides, web_search, web_read

@provides(web_search)
def search(query: str, **params) -> list[dict]: ...

@provides(web_read, urls=["example.com/*"])
def read_page(url: str, **params) -> dict: ...
```

Standard tool constants (import from `agentos`):
- `web_search`, `web_read` — discovery & retrieval
- `email_lookup` — people
- `flight_search`, `geocoding`, `map_tiles` — travel
- `file_list`, `file_read`, `file_info` — files
- `cookie_auth`, `oauth_auth` — auth provision
- `llm` — LLM inference (see [llm.md](llm.md))

### @connection(name) — bind to auth connection

```python
@connection("web")           # uses the "web" connection from frontmatter
def list_orders(...): ...

@connection("api")           # uses the "api" connection
def search(...): ...
```

Tells the engine which connection's credentials to inject into `params["auth"]`.

### @timeout(seconds) — override default 30s timeout

```python
@timeout(60)                 # allow up to 60 seconds
def slow_operation(...): ...
```

## SDK modules

All I/O goes through SDK modules. **Never** import `urllib`, `requests`, `subprocess`, `sqlite3`, or `os.popen` — the engine sandbox blocks them.

### http — HTTP requests

```python
from agentos import http

resp = http.get("https://api.example.com/data")
data = resp["json"]          # parsed JSON (dict/list)
html = resp["body"]          # raw response body (string)
code = resp["status"]        # HTTP status code (int)
ok   = resp["ok"]            # True if 2xx

# POST with JSON body
resp = http.post("https://api.example.com/items",
                 json={"name": "test"},
                 headers={"Authorization": "Bearer token"})

# POST with form data
resp = http.post("https://api.example.com/login",
                 data={"username": "u", "password": "p"})

# All methods: get, post, put, patch, delete, head
# There is NO http.request — dispatch by verb, always.

# Query string — pass dict via params= (engine URL-encodes for you)
resp = http.get("https://api.example.com/search",
                params={"q": "hello world", "limit": 10})
# → https://api.example.com/search?q=hello%20world&limit=10
```

### URL helpers

The SDK has four URL helpers on `http`. Use them — **never hand-roll URL encoding with `urllib`** (it's banned in the sandbox).

```python
from agentos import http

# Build a URL with query params (same behavior as passing params= to http.get)
url = http.build_url("https://api.example.com/search",
                     params={"q": "hello world", "limit": 10})
# → "https://api.example.com/search?q=hello%20world&limit=10"

# Parse a URL into its components
parts = http.parse_url("https://example.com/foo?a=1&b=2#top")
# → {"scheme": "https", "host": "example.com", "path": "/foo",
#    "query": {"a": "1", "b": "2"}, "fragment": "top"}

# Percent-encode / decode a single path or query component
http.encode("hello world/test")      # → "hello%20world%2Ftest"
http.decode("hello%20world%2Ftest")  # → "hello world/test"
```

When you need a dynamic path segment (e.g. `name:{company}` in a CDN URL), use `http.encode(name)`. When you need a query string, use `params=` or `build_url`. There's almost never a reason to build a URL with f-strings plus `encode` — the higher-level helpers are cleaner.

### Content-Type override — AWS JSON variants, etc.

Per-request `headers=` always beats the Content-Type implied by the body. For AWS services that want `application/x-amz-json-1.1` (e.g. Cognito):

```python
resp = await http.post(
    "https://cognito-idp.us-east-1.amazonaws.com/",
    json={"AuthFlow": "USER_PASSWORD_AUTH", ...},          # sets Content-Type: application/json
    headers={
        "Content-Type": "application/x-amz-json-1.1",       # overrides it
        "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth",
    },
)
```

You do NOT need a raw-bytes body mode for this — `json=dict` + `headers={"Content-Type": "..."}` is enough.

### http.headers() — browser-like headers for cookie-auth

This is the most important function for cookie-auth skills. WAFs (Cloudflare, CloudFront, Vercel) block requests that don't look like a real browser.

```python
# Spread into any request with **
resp = http.get(url, **http.headers(waf="cf", mode="navigate", accept="html"))
```

| Knob | Values | Default | What it does |
|------|--------|---------|-------------|
| `waf` | `"cf"`, `"vercel"`, `None` | `None` | WAF vendor — adds Sec-CH-UA client hints. `"cf"` covers both Cloudflare and CloudFront |
| `ua` | `"chrome-desktop"`, `"chrome-mobile"`, `"safari-desktop"`, or raw string | `"chrome-desktop"` | User-Agent header |
| `mode` | `"fetch"`, `"navigate"` | `"fetch"` | `"navigate"` adds Sec-Fetch-Dest: document + full browser hints |
| `accept` | `"json"`, `"html"`, `"any"` | `"any"` | Accept header — `"html"` sends the full browser Accept string |
| `extra` | dict | `None` | Additional headers merged last (highest priority) |

**When to use what:**

| Scenario | Headers call |
|----------|-------------|
| Public JSON API (no auth) | No headers needed — just `http.get(url)` |
| API with key in header | `headers={"x-api-key": key}` — no `http.headers()` needed |
| Cookie-auth, Cloudflare/CloudFront | `http.headers(waf="cf", mode="navigate", accept="html")` |
| Cookie-auth, Vercel | `http.headers(waf="vercel", mode="navigate", accept="html")` |
| Cookie-auth, no WAF | `http.headers(mode="navigate", accept="html")` |
| XHR/fetch to same-origin API | `http.headers(waf="cf", mode="fetch", accept="json")` |
| GraphQL endpoint | `http.headers(accept="json", extra={"Content-Type": "application/json"})` |

**What the engine auto-injects vs what Python must set:**

The engine provides:
- TLS fingerprint emulation (Chrome 145 via wreq) — automatic, not configurable
- Cookie jar management (Set-Cookie tracking, writeback)
- HTTP/2 toggle (from `http2` key in headers() return)

Python (your skill) provides via `http.headers()`:
- User-Agent, Sec-CH-UA and other client hints, Sec-Fetch-* metadata
- Accept / Accept-Language / Accept-Encoding
- Any custom headers (Authorization, Referer, Origin, etc.)

The engine is pure transport — it does NOT add browser headers automatically. For public APIs this is fine. For cookie-auth sites, you **must** use `http.headers()`.

### http.client() — session with cookie jar

For multi-request flows where cookies matter (login → navigate → scrape):

```python
from agentos import http, require_cookies

cookie_header = require_cookies(params, "list_orders")

with http.client(cookies=cookie_header) as c:
    c.get("https://www.example.com/",
          **http.headers(waf="cf", mode="navigate", accept="html"))
    resp = c.get("https://www.example.com/account/orders",
                 **http.headers(waf="cf", mode="navigate", accept="html"))
    orders = resp["body"]
```

The engine tracks `Set-Cookie` responses and diffs the jar on session close for automatic writeback to the credential store.

### http.cookies() — resolve cookies by domain

```python
from agentos import http

cookie_header = http.cookies(".uber.com")
# Returns "name=value; name=value; ..." from best available provider
```

Uses the auth system's provider discovery: tries all installed cookie providers (brave-browser, firefox), picks the freshest session, validates it.

### Cookie helpers

```python
from agentos import get_cookies, require_cookies, parse_cookie

cookies = get_cookies(params)                     # None if not present
cookies = require_cookies(params, "operation")    # raise with helpful message
session_id = parse_cookie(cookie_header, "session_id")
```

### sql — database queries

```python
from agentos import sql

rows = sql.query("SELECT id, name FROM users WHERE active = :active",
                 db="~/Library/Application Support/App/data.sqlite",
                 params={"active": 1})

sql.execute("INSERT INTO items (name) VALUES (:name)",
            db="~/data.db", params={"name": "test"})

# Cross-database JOIN
rows = sql.query("SELECT m.id FROM main.items m JOIN other.tags t ON ...",
                 db="~/main.db",
                 attach={"other": "~/tags.db"})
```

Use this instead of `import sqlite3`. The engine handles path resolution, logging, and permissions.

### shell — binary execution

```python
from agentos import shell

result = shell.run("git", ["log", "--oneline", "-5"], cwd="/path/to/repo")
print(result["stdout"])      # captured stdout
print(result["stderr"])      # captured stderr
print(result["exit_code"])   # 0 = success
```

Shell interpreters (bash, sh, zsh) are always blocked. Run binaries directly. Use this instead of `import subprocess`.

### crypto — browser cookie decryption

```python
from agentos import crypto

key = await crypto.pbkdf2(password="peanuts", salt="saltysalt",
                          iterations=1003, length=16)
plaintext = await crypto.aes(data=encrypted_hex, key=key.hex(),
                             iv="20" * 16)  # 16 space bytes (Chromium)
```

Used by browser cookie providers. You probably won't need this directly.

### oauth — token exchange

```python
from agentos import oauth

token = oauth.exchange(
    token_url="https://oauth2.googleapis.com/token",
    refresh_token=params["auth"]["refresh_token"],
    client_id=params["auth"]["client_id"],
)
access_token = token["access_token"]
```

### molt — cleaning scraped data

```python
from agentos import molt

molt(s)                          # clean string (strip HTML, normalize whitespace, kill sentinels)
molt("1,234 reviews", int)       # 1234
molt("4.5 out of 5", float)     # 4.5
molt("August 2010", "date")     # "2010-08"
molt(1616025600000, "date")     # "2021-03-18T..."
molt(None)                       # None

# Fine-grained imports if you need specific behavior:
from agentos import clean_text, clean_html, strip_tags
from agentos import parse_int, parse_float, parse_date
from agentos import iso_from_ms, iso_from_seconds
```

`molt()` is the universal cleaner — use it for any scraped value. It handles HTML entities, whitespace normalization, and sentinel detection ("N/A", "not available" → `None`).

### llm — agent workflows

LLM inference (one-shot, multi-turn agent loops with tool calling, structured output). See **[llm.md](llm.md)** for the full reference.

```python
from agentos import llm

result = await llm.oneshot(prompt="Summarize this.", model="sonnet")
```

### checkpoint — resume multi-phase workflows

See [llm.md](llm.md) for the full reference — checkpoint lives alongside agent workflows.

## Naming rules

| What | Convention | Example |
|------|-----------|---------|
| Python functions (tools) | `snake_case`, no prefix | `def list_posts(**params)` |
| Shape field keys (entity data) | `camelCase` | `"startDate"`, `"postedBy"` |
| Non-shape keys (API passthrough) | Keep source format | `"access_token"` from an API response |

Python is snake_case. Data going into the graph is camelCase. That's it.

**No `run_` / `op_` / `do_` prefixes on tool functions.** The engine parses Python as text and the tool name is the function name verbatim — `async def search_books` is called as `tool: "search_books"`. The skill id is already the namespace.

## Shape conventions

Shapes define the structure of entities. See the [Ontology overview](/docs/ontology/overview/) for the full reference (design principles, the `also` inheritance chain, `_tag` polymorphism, identity rules).

**Standard fields** (available on all shapes):
- `id` (string) — unique identifier
- `name` (string) — display name
- `url` (string) — canonical URL
- `image` (string) — image URL
- `published` (datetime) — when created/published
- `content` (string) — main text content

**Example — returning an event shape:**

```python
@returns("event[]")
def list_events(**params) -> list[dict]:
    return [{
        "id": "evt-123",
        "name": "Python Meetup",
        "url": "https://meetup.com/events/123",
        "startDate": "2026-04-10T18:00:00Z",    # camelCase!
        "endDate": "2026-04-10T20:00:00Z",
        "timezone": "America/Chicago",
        "eventType": "meetup",
        "status": "confirmed",
        "allDay": False,
    }]
```

**Common shapes:** event, product, person, account, book, email, post, result, webpage, order, review, article, place, domain, channel, conversation, message, file, folder.

Use `agent-sdk shapes` to list all shapes. Use `agent-sdk shapes event` to see a shape's fields and relations.

## Annotated examples

### Public API (no auth)

```python
"""Curl — simple URL fetching via HTTP GET."""

from lxml import html
from agentos import http, provides, returns, timeout, web_read

@returns("webpage")
@provides(web_read)
@timeout(35)
def read_webpage(*, url: str, **params) -> dict:
    """Fetch a URL and return its content, title, and content type."""
    resp = http.get(url, timeout=30.0)
    content = resp["body"]
    content_type = resp["headers"].get("content-type", "text/plain").split(";")[0].strip()

    title = ""
    if content_type.startswith("text/html") and content:
        doc = html.fromstring(content[:4000])
        title_el = doc.cssselect("title")
        if title_el:
            title = title_el[0].text_content().strip()

    return {
        "id": url,
        "name": title or url,
        "url": url,
        "content": content,
        "contentType": content_type,
    }
```

**Pattern:** No auth, no `http.headers()`, no `@connection`. Just `http.get()`.

### Cookie-auth (Goodreads)

```python
"""Goodreads — profile, books, and reviews via session cookies."""

from lxml import html as lxml_html
from agentos import http, molt, returns, connection, timeout
from agentos import require_cookies

@returns("person")
@connection("web")
@timeout(30)
def get_person(user_id: str, **params) -> dict:
    """Get a Goodreads user profile."""
    cookies = require_cookies(params, "get_person")

    with http.client(cookies=cookies) as c:
        resp = c.get(f"https://www.goodreads.com/user/show/{user_id}",
                     **http.headers(waf="cf", mode="navigate", accept="html"))

    doc = lxml_html.fromstring(resp["body"])
    name_el = doc.cssselect("h1.userProfileName")
    return {
        "id": user_id,
        "name": molt(name_el[0].text_content()) if name_el else user_id,
        "url": f"https://www.goodreads.com/user/show/{user_id}",
    }
```

**Pattern:** `@connection("web")` → engine injects cookies into `params["auth"]`. `require_cookies()` extracts them. `http.headers(waf="cf")` for CloudFront WAF. `lxml` + `cssselect` for HTML parsing. `molt()` to clean scraped text.

### API-key (Exa)

```python
"""Exa — semantic web search and content extraction."""

from agentos import http, returns, provides, connection, timeout, web_search

@returns("result[]")
@provides(web_search)
@connection("api")
@timeout(30)
def search(query: str, limit: int = 10, **params) -> list[dict]:
    """Search the web using Exa's neural search."""
    resp = http.post("https://api.exa.ai/search",
                     json={"query": query, "numResults": limit,
                           "type": "auto", "useAutoprompt": True},
                     headers={"x-api-key": params["auth"]["key"]},
                     **http.headers(accept="json"))
    return [{"id": r["url"],
             "name": r.get("title", r["url"]),
             "url": r["url"],
             "content": r.get("text", ""),
             "published": r.get("publishedDate")}
            for r in resp["json"].get("results", [])]
```

**Pattern:** `@connection("api")` → engine injects API key into `params["auth"]["key"]`. Header set directly on request.

## Common mistakes

**Blocked imports** — the sandbox blocks direct network/system access:

```python
# WRONG
import urllib.request        # use http.get()
import requests              # use http.get()
import subprocess            # use shell.run()
import sqlite3               # use sql.query()
import os; os.popen(...)     # use shell.run()

# RIGHT
from agentos import http, sql, shell
```

**snake_case shape fields** — shape fields must be camelCase:

```python
# WRONG
return {"start_date": "2026-04-10", "event_type": "meetup"}

# RIGHT
return {"startDate": "2026-04-10", "eventType": "meetup"}
```

Non-shape keys (API passthrough, internal metadata, engine contracts) keep their source format. The validator is shape-scoped — it only flags a snake_case key if the function's declared `@returns` shape has a matching camelCase field:

```python
# FINE — "access_token" isn't a shape field, keep what the API gives you
return {"id": token_id, "access_token": resp["access_token"]}

# FINE — "tool_calls" is the engine's canonical LLM wire format, not a shape field
# on whatever @returns schema this tool declares.
return {"content": text, "tool_calls": [...], "stop_reason": stop}
```

**Missing `**params`**:

```python
# WRONG
def list_items(query: str) -> list[dict]: ...

# RIGHT
def list_items(query: str, **params) -> list[dict]: ...
```

**Missing `@returns`**:

```python
# WRONG
def list_items(**params): ...

# RIGHT
@returns("product[]")
def list_items(**params) -> list[dict]: ...
```

**No http.headers() on cookie-auth**:

```python
# WRONG — naked request to a cookie-auth site
resp = http.get("https://www.goodreads.com/user/show/123",
                headers={"Cookie": cookies})

# RIGHT
resp = http.get("https://www.goodreads.com/user/show/123",
                cookies=cookies,
                **http.headers(waf="cf", mode="navigate", accept="html"))
```

**Missing `await` on async SDK calls** — the SDK is fully async. A missing `await` silently returns a coroutine instead of the real response and the failure surfaces downstream as a `'coroutine' object has no attribute 'get'` or similar:

```python
# WRONG — resp is a coroutine, not the response dict
resp = http.get("https://api.example.com/data")
data = resp["json"]   # AttributeError

# RIGHT
resp = await http.get("https://api.example.com/data")
data = resp["json"]
```

The function containing the `await` must itself be `async def`. If you're adding an `await` to a helper, propagate the cascade all the way up to the decorated tool function. `agent-sdk validate` catches missing awaits statically.

**`time.sleep()` in an `async def`** — blocks the event loop. Use `await asyncio.sleep(...)`:

```python
import time, asyncio

# WRONG — freezes the whole worker
async def fetch_all():
    time.sleep(1)

# RIGHT
async def fetch_all():
    await asyncio.sleep(1)
```

**`http.request("POST", ...)`** — doesn't exist. Dispatch by verb:

```python
# WRONG
resp = http.request("DELETE", url)

# RIGHT
resp = await http.delete(url)
```

**BeautifulSoup** — use `lxml` with `cssselect`:

```python
# WRONG
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# RIGHT
from lxml import html
doc = html.fromstring(body)
elements = doc.cssselect("div.item")
```

**Hardcoded User-Agent** — use `http.headers()`:

```python
# WRONG
headers = {"User-Agent": "Mozilla/5.0 ..."}

# RIGHT
http.headers(ua="chrome-desktop")  # or just http.headers() — chrome-desktop is default
```

**`run_`, `op_`, `do_` prefixes on tool functions** — the engine parses Python as text and the **tool name is the function name, verbatim**. No prefix stripping. The skill id is already the namespace — don't repeat it.

```python
# WRONG — skill caller now has to say tool: "run_search_books"
@returns("book[]")
async def run_search_books(**params): ...

# RIGHT
@returns("book[]")
async def search_books(**params): ...
```

This matters for the readme `test:` block too — the YAML key must match the Python function name exactly.

**Async chain half-converted** — if a helper eventually calls `http.get/post/…`, it must be `async def` and every caller of it must `await` it. Adding `await` to a sync helper raises `SyntaxError`; forgetting `await` on an async helper silently returns a coroutine and breaks at the first `.get("ok")`. There is no middle ground.

```python
# WRONG — broken_fn will return a coroutine, caller crashes
def _fetch_one(url):
    return http.get(url)   # missing await, and enclosing fn isn't async

# RIGHT — lift everything down to http.get into async
async def _fetch_one(url):
    resp = await http.get(url)
    return resp
```

`agent-sdk validate` flags both halves. If you touch one helper in a chain, walk the chain up and down.

**No `account` on a multi-account skill** — if more than one credential row exists for a skill (e.g. Brave synced two Goodreads cookies), the engine refuses to pick. Every `run()` call must include `"account": "<name>"`. This applies even to tools that don't actually need auth.

```bash
# Check what accounts exist:
agentos call accounts '{"skill":"goodreads"}'

# Then pass one by name:
agentos call run '{"skill":"goodreads","tool":"get_book","params":{"book_id":"4934"},"account":"26631647"}'
```

## Special return keys

Tools can return special keys alongside or instead of shape data:

```python
# Store credentials (cookies, API keys) in the credential store
return {"__secrets__": [http.skill_secret(
    domain=".exa.ai",
    identifier=email,
    item_type="session",
    value={"session_token": token},
)]}

# Cache runtime state (endpoints, discovered keys) on the skill's graph node
return {"__cache__": {"graphql_endpoint": url, "api_key": key}}

# Return structured result with metadata
return http.skill_result(status="code_sent", email=email)

# Return structured error
return http.skill_error("API key expired", status=401)
```

## Testing

AgentOS tests skills against **real services**, never mocks. The bar
is the same one a human gets the first time they try a tool: "did it
come back without an error?" If it did, the tool works. If it didn't,
the skill is broken and the quality sweep notices.

Two places declare tests, one runner executes them.

### 1. Declare tests in the readme `test:` block

Every tool in a skill should have a line in the readme frontmatter's
`test:` block. The key is the tool name; the value is either
`skip: true`, `{}` (no params), or
`{ params: { … } }` with real live-service inputs.

```yaml
---
id: hackernews
# … other frontmatter …

test:
  list_posts:
    params:
      feed: front
      limit: 3
  get_post:
    params:
      id: '1'
      url: null
---
```

Real examples — same shape, different domains:

- `skills/media/hackernews/readme.md` — public API, no auth.
- `skills/macos/macos-control/readme.md` — local shell/OS skill.
- `skills/media/goodreads/readme.md` — cookie-auth + AppSync GraphQL.

### 2. `agent-sdk validate` — static checks

```bash
agent-sdk validate skills/<skill>
# or across the whole tree:
agent-sdk validate --all
```

15 static checks, including: banned imports (sandbox), missing
`await`, sync `time.sleep` in async bodies, tool-name collisions,
shape conformance of return dicts, camelCase enforcement, frontmatter
field validation. Runs automatically on `pre-commit` — you will not
commit a skill that fails these.

### 3. `_quality/bin/run_tests.py` — effectiveness sweep

The integration test runner. Walks every skill readme, calls every
tool declared in `test:` through `agentos call run`, records
pass/fail, and writes an effectiveness percentage.

```bash
python3 _quality/bin/run_tests.py --skills-dir ~/dev/agentos/skills
```

Pass = the call returned without a top-level `_error`. No assertions
on output shape. Green means the tool hit the real service and came
back with something.

Tracked over time by the quality charter (`_quality/charter.md`) as
one of three numbers (effectiveness, size, active-surface). Deletion
should not drop effectiveness. Additions should not drop it either.

### 4. `agentos test-skill` / `agentos call run` — while iterating

For single-tool debugging during development:

```bash
# Single tool, via the running engine (full boot, auth, dispatch):
agentos call run '{"skill":"goodreads","tool":"search_books","params":{"query":"dune","limit":3},"account":"26631647"}'

# All testable tools in a skill, via a lightweight harness:
agentos test-skill goodreads

# Just one op:
agentos test-skill goodreads --op search_books
```

`agentos call run` exercises the whole live stack (engine, MCP,
Python worker, SDK, auth resolution) and is the closest thing to
what a client MCP would do. Use it when `run_tests.py` flags a tool
and you need to see the actual error.

### What NOT to do

- **No unit tests, no mocks.** Every test hits the real service. This
  is a deliberate project rule (`CLAUDE.md` rule 11). A mocked test
  that passes while production breaks is worse than no test at all.
- **No assertions on output structure beyond "did not throw".** Shape
  conformance is already enforced by `agent-sdk validate` at the AST
  level; runtime assertions duplicate that and rot faster than the
  API does.
- **No test-only params.** The readme `test:` block uses the same
  params a real caller would — public IDs, real queries. If a tool
  needs auth to be useful, the quality sweep will tell you via the
  credential-missing error; add the account and rerun.

## Quick reference

| Import | What |
|--------|------|
| `from agentos import http` | HTTP client (get, post, put, patch, delete, head, client, headers, cookies) |
| `from agentos import sql` | Database queries (query, execute) |
| `from agentos import shell` | Binary execution (run) |
| `from agentos import crypto` | Crypto operations (pbkdf2, aes) |
| `from agentos import oauth` | Token exchange (exchange) |
| `from agentos import molt` | Universal text cleaner |
| `from agentos import returns, provides, connection, timeout` | Decorators |
| `from agentos import web_search, web_read, ...` | Tool constants |
| `from agentos import get_cookies, require_cookies, parse_cookie` | Cookie helpers |
| `from agentos import skill_error, skill_result, skill_secret` | Result helpers |
| `from agentos import parse_int, parse_float, parse_date` | Type parsers |
| `from agentos import iso_from_ms, iso_from_seconds` | Timestamp converters |
| `from agentos import clean_text, clean_html, strip_tags` | Text cleaners |
| `from agentos import llm` | LLM inference — see [llm.md](llm.md) |
| `from agentos import checkpoint` | Checkpoint/resume — see [llm.md](llm.md) |

## CLI commands

```bash
agent-sdk new-skill <name>         # scaffold a new skill
agent-sdk validate [dir]           # check skill for errors
agent-sdk shapes                   # list all shapes
agent-sdk shapes <name>            # show one shape's fields
```
