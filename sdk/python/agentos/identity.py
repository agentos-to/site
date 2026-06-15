"""Identifier normalization helpers — call these from `check_session`,
`get_profile`, and credential-provider tools before returning.

The credential store and account-graph nodes hold **only canonical form**.
A `Joe@Home.com` in 1Password and a `joe@home.com` in Brave's cookie DB
have to collide on freshness-compare; stripping casing and punycoding
the domain at the SDK layer is how we make that happen, without any
engine-side normalization logic.

The engine trusts what apps return. These helpers are the contract.

Conventions per `_product/p1/fix-auth/credential-providers-and-identity.md`
Decision 8:

- **Email**: lowercase local-part + IDN-punycode domain. No Gmail
  dot-stripping, no plus-addressing stripping — those transformations
  are unsafe on Workspace custom domains, and the agent doesn't need
  them to join identities because `identifier`, `email`, and `userId`
  are independent fields.
- **Phone**: E.164 via `phonenumbers`. Input must carry a country code
  or the app must supply a `default_region`. Ambiguous input raises.
- **Handle**: NFKC normalization + casefold. Covers Unicode
  homoglyphs and mixed-case username collisions.
"""

from __future__ import annotations

import unicodedata

import idna
import phonenumbers


def normalize_email(raw: str) -> str:
    """Lowercase local-part + IDN-punycode domain.

    Raises `ValueError` on malformed input (missing `@`, empty local-part).

    Examples:
        normalize_email("Joe@Home.com")   → "joe@home.com"
        normalize_email("joe@münchen.de") → "joe@xn--mnchen-3ya.de"
    """
    s = raw.strip()
    local, sep, domain = s.partition("@")
    if not sep or not local or not domain:
        raise ValueError(f"not an email: {raw!r}")
    canonical_domain = idna.encode(domain, uts46=True).decode("ascii")
    return f"{local.lower()}@{canonical_domain}"


def normalize_phone(raw: str, default_region: str | None = None) -> str:
    """E.164 format via `phonenumbers`.

    If `raw` carries a country code (starts with `+`), `default_region`
    can be omitted. Otherwise the caller must pass the ISO-3166 region
    (e.g. `"US"`). Raises `ValueError` on ambiguous or unparseable input.

    Examples:
        normalize_phone("+1 (555) 123-4567")    → "+15551234567"
        normalize_phone("(555) 123-4567", "US") → "+15551234567"
    """
    try:
        parsed = phonenumbers.parse(raw, default_region)
    except phonenumbers.NumberParseException as e:
        raise ValueError(f"not a phone number: {raw!r} ({e})") from e
    if not phonenumbers.is_valid_number(parsed):
        raise ValueError(f"not a valid phone number: {raw!r}")
    return phonenumbers.format_number(
        parsed, phonenumbers.PhoneNumberFormat.E164
    )


def normalize_handle(raw: str) -> str:
    """NFKC normalization + casefold for social-style handles.

    Casefold is Unicode-aware (handles Turkish i, German ß, etc.) and
    catches more than `.lower()`. Use this for GitHub / Twitter /
    Mastodon / Reddit handles — anywhere the service treats usernames
    as case-insensitive but stores the user's original capitalization
    for display.

    Examples:
        normalize_handle("JoeContini")    → "joecontini"
        normalize_handle("Straße")        → "strasse"
    """
    return unicodedata.normalize("NFKC", raw.strip()).casefold()
