# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `python3 platform/codegen/generate.py`.

"""blobs.* ops — the content-addressed blob store at ~/.agentos/blobs.

Engine-owned bytes on disk; graph nodes reference blobs by the returned
path (a file-shaped node's `path` field). Apps hand the engine base64
and the engine owns placement, hashing, and dedup — no app ever
invents a path into the user's state dir. Handlers live in
agentos-exec-executors."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def get(path: str) -> dict[str, Any]:
    """
    Read bytes back from the engine's content-addressed blob store —
    the read half of `blobs.put`, behind the same policy gate. The
    path must resolve inside `~/.agentos/blobs`; the engine refuses
    anything else, so an app can only ever read bytes the store
    already owns — never an arbitrary file.

    Args:
        path: absolute blob-store path (from `blobs.put`, or the
            `path` field of a hydrated attachment).

    Returns:
        data (base64), sha256, size of the blob.
    """
    _req: dict[str, Any] = {}
    _req['path'] = path
    return await dispatch('blobs.get', _req)


async def put(data: str, *, ext: str | None = None) -> dict[str, Any]:
    """
    Store bytes in the engine's content-addressed blob store:
    `~/.agentos/blobs/<sha256[0:2]>/<sha256>.<ext>`. Identical bytes land
    on the same path, so re-storing is a free no-op — dedup by
    construction. The returned absolute path is what a file-shaped graph
    node carries in its `path` field.

    Args:
        data: base64-encoded bytes.
        ext: filename extension (no dot); names the stored file.

    Returns:
        path, sha256, size of the stored blob.
    """
    _req: dict[str, Any] = {}
    _req['data'] = data
    if ext is not None:
        _req['ext'] = ext
    return await dispatch('blobs.put', _req)
