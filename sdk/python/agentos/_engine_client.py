"""Auto-generated engine dispatch client — do not edit.

Generated from 5 namespaces, 12 ops.
Regenerate with: python3 docs/generate.py --docs

Source of truth: crates/core/src/tools.rs REGISTRY (D11).
"""

from __future__ import annotations

import json
import os
import socket
import asyncio
from pathlib import Path
from typing import Any


class EngineError(RuntimeError):
    """Raised when the engine returns an error for a tool call."""
    pass


def _default_socket_path() -> Path:
    """~/.agentos/engine.sock unless overridden by $AGENTOS_ENGINE_SOCK."""
    override = os.environ.get("AGENTOS_ENGINE_SOCK")
    if override:
        return Path(override)
    return Path.home() / ".agentos" / "engine.sock"


def _build_call_request(op: str, params: dict) -> tuple[str, str]:
    """Return (initialize_json, call_json) newline-terminated."""
    # Ask the engine for raw JSON so we can parse without stripping
    # markdown fences. Also inject view.format=json for ops that
    # otherwise return pre-rendered markdown (data.read, data.search).
    args = dict(params)
    args["__raw_json__"] = True
    view = dict(args.get("view", {}))
    view.setdefault("format", "json")
    args["view"] = view

    init = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {"name": "agentos-python-client", "version": "0.1"},
        },
    }
    initialized = {
        "jsonrpc": "2.0",
        "method": "notifications/initialized",
        "params": {},
    }
    call = {
        "jsonrpc": "2.0",
        "id": 2,
        "method": "tools/call",
        "params": {"name": op, "arguments": args},
    }
    return (
        json.dumps(init) + "\n" + json.dumps(initialized) + "\n",
        json.dumps(call) + "\n",
    )


def _parse_tool_result(line: str) -> Any:
    """Extract the tool result from a tools/call JSON-RPC response."""
    msg = json.loads(line)
    if "error" in msg and msg["error"]:
        raise EngineError(msg["error"].get("message", str(msg["error"])))
    content = msg.get("result", {}).get("content", [])
    if not content:
        return None
    text = content[0].get("text", "")
    # With __raw_json__: True, the engine serialised the value as
    # pretty JSON. Parse back to a Python value.
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        # Fallback: the engine returned markdown or plain text (a
        # tool that ignores __raw_json__). Return verbatim.
        return text


def _sync_call(sock_path: Path, op: str, params: dict) -> Any:
    """Send one tools/call over a Unix socket; block until reply."""
    init_block, call_line = _build_call_request(op, params)
    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:
        s.connect(str(sock_path))
        s.sendall(init_block.encode("utf-8"))
        # Read lines until initialize reply (id=1) is seen.
        buf = b""
        while True:
            chunk = s.recv(4096)
            if not chunk:
                raise EngineError("engine closed connection during initialize")
            buf += chunk
            if b"\n" in buf:
                line, _, rest = buf.partition(b"\n")
                buf = rest
                msg = json.loads(line.decode("utf-8"))
                if msg.get("id") == 1:
                    break
        s.sendall(call_line.encode("utf-8"))
        # Read lines until tools/call reply (id=2) arrives.
        while True:
            if b"\n" in buf:
                line, _, rest = buf.partition(b"\n")
                buf = rest
                if not line.strip():
                    continue
                msg = json.loads(line.decode("utf-8"))
                if msg.get("id") == 2:
                    return _parse_tool_result(line.decode("utf-8"))
                continue
            chunk = s.recv(65536)
            if not chunk:
                raise EngineError("engine closed connection during tools/call")
            buf += chunk


async def _async_call(sock_path: Path, op: str, params: dict) -> Any:
    """Async variant of _sync_call using asyncio streams."""
    init_block, call_line = _build_call_request(op, params)
    reader, writer = await asyncio.open_unix_connection(str(sock_path))
    try:
        writer.write(init_block.encode("utf-8"))
        await writer.drain()
        # Wait for initialize reply (id=1).
        while True:
            line = await reader.readline()
            if not line:
                raise EngineError("engine closed connection during initialize")
            msg = json.loads(line.decode("utf-8"))
            if msg.get("id") == 1:
                break
        writer.write(call_line.encode("utf-8"))
        await writer.drain()
        # Wait for tools/call reply (id=2).
        while True:
            line = await reader.readline()
            if not line:
                raise EngineError("engine closed connection during tools/call")
            if not line.strip():
                continue
            msg = json.loads(line.decode("utf-8"))
            if msg.get("id") == 2:
                return _parse_tool_result(line.decode("utf-8"))
    finally:
        writer.close()
        try:
            await writer.wait_closed()
        except Exception:
            pass


