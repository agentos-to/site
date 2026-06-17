# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `python3 platform/codegen/generate.py`.

"""The service vocabulary + the broker.

A service is a named interface the engine brokers between strangers:
the caller names the interface, never the app. Use the constants in
`@provides` declarations —

    from agentos import provides
    from agentos.services import web_search

    @provides(web_search)
    def search(query: str, **params) -> list[dict]:
        ...

— and `call(...)` / `list_providers(...)` to consume a service across
app boundaries without naming the provider.

Contracts live in `platform/ontology/services/*.yaml`; the engine mints
the graph-side service nodes and `provides` edges from those contracts
plus each app's own declarations.
"""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch

# --- Service names ----------------------------------------------------
# One constant per `ontology/services/*.yaml` entry, alphabetical.

# An API key for a platform (credential provision).
api_key = "api_key"

# Audio transcription — speech-to-text from an audio file. Providers
# wrap a
audio_transcription = "audio_transcription"

# High-level typed browser session API on top of cdp_access.
browser_session = "browser_session"

# Raw protocol-level access to a debug-attachable Chromium browser.
cdp_access = "cdp_access"

# Provide fresh browser cookies for a domain (auth provision).
cookie_auth = "cookie_auth"

# Find a person's email address from name/domain signals.
email_lookup = "email_lookup"

# Stat one file — size, kind, timestamps.
file_info = "file_info"

# List files under a path.
file_list = "file_list"

# Read one file's contents.
file_read = "file_read"

# Search flights between airports on a date.
flight_search = "flight_search"

# Resolve place names ↔ coordinates.
geocoding = "geocoding"

# LLM inference — completions/chat from a model provider.
llm = "llm"

# {email|handle, password} tuple for a domain (credential provision).
login_credentials = "login_credentials"

# Headed sign-in window on the engine-owned browser profile.
login_window = "login_window"

# Serve map tile imagery for a viewport.
map_tiles = "map_tiles"

# Provide OAuth credentials for a platform (auth provision).
oauth_auth = "oauth_auth"

# A password for a caller-supplied identifier (credential provision).
password = "password"

# Passkey / hardware-key challenge signing (reserved).
signs_for = "signs_for"

# Announce + serve mountable volumes (the KIO-worker / 9P read-only
# core).
volume_transport = "volume_transport"

# Fetch one URL and return it as a webpage with content.
web_read = "web_read"

# Search the web. Providers: Brave Search, Exa, SerpAPI, …
web_search = "web_search"


# --- The broker --------------------------------------------------------


async def call(name: str, *, app: str | None = None, params: Any | None = None, verb: str | None = None) -> dict[str, Any]:
    """
    Matchmake a provider for service `name` and dispatch `verb` on it.
    The tool's return value is passed through unchanged — no envelope.

    Used by SDK wrappers (`credentials.retrieve`, `llm.oneshot`, etc.)
    and by apps that consume a service across app boundaries without
    naming the provider.

    Args:
        name: service name (e.g. `"login_credentials"`, `"llm"`).
        verb: tool to invoke on the picked provider. Defaults to the
              provider's declared `via`.
        params: parameters forwarded to the picked tool, unchanged.
        app: optional app-id override; forces a specific provider.

    Returns:
        The picked tool's return value, unchanged.
    """
    _req: dict[str, Any] = {}
    _req['name'] = name
    if app is not None:
        _req['app'] = app
    if params is not None:
        _req['params'] = params
    if verb is not None:
        _req['verb'] = verb
    return await dispatch('services.call', _req)


async def list_providers(name: str, *, model: str | None = None) -> dict[str, Any]:
    """
    Enumerate apps that provide service `name`. Returns the ranked
    candidate list without dispatching any tool — useful for
    introspection, provider selection, or iterating providers with
    per-provider fallback logic in app code.

    Args:
        name: service name.
        model: optional model filter for `llm` service matches.

    Returns:
        `{providers: [{app_id, via, cred_state, urls?}, ...]}`.
    """
    _req: dict[str, Any] = {}
    _req['name'] = name
    if model is not None:
        _req['model'] = model
    return await dispatch('services.list_providers', _req)
