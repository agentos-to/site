# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `./dev.sh build` or `python3 codegen/gen_sdk_stubs.py`.

"""Cryptographic primitives — key derivation and symmetric decrypt.

Used almost exclusively by browser cookie decryption (Brave/Chrome/Edge all share the PBKDF2 + AES-128-CBC recipe)."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def aes(key: str, data: str, *, iv: str | None = None) -> bytes:
    """
    AES-128-CBC decrypt. Key, ciphertext, and IV are all hex-encoded.
    The returned plaintext is hex-encoded on the wire and decoded to
    bytes by the SDK stub.

    Args:
        key: hex (16 bytes = 32 hex chars for AES-128).
        data: ciphertext, hex.
        iv: hex. Default: 32 zero chars (Chrome convention).

    Returns:
        Plaintext bytes.
    """
    _req: dict[str, Any] = {}
    _req['key'] = key
    _req['data'] = data
    if iv is not None:
        _req['iv'] = iv
    hex_value = await dispatch('crypto.aes', _req)
    return bytes.fromhex(hex_value)


async def pbkdf2(password: str, salt: str, *, iterations: int | None = None, length: int | None = None) -> bytes:
    """
    PBKDF2-HMAC-SHA1 key derivation. Used by browser skills to reproduce
    Chrome's Safe Storage key stretch.

    Args:
        password, salt: opaque strings.
        iterations: default 1.
        length: output byte length (default 16).

    Returns:
        Derived key as bytes (hex-decoded by the SDK stub).
    """
    _req: dict[str, Any] = {}
    _req['password'] = password
    _req['salt'] = salt
    if iterations is not None:
        _req['iterations'] = iterations
    if length is not None:
        _req['length'] = length
    hex_value = await dispatch('crypto.pbkdf2', _req)
    return bytes.fromhex(hex_value)