class _DataNamespace:
    """Proxy for the `data` namespace."""

    def __init__(self, call):
        self._call = call

    def read(self, **params: Any) -> Any:
        """Read graph data by id, name, tags, shape, or system metadata.

        Examples:
            read({ id: "abc123" })
            read({ shape: "task", priority: 1 })
            read({ about: "shapes" })
        """
        return self._call("data.read", params)

    def search(self, **params: Any) -> Any:
        """Full-text search over local graph entities.

        Examples:
            search({ query: "project status" })
            search({ query: "pending tasks", shape: "task" })
        """
        return self._call("data.search", params)

    def delete(self, **params: Any) -> Any:
        """Soft-delete a node or relationship.

        Examples:
            delete({ id: "abc123" })
        """
        return self._call("data.delete", params)


class _SkillsNamespace:
    """Proxy for the `skills` namespace."""

    def __init__(self, call):
        self._call = call

    def run(self, **params: Any) -> Any:
        """Execute a skill tool directly.

        Examples:
            run({ skill: "exa", tool: "search", params: { query: "..." } })
        """
        return self._call("skills.run", params)

    def load(self, **params: Any) -> Any:
        """Load a skill manual (readme + tool list) before calling run.

        Examples:
            load({ skill: "exa" })
        """
        return self._call("skills.load", params)


class _AccountsNamespace:
    """Proxy for the `accounts` namespace."""

    def __init__(self, call):
        self._call = call

    def list(self, **params: Any) -> Any:
        """List accounts, auth health, and providers.

        Examples:
            accounts()
            accounts({ skill: "exa" })
        """
        return self._call("accounts.list", params)


class _SystemNamespace:
    """Proxy for the `system` namespace."""

    def __init__(self, call):
        self._call = call

    def boot(self, **params: Any) -> Any:
        """Session bootstrap: identity, project, recent activity, tools.

        Examples:
            boot()
        """
        return self._call("system.boot", params)

    def status(self, **params: Any) -> Any:
        """Engine snapshot: version, uptime, PID, DB path, recent op stats.

        Examples:
            status()
            status({ recent: 50 })
        """
        return self._call("system.status", params)

    def schema(self, **params: Any) -> Any:
        """Emit the full tool surface registry as JSON — single source of truth for SDK codegen and docs generation (see D11).

        Examples:
            system.schema()
        """
        return self._call("system.schema", params)


class _JobsNamespace:
    """Proxy for the `jobs` namespace."""

    def __init__(self, call):
        self._call = call

    def watch(self, **params: Any) -> Any:
        """Start a live skill event stream. The watcher runs indefinitely.

        Examples:
            jobs.watch({ skill: "whatsapp", stream: "messages" })
        """
        return self._call("jobs.watch", params)

    def cancel(self, **params: Any) -> Any:
        """Stop a running watcher or cancel an async job.

        Examples:
            jobs.cancel({ id: "whatsapp:messages" })
        """
        return self._call("jobs.cancel", params)

    def list(self, **params: Any) -> Any:
        """List running watchers and their status.

        Examples:
            jobs.list()
        """
        return self._call("jobs.list", params)


class Client:
    """Engine dispatch client.

    Connects to the engine's MCP socket (~/.agentos/engine.sock
    unless $AGENTOS_ENGINE_SOCK overrides) and dispatches tool
    calls through `tools/call`. Namespaces are attributes:

        client.data.read(id="abc")
        client.system.status()
        client.skills.run(skill="exa", tool="search", params={...})
    """

    def __init__(self, socket_path: Path | str | None = None):
        self._socket_path = (
            Path(socket_path) if socket_path else _default_socket_path()
        )
        self.data = _DataNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.skills = _SkillsNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.accounts = _AccountsNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.system = _SystemNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.jobs = _JobsNamespace(lambda op, params: _sync_call(self._socket_path, op, params))


class AsyncClient:
    """Engine dispatch client (async).

    Connects to the engine's MCP socket (~/.agentos/engine.sock
    unless $AGENTOS_ENGINE_SOCK overrides) and dispatches tool
    calls through `tools/call`. Namespaces are attributes:

        client.data.read(id="abc")
        client.system.status()
        client.skills.run(skill="exa", tool="search", params={...})
    """

    def __init__(self, socket_path: Path | str | None = None):
        self._socket_path = (
            Path(socket_path) if socket_path else _default_socket_path()
        )
        self.data = _DataNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.skills = _SkillsNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.accounts = _AccountsNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.system = _SystemNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.jobs = _JobsNamespace(lambda op, params: _async_call(self._socket_path, op, params))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return None


