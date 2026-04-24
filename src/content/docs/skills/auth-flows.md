---
title: "Auth Flows"
description: "How a skill authenticates against a service — reverse-engineered HTTP replay, credential providers, and the engine's auto-relogin path."
---

> **Building a login tool for a new skill?** Start with
> [How to add login to a skill](./adding-login.md) — the
> step-by-step how-to. This page is the reference; that one is
> the recipe.

Every login flow in agentOS is **reverse-engineered HTTP replayed from
Python**. No runtime browsers; no interactive steps once the skill is
written. When a skill needs to figure out a service's login sequence
for the first time, the author captures it with CDP
(`core/bin/browse-capture.py`) against a real Chrome/Brave session,
writes the sequence as `agentos.client` calls, and deletes the capture
artifacts once replay matches byte-for-byte.

## The pattern

1. **Reverse-engineer** once, interactively, with
   [`browse-capture.py`](../reverse-engineering/overview). Record the
   login sequence, note which endpoints set cookies, which tokens ride
   on `Authorization`, and which requests need specific headers.
2. **Implement** the sequence in the skill's `.py` file with
   `agentos.client`. Declare the connection with `client="browser"` or
   `"fetch"` so UA + `Sec-CH-UA*` + `Sec-Fetch-*` headers ride every
   request automatically; the ambient Jar carries cookies.
3. **Resolve** credentials via
   `credentials.retrieve(domain, required=[...])` — walks every
   `@provides(login_credentials)` provider, vault first (local,
   ~ms, no prompt), then 1Password, macOS Keychain, and any other
   provider. The LLM never sees raw values.
4. **Store** minted tokens via the `__secrets__` envelope on the
   login tool's return. The engine upserts the row keyed on
   `(domain, identifier)`; subsequent authed tools read it as
   `params.auth.*`.
5. **Delete** the capture notes once the HTTP replay works. The code
   is the source of truth; keep CDP captures out of the repo.

## The `check_session` convention

Every cookie-auth skill declares an `account.check` tool (by convention
named `check_session`). It tells the engine **who is logged in** — so
every subsequent credential row the engine writes can be keyed by a
human-readable identifier rather than the `"default"` sentinel. The
return shape is fixed:

```python
from agentos import client, connection, returns
from agentos.identity import normalize_email, normalize_handle

connection("web",
    base_url="https://example.com",
    client="browser",
    auth={"type": "cookies",
          "domain": ".example.com",
          "account": {"check": "check_session"}})


@returns("account")
@connection("web")
async def check_session(**params) -> dict:
    resp = await client.get("/me")
    if resp["status"] != 200:
        return {"authenticated": False}

    data = resp["json"]
    email_raw  = data["email"]
    handle_raw = data["handle"]
    return {
        "authenticated": True,                    # transient signal,
                                                    # consumed by the engine,
                                                    # not persisted
        "at":            {"shape": "organization",
                          "name": "Example Inc",
                          "url":  "https://example.com"},
        "identifier":    normalize_email(email_raw),  # canonical key
        "email":         normalize_email(email_raw),
        "handle":        normalize_handle(handle_raw),
        "displayName":   data.get("name"),
        "userId":        str(data["id"]),             # "123456" — stable
                                                        # internal ID
    }
```

### The fields the engine reads

| Field             | Required | Purpose |
|-------------------|----------|---------|
| `authenticated`   | yes      | Boolean. If `False`, the engine treats cookies as dead and doesn't persist. |
| `identifier`      | yes on `authenticated: True` | **Canonical key.** The string the vault and the graph's account node join on. Email for email-login services, handle for handle-login services, `userId` as a last resort. |
| `at`              | yes on authed | The namespace that owns the identifier. Usually an inline `{shape, name, url}` dict — the engine's extraction pipeline upserts the organization/product node as a side effect of the call. |
| `email`           | opt      | Normalized via `normalize_email`. Skills that have it should populate it even if it equals `identifier`. |
| `handle`          | opt      | NFKC-casefold via `normalize_handle`. |
| `phone`           | opt      | E.164 via `normalize_phone`. |
| `displayName`     | opt      | Human-readable label. |
| `userId`          | opt      | Service's stable internal ID — never changes across rename / email swap. Use this when URLs embed a numeric account id. Free-form string; the engine doesn't parse it. |
| `metadata`        | opt      | Skill-namespaced freeform JSON for service-specific extras: `{"amazon": {"isPrime": true}}`. |

