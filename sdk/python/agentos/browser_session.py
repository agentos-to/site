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

# Two defaults, by caller:
#   • Engine raw/agent `browser_session` verbs default to `attach` — the human's
#     daily headed browser (already open, live logins). Watch while developing.
#   • Connector SDK helpers pin `CONNECTOR_MODE = "background"` — headless bg
#     profile; payload surfaces in an app. Standing watches stay here.
#   • `login_window` is the one-shot sign-in for that SAME bg profile; close
#     when done or the whole bg process stays headed.
# Pass `mode="attach"` from a connector ONLY for a watch-live irreversible
# action (purchase / booking / submit) in the human's own browser.
CONNECTOR_MODE = "background"

# Agent-facing recovery — every NeedsAuth / login_window challenge steers here
# so plugins don't invent "flip headed" / mode=attach as the fix.
_LOGIN_RECOVERY = (
    " Recovery: call this plugin's `login` op (never mode=attach, never "
    "relaunch a headed browser to 'fix' a connector). `login` opens a "
    "one-shot login_window on the background profile when needed — cookies "
    "land where headless reads run. After check_session is authenticated, "
    "you MUST close with login_window close=true (or browser_session."
    "close_login_window); leaving it open heads the whole bg profile and "
    "wakes standing connectors."
)

_LOGIN_WINDOW_INSTRUCTIONS = (
    "A one-shot login_window opened on the engine's background profile "
    "(same cookie jar headless connector reads use — NOT the human's daily "
    "browser). Ask the human to sign in in that window only. Poll this "
    "plugin's check_session until authenticated. Then you MUST call "
    "login_window with close=true (or browser_session.close_login_window) — "
    "leaving it open heads the whole background profile and wakes standing "
    "connectors (WhatsApp, Instagram, …). Do not use mode=attach to fix a "
    "connector session."
)


async def eval(target, js, *, mode=CONNECTOR_MODE, await_promise=True, timeout=None):
    """Evaluate `js` in `target`'s tab and return its value — headless bg by
    default (`CONNECTOR_MODE`). This is the one call a browser-driven connector
    makes for programmatic in-origin work (same-origin `fetch()`, the platform's
    own JS modules); it pins the background profile so the mode never has to be
    threaded per call (the WhatsApp `_MODE` boilerplate, now in the SDK).
    Raw agent MCP calls (no SDK) default to `attach` at the engine instead.
    """
    params = {"target": target, "js": js, "await_promise": await_promise, "mode": mode}
    if timeout is not None:
        params["timeout"] = timeout
    return await services.call("browser_session", verb="eval", params=params)


async def navigate(target, url, *, mode=CONNECTOR_MODE, timeout=None, force=False):
    """Move `target`'s tab to `url` — background profile by default.

    Soft by default: if the tab is already at `url` (engine canonical match),
    skip the reload. Tabs are demuxed one-per-host already; this keeps SPA
    state warm across connector ops. Pass `force=True` (or use `reload`) for
    an intentional refresh.
    """
    params = {"target": target, "url": url, "mode": mode}
    if timeout is not None:
        params["timeout"] = timeout
    if force:
        params["force"] = True
    return await services.call("browser_session", verb="navigate", params=params)


async def ensure(target, url, *, mode=CONNECTOR_MODE, timeout=None):
    """Alias for soft `navigate` — land on `url` without reloading if already
    there. Prefer this in connectors that only need the right page warm.
    """
    return await navigate(target, url, mode=mode, timeout=timeout, force=False)


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


