# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `python3 platform/codegen/generate.py`.

"""plist.* ops — NSKeyedArchiver binary plist parsing.

Used by browser skills to parse keychain-stored NSKeyedArchiver blobs.
Handlers live in agentos-exec-executors."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def parse(hex_data: str, extract: dict[str, int]) -> dict[str, Any]:
    """
    Parse a hex-encoded NSKeyedArchiver binary plist and extract specific
    object indices.

    Args:
        hex_data: The plist as hex.
        extract: Mapping of {field_name: object_index} in the archived graph.

    Returns:
        Dict of {field_name: value}.
    """
    _req: dict[str, Any] = {}
    _req['hex_data'] = hex_data
    _req['extract'] = extract
    return await dispatch('plist.parse', _req)