### Normalization is the skill's job

The engine stores whatever it's given. To make `Joe@Home.com` from
1Password and `joe@home.com` from a Brave cookie export collide on the
freshness arbiter, **skills canonicalise before returning**. Three SDK
helpers live in `agentos.identity`:

- `normalize_email(raw)` — lowercase local-part + IDN-punycode domain.
  No Gmail dot-stripping or plus-address stripping (unsafe on
  Workspace custom domains).
- `normalize_phone(raw, default_region=None)` — E.164 via
  `phonenumbers`. Raises on ambiguous input.
- `normalize_handle(raw)` — Unicode NFKC + casefold.

`agent-sdk validate` flags `check_session` returns that skip
normalization or use a pure-integer `identifier`.

### Return shapes the engine recognizes

- `{authenticated: True, identifier: "..."}` + typed fields — the
  canonical success case. Engine persists the credential row keyed on
  the identifier, lands the account node on the graph.
- `{authenticated: False}` — "this session is dead." Engine treats
  cookies as expired; if the skill declares a `login` tool, the
  auto-relogin intercept dispatches it.
- `{authenticated: True, identifier: None}` — engine uses cookies for
  the current request but does not persist. Legal but not
  recommended: if `check_session` can return authenticated, it should
  always yield an identifier (scrape harder if needed). Skills that
  can't reliably produce an identifier should return
  `authenticated: False` instead so the auto-relogin path kicks in.
- `check_session` raises — engine logs, uses cookies without identity,
  doesn't persist. Raise only when the skill itself detects a bug
  (markup changed, selector broke); don't raise on auth state.

### Service-specific data goes in `metadata`

Amazon's `isPrime`, Chase's credit-score summary, Spotify's product
tier — none of these land as first-class fields on `account.yaml`.
They ride in the per-skill namespace of `metadata`:

```python
return {
    "authenticated": True,
    "at":          _AMAZON,
    "identifier":  normalize_email(email),
    "metadata":    {"amazon": {"isPrime": True,
                               "marketplaceId": "ATVPDKIKX0DER"}},
    "userId":      customer_id,
}
```

Only the skill that wrote a namespace ever reads it. The engine
stores the blob opaquely.

## The `login` tool and auto-relogin

When the engine's cookie or api-key resolver can't produce a credential
for a skill call — either the store is empty (cold start) or
re-extraction yielded the same stale cookies (`NeedsRelogin`) — the
engine looks for a tool named `login` on the skill. If it finds one,
it dispatches it, waits for the fresh `__secrets__` to land, and
retries the original call once. Skills opt in by shipping a `login`
tool; nothing else is required.

### What the `login` tool looks like

