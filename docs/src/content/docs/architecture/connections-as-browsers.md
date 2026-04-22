---
title: "Each connection is a client — a browser, a fetch, or an API"
description: Each skill connection is a sandboxed identity profile with its own cookie jar, its own auth, and its own kind of client. Tools on different connections never share state; tools on the same connection always do. The credential store is the vault; the per-call jar is a briefly-opened wallet.
---

A **connection** is how a skill reaches a service: a REST API, a cookie-
authed dashboard, a local SQLite file. This page is about the
architectural shape of connections — what makes them isolated, why
that isolation is by construction rather than by policy, and how the
ambient cookie-jar mechanism works without the skill author ever
touching cookies.

For the surface (what a skill author writes), see [Connections &
Auth](/skills/connections/). For the resolution algorithm (how the
engine picks the freshest cookie when multiple sources offer
candidates), see [Auth resolution](/architecture/auth-resolution/).
This page is the middle layer: **what a connection *is*.**

## The mental model

Each connection is a **sandboxed identity profile** paired with a
kind of client. The profile decides three things:

- **Client kind** — `"browser"`, `"fetch"`, or `"api"`. Picks the
  HTTP personality (header bundle, cookie behavior).
- **Identity** — cookies, API key, OAuth tokens, or none. What makes
  a request "authenticated."
- **Scope** — the `(domain, identifier)` key under which this
  connection's credentials live in the store.

Tools bind to a connection with `@connection("portal")`. Inside the
tool body, plain `client.get("/x")` does the right thing because the
connection owns the kind and the auth. **Skill code never threads
cookies, tokens, or browser headers.**

Two tools on *different* connections — even in the same skill — are
separate browser profiles. Two tools on the *same* connection share
state. Simple rule, enforced structurally.

## Credentials key on `(domain, identifier)`, not `(skill, connection_name)`

The credential store is keyed on who the identity *is*, not which
skill is asking for it.

```
credentials (SQLite row):
  domain       ← derived from the connection's base_url (or explicit domain=)
  identifier   ← account key within that domain (email, userId, customerId)
  item_type    ← cookies | api_key | oauth
  value        ← encrypted blob (AES-256-GCM)
```

**Domain derivation** (`crates/auth/src/domain.rs`):

1. Explicit `domain=` on the `connection(...)` call wins.
2. Otherwise, the registrable domain of `base_url` — `host_from_url`
   collapses `api.exa.ai`, `dashboard.exa.ai`, and `auth.exa.ai` into
   one namespace: `exa.ai`.
3. Fallback: the skill id.

### Why not key on `(skill, connection_name)`?

Imagine 20 skills declaring a connection named `portal`. Some point
at `tilefive.com`, some at `exa.ai`, some at `amazon.com`. The name
`portal` is a **local label inside the skill** — arbitrary, not
globally meaningful. Two skills shouldn't collide just because their
authors both picked a reasonable short name.

Keying on the derived domain instead gives four properties:

1. **One source of truth per identity.** Log into `claude.ai` once;
   every skill talking to Claude sees the same session.
2. **Skill rename / move is safe.** Reorganize `amazon.py` into a
   nested folder, rename its `web` connection to `account` — the
   cookies don't move because they're keyed on `amazon.com`.
3. **Subdomain sprawl collapses naturally.** `api.exa.ai` and
   `dashboard.exa.ai` share the `exa.ai` namespace; the `api`
   connection's key-auth row and the `dashboard` connection's
   cookie row live alongside each other as different `item_type`s.
4. **Multiple accounts within a domain stay separate.** Joe's
   Goodreads and Jane's Goodreads are distinct rows (`goodreads.com`
   + `26631647` vs `goodreads.com` + `19887766`). Same connection
   name, totally isolated.

The connection name is a *local label*. The domain is the *identity
namespace*. That's the architecture.

## Two jars, one for persistence, one for a single call

Cookies live in two places simultaneously. Understanding which jar
holds what is the key to the whole model.

```
┌────────────────────────────────────────────────────────────┐
│ Credential store                                           │
│ ─────────────────                                          │
│ Rust, SQLite at ~/.agentos/data/agentos.db                 │
│ Encrypted at rest (AES-256-GCM, key in macOS Keychain)     │
│ Rows keyed by (domain, identifier, item_type)              │
│ Persistent — survives engine restart, machine reboot       │
│ The vault.                                                 │
└────────────────────────────────────────────────────────────┘
            ↑ (write delta back on tool exit)
            │
            │ (seed on tool entry)
            ↓
┌────────────────────────────────────────────────────────────┐
│ Per-call jar                                               │
│ ─────────────                                              │
│ Python, ContextVar inside the SDK                          │
│ Plaintext — only in the Python worker's memory             │
│ Lives for exactly one tool invocation                      │
│ The briefly-opened wallet.                                 │
└────────────────────────────────────────────────────────────┘
            ↑         ↓
            │         │
      (read)          (append)
            │         │
            ↓         ↓
┌────────────────────────────────────────────────────────────┐
│ client.get / client.post calls inside the tool body            │
└────────────────────────────────────────────────────────────┘
```

