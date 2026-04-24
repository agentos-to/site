"""Python SDK Client codegen — registry → _engine_client.py.

Reads the registry from a running engine (via `agentos call --json
schema`) and emits `sdk-skills/agentos/_engine_client.py` with `Client`
+ `AsyncClient` classes. Each namespace becomes a `_<name>Namespace`
proxy; each op becomes a method on that proxy.

Usage pattern after codegen:

    from agentos import Client, AsyncClient

    client = Client()
    result = client.data.read(id="abc")
    result = client.system.status()

    async with AsyncClient() as c:
        result = await c.data.read(id="abc")

Both clients speak the same JSON-RPC dialect as `agentos call` — Unix
socket at `~/.agentos/engine.sock`, dotted op names (`data.read`).
Results default to parsed JSON. Errors raise `EngineError`.

Per D11 the registry in `crates/core/src/tools.rs` is the single
source of truth; this module is one consumer.
"""

from __future__ import annotations

import json
from pathlib import Path


def emit_sdk_client(namespaces: list[dict]) -> str:
    """Emit the generated _engine_client.py source as a string."""
    # Filter: skip empty namespaces (shapes, credentials, tools) — they
    # have nothing to call yet and emitting empty proxies is noise.
    ns_with_ops = [ns for ns in namespaces if ns.get("ops")]

    lines = _emit_preamble(ns_with_ops)
    lines += _emit_error_class()
    lines += _emit_transport()
    lines += _emit_namespace_classes(ns_with_ops)
    lines += _emit_client(ns_with_ops, async_=False)
    lines += _emit_client(ns_with_ops, async_=True)
    return "\n".join(lines) + "\n"


def _emit_preamble(namespaces: list[dict]) -> list[str]:
    op_count = sum(len(ns["ops"]) for ns in namespaces)
    return [
        '"""Auto-generated engine dispatch client — do not edit.',
        "",
        f"Generated from {len(namespaces)} namespaces, {op_count} ops.",
        "Regenerate with: python3 docs/generate.py --docs",
        "",
        "Source of truth: crates/core/src/tools.rs REGISTRY (D11).",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "import json",
        "import os",
        "import socket",
        "import asyncio",
        "from pathlib import Path",
        "from typing import Any",
        "",
        "",
    ]


def _emit_error_class() -> list[str]:
    return [
        "class EngineError(RuntimeError):",
        '    """Raised when the engine returns an error for a tool call."""',
        "    pass",
        "",
        "",
        "def _default_socket_path() -> Path:",
        '    """~/.agentos/engine.sock unless overridden by $AGENTOS_ENGINE_SOCK."""',
        '    override = os.environ.get("AGENTOS_ENGINE_SOCK")',
        "    if override:",
        "        return Path(override)",
        '    return Path.home() / ".agentos" / "engine.sock"',
        "",
        "",
    ]


