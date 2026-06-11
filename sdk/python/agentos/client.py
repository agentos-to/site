"""The Client surface — network verbs scoped to the current tool call.

Each connection is a client. There are three kinds: a browser, a fetch,
and an API client. The connection picks the kind via ``client="…"``;
apps write ``await client.get("/path")`` and the matching header bundle
is composed from the call's ``client="browser" | "fetch" | "api"`` kind.

Per-call overrides exist for the rare case where a single request
inside a tool needs to break from the connection's defaults:

    await client.get(url, client="fetch")     # XHR-style for one call
    await client.get(url, headers={...})       # merge on top of bundle
    await client.get(url, skip_cookies=[...])  # strip named cookies from
                                               # a caller-supplied Cookie:
"""

from __future__ import annotations

import json as _json
import urllib.parse as _urllib_parse

from agentos._bridge import dispatch


# ---------------------------------------------------------------------------
# Header bundles — per client kind. Moved from the old http.headers() helper;
# now driven by the connection's ``client="browser" | "fetch" | "api"`` value
# rather than by a caller-specified knob.
#
# Chrome identity: MUST track wreq's TLS emulation and the Rust
# BROWSER_DEFAULT_* constants in executor.rs. Updating the version is a
# two-repo change — Rust-side Emulation::ChromeNNN + Python-side _CHROME_*.
# ---------------------------------------------------------------------------


_CHROME_VERSION = "145"
_CHROME_FULL_VERSION = "145.0.7493.92"

_UA_DESKTOP = (
    f"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    f"AppleWebKit/537.36 (KHTML, like Gecko) "
    f"Chrome/{_CHROME_VERSION}.0.0.0 Safari/537.36"
)

# Baseline that every browser/fetch request carries.
_BUNDLE_COMMON = {
    "User-Agent": _UA_DESKTOP,
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Sec-CH-UA": f'"Chromium";v="{_CHROME_VERSION}", "Not:A-Brand";v="99"',
    "Sec-CH-UA-Mobile": "?0",
    "Sec-CH-UA-Platform": '"macOS"',
}