### Lifecycle of one tool call

Concretely, with ABP's `book_class` on the `portal` connection:

1. **Tool entry.** Engine resolves cookies for
   `(tilefive.com, joe@contini.co)` from the credential store.
   Decrypts in memory, hands to the Python worker as
   `params["auth"]["cookies"]`.
2. **SDK seeds the per-call jar.** The Python worker builds a
   ``Client(connection=…, jar=Jar.from_seed(cookies))`` and sets it
   on ``_current_client`` — one ContextVar scoped to this tool call.
3. **Tool body runs.** `client.post("/bookings", json=...)`. Inside
   ``client._request``, the SDK reads ``_current_client``, pulls the
   outbound `Cookie:` header from ``jar.cookie_header_for(url)``,
   composes the per-kind header bundle, sends it.
4. **Response comes back.** SDK parses `Set-Cookie` headers and calls
   ``jar.ingest(url, set_cookie)`` — the same live jar, mutated in
   place.
5. **Tool body returns.** SDK snapshot-diffs ``jar._live`` vs
   ``jar._seed`` and appends ``__cookie_delta__: {added, changed,
   removed}`` to the return dict.
6. **Engine receives the delta.** Upserts the new cookie values into
   the credential store row (`domain=tilefive.com`,
   `identifier=joe@contini.co`). Row is now updated.
7. **Per-call jar dies.** ContextVar goes out of scope. Plaintext
   cookies no longer exist anywhere in memory.

Next time anyone calls `book_class` or `get_my_memberships` on the
`portal` connection, step 1 reads the **updated** cookies.
Session tokens that rotate on every request stay current
automatically, across processes and engine restarts.

### Why two jars and not one?

Because they have different lifetimes and different security
requirements:

- The credential store must persist across restarts → must be on
  disk → must be encrypted.
- The per-call jar must be fast to read/write during a tool body
  → must be in-process → lives in memory only.

Copying the credential row into memory for the duration of the call,
then writing the diff back, gives us both: fast access during work,
no plaintext on disk at rest.

## Three client kinds

A connection picks one of three client kinds. The kind decides cookie
behavior and header personality.

| `client=` | Cookie jar | Headers | When to use |
|---|---|---|---|
| `"browser"` | Yes — full per-call jar, Set-Cookie writeback | Navigate bundle (`Sec-Fetch-*`, `Upgrade-Insecure-Requests`, UA, `Sec-CH-UA`) | Cookie-authed dashboards, site scraping, login flows |
| `"fetch"` | Yes — same as browser | XHR bundle (`Sec-Fetch-Mode: cors`, no nav headers) | AJAX-style API calls a real browser's JS would make |
| `"api"` (default) | No jar. Stateless. | None added — caller passes any needed headers | REST APIs with key or token auth |

Individual tools can override with `client="..."`, `incognito=True`, or
extra `headers=` on the HTTP call — rare, maybe 5% of tools. 95%
inherit from the connection.

## What this replaces

Before this model landed, skills carried cookies manually:

```python
# BEFORE — the skill threads cookies everywhere
async def list_api_keys(**params):
    cookie_header = require_cookies(params, "list_api_keys")
    async with http.client(cookies=cookie_header, http2=False,
                           **http.headers(accept="json")) as c:
        resp = await c.get("/api/keys")
    return parse(resp)
```

Now:

```python
# AFTER — the connection owns the client kind and the jar
connection("dashboard",
    base_url="https://dashboard.exa.ai",
    client="browser",
    auth={"type": "cookies", "domain": ".exa.ai"})

@connection("dashboard")
async def list_api_keys(**params):
    resp = await client.get("/api/keys")
    return parse(resp["json"])
```

The skill shrinks. The engine doesn't grow. The cookie-auth `Set-Cookie`
roundtrip that used to require a session context manager happens
automatically because the per-call jar is ambient to every HTTP call
the tool body makes.

## Why this is secure by construction

- **Tools on different connections cannot see each other's cookies.**
  Different connections → different `(domain, identifier)` keys →
  different rows → different in-memory jars. There's no code path
  that would let one jar read the other.
- **A compromised skill cannot reach across identities.** It can
  only touch the credential row its resolved connection maps to. It
  can't enumerate rows, can't open a jar for a different domain.
- **Plaintext lives for seconds, in one process.** The per-call jar
  dies with the tool call. The Python worker's memory pages get
  reused; no persistent plaintext exists.
- **Encryption at rest covers every identity.** Same AES-256-GCM
  path for API keys, cookies, OAuth tokens. No connection type has
  a weaker storage path.

## Related

- [Security](/architecture/security/) — the broader invariants (skill
  decoupling, engine refuses to know entity types, credentials
  encrypted at rest).
- [Auth resolution](/architecture/auth-resolution/) — the algorithm
  the engine uses to pick the freshest cookie when store, cache,
  and browser providers all offer candidates for the same
  `(domain, identifier)`.
- [Connections & Auth (skill author's view)](/skills/connections/) —
  the surface. What the `connection(...)` call looks like, what
  `client=` does, which auth types are supported.
