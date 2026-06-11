"""macOS Keychain access — thin facade over the cross-platform `secrets` SDK.

The actual implementation is the platform-abstract `agentos.secrets` module,
which on macOS talks to the login keychain via the `security` CLI. This
module exists so existing apps can `from agentos.macos import keychain`
during the runtime-core cutover; new code should import `secrets` directly.

    from agentos import secrets

    token = await secrets.read("Claude Code-credentials")
    blob  = await secrets.read_binary("Mimestream: joe@example.com", account="OAuth")
"""

from __future__ import annotations

from agentos import secrets


async def read(
    service: str,
    *,
    account: str | None = None,
    binary: bool = False,
) -> str | bytes:
    """Read a secret from the platform secret store.

    Args:
        service: Secret service name. Required.
        account: Account name. Defaults to the current user when omitted.
        binary: If True, return the secret as `bytes` (hex-decoded on the
            engine side). Use for NSKeyedArchiver plists and other
            non-string entries.

    Returns:
        The secret as `str` (text mode) or `bytes` (binary mode).

    Raises:
        RuntimeError: The entry was not found or the lookup failed.
    """
    if binary:
        return await secrets.read_binary(service=service, account=account)
    return await secrets.read(service=service, account=account)
