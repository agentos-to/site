# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `./dev.sh build` or `python3 codegen/gen_sdk_stubs.py`.

"""OS-level secret store access through the engine.

Reads entries from the platform's secret store — macOS login keychain via the `security` CLI, Windows Credential Manager, or Linux Secret Service. The underlying platform is chosen by the Rust crate `agentos-secrets` at compile time via `#[cfg(target_os)]`. All calls are async and routed through the engine so every read is logged and auditable."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def read(service: str, *, account: str | None = None) -> str:
    """
    Read a UTF-8 secret from the platform secret store.

    Args:
        service: Keychain service name (e.g. "Chrome Safe Storage").
        account: Account name. Defaults to the current $USER.

    Returns:
        The secret as a UTF-8 string.
    """
    _req: dict[str, Any] = {}
    _req['service'] = service
    if account is not None:
        _req['account'] = account
    return await dispatch('secrets.read', _req)


async def read_binary(service: str, *, account: str | None = None) -> bytes:
    """
    Read a binary secret from the platform secret store. Used for
    NSKeyedArchiver blobs (Chrome Safe Storage binary entries, etc.).

    Bytes travel hex-encoded; the generated SDK stub decodes to bytes.

    Args:
        service: Keychain service name.
        account: Account name. Defaults to the current $USER.

    Returns:
        The secret value as bytes (decoded from hex by the SDK stub).
    """
    _req: dict[str, Any] = {}
    _req['service'] = service
    if account is not None:
        _req['account'] = account
    hex_value = await dispatch('secrets.read_binary', _req)
    return bytes.fromhex(hex_value)
