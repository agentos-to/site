# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `python3 platform/codegen/generate.py`.

"""shell.* ops — controlled binary execution.

Shell interpreters (sh, bash, zsh, fish, …) are blocked at the handler;
only direct binaries run. Handlers live in agentos-exec-executors."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def run(binary: str, *, args: list[str] | None = None, cwd: str | None = None, input: str | None = None, stream: bool | None = None, timeout: float | None = None) -> dict[str, Any]:
    """
    Execute a binary with controlled argv. The invocation is NOT shell-parsed,
    and shell interpreters (sh, bash, zsh, fish, etc.) are rejected to prevent
    command-injection shortcuts.

    For a streaming command that never self-terminates (`dns-sd`, `log stream`,
    `tcpdump`), pass `stream: true` with a `timeout`: the child is killed at the
    deadline and whatever it printed so far is returned as a normal result with
    `timed_out: true` — instead of the default mode, where a timeout raises and
    the partial output is lost.

    Args:
        binary, args, timeout, cwd, input, stream.

    Returns:
        {exit_code, stdout, stderr, timed_out}.
    """
    _req: dict[str, Any] = {}
    _req['binary'] = binary
    if args is not None:
        _req['args'] = args
    if cwd is not None:
        _req['cwd'] = cwd
    if input is not None:
        _req['input'] = input
    if stream is not None:
        _req['stream'] = stream
    if timeout is not None:
        _req['timeout'] = timeout
    return await dispatch('shell.run', _req)
