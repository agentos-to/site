"""Deprecated ``http`` namespace — kept alive through Wave 3 corpus sweep.

All network verbs route to ``agentos.client``; URL helpers route to
``agentos.url``. Wave 3 rewrites skill callsites to call those directly;
Wave 4 deletes this file.

Skills should stop importing this module. The remaining public surface:

  - ``http.get/post/put/delete/patch/head`` — aliases for ``client.*``.
  - ``http.build_url/parse_url/encode/decode`` — aliases for ``url.*``.
  - ``http.headers(...)`` — legacy header-bundle composer. Now redundant
    (the Client's ``client="..."`` value owns the bundle); merges
    harmlessly on top at the callsite.
  - ``http.client(...)`` — legacy session context manager backed by the
    engine's ``http.session_*`` ops. Wave 4 deletes.
  - ``http.cookies(domain=, account=)`` — cookie resolver passthrough.
  - Skill helpers: ``skill_error / skill_result / skill_secret /
    get_cookies / require_cookies / parse_cookie``.
"""

from __future__ import annotations

from agentos._bridge import dispatch
from agentos import client as _client
from agentos import url as _url


# ── Network verbs — direct alias to the new client surface. ───────────────

get = _client.get
post = _client.post
put = _client.put
delete = _client.delete
patch = _client.patch
head = _client.head


# ── URL helpers — direct alias to the new url surface. ────────────────────

build_url = _url.build
parse_url = _url.parse
encode = _url.encode
decode = _url.decode
ParsedURL = _url.ParsedURL


# ── Legacy header composer ────────────────────────────────────────────────
# The new Client owns the bundle via connection ``client="..."``; calls to
# ``http.headers(...)`` are redundant but harmless — caller-supplied
# headers merge on top of the ambient bundle in client._request.

_CHROME_VERSION = "145"
_CHROME_FULL_VERSION = "145.0.7493.92"

_UA = {
    "chrome-desktop": f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{_CHROME_VERSION}.0.0.0 Safari/537.36",
    "chrome-mobile": f"Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/{_CHROME_VERSION}.0.0.0 Mobile/15E148 Safari/604.1",
    "safari-desktop": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
}

_WAF = {
    "cf": {"hints": {
        "Sec-CH-UA": f'"Chromium";v="{_CHROME_VERSION}", "Not:A-Brand";v="99"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"macOS"',
    }, "http2": True},
    "vercel": {"hints": {}, "http2": False},
}

_MODE = {
    "fetch": {
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    },
    "navigate": {
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
        "Upgrade-Insecure-Requests": "1",
        "Cache-Control": "max-age=0",
        "Device-Memory": "8",
        "Downlink": "10",
        "DPR": "2",
        "ECT": "4g",
        "RTT": "50",
        "Viewport-Width": "1512",
        "Sec-CH-Device-Memory": "8",
        "Sec-CH-DPR": "2",
        "Sec-CH-UA-Full-Version-List": f'"Chromium";v="{_CHROME_FULL_VERSION}", "Not:A-Brand";v="99.0.0.0"',
    },
}

