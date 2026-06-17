# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `python3 platform/codegen/generate.py`.

"""services.* ops — generic service dispatch.

Apps never name each other. Consumers ask for a service; the engine
walks the apps providing it, picks one (the service node's
`defaults_to` app first, then the usual ranking), dispatches."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


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
