"""agentOS SDK — apps import what they need.

    from agentos import client, url, molt, shape   # network verbs, URL math, text, shapes
    from agentos import sql, crypto, oauth          # engine-dispatched modules
    from agentos import returns, provides           # operation decorators
    from agentos.services import web_search, web_read  # service constants
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
from agentos import llm
from agentos import checkpoint

# --- Operation decorators (read by engine via AST, no-ops at runtime) ---
from agentos.decorators import returns, provides, connection, timeout, claims, test

# --- Standard service constants (for @provides declarations) ---
# NOTE: the `llm` service constant is NOT imported here — `agentos.llm` is
# the SDK module. Use `from agentos.services import llm` in @provides.
from agentos.services import (
    web_search, web_read, email_lookup, flight_search,
    geocoding, map_tiles, file_list, file_read, file_info,
    volume_transport,
    cookie_auth, oauth_auth,
    login_credentials, password, api_key, signs_for,
    cdp_access, browser_session,
)

# --- Engine-dispatched modules (auth bridge) ---
from agentos import credentials

# --- The service broker — the primitive under every @provides(X) ---
from agentos import services

# --- Identity normalization helpers ---
from agentos import identity
from agentos.identity import normalize_email, normalize_phone, normalize_handle

# --- Fine-grained (available when you need specific control) ---
from agentos.text import clean_text, clean_html, clean_sentinel, strip_tags
from agentos.text import parse_int, parse_float
from agentos.dates import parse_date, iso_from_ms, iso_from_seconds

# Engine dispatch Client — talks to a running engine over its MCP socket.
# Auto-generated from the registry in crates/core/src/tools.rs (see D11
# in _roadmap/p1/unified-surface/unified-surface.md). External Python
# scripts use `from agentos import Client, AsyncClient`; apps use
# their in-process SDK modules above.
from agentos._engine_client import Client, AsyncClient, EngineError

__all__ = [
    # Core modules
    "client", "url", "molt", "shape",
    # Engine dispatch (external Python scripts)
    "Client", "AsyncClient", "EngineError",
    # Engine-dispatched modules
    "sql", "blobs", "crypto", "oauth", "shell", "llm", "checkpoint", "credentials",
    "services",
    # Identity helpers
    "identity", "normalize_email", "normalize_phone", "normalize_handle",
    # Operation decorators
    "returns", "provides", "connection", "timeout", "claims", "test",
    # Standard services
    "web_search", "web_read", "email_lookup", "flight_search",
    "geocoding", "map_tiles", "file_list", "file_read", "file_info",
    "volume_transport",
    "cookie_auth", "oauth_auth",
    "login_credentials", "password", "api_key", "signs_for",
    # App result helpers
    "app_error", "app_result", "app_secret",
    # Text (fine-grained)
    "clean_text", "clean_html", "clean_sentinel", "strip_tags",
    # Parsers (specific)
    "parse_int", "parse_float", "parse_date",
    "iso_from_ms", "iso_from_seconds",
]
