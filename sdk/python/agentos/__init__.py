"""agentOS SDK — apps import what they need.

    from agentos import client, url, molt, shape   # network verbs, URL math, text, shapes
    from agentos import sql, crypto, oauth          # engine-dispatched modules
    from agentos import returns, provides           # operation decorators
    from agentos import services                     # the brokered-service primitive
    from agentos.macos import keychain, plist       # platform-specific

    resp = await client.get("/api/auth/session")   # jar + bundle from the connection
    u = url.build("https://ex.com/s", params={"k": "coffee"})
    molt(s)                        # shed the mess → clean string
    rows = sql.query("SELECT ...", db="~/data.db")
"""

# --- Core modules ---
from agentos.text import molt
from agentos import client
from agentos import url
from agentos import shapes as shape

# --- App-result helpers ---
from agentos.results import app_error, app_result, app_secret

# --- Engine-dispatched modules ---
from agentos import sql
from agentos import blobs
from agentos import crypto
from agentos import oauth
from agentos import shell
from agentos.agent import chat, agent, AgentError
from agentos import checkpoint

# --- Operation decorators (read by engine via AST, no-ops at runtime) ---
from agentos.decorators import returns, provides, connection, timeout, claims, test, account

# --- Challenge artifacts (account protocol) ---
from agentos import qr

# --- Engine-dispatched modules (auth bridge) ---
from agentos import credentials

# --- Browser-driven session helpers — honest check + typed NeedsAuth ---
# The honest "will writes work?" signal for a connector running inside the
# engine-owned browser tab: the real httpOnly session cookie, read via the
# browser plane. Every browser-driven check_session gates on this.
from agentos import browser_session

# --- The service broker — the primitive under every @provides("name") ---
# Services are named by their bare string, never a constant — a service
# is self-registered from `@provides`, the same way an edge verb is from
# `create`. `services.call` / `services.list_providers` are the broker.
from agentos import services

# --- Identity normalization helpers ---
from agentos import identity
from agentos.identity import normalize_email, normalize_phone, normalize_handle

# --- Fine-grained (available when you need specific control) ---
from agentos.text import clean_text, clean_html, clean_sentinel, strip_tags
from agentos.text import parse_int, parse_float
from agentos.dates import parse_date, iso_from_ms, iso_from_seconds, canonicalize_datetime

# Engine dispatch Client — talks to a running engine over its MCP socket.
# Auto-generated from the registry in crates/core/src/tools.rs (see D11
# in _product/p1/unified-surface/unified-surface.md). External Python
# scripts use `from agentos import Client, AsyncClient`; apps use
# their in-process SDK modules above.
from agentos._engine_client import Client, AsyncClient, EngineError

__all__ = [
    # Core modules
    "client", "url", "molt", "shape",
    # Engine dispatch (external Python scripts)
    "Client", "AsyncClient", "EngineError",
    # Engine-dispatched modules
    "sql", "blobs", "crypto", "oauth", "shell", "checkpoint", "credentials",
    "services", "browser_session",
    # Model brokering — chat (one completion) + agent (a tool-loop)
    "chat", "agent", "AgentError",
    # Identity helpers
    "identity", "normalize_email", "normalize_phone", "normalize_handle",
    # Operation decorators
    "returns", "provides", "connection", "timeout", "claims", "test", "account",
    # Challenge artifacts
    "qr",
    # App result helpers
    "app_error", "app_result", "app_secret",
    # Text (fine-grained)
    "clean_text", "clean_html", "clean_sentinel", "strip_tags",
    # Parsers (specific)
    "parse_int", "parse_float", "parse_date",
    "iso_from_ms", "iso_from_seconds", "canonicalize_datetime",
]
