# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `./dev.sh build` or `python3 codegen/gen_sdk_stubs.py`.

"""Job-progress updates — fire-and-forget.

`progress.report` publishes on the job event bus and does not return a payload."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def report(job_id: str, *, current: int | None = None, message: str | None = None, total: int | None = None) -> None:
    """
    Publish a progress update on the job event bus. Fire-and-forget —
    no wire ack.

    Args:
        job_id: stable job identifier.
        current, total: step counters.
        message: human-readable status line.

    Returns:
        None.
    """
    _req: dict[str, Any] = {}
    _req['job_id'] = job_id
    if current is not None:
        _req['current'] = current
    if message is not None:
        _req['message'] = message
    if total is not None:
        _req['total'] = total
    await dispatch('progress.report', _req)
    return None