def _emit_transport() -> list[str]:
    """JSON-RPC transport over a Unix socket. One class for sync, another
    for async. Both do initialize → notifications/initialized → tools/call
    → read reply. No persistent connection — each call opens + closes.

    Keeping it one-shot avoids connection-lifecycle issues for scripts.
    If perf becomes a concern we can add keep-alive variants, but for
    interactive use the socket overhead is negligible.
    """
    return [
        "def _build_call_request(op: str, params: dict) -> tuple[str, str]:",
        '    """Return (initialize_json, call_json) newline-terminated."""',
        '    # Ask the engine for raw JSON so we can parse without stripping',
        '    # markdown fences. Also inject view.format=json for ops that',
        '    # otherwise return pre-rendered markdown (data.read, data.search).',
        '    args = dict(params)',
        '    args["__raw_json__"] = True',
        '    view = dict(args.get("view", {}))',
        '    view.setdefault("format", "json")',
        '    args["view"] = view',
        "",
        "    init = {",
        '        "jsonrpc": "2.0",',
        '        "id": 1,',
        '        "method": "initialize",',
        '        "params": {',
        '            "protocolVersion": "2024-11-05",',
        '            "capabilities": {},',
        '            "clientInfo": {"name": "agentos-python-client", "version": "0.1"},',
        "        },",
        "    }",
        "    initialized = {",
        '        "jsonrpc": "2.0",',
        '        "method": "notifications/initialized",',
        '        "params": {},',
        "    }",
        "    call = {",
        '        "jsonrpc": "2.0",',
        '        "id": 2,',
        '        "method": "tools/call",',
        '        "params": {"name": op, "arguments": args},',
        "    }",
        '    return (',
        '        json.dumps(init) + "\\n" + json.dumps(initialized) + "\\n",',
        '        json.dumps(call) + "\\n",',
        "    )",
        "",
        "",
        "def _parse_tool_result(line: str) -> Any:",
        '    """Extract the tool result from a tools/call JSON-RPC response."""',
        "    msg = json.loads(line)",
        '    if "error" in msg and msg["error"]:',
        '        raise EngineError(msg["error"].get("message", str(msg["error"])))',
        '    content = msg.get("result", {}).get("content", [])',
        "    if not content:",
        "        return None",
        '    text = content[0].get("text", "")',
        "    # With __raw_json__: True, the engine serialised the value as",
        "    # pretty JSON. Parse back to a Python value.",
        "    try:",
        "        return json.loads(text)",
        "    except json.JSONDecodeError:",
        "        # Fallback: the engine returned markdown or plain text (a",
        "        # tool that ignores __raw_json__). Return verbatim.",
        "        return text",
        "",
        "",
        "def _sync_call(sock_path: Path, op: str, params: dict) -> Any:",
        '    """Send one tools/call over a Unix socket; block until reply."""',
        "    init_block, call_line = _build_call_request(op, params)",
        "    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s:",
        "        s.connect(str(sock_path))",
        '        s.sendall(init_block.encode("utf-8"))',
        "        # Read lines until initialize reply (id=1) is seen.",
        '        buf = b""',
        "        while True:",
        "            chunk = s.recv(4096)",
        "            if not chunk:",
        '                raise EngineError("engine closed connection during initialize")',
        "            buf += chunk",
        '            if b"\\n" in buf:',
        "                line, _, rest = buf.partition(b\"\\n\")",
        "                buf = rest",
        '                msg = json.loads(line.decode("utf-8"))',
        "                if msg.get(\"id\") == 1:",
        "                    break",
        '        s.sendall(call_line.encode("utf-8"))',
        "        # Read lines until tools/call reply (id=2) arrives.",
        "        while True:",
        '            if b"\\n" in buf:',
        '                line, _, rest = buf.partition(b"\\n")',
        "                buf = rest",
        '                if not line.strip():',
        "                    continue",
        '                msg = json.loads(line.decode("utf-8"))',
        '                if msg.get("id") == 2:',
        "                    return _parse_tool_result(line.decode(\"utf-8\"))",
        "                continue",
        "            chunk = s.recv(65536)",
        "            if not chunk:",
        '                raise EngineError("engine closed connection during tools/call")',
        "            buf += chunk",
        "",
        "",
        "async def _async_call(sock_path: Path, op: str, params: dict) -> Any:",
        '    """Async variant of _sync_call using asyncio streams."""',
        "    init_block, call_line = _build_call_request(op, params)",
        "    reader, writer = await asyncio.open_unix_connection(str(sock_path))",
        "    try:",
        '        writer.write(init_block.encode("utf-8"))',
        "        await writer.drain()",
        "        # Wait for initialize reply (id=1).",
        "        while True:",
        "            line = await reader.readline()",
        "            if not line:",
        '                raise EngineError("engine closed connection during initialize")',
        '            msg = json.loads(line.decode("utf-8"))',
        "            if msg.get(\"id\") == 1:",
        "                break",
        '        writer.write(call_line.encode("utf-8"))',
        "        await writer.drain()",
        "        # Wait for tools/call reply (id=2).",
        "        while True:",
        "            line = await reader.readline()",
        "            if not line:",
        '                raise EngineError("engine closed connection during tools/call")',
        "            if not line.strip():",
        "                continue",
        '            msg = json.loads(line.decode("utf-8"))',
        '            if msg.get("id") == 2:',
        "                return _parse_tool_result(line.decode(\"utf-8\"))",
        "    finally:",
        "        writer.close()",
        "        try:",
        "            await writer.wait_closed()",
        "        except Exception:",
        "            pass",
        "",
        "",
    ]