# Full Chrome navigation bundle — what a real browser address-bar hit sends.
_BUNDLE_BROWSER = {
    **_BUNDLE_COMMON,
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,image/apng,*/*;q=0.8"
    ),
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "Cache-Control": "max-age=0",
    # Structured client hints — Amazon Lightsaber and similar WAFs check.
    "Sec-CH-UA-Full-Version-List": (
        f'"Chromium";v="{_CHROME_FULL_VERSION}", '
        f'"Not:A-Brand";v="99.0.0.0"'
    ),
}

# XHR-style bundle — what in-page fetch()/XMLHttpRequest sends.
_BUNDLE_FETCH = {
    **_BUNDLE_COMMON,
    "Accept": "application/json",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}


def _bundle_for(kind: str | None) -> dict:
    """Return the header bundle for a client kind, or an empty dict for
    the stateless ``"api"`` kind. Unknown kinds fall through to empty —
    the validator blocks them statically."""
    if kind == "browser":
        return dict(_BUNDLE_BROWSER)
    if kind == "fetch":
        return dict(_BUNDLE_FETCH)
    return {}


# ---------------------------------------------------------------------------
# Body serialization — SDK owns this, engine is pure transport.
# ---------------------------------------------------------------------------


def _prepare_body(json=None, data=None, body=None, headers=None):
    """Turn the SDK-level conveniences (json=, data=, body=) into a raw
    body string + Content-Type header. Returns ``(body, headers_dict)``.

    Priority: ``json`` > ``data`` > ``body``. Caller-supplied
    ``Content-Type`` in ``headers`` always wins — ``setdefault`` never
    overrides."""
    out_headers = dict(headers or {})
    out_body = None
    if json is not None:
        out_body = _json.dumps(json)
        out_headers.setdefault("Content-Type", "application/json")
    elif data is not None:
        if isinstance(data, dict):
            out_body = _urllib_parse.urlencode(data, doseq=True)
            out_headers.setdefault(
                "Content-Type", "application/x-www-form-urlencoded"
            )
        else:
            out_body = data  # raw string / bytes passthrough
    elif body is not None:
        out_body = body
    return out_body, out_headers


# ---------------------------------------------------------------------------
# _request — the single code path every verb funnels into.
# ---------------------------------------------------------------------------


async def _request(method: str, url: str, **kwargs) -> dict:
    """Serialize SDK kwargs into an ``http.request`` envelope, attach the
    header bundle for the call's client kind, and dispatch.

    Per-call overrides:
      - ``client="browser" | "fetch" | "api"`` selects the header bundle
        for this call. ``api`` (the default) ships no bundle.
      - ``headers={...}`` merge on top of the bundle (caller wins).
      - ``skip_cookies=["name", ...]`` strips specific cookie names from
        a caller-supplied ``Cookie:`` header before send. Used by Amazon
        to drop ``csd-key`` / ``csm-hit`` / ``aws-waf-token``, which trip
        Lightsaber bot detection."""
    json_body = kwargs.pop("json", None)
    data = kwargs.pop("data", None)
    body = kwargs.pop("body", None)
    headers = kwargs.pop("headers", None)
    kind = kwargs.pop("client", None)
    skip_cookies = kwargs.pop("skip_cookies", None) or ()

    out_body, caller_headers = _prepare_body(
        json=json_body, data=data, body=body, headers=headers
    )

    # Compose headers: bundle < caller. (Same-key caller entry wins.)
    bundle = _bundle_for(kind)
    merged_headers = {**bundle, **caller_headers}

    # Strip named cookies from a caller-supplied Cookie: header.
    if skip_cookies:
        cookie_header = next(
            (v for k, v in merged_headers.items() if k.lower() == "cookie"),
            None,
        )
        if cookie_header:
            skip_set = set(skip_cookies)
            parts = [p for p in (part.strip() for part in cookie_header.split(";")) if p]
            filtered = "; ".join(
                p for p in parts if p.split("=", 1)[0] not in skip_set
            )
            for k in list(merged_headers):
                if k.lower() == "cookie":
                    if filtered:
                        merged_headers[k] = filtered
                    else:
                        del merged_headers[k]

    envelope = {"method": method, "url": url, **kwargs}
    if out_body is not None:
        envelope["body"] = out_body
    if merged_headers:
        envelope["headers"] = merged_headers

    return await dispatch("http.request", envelope)


# ---------------------------------------------------------------------------
# Public verbs. Thin wrappers — one implementation, six names.
# ---------------------------------------------------------------------------


async def get(url: str, **kwargs) -> dict:
    """HTTP GET. Returns ``{status, ok, url, headers, body, json}``."""
    return await _request("GET", url, **kwargs)


async def post(url: str, **kwargs) -> dict:
    """HTTP POST. Accepts ``json=``, ``data=``, ``body=``, ``headers=``,
    ``params=``.

    - ``json=obj`` — serialized as JSON; Content-Type = ``application/json``.
    - ``data=dict`` — URL-encoded form; Content-Type =
      ``application/x-www-form-urlencoded``.
    - ``data=str`` / ``body=str`` — sent as-is; no Content-Type added.
    - ``headers={"Content-Type": "..."}`` — always wins."""
    return await _request("POST", url, **kwargs)


async def put(url: str, **kwargs) -> dict:
    """HTTP PUT. Same body conventions as ``post``."""
    return await _request("PUT", url, **kwargs)


async def delete(url: str, **kwargs) -> dict:
    """HTTP DELETE. Same body conventions as ``post``."""
    return await _request("DELETE", url, **kwargs)


async def patch(url: str, **kwargs) -> dict:
    """HTTP PATCH. Same body conventions as ``post``."""
    return await _request("PATCH", url, **kwargs)


async def head(url: str, **kwargs) -> dict:
    """HTTP HEAD."""
    return await _request("HEAD", url, **kwargs)
