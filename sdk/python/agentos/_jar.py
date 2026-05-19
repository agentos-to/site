"""Per-call cookie jar — SDK-internal, ambient to one tool invocation.

One ContextVar, one tool call, one Client. The ``Client`` owns a live
mutable ``Jar`` of structured ``Cookie`` records. Reads see writes —
there is no frozen "cookies_in" string. At tool exit the worker snapshots
the jar against its seed and emits a structured ``{added, changed,
removed}`` delta; the engine upserts that into the credential row keyed
on ``(domain, identifier)`` frozen at entry.

Shape is RFC 6265bis-aligned: uniqueness is ``(domain, path, name)``;
attributes mirror Chromium ``net::CookieMonster`` / stdlib
``http.cookiejar`` / aiohttp. Deletions (``Max-Age=0`` or a past
``Expires``) are represented as the cookie being absent from ``_live``.

Skills never touch this module. ``client.get/post`` reads the
``_current_client`` ContextVar, pulls the Cookie: header from
``Client.jar.cookie_header_for(url)``, and feeds response ``Set-Cookie``
back in via ``Client.jar.ingest(url, …)``. The ContextVar is reset in
``finally`` in the worker so state never bleeds across tool calls.
"""

from __future__ import annotations

from contextvars import ContextVar
from dataclasses import dataclass, field
from email.utils import parsedate_to_datetime
from typing import Literal
from urllib.parse import urlsplit
import time


# ---------------------------------------------------------------------------
# Cookie — one structured record.
# ---------------------------------------------------------------------------


@dataclass
class Cookie:
    """A single cookie. Shape mirrors the Rust ``Cookie`` in
    ``crates/auth``: name/value/domain/path/expires/secure/http_only/
    same_site. Uniqueness key is ``(domain, path, name)`` everywhere."""

    name: str
    value: str
    domain: str
    path: str = "/"
    expires: float | None = None  # unix seconds; None = session cookie
    secure: bool = False
    http_only: bool = False
    same_site: Literal["Strict", "Lax", "None"] | None = None

    @property
    def key(self) -> tuple[str, str, str]:
        return (self.domain, self.path, self.name)

    def is_expired(self, now: float | None = None) -> bool:
        if self.expires is None:
            return False
        return self.expires <= (now if now is not None else time.time())

    def to_dict(self) -> dict:
        d = {"name": self.name, "value": self.value, "domain": self.domain, "path": self.path}
        if self.expires is not None:
            d["expires"] = int(self.expires)
        if self.secure:
            d["secure"] = True
        if self.http_only:
            d["http_only"] = True
        if self.same_site is not None:
            d["same_site"] = self.same_site
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "Cookie":
        return cls(
            name=d["name"],
            value=d["value"],
            domain=d["domain"],
            path=d.get("path", "/"),
            expires=d.get("expires"),
            secure=bool(d.get("secure", False)),
            http_only=bool(d.get("http_only", False)),
            same_site=d.get("same_site"),
        )


# ---------------------------------------------------------------------------
# Jar — live mutable store + frozen entry snapshot for diff at exit.
# ---------------------------------------------------------------------------


def _domain_matches(cookie_domain: str, request_host: str) -> bool:
    """RFC 6265 §5.1.3 domain-match. ``cookie_domain`` without a leading
    dot is host-only; with a leading dot it covers subdomains too. Host
    comparison is case-insensitive."""
    if not cookie_domain:
        return False
    host = request_host.lower()
    cd = cookie_domain.lower()
    if cd.startswith("."):
        bare = cd[1:]
        return host == bare or host.endswith("." + bare)
    # host-only
    return host == cd


def _path_matches(cookie_path: str, request_path: str) -> bool:
    """RFC 6265 §5.1.4 path-match."""
    cp = cookie_path or "/"
    rp = request_path or "/"
    if rp == cp:
        return True
    if rp.startswith(cp):
        return cp.endswith("/") or rp[len(cp):].startswith("/")
    return False