async def login_window(login_url, *, label=None, instructions=None, retrieval=None, strategy="profile"):
    """Open a headed sign-in window and return a `login_window` auth_challenge.

    Default ``strategy="profile"``: chromeless window on a **dedicated login
    profile** — the headless bg daemon stays up (standing Uber/WhatsApp tabs
    do not paint). After sign-in: ``merge_login_session`` then
    ``close_login_window``. Pass ``strategy="flip"`` only when merge isn't
    enough (legacy same-jar flip).

    Drive the window with ``mode="login"`` while it is open.
    """
    name = label or "Sign in"
    try:
        await services.call(
            "browser_session",
            verb="login_window",
            params={"url": login_url, "label": name, "strategy": strategy},
        )
    except Exception as e:
        return app_error(
            f"Could not open login_window for {name}: {e}. "
            f"Retry after close_login_window, or open {login_url} once the "
            f"browser is healthy.",
            code="LoginWindowFailed",
            login_url=login_url,
            label=name,
        )
    if strategy == "profile":
        default_instructions = (
            "A headed login window opened on the engine's **login profile** "
            "(background stays headless). Sign in there (or let the agent "
            "drive with mode=login). Then call browser_session."
            "merge_login_session for this domain, then login_window "
            "close=true. Never use mode=attach to fix a connector session."
        )
    else:
        default_instructions = _LOGIN_WINDOW_INSTRUCTIONS
    challenge = {
        "shape": "auth_challenge",
        "kind": "login_window",
        "name": name,
        "url": login_url,
        "strategy": strategy,
        "instructions": instructions or default_instructions,
        "continueWith": "check_session",
        "mode": "login" if strategy == "profile" else "background",
    }
    if retrieval:
        challenge["retrieval"] = retrieval
    return challenge


async def close_login_window(*, strategy="profile"):
    """Tear down the headed login surface. Default closes the login profile
    (bg was never flipped). Pass ``strategy="flip"`` after a legacy flip.
    """
    return await services.call(
        "browser_session",
        verb="login_window",
        params={"close": True, "strategy": strategy},
    )


async def merge_login_session(*, domain=None, urls=None):
    """Copy cookies + local/session storage from the login profile → bg.

    Call after a successful sign-in in ``login_window(strategy=profile)``,
    before ``close_login_window``.
    """
    params = {}
    if urls:
        params["urls"] = list(urls)
    elif domain:
        params["domain"] = domain
    else:
        raise ValueError("merge_login_session needs domain= or urls=")
    return await services.call(
        "browser_session",
        verb="merge_login_session",
        params=params,
    )


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


def needs_auth(message, *, login_op=None, login_url=None, **extra):
    """A typed ``NeedsAuth`` app_error — the one shape the Messaging UI /
    agent acts on.

    Always steers recovery at the plugin's ``login`` op (which opens
    ``login_window`` / returns ``auth_challenge``) — never ``mode=attach``,
    never a free-form headed browser relaunch. Pass ``login_op="reddit.login"``
    when you know the tool name; otherwise a generic Recovery footer is
    appended. Plugin authors: prefer this over hand-rolled RuntimeError /
    app_error strings.

    The engine auto-dispatches ``@account.login`` on this code (when
    ``pref:system.autoLogin`` is on — the default) and retries the
    original op once, or surfaces an ``auth_challenge``.
    """
    msg = (message or "").rstrip()
    if login_op:
        recovery = (
            f" Recovery: call `{login_op}` (never mode=attach, never relaunch "
            f"a headed browser). After check_session is authenticated, close "
            f"with login_window close=true / browser_session.close_login_window."
        )
    else:
        recovery = _LOGIN_RECOVERY
    # Don't double-stamp if the caller already included the standard footer.
    if "Recovery:" not in msg and "close_login_window" not in msg:
        msg = f"{msg}{recovery}"
    if login_url:
        extra["login_url"] = login_url
    if login_op:
        extra.setdefault("continueWith", login_op.rsplit(".", 1)[-1])
    return app_error(msg, code="NeedsAuth", **extra)


# ── First-class login cascade (LoginFlow / OtpSpec) ──────────────────
# Target author surface — plugins migrate onto these; Uber + Exa are the
# reference shapes. Headless password fill lives on LoginFlow; CAPTCHA /
# unreadable MFA escalate to login_window.

from dataclasses import dataclass
import re as _re
from typing import Sequence
from urllib.parse import urlparse


@dataclass
class OtpSpec:
    """OTP / MFA channel policy for a connector login.

    Channel resolution order (first hit wins):
      1. Explicit arg on this call
      2. Account ``metadata.<plugin>.lastAuthMethod`` (``remember_as``)
      3. System ``pref:system.otpOrder`` (default email-first)
      4. This ``default_order``
      5. Filter to on-screen + retrievable channels
    """

    channels: Sequence[str] = ("email",)
    default_order: Sequence[str] = ("email", "sms", "whatsapp")
    remember_as: str = "lastAuthMethod"
    verify_tool: str = "verify_login_code"


