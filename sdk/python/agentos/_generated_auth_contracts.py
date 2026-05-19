"""Auto-generated auth provider contracts — do not edit.

Single source of truth: docs/auth-contracts/{oauth,cookie}.yaml.
Regenerate with: python docs/generate.py

Skills decorated `@provides(oauth_auth, ...)` should return a dict
matching `OAuthCredential`. Skills decorated `@provides(cookie_auth, ...)`
return `CookieCredential`. agent-sdk validate enforces this at commit
time using the AUTH_CONTRACTS dict at the bottom of this file.
"""

from __future__ import annotations

from typing import Any, TypedDict

class OAuthCredential(TypedDict, total=False):
    """Return shape for `@provides(oauth_auth, ...)` skill operations. Engine consumes via crates/auth/src/types.rs (Session::to_auth_header, auth_fields) and crates/auth/src/resolve.rs (token-refresh path).

    All fields snake_case to match the OAuth 2.0 spec (RFC 6749 §5.1)
    and the engine resolver (crates/auth/src/types.rs). Required:
    `access_token`. Strongly recommended for refresh:
    `refresh_token`, `expires_in`, `client_id`, `token_url`.
    """
    access_token: str
    refresh_token: str
    expires_in: int
    scope: str
    client_id: str
    token_url: str


class Cookie(TypedDict, total=False):
    """A single cookie in a CookieCredential.cookies array."""
    name: str
    value: str
    expires: float
    created: float
    domain: str
    path: str
    secure: bool
    httpOnly: bool


class CookieCredential(TypedDict, total=False):
    """Return shape for `@provides(cookie_auth, ...)` skill operations. Top-level dict with `cookies: [Cookie, ...]`; each Cookie has a `name` + `value` and optional `expires` / `created` for freshness arbitration in crates/auth/src/source.rs."""
    domain: str
    cookies: list[Cookie]
    count: int
    source: str


# Machine-readable contract — what agent-sdk validate enforces.
# Every key here corresponds to a `@provides(<name>_auth, ...)`
# decorator. Format:
#   {'required': [field, ...], 'recommended': [field, ...],
#    'forbidden_camel_case': {camelCase: snake_case_replacement, ...}}
AUTH_CONTRACTS: dict[str, dict] = {
    'cookie': {
        'required': [],
        'recommended': [],
        'forbidden_camel_case': {'cookieName': 'name', 'cookieValue': 'value', 'expiresAt': 'expires', 'createdAt': 'created', 'httpOnlyFlag': 'httpOnly'},
        'cookie_fields_required': ['name', 'value'],
        'cookie_fields_recommended': ['expires', 'created', 'domain', 'path', 'secure', 'httpOnly'],
    },
    'oauth': {
        'required': ['access_token'],
        'recommended': ['refresh_token', 'expires_in', 'scope', 'client_id', 'token_url'],
        'forbidden_camel_case': {'accessToken': 'access_token', 'refreshToken': 'refresh_token', 'expiresIn': 'expires_in', 'clientId': 'client_id', 'tokenUrl': 'token_url', 'clientSecret': 'client_secret'},
    },
}
