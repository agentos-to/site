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

# Browser-driven connectors are HEADLESS-BY-DEFAULT: they run in the engine's
# background profile, and their payload surfaces in an app (Mail, Messaging, a
# feed) — the shared surface rule 19 asks for, so no browser window is needed
# for a read. This is the connector-facing default; the engine's own verb
# handlers still default to `attach` for interactive UI driving. A connector
# passes `mode="attach"` ONLY for an action a human should watch live in their
# own browser (an irreversible purchase / booking / submit).
CONNECTOR_MODE = "background"


async def eval(target, js, *, mode=CONNECTOR_MODE, await_promise=True, timeout=None):
    """Evaluate `js` in `target`'s tab and return its value — headless by
    default (`CONNECTOR_MODE`). This is the one call a browser-driven connector
    makes for programmatic in-origin work (same-origin `fetch()`, the platform's
    own JS modules); it pins the background profile so the mode never has to be
    threaded per call (the WhatsApp `_MODE` boilerplate, now in the SDK).
    """
    params = {"target": target, "js": js, "await_promise": await_promise, "mode": mode}
    if timeout is not None:
        params["timeout"] = timeout
    return await services.call("browser_session", verb="eval", params=params)


async def navigate(target, url, *, mode=CONNECTOR_MODE, timeout=None):
    """Move `target`'s tab to `url` — background profile by default."""
    params = {"target": target, "url": url, "mode": mode}
    if timeout is not None:
        params["timeout"] = timeout
    return await services.call("browser_session", verb="navigate", params=params)


async def snapshot(target, *, mode=CONNECTOR_MODE, timeout=None):
    """The tab's accessibility tree — `{title, url, tree:[{ref, role, name, bounds, …}]}`.
    Headless by default. Find a control's `ref` here, then act on it with `click`.
    """
    params = {"target": target, "mode": mode}
    if timeout is not None:
        params["timeout"] = timeout
    return await services.call("browser_session", verb="snapshot", params=params)


async def click(target, ref, *, mode=CONNECTOR_MODE, timeout=None):
    """A TRUSTED click (real CDP input, not a synthetic DOM `.click()`) on the
    element `ref` names, from a prior `snapshot`. Use this — not `eval` +
    `element.click()` — whenever a site's own code checks `event.isTrusted`
    (jsaction dispatchers commonly do); a synthetic click silently no-ops there.
    Returns the tab's fresh post-click snapshot.
    """
    params = {"target": target, "ref": ref, "mode": mode}
    if timeout is not None:
        params["timeout"] = timeout
    return await services.call("browser_session", verb="click", params=params)


async def login_window(login_url, *, label=None, instructions=None, retrieval=None):
    """Begin an interactive login the connector can't drive headless: open a
    headed sign-in window ON the engine's background profile (a chromeless
    `--app` flip of that profile — reads like a native dialog), and return the
    `login_window`-kind `auth_challenge` telling the agent what to do next.

    The one headed moment of a headless connector. Because the window is a flip
    of the SAME profile every headless op reads, the session the human creates
    persists straight through to the daemon. The `login_window` service does the
    flip; the agent waits for the human, polls `check_session` until
    authenticated, then calls the service again with `close=True` to return the
    profile to its headless daemon.

    Return it from a connector's `login` (declare `@returns("account |
    auth_challenge")`). One protocol, three kinds: `qr` (an artifact),
    `code`/`magic_link` (read from the inbox by judgment), `login_window` (this).

    `retrieval` carries a where-to-look hint when the sign-in has a 2FA/email
    sub-step the agent can finish autonomously (e.g. Instagram's login code) —
    the same hint shape the `code`/`magic_link` kinds use.
    """
    name = label or "Sign in"
    await services.call(
        "browser_session",
        verb="login_window",
        params={"url": login_url, "label": name},
    )
    challenge = {
        "shape": "auth_challenge",
        "kind": "login_window",
        "name": name,
        "url": login_url,
        "instructions": instructions
        or (
            "A sign-in window opened on the engine's background profile. Ask the "
            "human to sign in there, then poll check_session until it reports "
            "authenticated — the session lands in the same profile every "
            "headless op reads from. When done, call the login_window service "
            "with close=true to return the profile to its headless daemon."
        ),
        "continueWith": "check_session",
    }
    if retrieval:
        challenge["retrieval"] = retrieval
    return challenge


async def read_cookies(target, *, mode=CONNECTOR_MODE, urls=None):
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


async def response_body(target, url, *, mode=CONNECTOR_MODE, timeout=None):
    """Read CDN / cross-origin media bytes via CDP ``Network.getResponseBody``.

    Page ``fetch(cdnUrl)`` is CORS-blocked for hosts like ``fbcdn`` /
    ``scontent``, but the site paints the same URL with ``<img src>`` /
    ``<video src>``. This verb watches the browser network plane (or falls
    back to ``Network.loadNetworkResource`` + ``IO.read``) and returns
    ``{data (base64), mime, size, url, via}``. Cap 15MB. Use this for story /
    DM media hydrate — not in-page ``fetch``, not a second engine HTTP hop
    unless you must.
    """
    params = {"target": target, "url": url, "mode": mode}
    if timeout is not None:
        params["timeout"] = timeout
    return await services.call("browser_session", verb="response_body", params=params)


async def session_cookie_present(target, name, *, mode=CONNECTOR_MODE):
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