def _emit_namespace_classes(namespaces: list[dict]) -> list[str]:
    """One proxy class per namespace, one method per op. Sync and async
    share the class shape — the `_call` override on the client instance
    differentiates at the transport layer."""
    lines = []
    for ns in namespaces:
        ns_name = ns["name"]
        class_name = f"_{_pascal(ns_name)}Namespace"
        lines.append(f"class {class_name}:")
        lines.append(f'    """Proxy for the `{ns_name}` namespace."""')
        lines.append("")
        lines.append("    def __init__(self, call):")
        lines.append("        self._call = call")
        lines.append("")
        for op in ns["ops"]:
            op_name = op["name"]
            op_desc = op.get("description", "").strip()
            examples = op.get("examples") or []
            dotted = f"{ns_name}.{op_name}"
            # Method body: forward **kwargs as params dict through transport.
            lines.append(f"    def {_py_method_name(op_name)}(self, **params: Any) -> Any:")
            if op_desc:
                lines.append(f'        """{op_desc}')
                if examples:
                    lines.append("")
                    lines.append("        Examples:")
                    for ex in examples:
                        lines.append(f"            {ex}")
                lines.append('        """')
            lines.append(f'        return self._call("{dotted}", params)')
            lines.append("")
        lines.append("")
    return lines


def _emit_client(namespaces: list[dict], *, async_: bool) -> list[str]:
    """Client / AsyncClient class. Each namespace is a member;
    `__init__` wires a transport closure into each proxy."""
    cls = "AsyncClient" if async_ else "Client"
    call_fn = "_async_call" if async_ else "_sync_call"
    doc_extra = "" if not async_ else " (async)"

    lines = [
        f"class {cls}:",
        f'    """Engine dispatch client{doc_extra}.',
        "",
        "    Connects to the engine's MCP socket (~/.agentos/engine.sock",
        "    unless $AGENTOS_ENGINE_SOCK overrides) and dispatches tool",
        "    calls through `tools/call`. Namespaces are attributes:",
        "",
        "        client.data.read(id=\"abc\")",
        "        client.system.status()",
        "        client.skills.run(skill=\"exa\", tool=\"search\", params={...})",
        '    """',
        "",
        '    def __init__(self, socket_path: Path | str | None = None):',
        "        self._socket_path = (",
        "            Path(socket_path) if socket_path else _default_socket_path()",
        "        )",
    ]

    # Wire each namespace.
    for ns in namespaces:
        ns_name = ns["name"]
        class_name = f"_{_pascal(ns_name)}Namespace"
        attr = _py_attr_name(ns_name)
        lines.append(
            f"        self.{attr} = {class_name}(lambda op, params: {_bound_call(call_fn, async_)})"
        )

    lines.append("")

    if async_:
        # AsyncClient supports `async with` for parity with AsyncClient in
        # Anthropic / OpenAI SDKs. No actual cleanup needed (each call is
        # one-shot) but the pattern is idiomatic.
        lines += [
            "    async def __aenter__(self):",
            "        return self",
            "",
            "    async def __aexit__(self, exc_type, exc, tb):",
            "        return None",
            "",
        ]

    lines.append("")
    return lines


def _bound_call(call_fn: str, async_: bool) -> str:
    """Return the expression that invokes the transport with this
    client's socket path. Captures `self._socket_path` as a closure."""
    if async_:
        return f"{call_fn}(self._socket_path, op, params)"
    return f"{call_fn}(self._socket_path, op, params)"


def _pascal(name: str) -> str:
    return "".join(part.capitalize() for part in name.replace("-", "_").split("_"))


def _py_method_name(op_name: str) -> str:
    # Op names in the registry are already snake_ish; keep hyphens → underscores.
    safe = op_name.replace("-", "_")
    if safe in _PY_RESERVED:
        safe = f"{safe}_"
    return safe


def _py_attr_name(ns_name: str) -> str:
    safe = ns_name.replace("-", "_")
    if safe in _PY_RESERVED:
        safe = f"{safe}_"
    return safe


_PY_RESERVED = {
    "from", "import", "class", "return", "def", "if", "else", "for",
    "while", "with", "as", "try", "except", "finally", "raise", "pass",
    "break", "continue", "and", "or", "not", "in", "is", "lambda",
    "global", "nonlocal", "yield", "assert", "del", "True", "False",
    "None", "async", "await",
}
