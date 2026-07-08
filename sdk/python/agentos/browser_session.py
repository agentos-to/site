"""Browser-driven session helpers — honesty + recovery, shared by every
connector that runs inside the engine-owned browser tab.

The bug this exists to kill: a browser-driven `check_session` that infers
"logged in" from cached page state — a warm Relay/JS store, a persisted
`ds_user_id`, stale HTML — is **lying**. That state survives an expired
session (reads keep replaying the cache), so `authenticated: true` can
coexist with every write failing "logged out". An account protocol that
can't tell "reads work" from "writes work" is broken.

The honest signal is the platform's real **session cookie**, which is
httpOnly — invisible to in-page `document.cookie`. Only the browser plane
can read it (`browser_session` verb `cookies` → CDP `Network.getCookies`).
So the honest check lives here, once, and every browser-driven connector
gates `check_session` on `session_cookie_present(...)` — `authenticated`
means *writes will work*, proven by the true signal.

See the system doc `apps-browser-driven` (§ "The honest account check").
"""

from . import services
from .results import app_error


async def read_cookies(target, *, mode="launch", urls=None):
    """All cookies the browser would send to `target`, INCLUDING httpOnly.

    Returns ``{name: {name, value, httpOnly, secure, domain, path, expires,
    session}}`` — the httpOnly session cookie `document.cookie` can never
    see. `urls` scopes the read to specific origins (default: the target's
    own https origin). Cheap — a cookie read, no navigation.
    """
    params = {"target": target, "mode": mode}
    if urls:
        params["urls"] = urls
    resp = await services.call("browser_session", verb="cookies", params=params)
    rows = resp.get("cookies") if isinstance(resp, dict) else resp
    jar = {}
    for c in rows or []:
        name = c.get("name") if isinstance(c, dict) else None
        if name:
            jar[name] = c
    return jar


async def session_cookie_present(target, name, *, mode="launch"):
    """True iff the httpOnly session cookie `name` exists for `target`.

    THE honest gate for a browser-driven `check_session`: present → the
    session is live and writes will work (a stale in-page token is a
    recoverable self-heal, not a logout); absent → genuinely logged out,
    so `check_session` returns ``authenticated: false`` and the
    login/recovery flow takes over.
    """
    jar = await read_cookies(target, mode=mode)
    return name in jar


def needs_auth(message, *, login_url=None, **extra):
    """A typed ``NeedsAuth`` app_error — the one shape the Messaging UI /
    agent acts on. A write that hit a logged-out session returns THIS
    (never the platform's raw error code), so the surface can drive the
    login/recovery flow instead of showing a cryptic failure.
    """
    if login_url:
        extra["login_url"] = login_url
    return app_error(message, code="NeedsAuth", **extra)
