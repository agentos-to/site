"""URL string helpers — pure string math, no network, no identity.

Apps can't import ``urllib.parse`` directly (banned in the sandbox).
These helpers cover the cases ``client.get/post`` can't do for you
via ``params={...}``:

    url.build       — when you need the URL *string itself* (storing, returning, logging)
    url.parse       — when you need to inspect the parts of a URL you were given
    url.encode      — percent-encode a single PATH segment value
    url.decode      — percent-decode
    url.registrable — the eTLD+1 of a host (``"www.amazon.com"`` → ``"amazon.com"``)
    url.same_site   — do two hosts share a registrable domain?

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
    returning it from an app, or logging it. For plain outbound
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


# Multi-part public suffixes that actually come up in practice.
# The real Public Suffix List has ~10k entries; we cover the 99% case
# without a 200KB dependency that's a supply-chain attack surface.
# Extend as needed when a real service hits one that isn't here.
_MULTI_PART_SUFFIXES = frozenset({
    # Country-code second-level domains — commerce
    "co.uk", "co.jp", "co.kr", "co.nz", "co.za", "co.in", "co.il",
    "com.au", "com.br", "com.mx", "com.cn", "com.tw", "com.hk",
    "com.sg", "com.my", "com.ar", "com.tr", "com.pe", "com.ph",
    # Country-code second-level domains — organisations
    "org.uk", "org.au", "org.nz", "org.br", "org.za",
    "net.au", "net.nz", "ac.uk", "ac.jp", "gov.uk", "gov.au",
    # Google country domains — tricky because google.co.uk is one site
    # but google.com and google.de aren't related to the user's .co.uk
    # account; eTLD+1 handles this correctly via the co.uk suffix above.
})


def registrable(host: str) -> str:
    """Return the registrable domain ("eTLD+1") of a host.

    Strips subdomains and any leading dot; handles common multi-part
    TLDs (``co.uk``, ``com.au`` — see ``_MULTI_PART_SUFFIXES``).

        url.registrable("www.amazon.com")         # → "amazon.com"
        url.registrable("portal.aws.amazon.com")  # → "amazon.com"
        url.registrable("shop.amazon.co.uk")      # → "amazon.co.uk"
        url.registrable(".amazon.com")            # → "amazon.com"
        url.registrable("localhost")              # → "localhost"
        url.registrable("amazon.com:8080")        # → "amazon.com"

    Returns the input stripped to lowercase if it has fewer than
    two labels (e.g. ``"localhost"``).
    """
    h = host.strip().lower().lstrip(".")
    if ":" in h:
        h = h.split(":", 1)[0]
    labels = h.split(".")
    if len(labels) < 2:
        return h
    # If the last two labels form a known multi-part suffix, take three.
    tail_two = ".".join(labels[-2:])
    if tail_two in _MULTI_PART_SUFFIXES and len(labels) >= 3:
        return ".".join(labels[-3:])
    return tail_two


def same_site(a: str, b: str) -> bool:
    """Do two hosts share a registrable domain?

        url.same_site("www.amazon.com", "shop.amazon.com")  # → True
        url.same_site("amazon.com", "amazon.sg")            # → False
        url.same_site("aws.amazon.com", "www.amazon.com")   # → True

    Useful for credential-provider matching: decide whether a stored
    login URL belongs to the same site as the one the app is trying
    to authenticate against.
    """
    return registrable(a) == registrable(b)