_ACCEPT = {
    "json": {"Accept": "application/json"},
    "html": {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8"},
    "any":  {"Accept": "*/*"},
}


def headers(*, waf=None, ua="chrome-desktop", mode="fetch", accept="any", extra=None):
    """Build request headers from independent knobs. Deprecated — the
    new Client owns the header bundle via ``client="..."`` on the
    connection declaration. Kept as a pass-through for unmigrated
    callsites; Wave 3 sweep deletes these calls."""
    h = {}
    result = {}
    h["User-Agent"] = _UA.get(ua, ua)
    h["Accept-Language"] = "en-US,en;q=0.9"
    h["Accept-Encoding"] = "gzip, deflate, br, zstd"
    if waf:
        cfg = _WAF[waf]
        h.update(cfg["hints"])
        result["http2"] = cfg["http2"]
        h.update(_MODE[mode])
    h.update(_ACCEPT[accept])
    if extra:
        h.update(extra)
    result["headers"] = h
    return result


# ── Legacy session client ─────────────────────────────────────────────────
# HTTP requests routed through engine ``http.session_*`` ops with explicit
# cookie-jar writeback. Wave 4 deletes this path — every live callsite
# migrates to the ambient Client/Jar in Wave 3.


def client(
    cookies: str | None = None,
    *,
    headers: dict | None = None,
    skip_cookies: list[str] | None = None,
    timeout: float = 30.0,
    http2: bool = True,
    retry: int = 0,
    retry_delay: float = 2.0,
) -> "HttpSession":
    """Create an HTTP session with cookie-jar tracking. Deprecated —
    the new Client/Jar handles this via the connection; Wave 3 sweeps
    callsites, Wave 4 deletes this path."""
    return HttpSession(
        cookies=cookies, headers=headers, skip_cookies=skip_cookies,
        timeout=timeout, http2=http2,
    )


class HttpSession:
    """Legacy async session context manager — routes through engine
    ``http.session_open / session_close / session_request`` ops."""

    def __init__(self, **config):
        self._config = config
        self._session_id: str | None = None

    async def __aenter__(self):
        result = await dispatch("http.session_open", self._config)
        self._session_id = result["session_id"]
        return self

    async def __aexit__(self, *_):
        if self._session_id:
            await dispatch("http.session_close", {"session_id": self._session_id})
            self._session_id = None

    async def get(self, url: str, **kwargs) -> dict:
        return await self._request("GET", url, **kwargs)

    async def post(self, url: str, **kwargs) -> dict:
        return await self._request("POST", url, **kwargs)

    async def put(self, url: str, **kwargs) -> dict:
        return await self._request("PUT", url, **kwargs)

    async def delete(self, url: str, **kwargs) -> dict:
        return await self._request("DELETE", url, **kwargs)

    async def patch(self, url: str, **kwargs) -> dict:
        return await self._request("PATCH", url, **kwargs)

    async def _request(self, method: str, url: str, **kwargs) -> dict:
        json_body = kwargs.pop("json", None)
        data = kwargs.pop("data", None)
        body = kwargs.pop("body", None)
        hdrs = kwargs.pop("headers", None)
        out_body, out_headers = _client._prepare_body(
            json=json_body, data=data, body=body, headers=hdrs
        )
        envelope = {
            "session_id": self._session_id,
            "method": method,
            "url": url,
            **kwargs,
        }
        if out_body is not None:
            envelope["body"] = out_body
        if out_headers:
            envelope["headers"] = out_headers
        return await dispatch("http.session_request", envelope)


# ── Legacy cookie resolver ────────────────────────────────────────────────


async def cookies(domain: str, account: str | None = None) -> str:
    """Resolve cookies for a domain via the auth resolver."""
    params = {"domain": domain}
    if account:
        params["account"] = account
    result = await dispatch("cookie.resolve", params)
    return result.get("cookies", "")


# ── Skill helpers — tiny data builders, no network. ───────────────────────


def skill_error(message: str, **extra) -> dict:
    """Return a structured error dict from a skill operation."""
    result = {"error": message}
    result.update(extra)
    return {"__result__": result}


def skill_result(**fields) -> dict:
    """Return a structured result dict from a skill operation."""
    return {"__result__": fields}


def get_cookies(params: dict | None) -> str | None:
    """Extract cookie header from the runtime params dict."""
    if not params:
        return None
    auth = params.get("auth")
    if not auth:
        return None
    cookies = auth.get("cookies") or ""
    return cookies if cookies else None


def require_cookies(params: dict | None, op: str) -> str:
    """Extract cookie header or raise with a helpful message."""
    header = get_cookies(params)
    if not header:
        raise ValueError(f"{op} requires session cookies — sign in via the browser first")
    return header


def parse_cookie(cookie_header: str, name: str) -> str | None:
    """Extract a single cookie value from a header string."""
    for part in cookie_header.split(";"):
        k, _, v = part.strip().partition("=")
        if k == name:
            return v or None
    return None


def skill_secret(
    domain: str,
    identifier: str,
    item_type: str,
    value: dict,
    *,
    source: str | None = None,
    label: str | None = None,
    metadata: dict | None = None,
) -> dict:
    """Build a __secrets__ entry for credential storage."""
    entry = {
        "domain": domain,
        "identifier": identifier,
        "item_type": item_type,
        "value": value,
    }
    if source:
        entry["source"] = source
    if label:
        entry["label"] = label
    if metadata:
        entry["metadata"] = metadata
    return entry
