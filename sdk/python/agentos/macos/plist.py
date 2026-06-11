"""macOS NSKeyedArchiver binary plist parsing — facade over `agentos.plist`.

The cross-platform implementation lives in `agentos.plist`. This module
exists so existing apps can continue to `from agentos.macos import plist`
during the runtime-core cutover; new code should import `plist` directly.

    from agentos import plist

    fields = await plist.parse(
        hex_data,
        extract={"refresh_token": 32, "client_id": 13, "token_url": 10},
    )
"""

from __future__ import annotations

from agentos import plist as _plist


async def parse(hex_data: str, extract: dict[str, int]) -> dict[str, str]:
    """Parse an NSKeyedArchiver binary plist and extract string fields.

    Args:
        hex_data: Hex-encoded binary plist data. Typically obtained from
            `secrets.read_binary(...)`.
        extract: Dict mapping output field names to NSKeyedArchiver object
            indices. The engine walks the object graph at each index and
            returns the string at that position.

    Returns:
        Dict of field name → extracted string. Indices that don't resolve
        to a string are omitted.

    Raises:
        RuntimeError: The plist is malformed or the engine call fails.
    """
    return await _plist.parse(hex_data=hex_data, extract=extract)
