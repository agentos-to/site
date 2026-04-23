# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `./dev.sh build` or `python3 codegen/gen_sdk_stubs.py`.

"""Agent-driven credential resolution.

`credentials.retrieve(domain, required)` asks the engine to matchmake an installed `@provides(login_credentials)` skill (1Password, Keychain, etc.) and return the resolved fields. Skills call this from their `login` tools when the caller didn't pass credentials explicitly."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def retrieve(domain: str, *, account: str | None = None, required: list[str] | None = None) -> dict[str, Any]:
    """
    Ask the engine to resolve login credentials for the given domain by
    matchmaking skills that declare `@provides(login_credentials)`.
    Returns `{found, identifier, value, source}`. Skills call this from
    their `login` tools when the caller didn't pass credentials explicitly.

    Args:
        domain: Canonical credential-store domain (e.g. `".approach.app"`).
        required: Field names the caller needs (e.g. `["email", "password"]`).
        account: Optional disambiguator when multiple items match.

    Returns:
        A `{found, identifier, value, source}` envelope. On no-match,
        `found` is `false` and the caller should raise `NeedsCredentials`.
    """
    _req: dict[str, Any] = {}
    _req['domain'] = domain
    if account is not None:
        _req['account'] = account
    if required is not None:
        _req['required'] = required
    return await dispatch('credentials.retrieve', _req)