def _parse_set_cookie(raw: str, request_url: str) -> Cookie | None:
    """Parse one Set-Cookie header value into a ``Cookie`` record.

    Does NOT split a comma-joined Set-Cookie string — callers pass one
    cookie's worth of attributes at a time. Returns ``None`` if the
    name/value is missing. Applies request-URL defaults for domain
    (host-only) and path (derived from the URL path)."""
    parts = [p.strip() for p in raw.split(";") if p.strip()]
    if not parts:
        return None
    name_val = parts[0]
    if "=" not in name_val:
        return None
    name, _, value = name_val.partition("=")
    name = name.strip()
    value = value.strip()
    if not name:
        return None

    parsed = urlsplit(request_url)
    default_domain = parsed.hostname or ""
    default_path = parsed.path or "/"
    if not default_path.startswith("/"):
        default_path = "/"
    # RFC 6265 §5.1.4 default-path: up to the last "/", or "/".
    if default_path != "/":
        idx = default_path.rfind("/")
        default_path = default_path[:idx] if idx > 0 else "/"

    domain: str | None = None
    path: str | None = None
    expires: float | None = None
    max_age: int | None = None
    secure = False
    http_only = False
    same_site: str | None = None

    for attr in parts[1:]:
        if "=" in attr:
            k, _, v = attr.partition("=")
            k = k.strip().lower()
            v = v.strip()
            if k == "domain":
                # Leading dot is cosmetic per RFC 6265bis — normalize to
                # with-leading-dot so subdomain matches work.
                domain = v if v.startswith(".") else "." + v if v else None
            elif k == "path":
                path = v or "/"
            elif k == "expires":
                try:
                    dt = parsedate_to_datetime(v)
                    if dt is not None:
                        expires = dt.timestamp()
                except (TypeError, ValueError):
                    pass
            elif k == "max-age":
                try:
                    max_age = int(v)
                except ValueError:
                    pass
            elif k == "samesite":
                lv = v.lower()
                if lv == "strict":
                    same_site = "Strict"
                elif lv == "lax":
                    same_site = "Lax"
                elif lv == "none":
                    same_site = "None"
        else:
            flag = attr.strip().lower()
            if flag == "secure":
                secure = True
            elif flag == "httponly":
                http_only = True

    # Max-Age wins over Expires per RFC 6265 §5.3.
    if max_age is not None:
        expires = time.time() + max_age

    if domain is None:
        domain = default_domain  # host-only cookie
    if path is None:
        path = default_path

    return Cookie(
        name=name,
        value=value,
        domain=domain,
        path=path or "/",
        expires=expires,
        secure=secure,
        http_only=http_only,
        same_site=same_site,
    )


