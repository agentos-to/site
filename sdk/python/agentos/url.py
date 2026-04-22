"""URL string helpers — pure string math, no network, no identity.

Skills can't import ``urllib.parse`` directly (banned in the sandbox).
These four helpers cover the cases ``client.get/post`` can't do for you
via ``params={...}``:

    url.build   — when you need the URL *string itself* (storing, returning, logging)
    url.parse   — when you need to inspect the parts of a URL you were given
    url.encode  — percent-encode a single PATH segment value
    url.decode  — percent-decode

Query params on an outbound request: pass ``params=`` to
``client.get/post`` — the engine encodes for you.
"""

from __future__ import annotations

import urllib.parse as _urllib_parse


class ParsedURL:
    """Parsed URL with the query already decoded into a dict.

    Attributes:
        scheme:   URL scheme (e.g. ``"https"``).
        host:     Host including port if present (e.g. ``"api.example.com:8080"``).
        path:     URL path (e.g. ``"/v1/users"``).
        query:    Query params as a dict. Multi-value params become lists;
                  single-value params are plain strings.
        fragment: URL fragment (without the leading ``"#"``).
    """

    __slots__ = ("scheme", "host", "path", "query", "fragment")

    def __init__(
        self,
        scheme: str,
        host: str,
        path: str,
        query: dict[str, str | list[str]],
        fragment: str,
    ):
        self.scheme = scheme
        self.host = host
        self.path = path
        self.query = query
        self.fragment = fragment

    def __repr__(self) -> str:
        return (
            f"ParsedURL(scheme={self.scheme!r}, host={self.host!r}, "
            f"path={self.path!r}, query={self.query!r}, "
            f"fragment={self.fragment!r})"
        )


def build(base: str, params: dict | None = None) -> str:
    """Build a URL by attaching query params to a base URL.

    Use this when you need the URL *string itself* — storing it,
    returning it from a skill, or logging it. For plain outbound
    requests, pass ``params=`` directly to ``client.get/post``.

        u = url.build("https://www.amazon.com/s", params={"k": "coffee"})
        # → "https://www.amazon.com/s?k=coffee"

    Params are URL-encoded using form rules (spaces become ``'+'``).
    List values produce repeated keys (``?k=a&k=b``). ``None`` values
    are skipped."""
    if not params:
        return base
    filtered = {k: v for k, v in params.items() if v is not None}
    if not filtered:
        return base
    query = _urllib_parse.urlencode(filtered, doseq=True)
    sep = "&" if "?" in base else "?"
    return f"{base}{sep}{query}"


def parse(url: str) -> ParsedURL:
    """Parse a URL into a ``ParsedURL`` with the query pre-decoded.

    Unlike ``urllib.parse.urlparse``, the query is returned as a dict —
    no separate ``parse_qs`` step. Single-value params are scalars;
    multi-value params become lists.

        p = url.parse("https://example.com/cb?email=a@b.com&x=1")
        p.scheme     # "https"
        p.host       # "example.com"
        p.path       # "/cb"
        p.query      # {"email": "a@b.com", "x": "1"}
    """
    p = _urllib_parse.urlparse(url)
    raw_query = _urllib_parse.parse_qs(p.query, keep_blank_values=True)
    query: dict[str, str | list[str]] = {
        k: (v[0] if len(v) == 1 else v) for k, v in raw_query.items()
    }
    return ParsedURL(
        scheme=p.scheme,
        host=p.netloc,
        path=p.path,
        query=query,
        fragment=p.fragment,
    )


def encode(value: str) -> str:
    """Percent-encode a single value for use in a URL path segment.

    This is the escape hatch for values that go into the URL path (not
    query params). For query params, prefer ``url.build(..., params=...)``
    or pass ``params=`` directly to ``client.get/post``.

        u = f"https://img.logo.dev/name:{url.encode(name)}"
    """
    return _urllib_parse.quote(value, safe="")


def decode(value: str) -> str:
    """Percent-decode a value. Inverse of ``encode``.

        folder = url.decode(folder[7:])  # strip "file://" then decode
    """
    return _urllib_parse.unquote(value)
