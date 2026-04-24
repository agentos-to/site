---
title: "How to add login to a skill"
description: "Step-by-step walkthrough for wiring a new service's login flow into a skill. Copy-pasteable templates, the three credential resolution paths, common gotchas."
---

Your skill talks to a service that requires a login. This page
walks through adding a `login` tool to that skill so the engine
can auto-authenticate on cold start and auto-re-login on session
expiry — without the user pasting a password into settings.

Skip to [Reference implementations](#reference-implementations) if
you just want to copy an existing skill and adapt it.

For the *why* behind every step, see
[Auth flows](./auth-flows.md) — this page is the how-to; that
page is the reference.

## The 7-step recipe

### 1. Split the connection into `public` and authed

The `login` tool needs to *produce* credentials, so it can't run
on a connection that requires them. Use `@connection("public")`
for `login` and any other pre-auth endpoints (e.g. the ones that
set CSRF cookies).

```python
connection(
    "public",
    base_url="https://accounts.example.com",
    client="fetch")                         # no auth; login posts here

connection(
    "portal",
    base_url="https://api.example.com",
    client="fetch",
    auth={"type": "cookies",
          "domain": ".example.com",
          "account": {"check": "check_session"}},
    optional=True,
    label="Example Portal Session",
    help_url="https://example.com/login")
```

Authed tools (`get_orders`, `book_thing`, etc.) go on `portal`;
`login` and `check_session` go on `public`.

### 2. Reverse-engineer the login HTTP sequence

This is the manual step. See
[Reverse engineering — auth](./reverse-engineering/3-auth/). The
summary:

1. Open the service's login page with `browse-capture.py`.
2. Click through the real login flow while capturing network
   traffic.
3. Identify the POST(s) that establish the session. Note which
   endpoints set which cookies and which tokens ride on
   `Authorization`.
4. Delete the capture artifacts when you're done — the Python
   code is the source of truth.

**Be a user.** Start at `https://www.example.com` — the canonical
homepage — and follow the prompts to the login page the way any
visitor would. Don't try to guess the "internal" signin URL;
services like Amazon return anti-bot error pages when you hit
`/ap/signin` directly without the `openid.return_to=...` params a
real browser would build. Clicking the homepage's "Sign In" link
lets the site construct the correct URL itself, and you get a
realistic request chain to replay.

Most logins are one of three shapes:

- **Form POST.** `POST /login` with username+password form data;
  `Set-Cookie: session=...` comes back.
- **OAuth / Cognito / SAML.** One or two POSTs to an identity
  provider; an `IdToken` / session cookie lands on the portal
  host on a follow-up call.
- **OTP / magic link.** Two tools: `send_login_code` + then
  `verify_login_code`. See Exa for the template.

All three are just HTTP. You never run a browser at runtime.

### 3. Write the `login` tool

Copy this template, swap the handshake body for what you learned
in step 2:

```python
from agentos import (
    client, connection, credentials, normalize_email,
    returns, skill_error, skill_secret,
)

@returns({"status": "string", "identifier": "string"})
@connection("public")
async def login(*, email: str = "", password: str = "", **params) -> dict:
    """Log in to Example and persist a session for reuse.

    Resolves credentials in this order:
      1. Caller passed email+password explicitly.
      2. credentials.retrieve() matchmakes an installed
         @provides(login_credentials) skill (1Password, Keychain).
      3. No match → NeedsCredentials structured error.
    """
    # --- Resolve credentials ---------------------------------------
    if not email or not password:
        creds = await credentials.retrieve(
            domain=".example.com",
            required=["email", "password"])
        if creds and creds.get("found"):
            val = creds.get("value") or {}
            email    = email    or val.get("email")    or ""
            password = password or val.get("password") or ""

    if not email or not password:
        return skill_error(
            "Missing credentials for .example.com.",
            code="NeedsCredentials",
            domain=".example.com",
            required=["email", "password"],
            help_url="https://example.com/login")

    # --- Run the reverse-engineered handshake ----------------------
    # Replace with whatever step 2 revealed. Cookies the service
    # sets via `Set-Cookie` land automatically in the ambient Jar;
    # the engine's __cookie_delta__ sideband persists them on return.
    resp = await client.post(
        "/login",
        json={"email": email, "password": password})
    if resp["status"] != 200:
        return skill_error(f"login failed: HTTP {resp['status']}",
                           code="AuthFailed")

    # --- Return the identity + any tokens that aren't cookies ------
    canonical = normalize_email(email)
    return {
        "__secrets__": [skill_secret(
            domain=".example.com",
            identifier=canonical,
            item_type="login_credentials",
            value={"email": canonical, "password": password},
            source="example",
            metadata={"masked": {"password": "••••••••"}})],
        "__result__": {
            "status": "authenticated",
            "identifier": canonical,
        },
    }
```

**Key rules:**

- **`@connection("public")`** — login produces credentials, so
  pin it to a connection that doesn't require any.
- **Return a `skill_error` with `code="NeedsCredentials"` when
  creds are missing.** The engine detects this and stops — no
  infinite retry loop — and surfaces the structured `required`
  list so the agent can ask for exactly what's missing.
- **Return `__secrets__` on success.** The engine's writeback
  path stamps `last_verified = now()` and upserts on
  `(domain, identifier, item_type)`. Subsequent calls read
  whatever's newest.
- **Cookies self-persist via the ambient Jar.** Any `Set-Cookie`
  the service returns during the handshake rides back through
  `__cookie_delta__` — you don't need to capture them by hand.

### 4. Write `check_session`

The engine calls `check_session` after login to get the identity
(so the credential row gets keyed on a real email / handle, not
`"default"`). It's also what the cookie resolver runs to tell
if the current session is still alive.

```python
from agentos.identity import normalize_email

@returns("account")
@connection("portal")
async def check_session(**params) -> dict:
    resp = await client.get("/me")
    if resp["status"] != 200:
        return {"authenticated": False}

    data = resp["json"]
    return {
        "authenticated": True,
        "at":          {"shape": "organization",
                        "name": "Example Inc",
                        "url":  "https://example.com"},
        "identifier":  normalize_email(data["email"]),
        "email":       normalize_email(data["email"]),
        "displayName": data.get("name"),
        "userId":      str(data["id"]),
    }
```

See [Auth flows §`check_session` convention](./auth-flows.md#the-check_session-convention)
for every field the engine reads and when to populate it.

### 5. Strip `params.auth.key` from every authed tool

If your skill previously had users paste credentials into
settings, authed tools probably read `params["auth"]["key"]`.
Delete those reads. With the cookie/api_key auth in step 1, the
engine injects credentials automatically — cookies via the
ambient Jar, api_keys via `params.auth.<field>`.

```python
# BEFORE (paste-based)
token = _mint_id_token(params["auth"]["key"])
resp = await client.get("/orders", headers={"Authorization": token})

# AFTER (engine-driven)
resp = await client.get("/orders")   # cookies ride automatically
```

### 6. Write the `logout` tool

Symmetric with `login`. The service-side revoke is the part the
engine can't do for you; the engine handles everything else
(delete skill-written rows, invalidate cache) after your tool
returns. See [Do I need a `logout` tool?](#do-i-need-a-logout-tool)
for the full template and the three-verb model
(`logout` / `clear_session` / `remove`). One new tool in your
skill, one new line in the connection's `AccountBlock`:

```python
auth={"type": "api_key",
      "account": {"check":  "check_session",
                  "login":  "login",
                  "logout": "logout"}}   # ← add this
```

Skipping this step leaves the validator warning live and reduces
logout to a local-cache delete. Ship it.

### 7. Ship it

```bash
./dev.sh restart                # Python changes don't need a rebuild
agentos call run '{"skill":"example","tool":"login"}'
# ... test a few authed tools ...
agentos call accounts '{"action":"logout","skill":"example"}'
```

Expected path end-to-end:

1. You (or an agent) call `example.login()` with no args.
2. `credentials.retrieve(".example.com", ...)` dispatches every
   installed `@provides(login_credentials)` skill.
3. 1Password or Keychain returns `{email, password}` via
   `__secrets__`. The engine writes the provider row.
4. Your `login` runs the reverse-engineered handshake.
5. Session cookies land via the ambient Jar. `__secrets__`
   writeback stamps the row.
6. The next call to `example.book_thing()` picks up the cookies
   via domain lookup — `account=None` works.
7. When the user's done, `accounts({action:"logout", skill})`
   dispatches your `logout` op (service-side revoke), then the
   engine deletes the skill-written row and invalidates cache.
   Provider rows (1Password) stay — the password is safe, only
   the session is gone.

Cold-start, **one call, no passwords typed, no LLM sees a secret.**
Clean shutdown, **one call, tokens dead at the service, local
cache clear.**

## The three credential resolution paths

Your `login` tool's credentials can come from three places, tried
in this order:

1. **Explicit args.** `example.login(email="...", password="...")`.
   First-time paste by the user, or an agent forwarding a
   one-shot prompt.
2. **`credentials.retrieve(domain, required)`.** Matchmakes every
   installed `@provides(login_credentials)` skill — 1Password,
   Keychain, any future browser saved-password skill. Joe pastes
   his password into 1Password once; every skill finds it.
3. **`NeedsCredentials` error.** Nothing matched → structured
   error with the `required` list. The agent surfaces the ask
   ("I need `email` and `password` for `.example.com`").

**Your `login` tool handles all three** with the template in
step 3 above. It doesn't care where the creds came from.

## When does the engine call `login` automatically?

Two cases, both handled by the engine's auto-relogin intercept:

- **Cold start.** An authed tool runs, the credential store has
  no row for the domain, engine can't resolve → `AuthFailed` →
  engine looks for a `login` tool → dispatches it → retries the
  original call once.
- **Stale session.** Cookies fail with 401/403; cookie providers
  re-extract; if fresh extraction returns the same stale
  cookies, `NeedsRelogin` fires → engine dispatches `login` →
  retries once.

If `login` returns `NeedsCredentials`, the engine stops — no
cascade. If `login` succeeds, the original call sees fresh creds
via `account=None` lookup.

You don't write any retry logic. It's engine-side.

## Reference implementations

Three skills in the public repo, each a different auth shape.
Copy the one closest to yours.

| Skill | Auth shape | What to learn from it |
|---|---|---|
| [`skills/fitness/austin-boulder-project/abp.py`](https://github.com/agentos-to/skills/tree/main/fitness/austin-boulder-project) | Cognito / Amplify | OAuth-provider handshake + portal session follow-up |
| [`skills/web/exa/exa.py`](https://github.com/agentos-to/skills/tree/main/web/exa) | NextAuth + email OTP | Two-step flow (`send_login_code` + `verify_login_code`) |
| [`skills/media/goodreads/goodreads_web.py`](https://github.com/agentos-to/skills/tree/main/media/goodreads) | Plain form POST | Cookie-only, no tokens, identity scraped from `/user/edit` |

## Troubleshooting

### `credentials.retrieve` returns `{provided: false}` and I don't know why

Most likely cause: **the provider's backing store is locked, not
"no match."** The 1Password provider, for example, surfaces a
structured `OnePasswordLocked` error when the vault is locked
(you'll see it as a `skill_error` response) — unlock the
1Password desktop app and retry.

If you don't see `OnePasswordLocked` but still get
`{provided: false}`, the item genuinely doesn't match. Check:

- **URL field on the 1Password item.** Must contain the domain
  host (or a subdomain). URL format:
  `https://host.example.com/...` — the path is ignored; only the
  host is matched.
- **Domain format on the call.** Both `".example.com"` and
  `"example.com"` work; provider does cookie-style suffix
  matching.
- **Item category.** The 1Password provider only walks the
  `Login` category. Loyalty / membership items sometimes live
  under `Membership` or `Identity` — move them to `Login`, or
  add a dedicated Login item.

### My service uses a non-email username

Fine — the `value` dict can hold whatever fields your handshake
needs. Call them `username` / `password` instead of `email` /
`password`, and update `required=[...]` to match:

```python
creds = await credentials.retrieve(
    domain=".example.com",
    required=["username", "password"])
```

The `identifier` you return in `__secrets__` still goes into the
credential row's canonical-key column — use whatever string the
service uses as its login ID (username, phone number, member
number). The engine doesn't care that it's not an email.

### The handshake is multi-step (email OTP, SMS code, OAuth consent)

Expose the flow as multiple tools instead of one. See
[Auth flows § multi-step flows](./auth-flows.md#multi-step-flows-email-codes-sms-oauth-consent)
for the pattern. Exa's `send_login_code` / `verify_login_code` is
the canonical example.

### I get `AuthFailed` even though my login succeeded

Three common causes:

1. **`check_session` returning the wrong identity.** The engine
   uses `check_session`'s `identifier` to key the credential
   row. If `check_session` returns a different identifier than
   what `login` wrote, the next lookup misses. Make them match.
2. **Cookies landed on a different domain than the connection
   declares.** If `connection(... domain=".example.com")` but
   the service sets cookies on `.api.example.com`, the lookup
   won't find them. Align `connection.domain` with what
   `Set-Cookie` actually uses.
3. **`login` returned without awaiting the handshake.** Python
   async — forgot an `await` on `client.post()`. Check that the
   response body contains what you expect before returning.

### Do I need a `logout` tool?

**Yes — every cookie / api_key / oauth skill should ship one.**
`check_session`, `login`, and `logout` are the three legs of the
account protocol; they belong together. The validator
(`check_logout_presence` in `agent-sdk validate`) warns when a
skill declares `account.login` without `account.logout`.

The engine dispatches your `logout` op on
`accounts({action:"logout", skill})`, passes the live session in
as `params.auth.*`, and runs the cleanup tail (delete skill rows,
invalidate cache) after you return. Your tool's job is the one
piece the engine can't do: the service-side revoke call.

Shape:

```python
@returns({"ok": "boolean", "message": "string"})
@connection("portal")           # authed connection — we still have the session
async def logout(**params) -> dict:
    """Tell the service this session is over."""
    auth = params.get("auth") or {}
    token = auth.get("accessToken") or auth.get("idToken") or auth.get("key")
    if not token:
        return {"ok": False, "message": "No live token; skipped revoke."}

    resp = await client.post(SERVICE_REVOKE_URL, json={"token": token},
                              headers={"Authorization": token})

    # Already-revoked tokens often return 400/401 — that's "done," not "failed."
    if resp["status"] in (200, 204) or _is_already_revoked(resp):
        return {"ok": True, "message": "Session revoked."}
    return {"ok": False, "message": f"Revoke failed: HTTP {resp['status']}"}
```

Wire it into the connection:

```python
auth={"type": "api_key",           # or "cookies", or "oauth"
      "account": {"check":  "check_session",
                  "login":  "login",
                  "logout": "logout"}}
```

Full walkthrough (why server-side revoke matters, how the engine
runs cleanup, the three-verb table — `logout` vs `clear_session`
vs `remove`) lives in
[Auth flows § The `logout` tool and server-side revoke](./auth-flows.md#the-logout-tool-and-server-side-revoke).

**Reference:** ABP's Cognito `GlobalSignOut` implementation at
[`skills/fitness/austin-boulder-project/abp.py`](https://github.com/agentos-to/skills/blob/main/fitness/austin-boulder-project/abp.py).

**Skills without a `logout`** can still be logged out via
`accounts({action:"clear_session", skill})` — engine-side cleanup
only, no server call. Good for "I just want to forget the
session locally," but not for "kill this session everywhere."
Ship a `logout` tool so your users get the stronger guarantee.

## See also

- [Auth flows](./auth-flows.md) — reference doc for everything
  above: field conventions, engine internals, cookie resolution,
  secret safety.
- [Connections](./connections.md) — `connection(...)` surface,
  auth types (`cookies` / `api_key` / `oauth`), client bundles.
- [Reverse engineering — auth](./reverse-engineering/3-auth/) —
  the CDP capture methodology for step 2.
