# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `./dev.sh build` or `python3 codegen/gen_sdk_stubs.py`.

"""Generic capability dispatch — one primitive over every `@provides(X)` skill.

`capability.call(name, verb, params)` matchmakes a provider for the named capability and dispatches `verb` on it. `capability.list_providers(name)` enumerates candidates without dispatching. Replaces per-capability bespoke SDK wrappers — skills that need cross-skill access to a capability reach through this module, and the engine never needs bespoke Rust per new capability."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def call(name: str, *, params: Any | None = None, skill: str | None = None, verb: str | None = None) -> dict[str, Any]:
    """
    Matchmake a provider for capability `name` and dispatch `verb` on it.
    The tool's return value is passed through unchanged — no envelope.

    Used by SDK wrappers (`credentials.retrieve`, `llm.oneshot`, etc.)
    and by skills that consume a capability across skill boundaries
    without naming the provider.

    Args:
        name: capability name (e.g. `"login_credentials"`, `"llm"`).
        verb: tool to invoke on the picked provider. Defaults to the
              provider's declared `via`.
        params: parameters forwarded to the picked tool, unchanged.
        skill: optional skill-id override; forces a specific provider.

    Returns:
        The picked tool's return value, unchanged.
    """
    _req: dict[str, Any] = {}
    _req['name'] = name
    if params is not None:
        _req['params'] = params
    if skill is not None:
        _req['skill'] = skill
    if verb is not None:
        _req['verb'] = verb
    return await dispatch('capability.call', _req)


async def list_providers(name: str, *, model: str | None = None) -> dict[str, Any]:
    """
    Enumerate skills that declared `@provides(name, ...)`. Returns the
    ranked candidate list without dispatching any tool — useful for
    introspection, provider selection, or iterating providers with
    per-provider fallback logic in skill code.

    Args:
        name: capability name.
        model: optional model filter for `llm` capability matches.

    Returns:
        `{providers: [{skill_id, via, cred_state, urls?}, ...]}`.
    """
    _req: dict[str, Any] = {}
    _req['name'] = name
    if model is not None:
        _req['model'] = model
    return await dispatch('capability.list_providers', _req)
