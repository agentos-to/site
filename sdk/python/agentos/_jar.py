"""Per-call cookie jar — SDK-internal, ambient to one tool invocation.

Two ContextVars, both scoped to exactly one tool call:

- ``_current_connection`` — set at tool entry from the engine's
  ``__call__.connection`` channel. Carries ``{name, mode, domain,
  identifier, cookies_in}`` where ``cookies_in`` is the Cookie-header
  string already resolved by the engine (same bytes today's skills
  read from ``params["auth"]["cookies"]``).
- ``_jar_delta`` — accumulates ``Set-Cookie`` captures during the tool
  body. On tool exit, ``_bridge`` merges non-empty deltas into
  ``__cookie_delta__`` on the result; the engine upserts into the
  credential row keyed on ``(domain, identifier)``.

Skills never touch either. ``http.get/post`` reads
``_current_connection`` to decide whether to attach cookies +
browser-header bundles, and appends to ``_jar_delta`` after each
response. Plaintext cookies live in the Python worker's memory for
exactly the duration of one tool call, then die when the ContextVars
reset.

No export from ``agentos/__init__.py`` — this module is strictly
SDK-internal.
"""

from __future__ import annotations

from contextvars import ContextVar
from typing import TypedDict


class ConnectionCtx(TypedDict, total=False):
    name: str
    mode: str  # "browser" | "fetch" | "api"
    domain: str
    identifier: str
    cookies_in: str  # Cookie-header bytes, resolved by the engine


_current_connection: ContextVar[ConnectionCtx | None] = ContextVar(
    "agentos_current_connection", default=None
)

_jar_delta: ContextVar[dict[str, str]] = ContextVar(
    "agentos_jar_delta", default={}
)