The canonical shape, lifted from
[`skills/fitness/austin-boulder-project/abp.py`](https://github.com/agentos-to/skills/blob/main/fitness/austin-boulder-project/abp.py):

```python
from agentos import (
    client, connection, credentials, normalize_email,
    returns, skill_error, skill_secret,
)

@returns({"status": "string", "identifier": "string"})
@connection("public")
async def login(*, email: str = "", password: str = "", **params) -> dict:
    """Log in to the service and persist a session for reuse.

    Three resolution paths for the initial credentials:
      1. Caller passed email+password explicitly.
      2. credentials.retrieve(...) matchmakes an installed
         @provides(login_credentials) skill (1Password etc.).
      3. NeedsCredentials structured error → agent surfaces to user.
    """
    if not email or not password:
        creds = await credentials.retrieve(
            domain=".approach.app",
            required=["email", "password"],
        )
        if creds and creds.get("found"):
            val = creds.get("value") or {}
            email = email or val.get("email") or ""
            password = password or val.get("password") or ""

    if not email or not password:
        return skill_error(
            "Missing credentials for .approach.app.",
            code="NeedsCredentials",
            domain=".approach.app",
            required=["email", "password"],
        )

    # Service-specific handshake (Cognito here; OAuth / form-POST elsewhere).
    result = await _run_handshake(email, password)

    canonical = normalize_email(email)
    return {
        "__secrets__": [skill_secret(
            domain=".approach.app",
            identifier=canonical,
            item_type="login_credentials",
            value={
                "email": canonical,
                "password": password,
                "idToken": result["IdToken"],
                "refreshToken": result.get("RefreshToken"),
            },
            source="<skill-id>",
            metadata={"masked": {"password": "••••••••"}},
        )],
        "__result__": {
            "status": "authenticated",
            "identifier": canonical,
        },
    }
```

Key points:

- **`@connection("public")`** (or any connection with no auth-resolve
  step) — login *produces* credentials, so the engine can't try to
  resolve them before the body runs. Pin it to a public connection on
  the same skill.
- **`credentials.retrieve(domain, required)`** is the matchmaking
  primitive. It checks the store first; if nothing covers
  `required=[…]`, it dispatches every installed
  `@provides(login_credentials)` tool, picks the freshest hit, writes
  the row, and returns.
- **`skill_error(code="NeedsCredentials", …)`** is how login signals
  "no provider matched." The engine's auto-relogin intercept detects
  this shape and stops — no infinite retries, and the original auth
  failure surfaces to the agent with the structured `required` list
  so it can ask the user for exactly what's missing.
- **`__secrets__` landing** — return a list of
  [`skill_secret(...)`](#secret-safe-credential-return) envelopes.
  The engine's writeback path stamps `last_verified = now()` and
  upserts on `(domain, identifier, item_type)`, so a fresh login
  always ranks above a stale provider row on the next `get_best`.

### How authed tools read the result

For **`auth.type: "api_key"`** connections, the store row's `value`
fields splat onto `params.auth` on the next dispatch. The ABP login
writes `{email, password, idToken, refreshToken}`; authed tools read:

```python
@connection("portal")
async def book_class(**params) -> dict:
    token = params["auth"]["idToken"]
    resp = await client.post(
        f"{PORTAL_API}/bookings/...",
        headers={"Authorization": token},
        json={...},
    )
```

For **`auth.type: "cookies"`**, login writes cookies into the ambient
Jar (or returns a `__cookie_delta__`); authed tools just use
`client.get/post`, and the engine injects cookies automatically.

### Engine side — the auto-relogin intercept

The engine's
[`executor.rs::try_auto_relogin_and_retry`](https://github.com/agentos-to/core/blob/main/crates/core/src/skills/executor.rs)
wraps every tool dispatch:

1. Skill call fails with `AuthFailed` or `NeedsRelogin`.
2. Engine looks up the skill's `login` tool. If none, bubble the
   error.
3. Dispatch `login` with empty params (caller's creds aren't in
   scope; `credentials.retrieve` is expected to find them). Run the
   result's `__secrets__` writeback so the new row lands.
4. If `login` returned a `skill_error(...)` dict (NeedsCredentials
   etc.), surface the original error — no retry, no loop.
5. Otherwise retry the original tool once with `account=None` so
   `resolve_credential` picks the freshly-written row. Return the
   retry's result.

One login, one retry, no cascades. Tools that aren't `login` never
chase themselves.

### When does it fire?

- **Cold start** — store empty, first authed call triggers login.
- **Stale cookie session** — the cookie-auth retry loop re-extracts
  from browser providers; if the extraction returns identical-to-
  failed cookies, `NeedsRelogin` fires and the same intercept
  dispatches login.
- **Token expiry** — Cognito/JWT tokens expire; next authed call
  returns 401, falls into `AuthFailed`, and login mints a fresh one.

### Credential providers

A provider skill declares `@provides(login_credentials)` (or
`@provides(password)` / `@provides(api_key)`) and accepts `domain`
plus optional `account`:

```python
from agentos import (
    connection, login_credentials, normalize_email,
    provides, returns, shell, skill_secret,
)

@returns({"provided": "boolean", "identifier": "string"})
@provides(login_credentials, description="...")
@connection("local")
async def get_credentials(*, domain: str, account: str | None = None, **params) -> dict:
    match = await _find_for_domain(domain)
    if not match:
        return {"provided": False}
    email, password = match
    canonical = normalize_email(email) if "@" in email else email
    return {
        "__secrets__": [skill_secret(
            domain=domain,
            identifier=canonical,
            item_type="login_credentials",
            value={"email": canonical, "password": password},
            source="<skill-id>",
            metadata={"masked": {"password": "••••••••"}},
        )],
        "__result__": {"provided": True, "identifier": canonical},
    }
```

`@provides(login_credentials)` takes no `domains=` list — password
managers hold creds for arbitrary services. The engine calls every
installed provider with the target domain at dispatch time, same
pattern the cookie providers use.

Reference implementations:

- **`vault`** — a system skill (Rust, `crates/capabilities/src/vault.rs`), not an installable skill. Exposes the local vault (`agentos.db` `credentials` table, AES-256-GCM at rest, key in macOS Keychain) as a `@provides(login_credentials)` provider. Always tried first: ~ms, no prompts. Read-only; only returns what other providers have persisted.
- [`skills/secrets/onepassword/`](https://github.com/agentos-to/skills/tree/main/secrets/onepassword) — wraps the `op` CLI, returns 1Password Login items. Consulted on a vault miss; its `__secrets__` writeback populates the vault, so subsequent calls bypass it.
- [`skills/macos/macos-keychain/`](https://github.com/agentos-to/skills/tree/main/macos/macos-keychain) — wraps `security find-internet-password`.

### The end-to-end story, once

Joe says *"book me a 6pm class at ABP."* Cold state — no row for
`.approach.app` in the vault, not logged into Brave.

1. `abp.book_class` → engine resolves the `portal` connection's
   api_key auth → store miss → `AuthFailed`.
2. Engine intercept: ABP declares a `login` tool → dispatch
   `abp.login` with empty params.
3. ABP `login` calls
   `credentials.retrieve(".approach.app", required=["email", "password"])`.
4. SDK walks providers, vault first: `vault.get_credentials(domain=".approach.app")`
   → `auth_store.read` → store miss (cold state). Vault returns
   `{provided: false}`, SDK falls through.
5. Next provider: `onepassword.get_credentials(domain=".approach.app")`
   runs, `op item list --categories Login` finds the ABP Login item,
   returns `{email, password}` via `__secrets__`. The engine persists
   the row; future calls go through the vault directly.
6. The SDK reads the freshly-written row by identifier, returns
   `{found, value, identifier, source: "onepassword"}` to ABP's
   `login`.
6. ABP `login` runs Cognito `USER_PASSWORD_AUTH` → `IdToken`.
7. ABP `login` returns another `__secrets__` envelope with
   `{email, password, idToken, refreshToken}`; engine writes the row
   keyed on `(.approach.app, abp@contini.co, login_credentials)`.
8. Engine retries `abp.book_class` with `account=None`;
   `resolve_credential` picks the freshly-written row; `params.auth.idToken`
   rides as `Authorization`; Tilefive 200 OK; class booked.

Joe never pasted the password. The LLM never saw it. Adding
`macos-keychain` later is orthogonal — the freshness arbiter picks
whichever provider returned first.

## The `logout` tool and server-side revoke

`check_session`, `login`, and `logout` are the three legs of the
account protocol — they belong in every cookie/api_key/oauth skill,
together. `check_session` asks "who is this session?"; `login`
establishes a new session; `logout` ends one.

Agents trigger logout through the engine:

```bash
agentos call accounts '{"action":"logout","skill":"austin-boulder-project"}'
# → {
#     "revoked_server_side": true,
#     "revoke_result": {"ok": true, "message": "Cognito session revoked."},
#     "rows_removed": 1
#   }
```

The engine walks the declared `account.logout` op, dispatches it with
the live session injected as `params.auth.*` (so the skill can hit
the revoke endpoint with the tokens it needs to kill), then runs
the cleanup tail: delete credential rows where `source == skill_id`,
invalidate the session cache. Provider rows — the 1Password /
Keychain rows that hold the password — are deliberately untouched.
Logout forgets the session, not the password.

### Declaring `logout` on the connection

Extend the connection's `auth.account` block with a `logout` slot:

```python
connection("portal",
    base_url="https://portal.api.prod.tilefive.com",
    domain=".approach.app",
    client="api",
    auth={"type": "api_key",
          "account": {"check":  "check_session",
                      "login":  "login",
                      "logout": "logout"}},
    label="ABP Portal Session")
```

Same pattern for `cookies` and `oauth` auth types. All three
slots are just operation names on the same skill — the engine
finds the op by name and runs it.

### What the `logout` tool looks like

Canonical shape, lifted from ABP's Cognito implementation:

```python
@test.skip(reason="destructive — revokes the live session")
@returns({"ok": "boolean", "message": "string"})
@connection("portal")
async def logout(**params) -> dict:
    """Revoke the current Cognito session via GlobalSignOut.

    GlobalSignOut invalidates every IdToken / AccessToken for this
    user across all devices — the correct "log out" semantic. After
    it returns, every access token dies within its natural TTL
    (~1h for Cognito); every refresh token is dead immediately.

    Engine runs the cleanup tail (delete skill rows, invalidate
    cache) after this returns, so no `__secrets__` here.
    """
    auth = params.get("auth") or {}
    access_token = auth.get("accessToken")
    if not access_token:
        # No live session to revoke — engine's cleanup still runs.
        return {"ok": False, "message": "No live token; skipped revoke."}

    resp = await client.post(
        COGNITO_ENDPOINT,
        json={"AccessToken": access_token},
        headers={
            "Content-Type": "application/x-amz-json-1.1",
            "X-Amz-Target": "AWSCognitoIdentityProviderService.GlobalSignOut",
        },
    )

    # Already-revoked tokens return NotAuthorizedException —
    # that's "done," not "failed."
    if resp["status"] == 200:
        return {"ok": True, "message": "Cognito session revoked."}
    j = resp.get("json") or {}
    if (j.get("__type") if isinstance(j, dict) else None) == "NotAuthorizedException":
        return {"ok": True, "message": "Session already expired."}
    return {"ok": False,
            "message": f"Revoke failed: HTTP {resp['status']}"}
```

Key points:

- **Runs on the authed connection**, not `public`. The revoke
  endpoint needs the live session to prove who's logging out.
- **Engine owns the cleanup tail.** The skill doesn't delete rows
  or clear cache — it does the service call and returns
  `{ok, message}`. Keeps skills focused; keeps cleanup uniform.
- **No `__secrets__` return.** Returning one is a no-op; the
  engine treats logout as a "forget," not a "store" flow.
- **Idempotent.** A second logout call finds no access token and
  returns `ok: false` honestly — the engine reports
  `revoked_server_side: false`, no lie about the service call.
- **Failing revoke doesn't block cleanup.** If the revoke call
  errors out (network, expired token, service down), the engine
  *still* deletes the local rows. Rationale: the user asked to
  log out; tokens need to be gone locally regardless of whether
  the server got the message. The failure surfaces in the
  response.

### Why server-side revoke matters

Two places "logout" can happen:

- **Client-side only.** Delete our copy of the cookie/token. Fast,
  offline, obvious — *but the token is still valid at the service*.
  Anyone with a copy (leaked DB backup, stolen laptop, malware)
  can keep using it until natural expiry: 30+ days for Cognito,
  indefinite for OAuth refresh tokens, whatever the service set
  for cookies.
- **Server-side revoke.** Tell the service "end this session." For
  cookies this usually hits `/logout`; for JWT/OAuth it's the
  revoke endpoint; for Cognito it's `GlobalSignOut`. Now the
  token is dead wherever it was copied to.

AgentOS's threat model makes this load-bearing.
`~/.agentos/data/agentos.db` holds every session the engine has
collected. If that file walks out the door, every session in it is
live until natural expiry — unless the service was told to revoke.
Without a `logout` tool, your logout is cosmetic: good for
"switching accounts," inadequate for "my laptop was stolen and I
want to kill everything."

That's why every cookie/api_key/oauth skill should ship a `logout`
tool. The validator warns when a connection declares
`account.login` without `account.logout` — a warning, not an
error, during the migration window while existing skills catch up.

### `logout` vs `clear_session` vs `remove`

Three engine verbs, ordered by scope of destruction:

| Verb | Engine action | Server called? |
|---|---|---|
| `accounts({action:"logout",        skill})` | Calls the skill's `logout` op, **then** deletes rows where `source == skill_id` + invalidates cache. | Yes (when the skill declares a `logout` op) |
| `accounts({action:"clear_session", skill})` | Deletes rows where `source == skill_id` + invalidates cache. No skill dispatch. | No |
| `accounts({action:"remove",        skill})` | Deletes **every** credential row for the domain, including provider rows (1Password, Keychain). | No |

`clear_session` is the honest "I just want to forget the session
locally" — debugging, rotating, clearing a bad cache. `logout` is
the same plus the service call. `remove` is the nuclear option
for "I'm done with this account entirely."

Skills without a `logout` op can still be logged out via
`clear_session`: the cleanup tail is the same; only the server-side
call is missing. So adding `logout` is always an upgrade over the
baseline — never a regression.

## Dashboard connections

Skills with web dashboards declare a `dashboard` connection alongside their `api` connection. Connections are declared at **module level** in Python; see [Connections & Auth](./connections.md) for the full surface.

```python
from agentos import connection

connection("api",
    base_url="https://api.example.com",
    auth={"type": "api_key", "header": {"x-api-key": ".auth.key"}})

connection("dashboard",
    base_url="https://dashboard.example.com",
    auth={"type": "cookies",
          "domain": ".example.com",
          "login": [{"sso": "google"}, {"email_link": True}]})
```

All auth goes under a single `auth=` dict with a `type` discriminator (`api_key`, `cookies`, `oauth`). The `login` entry declares available login methods. Login tools are Python functions that execute the flow with `agentos.http`.

## Secret-safe credential return

Login and API key extraction operations return credentials via `__secrets__`:

```python
def get_api_key(*, _call=None, **params):
    # ... HTTPX calls to get the key ...
    return {
        "__secrets__": [{
            "issuer": "api.example.com",
            "identifier": "user@example.com",
            "item_type": "api_key",
            "label": "Example API Key",
            "source": "example",
            "value": {"key": api_key},
            "metadata": {"masked": {"key": "••••" + api_key[-4:]}}
        }],
        "__result__": {"status": "authenticated", "identifier": "user@example.com"}
    }
```

The engine writes `__secrets__` to the vault, creates an account entity on the graph, and strips the secrets before the MCP response reaches the agent.

## Cookie resolution chain

The engine uses **timestamp-based resolution** — all cookie sources are checked, and the one with the newest cookies wins. There's no fixed priority order. See `connections.md` → Resolution Algorithm for the full explanation with worked examples.

**Sources (all checked on every resolve):**

1. **In-memory cache** — cookies from the last extraction, updated by `Set-Cookie` responses from our own HTTP requests (writeback). Can be *newer* than the browser when a server rotates tokens.
2. **Browser providers** (Brave, Firefox) — fresh extraction from the browser's local cookie database (~20ms). Reflects the user's latest browsing.
3. **Credential store** (`credentials.sqlite`) — persistent copy, also updated by writeback. Survives engine restart.

The candidate with the highest `newest_cookie_at` (latest per-cookie timestamp) wins. On ties, the cache wins (first candidate). No TTL — timestamps are the only arbiter.

### Provider scoring (within the provider tier)

When multiple browser providers return cookies for the same domain:

1. **Required names** — providers with all cookies listed in `auth.names` score highest
2. **Creation timestamp** — most recently created cookies win
3. **Cookie count** — final tiebreaker

### Retry on auth failure

On `SESSION_EXPIRED:` prefix (or Python exceptions containing `401`, `403`,
`unauthorized`, `forbidden`), the engine:

1. Marks the current provider as failed
2. Excludes it from the candidate list
3. Re-runs provider selection — next-best provider wins
4. Retries the operation once with the new provider's cookies

If that retry returns identical cookies to the ones that just failed,
the engine raises `NeedsRelogin` and falls into the auto-relogin
intercept above. One retry per layer — no infinite loops.

### Providers always return the full cookie jar

The `names` field in connection auth is purely a **selection hint** — it helps
the engine choose the right provider. Providers always return all cookies for the
domain, never a filtered subset. Skills that need the full cookie jar (which is
most of them) work correctly regardless of whether `names` is declared.

## Key rules

- **Reverse-engineer with CDP, replay with HTTP.** Interactive capture
  is one-time, during skill authoring; the shipped skill must replay
  the sequence byte-for-byte in pure Python with `agentos.client`.
  Delete the capture notes once the replay works — the code is the
  source of truth.
- **Never drive a browser at runtime.** No Playwright, no CDP, no
  headless Chrome. If a step can't be replayed from Python, the
  answer is to keep reverse-engineering until it can.
- **All I/O through SDK modules.** `client.get/post`, `shell.run`,
  `sql.query`. Never `urllib`, `subprocess`, `sqlite3`, `requests`,
  `httpx`.
- **Never expose secrets in `__result__`.** Secrets go in
  `__secrets__` only. The agent sees masked versions via
  `metadata.masked`.
- **Cross-skill auth goes through the engine, not the agent.** When
  a login tool needs credentials, it calls
  `credentials.retrieve(domain, required=[...])` — the engine
  matchmakes installed `@provides(login_credentials)` skills. The
  agent isn't in the loop.

## Multi-step flows (email codes, SMS, OAuth consent)

Some logins need an input the skill can't obtain from its own
credential row — a verification code from email, an SMS code, an
OAuth consent redirect. The skill exposes the flow as separate tools
and lets the agent orchestrate:

```
Agent calls skill.send_login_code({ email })
  → agentos.client: CSRF + trigger verification email
  → Returns: { status: "code_sent", hint: "subject 'Sign in to …'" }

Agent reads email via any @provides(email_lookup) skill, extracts code.

Agent calls skill.verify_login_code({ email, code })
  → agentos.client: submit code, capture Set-Cookie / token
  → Returns { status: "authenticated", identifier }
  → __secrets__ lands the session row via the usual writeback path.
```

The `hint` field tells the agent what to search for. It never
hard-codes "use Gmail" — any email skill works because they all
`@provides(email_lookup)`.

### When to use this pattern

- Email verification codes (NextAuth, WorkOS, etc.).
- SMS / TOTP verification.
- OAuth consent that requires user approval.

### Reference implementations

- [`skills/web/exa/exa.py`](https://github.com/agentos-to/skills/blob/main/web/exa/exa.py) — NextAuth email-code flow.
- [`skills/fitness/austin-boulder-project/abp.py`](https://github.com/agentos-to/skills/blob/main/fitness/austin-boulder-project/abp.py) — Cognito password login, single tool.

## See also

- [How to add login to a skill](./adding-login.md) — step-by-step recipe for wiring a new service's login flow.
- [Reverse engineering overview](../reverse-engineering/overview) — CDP capture methodology (one-time, during skill authoring).
- [Connections](./connections.md) — auth types (`cookies`, `api_key`, `oauth`), connection-level `domain:` override, per-connection `client=` bundles.
