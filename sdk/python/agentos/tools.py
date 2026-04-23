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

# LLM inference
llm = "llm"

# Auth provision (browser cookie providers, OAuth providers)
cookie_auth = "cookie_auth"
oauth_auth = "oauth_auth"

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