_CAPTCHA_RE = _re.compile(
    r"captcha|recaptcha|hcaptcha|cf-turnstile|verify you.?re human|are you a robot",
    _re.I,
)
_CARD_DIGITS_RE = _re.compile(
    r"card (ending|digits)|last\s*4|payment.?card|credit.?card",
    _re.I,
)
_OTP_HINT_RE = _re.compile(
    r"verification code|enter (the )?code|one.?time|otp|authenticator|2fa|two.?factor",
    _re.I,
)


def _snap_nodes(snap: dict) -> list:
    tree = snap.get("tree") if isinstance(snap, dict) else None
    return tree if isinstance(tree, list) else []


def _snap_text(snap: dict) -> str:
    parts = []
    for n in _snap_nodes(snap):
        if isinstance(n, dict) and n.get("name"):
            parts.append(str(n["name"]))
    title = (snap.get("title") or "") if isinstance(snap, dict) else ""
    return f"{title} {' '.join(parts)}"


def _find_ref(snap: dict, *, role: str | None = None, name_re: str | None = None):
    pat = _re.compile(name_re, _re.I) if name_re else None
    for n in _snap_nodes(snap):
        if not isinstance(n, dict) or not n.get("ref"):
            continue
        if role and (n.get("role") or "").lower() != role.lower():
            continue
        if pat and not pat.search(n.get("name") or ""):
            continue
        return n["ref"]
    return None


def detect_login_wall(snap: dict) -> str | None:
    """Classify a post-submit screen: captcha / card_digits / otp / None."""
    text = _snap_text(snap)
    if _CAPTCHA_RE.search(text):
        return "captcha"
    if _CARD_DIGITS_RE.search(text):
        return "card_digits"
    if _OTP_HINT_RE.search(text):
        return "otp"
    return None


