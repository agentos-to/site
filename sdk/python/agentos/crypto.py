# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `python3 platform/codegen/generate.py`.

"""crypto.* ops — key derivation and symmetric decryption.

Used almost exclusively by browser apps decrypting stored cookies.
Handlers live in agentos-exec-executors."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def aes(key: str, data: str, *, iv: str | None = None) -> bytes:
    """
    AES-CBC decrypt with PKCS7 padding. The AES variant is chosen by key
    length: a 16-byte key → AES-128, a 32-byte key → AES-256. Key,
    ciphertext, and IV are all hex-encoded; plaintext is hex on the wire
    and decoded to bytes by the SDK stub.

    Args:
        key: hex — 16 bytes (AES-128) or 32 bytes (AES-256).
        data: ciphertext, hex.
        iv: hex, 16 bytes. Default: 32 zero chars (Chrome convention).

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


async def aes_gcm(key: str, data: str, iv: str) -> bytes:
    """
    AES-GCM authenticated decrypt. Key length selects AES-128 (16) or
    AES-256 (32). Ciphertext must include the trailing GCM tag (as produced
    by A256GCM / similar). IV/nonce is typically 12 bytes.

    Args:
        key: hex — 16 or 32 bytes.
        data: ciphertext ‖ tag, hex.
        iv: nonce as hex.

    Returns:
        Plaintext bytes.
    """
    _req: dict[str, Any] = {}
    _req['key'] = key
    _req['data'] = data
    _req['iv'] = iv
    hex_value = await dispatch('crypto.aes_gcm', _req)
    return bytes.fromhex(hex_value)


async def hkdf(key: str, *, info: str | None = None, length: int | None = None, salt: str | None = None) -> bytes:
    """
    HKDF-SHA256 key derivation (RFC 5869): HMAC-extract then expand. The
    canonical primitive for end-to-end media — WhatsApp/Signal expand a
    32-byte mediaKey into iv‖cipherKey‖macKey via an application-specific
    info string (e.g. "WhatsApp Audio Keys").

    Args:
        key: input keying material (IKM) as hex.
        info: context/application string (UTF-8). Default empty.
        salt: optional salt as hex. Empty → 32 zero bytes (SHA-256 block).
        length: output length in bytes. Default 32.

    Returns:
        Derived key material as bytes (hex-decoded by the SDK stub).
    """
    _req: dict[str, Any] = {}
    _req['key'] = key
    if info is not None:
        _req['info'] = info
    if length is not None:
        _req['length'] = length
    if salt is not None:
        _req['salt'] = salt
    hex_value = await dispatch('crypto.hkdf', _req)
    return bytes.fromhex(hex_value)


async def pbkdf2(password: str, salt: str, *, iterations: int | None = None, length: int | None = None) -> bytes:
    """
    PBKDF2-HMAC-SHA1 key derivation. Used by browser apps to reproduce
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


async def pbkdf2_sha256(password: str, salt: str, iterations: int, *, length: int | None = None) -> bytes:
    """
    PBKDF2-HMAC-SHA256. Companion to crypto.pbkdf2 (which is SHA1 for
    Chromium cookie unlock). Salt is hex so callers can pass binary
    material from a prior HKDF step.

    Args:
        password: UTF-8 password string.
        salt: salt as hex.
        iterations: iteration count.
        length: output byte length (default 32).

    Returns:
        Derived key as bytes (hex-decoded by the SDK stub).
    """
    _req: dict[str, Any] = {}
    _req['password'] = password
    _req['salt'] = salt
    _req['iterations'] = iterations
    if length is not None:
        _req['length'] = length
    hex_value = await dispatch('crypto.pbkdf2_sha256', _req)
    return bytes.fromhex(hex_value)


async def rsa_oaep(jwk: str, data: str) -> bytes:
    """
    RSA-OAEP with SHA-1 (the common default used by 1Password keysets).
    The private key is a JSON Web Key object as a string (`kty=RSA` with
    `n`, `e`, `d`, `p`, `q` as base64url). Ciphertext is hex.

    Args:
        jwk: RSA private JWK as a JSON string.
        data: ciphertext as hex.

    Returns:
        Plaintext bytes.
    """
    _req: dict[str, Any] = {}
    _req['jwk'] = jwk
    _req['data'] = data
    hex_value = await dispatch('crypto.rsa_oaep', _req)
    return bytes.fromhex(hex_value)