@dataclass
class Jar:
    """Live mutable cookie store with a frozen entry snapshot.

    Keyed on ``(domain, path, name)`` — RFC 6265bis / Chromium consensus.
    ``_live`` is the working set reads and writes both touch; ``_seed``
    is the deep-copied snapshot taken at construction so ``delta()`` at
    tool exit can diff against it without reference aliasing."""

    _live: dict[tuple[str, str, str], Cookie] = field(default_factory=dict)
    _seed: dict[tuple[str, str, str], Cookie] = field(default_factory=dict)

    # --- construction --------------------------------------------------

    @classmethod
    def from_seed(cls, cookies: list[Cookie] | list[dict] | None) -> "Jar":
        jar = cls()
        if not cookies:
            return jar
        for c in cookies:
            cookie = c if isinstance(c, Cookie) else Cookie.from_dict(c)
            jar._live[cookie.key] = cookie
        # Frozen copy for delta comparison. dataclass replace via dict.
        jar._seed = {
            k: Cookie(**{**v.__dict__}) for k, v in jar._live.items()
        }
        return jar

    # --- introspection -------------------------------------------------

    @property
    def cookies(self) -> list[Cookie]:
        """Snapshot list of currently-live cookies (excludes expired).
        Order is insertion order; callers must not mutate the returned
        list to modify jar state."""
        now = time.time()
        return [c for c in self._live.values() if not c.is_expired(now)]

    # --- per-request read/write ---------------------------------------

    def cookie_header_for(self, url: str) -> str:
        """Filter ``_live`` by domain-match + path-match + Secure + expiry
        and serialize to an RFC 6265 ``Cookie:`` request header value.

        Caller passes the full outbound URL; scheme decides whether
        ``secure`` cookies are allowed; host + path drive the matching."""
        parsed = urlsplit(url)
        host = (parsed.hostname or "").lower()
        path = parsed.path or "/"
        is_https = parsed.scheme.lower() == "https"
        now = time.time()

        eligible: list[Cookie] = []
        for c in self._live.values():
            if c.is_expired(now):
                continue
            if c.secure and not is_https:
                continue
            if not _domain_matches(c.domain, host):
                continue
            if not _path_matches(c.path, path):
                continue
            eligible.append(c)

        # RFC 6265 §5.4: longer-path first; ties broken by earlier
        # creation time (we don't track creation — insertion order works
        # well enough and mirrors stdlib behavior).
        eligible.sort(key=lambda c: -len(c.path))
        return "; ".join(f"{c.name}={c.value}" for c in eligible)

    def ingest(self, url: str, set_cookie: str | list[str] | None) -> None:
        """Parse one or more ``Set-Cookie`` header values and upsert into
        ``_live`` keyed on ``(domain, path, name)``.

        Deletions (``Max-Age=0`` / past ``Expires``) land in ``_live`` as
        an expired record then get pruned immediately — the net effect
        is absence, which is what ``delta()`` needs to emit as
        ``removed``.

        Accepts either a single joined string (multi-cookie handling is
        best-effort: the engine's header capture flattens same-name
        headers, so in practice we see one per call) or a list."""
        if not set_cookie:
            return
        raws = set_cookie if isinstance(set_cookie, list) else [set_cookie]
        for raw in raws:
            if not raw:
                continue
            cookie = _parse_set_cookie(raw, url)
            if cookie is None:
                continue
            if cookie.is_expired():
                # Deletion semantics: drop any matching live cookie.
                self._live.pop(cookie.key, None)
            else:
                self._live[cookie.key] = cookie

    # --- exit diff -----------------------------------------------------

    def delta(self) -> dict:
        """Diff ``_live`` vs ``_seed``. Returns the wire shape the engine
        expects inside ``__cookie_delta__``:

            {"added":   [Cookie.to_dict(), ...],
             "changed": [Cookie.to_dict(), ...],
             "removed": [{"domain": d, "path": p, "name": n}, ...]}

        Empty lists are included so callers can treat the result
        uniformly; the worker decides whether to omit the sidecar
        entirely when all three are empty."""
        added: list[dict] = []
        changed: list[dict] = []
        removed: list[dict] = []

        now = time.time()
        live_keys = set(k for k, c in self._live.items() if not c.is_expired(now))
        seed_keys = set(self._seed.keys())

        for key in live_keys - seed_keys:
            added.append(self._live[key].to_dict())
        for key in seed_keys - live_keys:
            d, p, n = key
            removed.append({"domain": d, "path": p, "name": n})
        for key in live_keys & seed_keys:
            live = self._live[key]
            seed = self._seed[key]
            if live.__dict__ != seed.__dict__:
                changed.append(live.to_dict())

        return {"added": added, "changed": changed, "removed": removed}

    def is_empty_delta(self) -> bool:
        d = self.delta()
        return not d["added"] and not d["changed"] and not d["removed"]


# ---------------------------------------------------------------------------
# Client — the tool call's identity + jar. One per tool invocation.
# ---------------------------------------------------------------------------


@dataclass
class Client:
    """Held by ``_current_client`` for the lifetime of one tool call.

    ``connection`` is a frozen dict of ``{name, client, domain,
    identifier}`` — never re-read from the live credentials row on
    exit; the engine already has those values from the seed it shipped.
    ``jar`` is ``None`` for ``client="api"`` (stateless; no seeding, no
    writeback); otherwise a ``Jar`` seeded from the engine's cookie
    list."""

    connection: dict
    jar: Jar | None = None


# Public accessor — skills call ``client.current()``, not this name.
_current_client: ContextVar[Client | None] = ContextVar(
    "agentos_current_client", default=None
)