@dataclass
class LoginFlow:
    """Declarative connector login — brokered creds → headless → OTP → window.

    ``headless_password_fill`` drives a generic identifier+password form in
    the background profile. Site-specific OTP (Uber/Exa) still owns the
    channel picker; CAPTCHA / card digits escalate via ``escalate_to_window``.
    """

    domain: str
    login_url: str
    label: str = "Sign in"
    credentials: Sequence[str] = ("email", "password")
    otp: OtpSpec | None = None
    window_on: Sequence[str] = ("captcha", "card_digits", "unknown_challenge")
    plugin_key: str = ""  # metadata.<plugin_key> for lastAuthMethod
    target: str = ""  # browser_session host; derived from login_url when empty

    def surface_target(self) -> str:
        if self.target:
            return self.target
        host = urlparse(self.login_url).hostname or ""
        return host or self.domain.lstrip(".")

    async def retrieve_credentials(self, *, account: str | None = None) -> dict:
        """Brokered ``credentials.retrieve`` — vault → default provider → others."""
        from agentos import credentials as creds

        return await creds.retrieve(
            domain=self.domain,
            account=account,
            required=list(self.credentials),
        )

    async def otp_channel_order(
        self, *, account_pref: str | None = None, explicit: str | None = None
    ) -> list[str]:
        """Resolve OTP channel preference for this login attempt."""
        return await resolve_otp_order_async(
            otp=self.otp,
            account_pref=account_pref,
            explicit=explicit,
        )

    async def escalate_to_window(
        self, *, reason: str | None = None, retrieval=None, strategy="profile"
    ):
        """Prefer dedicated login profile (bg stays headless); flip is fallback.

        After sign-in with strategy=profile: ``merge_login_session`` then
        ``close_login_window``. Drive the window with ``mode="login"``.
        """
        instructions = None
        if reason:
            if strategy == "profile":
                instructions = (
                    f"{reason} Window is on the login profile (bg still "
                    f"headless). Complete any human-only step, then "
                    f"merge_login_session(domain={self.domain!r}) and "
                    f"close_login_window."
                )
            else:
                instructions = (
                    f"{reason} Finish any human-only step in the headed "
                    f"window, then poll check_session and close_login_window "
                    f"(strategy=flip)."
                )
        return await login_window(
            self.login_url,
            label=self.label,
            instructions=instructions,
            retrieval=retrieval,
            strategy=strategy,
        )

    async def merge_into_background(self, *, urls=None):
        """Copy this flow's domain session from login profile → bg."""
        if urls:
            return await merge_login_session(urls=urls)
        origins = [
            f"https://{self.domain.lstrip('.')}/",
            self.login_url if "://" in self.login_url else f"https://{self.login_url}/",
        ]
        # Dedupe
        seen = set()
        uniq = []
        for u in origins:
            if u not in seen:
                seen.add(u)
                uniq.append(u)
        return await merge_login_session(urls=uniq)

    async def type_secret(self, target: str, ref: str, *, account: str | None = None):
        """Inject the vault password for ``self.domain`` — never into model context."""
        params = {
            "target": target,
            "ref": ref,
            "domain": self.domain,
            "mode": CONNECTOR_MODE,
            "item_type": "login_credentials",
            "field": "password",
        }
        if account:
            params["account"] = account
        return await services.call("browser_session", verb="type_secret", params=params)

    async def headless_password_fill(
        self,
        *,
        email: str | None = None,
        account: str | None = None,
        check_session=None,
    ) -> dict:
        """Navigate → fill identifier + password → submit; escalate on walls.

        Returns:
          - account dict if ``check_session`` reports authenticated
          - ``auth_challenge`` (login_window) on captcha / card / window_on
          - ``{"status": "submitted", "identifier": …}`` when the form
            submitted without an immediate wall (caller may poll OTP)
          - ``app_error`` NeedsCredentials / unlock when retrieve fails
        """
        import asyncio

        if check_session is not None:
            existing = await check_session()
            if isinstance(existing, dict) and existing.get("authenticated"):
                return existing

        creds = await self.retrieve_credentials(account=account or email)
        if creds.get("unlock_required"):
            return creds
        if not creds.get("found"):
            return app_error(
                f"No login credentials for {self.domain} from any "
                f"login_credentials provider (vault → default → others).",
                code="NeedsCredentials",
                required=list(self.credentials),
                domain=self.domain,
            )
        value = creds.get("value") or {}
        identifier = (
            email
            or value.get("email")
            or value.get("username")
            or creds.get("identifier")
            or ""
        ).strip()
        if not identifier and "email" in self.credentials:
            return app_error(
                f"No email/username for {self.domain}.",
                code="NeedsCredentials",
                required=list(self.credentials),
                domain=self.domain,
            )
        if "password" in self.credentials and not value.get("password"):
            # retrieve required password — if found but empty, treat as miss
            return app_error(
                f"Password missing for {self.domain}.",
                code="NeedsCredentials",
                required=["password"],
                domain=self.domain,
            )

        target = self.surface_target()
        await navigate(target, self.login_url)
        await asyncio.sleep(1.0)
        snap = await snapshot(target) or {}

        wall = detect_login_wall(snap)
        if wall and wall in self.window_on:
            return await self.escalate_to_window(
                reason=f"{self.label} showed a {wall} wall before fill."
            )

        id_box = (
            _find_ref(snap, role="textbox", name_re=r"email|phone|mobile|user|login")
            or _find_ref(snap, role="textbox")
        )
        if id_box and identifier:
            await services.call(
                "browser_session",
                verb="type",
                params={
                    "target": target,
                    "ref": id_box,
                    "text": identifier,
                    "clear": True,
                    "mode": CONNECTOR_MODE,
                },
            )

        pw_box = _find_ref(snap, role="textbox", name_re=r"password")
        if not pw_box:
            # Some forms reveal password after Continue
            cont = _find_ref(snap, role="button", name_re=r"^continue$|next|submit")
            if cont:
                snap = await click(target, cont) or {}
                await asyncio.sleep(0.8)
                snap = await snapshot(target) or {}
                pw_box = _find_ref(snap, role="textbox", name_re=r"password")

        if pw_box and "password" in self.credentials:
            await self.type_secret(target, pw_box, account=identifier or None)

        wall = detect_login_wall(await snapshot(target) or {})
        if wall and wall in self.window_on:
            return await self.escalate_to_window(
                reason=f"{self.label} requires a human step ({wall}) after fill."
            )

        submit = (
            _find_ref(snap, role="button", name_re=r"^sign in$|^log in$|submit|continue|next")
            or _find_ref(await snapshot(target) or {}, role="button",
                         name_re=r"^sign in$|^log in$|submit|continue|next")
        )
        if submit:
            await click(target, submit)
            await asyncio.sleep(1.2)

        snap = await snapshot(target) or {}
        wall = detect_login_wall(snap)
        if wall == "otp" and self.otp:
            return {
                "shape": "auth_challenge",
                "kind": "code_sent",
                "name": f"{self.label} verification",
                "continueWith": self.otp.verify_tool,
                "payload": identifier,
                "instructions": (
                    f"A verification code was requested for {self.label}. "
                    f"Retrieve it and call `{self.otp.verify_tool}`."
                ),
            }
        if wall and wall in self.window_on:
            return await self.escalate_to_window(
                reason=f"{self.label} requires a human step ({wall}) after submit."
            )

        if check_session is not None:
            await asyncio.sleep(0.5)
            existing = await check_session()
            if isinstance(existing, dict) and existing.get("authenticated"):
                try:
                    await close_login_window()
                except Exception:
                    pass
                return existing

        return {"status": "submitted", "identifier": identifier, "at": target}

    async def run(self, *, email: str | None = None, check_session=None, **_kwargs):
        """Cascade entry: headless password fill when password is declared."""
        if "password" in self.credentials:
            return await self.headless_password_fill(
                email=email, check_session=check_session
            )
        # Email-OTP-only (Exa): retrieve + leave site drive to the plugin.
        creds = await self.retrieve_credentials(account=email)
        return creds


