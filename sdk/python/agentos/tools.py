"""Standard tool constants — the vocabulary of capabilities skills can provide.

Import these for @provides decorators. Using constants instead of strings gives:
- IDE autocomplete
- Typo detection (@provides(web_serach) → NameError at import time)
- Discoverability (agent-sdk tools)
- One definition, everywhere

Usage:
    from agentos import provides, web_search, web_read

    @provides(web_search)
    def search(query: str, **params) -> list[dict]:
        ...
"""

# Discovery & retrieval
web_search = "web_search"
web_read = "web_read"

# People
email_lookup = "email_lookup"

# Travel
flight_search = "flight_search"
geocoding = "geocoding"
map_tiles = "map_tiles"

# Files
file_list = "file_list"
file_read = "file_read"
file_info = "file_info"

# Volume transport — the skill announces mountable volumes and serves
# their contents to the finder/graph layer. One capability, a fixed
# three-verb interface (the KIO-worker / 9P read-only core):
#
#   list_volumes()              → volume[]  (ANNOUNCE — called at boot +
#                                 on refresh; entries upsert as volume
#                                 nodes under a realm)
#   list_contents(id, cursor?)  → typed child nodes + nextCursor (SERVE)
#   read_node(id)               → one node's full detail
#
# `@provides(volume_transport)` goes on `list_volumes` only — it marks
# the skill as a transport; `list_contents` / `read_node` are reached by
# their fixed names on the announcing skill (browse binds to the stamped
# provider, never a fresh capability walk). Read-only by construction:
# the write verbs don't exist yet. Contract:
# core/_roadmap/p2/realms-transports/plan.md "The transport contract".
volume_transport = "volume_transport"

# LLM inference
llm = "llm"

# Auth provision (browser cookie providers, OAuth providers)
cookie_auth = "cookie_auth"
oauth_auth = "oauth_auth"

# Browser control — the capability stack for driving a live browser.
#
# `cdp_access`       — raw, protocol-level access. A provider returns a CDP
#                      WebSocket URL + target descriptor for a debug-attachable
#                      Chromium browser. Tiny surface: one `cdp_connect` tool.
#                      Brave is today's provider; Chrome/Link/Arc could join.
# `browser_session`  — high-level, typed session API on top of `cdp_access`.
#                      A provider exposes `session_open / navigate / evaluate /
#                      on_event / get_cookies / get_storage / close`, hides the
#                      protocol. This is what reverse-engineering, scraping,
#                      and interaction-driving skills should consume — never
#                      `cdp_access` directly.
#
# See `_roadmap/p2/browser-control-skill.md` for the architecture.
cdp_access = "cdp_access"
browser_session = "browser_session"

# Credential provision (password managers, keychains, vaults).
# Providers declaring these wire in through the engine's
# `credentials.retrieve` matchmaking — skills' `login` tools resolve
# their inputs without the LLM ever seeing raw secret values.
#
# `login_credentials` — `{email|handle, password}` tuple for a domain.
# `password`          — a password for a caller-supplied identifier.
# `api_key`           — an API key for a service.
#
# `signs_for` is reserved for passkey / hardware-key providers that sign
# challenges rather than returning secret material. No resolver ships in
# P1; the constant is defined so the interface shape is fixed now.
login_credentials = "login_credentials"
password = "password"
api_key = "api_key"
signs_for = "signs_for"
