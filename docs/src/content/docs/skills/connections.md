---
title: "Connections & Auth"
description: "Skills declare their external service dependencies as module-level connection() calls in Python. Each connection carries base_url, auth, optional description, label, help_url, and local data sources."
---

A **connection** is how a skill reaches an external service (HTTP API, OAuth-
protected endpoint) or a local data source (SQLite file, app cache). Every
skill declares its connections at **module level** in Python. There is no
`connections:` YAML frontmatter block — the engine reads Python.

## The shape

```python
# skills/your-skill/your_skill.py
from agentos import connection

connection("api",
    base_url="https://api.example.com/v1",
    auth={"type": "api_key",
          "header": {"x-api-key": ".auth.key"}},
    label="API Key",
    help_url="https://example.com/api-keys")
```

Each call to `connection(...)` at module scope registers one named connection
on the skill. Tools bind to a connection with the `@connection("name")`
decorator. Skills with exactly one connection auto-infer; tools on
multi-connection skills must tag the connection they use.

```python
from agentos import connection, http, returns

connection("api",
    base_url="https://api.example.com/v1",
    auth={"type": "api_key", "header": {"x-api-key": ".auth.key"}})


@returns("post[]")
@connection("api")
async def list_posts(**params):
    return (await http.get("/posts"))["json"]
```

## Common patterns

**Single API-key connection** — the most common shape:

```python
connection("api",
    base_url="https://api.example.com/v1",
    auth={"type": "api_key",
          "header": {"x-api-key": ".auth.key"}},
    label="API Key",
    help_url="https://example.com/api-keys")
```

**Public + authed** — two identities against the same service:

```python
connection("graphql",
    base_url="https://api.example.com/graphql")

connection("web",
    auth={"type": "cookies", "domain": ".example.com"})
```

**Multi-backend** — same data, different transports (SDK + CLI):

```python
connection("sdk",
    description="Python SDK — typed models, batch ops, biometric auth",
    vars={"account_name": "my-account"})

connection("cli",
    description="CLI tool — stable JSON contract, fallback path",
    vars={"binary_path": "/opt/homebrew/bin/mytool"})
```

When connections differ by transport rather than service, a tool can name
either: `@connection(["sdk", "cli"])`. The caller picks the effective
connection; the first entry is the default. Tool bodies see the resolved
name in `params["connection"]`.

## Rules

- `base_url` resolves relative URLs in `http.get(...)` / `http.post(...)`.
- Single-connection skills auto-infer: no `@connection` decorator needed.
- Multi-connection skills must decorate every public tool.
- A tool that should skip auth entirely uses `@connection("none")` (or omits
  auth by virtue of its connection having no `auth=` dict).
- `optional=True` on a connection means the skill works anonymously but
  improves with credentials.
- Connections without any auth (just `base_url` / `sqlite` / `vars`) are
  valid — they serve as service declarations.

**Naming conventions.** Connection names are arbitrary, but three are common:

- `api` — REST API with key or token auth.
- `graphql` — GraphQL / AppSync (may or may not carry auth).
- `web` — cookie-authenticated website (user session).

## Auth types

The `auth=` dict carries a `type` discriminator. Three types are supported.

**`api_key`** — static keys or tokens injected via `header`, `query`, or
`body` templates. Values are jaq expressions evaluated against the
credential blob:

```python
connection("api",
    auth={"type": "api_key",
          "header": {"Authorization": '"Bearer " + .auth.key'}},
    label="API Key")
```

**`cookies`** — session cookies resolved from the credential store (for
stored sessions) or provider skills (Brave, Firefox):

```python
connection("web",
    auth={"type": "cookies",
          "domain": ".claude.ai",
          "names": ["sessionKey"]})
```

**`oauth`** — OAuth 2.0 refresh and provider-based acquisition:

```python
connection("gmail",
    auth={"type": "oauth",
          "service": "google",
          "scopes": ["https://mail.google.com/"]})
```

### Resolution algorithm

Cookie auth uses **timestamp-based resolution** — every source is checked,
the one with the newest cookies wins. No fixed priority order, no
TTL-based expiry.

Three cookie sources exist, each with different freshness characteristics:

| Source | What it is | Freshness |
|---|---|---|
| Credential store | Persisted cookies in `~/.agentos/data/agentos.db` | Age of last persisted write |
| Browser provider (Brave/Firefox) | Live cookies read from the user's profile | Always current — the browser is the source of truth |
| Playwright | Cookies from an engine-driven headless browser | Fresh per capture |

## Local data sources

Connections can point at local files instead of (or in addition to) remote
services.

```python
connection("db",
    sqlite="~/Library/Messages/chat.db",
    vars={"account_email": "me@example.com"})
```

- **`sqlite=`** — tilde-expanded path to a SQLite file. `sql.query(...)`
  uses this path when the calling tool is bound to this connection.
- **`vars=`** — non-secret config merged into the executor context. Scripts
  read these via `params["connection"]["vars"]` without hardcoding paths.

Skills that are purely local (no external services) declare their
connection the same way — just omit `base_url` and `auth`.

## How the engine reads it

At first dispatch of any tool in the skill, the engine walks the skill's
`.py` files, finds every module-level `connection(...)` call, and extracts
the literal kwargs into the skill's in-memory `Connection` map. Subsequent
dispatches hit the cache. `connection(...)` is a runtime no-op — the
engine never executes Python to populate connections; it reads the AST.

This means connection declarations **must use literals** for auth dicts,
URLs, and labels. You can't write `base_url=os.environ["X"]` at module
top — the AST walker doesn't evaluate Python expressions. Secrets belong
in the credential store, not in source; skills reference them via the
jaq expressions in `auth.header` / `auth.query` / `auth.body`.