_SYSTEM_OTP_DEFAULT = ("email", "sms", "whatsapp", "voice")


async def _system_otp_order() -> list[str] | None:
    """Optional ``pref:system.otpOrder`` — comma string or list."""
    try:
        from agentos._bridge import dispatch

        settings = await dispatch(
            "data.read",
            {"id": "settings", "fields": ["pref:system"]},
        )
        if not isinstance(settings, dict):
            return None
        blob = settings.get("pref:system")
        if isinstance(blob, str):
            import json

            blob = json.loads(blob)
        if not isinstance(blob, dict):
            return None
        raw = blob.get("otpOrder")
        if isinstance(raw, list):
            return [str(c).lower().strip() for c in raw if c]
        if isinstance(raw, str) and raw.strip():
            return [c.strip().lower() for c in raw.split(",") if c.strip()]
        return None
    except Exception:
        return None


def resolve_otp_order(
    *,
    otp: OtpSpec | None = None,
    account_pref: str | None = None,
    explicit: str | None = None,
    system_order: Sequence[str] | None = None,
) -> list[str]:
    """Build the OTP channel try-order (sync; pass system_order if known).

    Default preference is **email**. Account ``lastAuthMethod`` floats to
    the front when it is in the supported set.
    """
    supported = list((otp.channels if otp else None) or _SYSTEM_OTP_DEFAULT)
    plugin_default = list(
        (otp.default_order if otp else None) or _SYSTEM_OTP_DEFAULT
    )
    base = list(system_order) if system_order else list(plugin_default)
    # Keep only channels this plugin supports, preserve order, append rest.
    ordered: list[str] = []
    for c in base:
        c = (c or "").lower().strip()
        if c and c in supported and c not in ordered:
            ordered.append(c)
    for c in supported:
        if c not in ordered:
            ordered.append(c)
    pref = (explicit or account_pref or "").lower().strip()
    if pref and pref in ordered:
        ordered = [pref] + [c for c in ordered if c != pref]
    return ordered


async def resolve_otp_order_async(
    *,
    otp: OtpSpec | None = None,
    account_pref: str | None = None,
    explicit: str | None = None,
) -> list[str]:
    """Like ``resolve_otp_order`` but loads ``pref:system.otpOrder``."""
    system = await _system_otp_order()
    return resolve_otp_order(
        otp=otp,
        account_pref=account_pref,
        explicit=explicit,
        system_order=system,
    )
