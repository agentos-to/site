"""Auto-generated engine dispatch client — do not edit.

Generated from 4 namespaces, 18 ops.
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
        """Read one node (or link) by id. On a volume read, add `expand`/`depth` to get a hydrated nested subtree (the whole tree in one call) following containment edges — see the `expand` param.

        Args:
            id (string, required): Node or link id.
            depth (int, optional): SUBTREE PROJECTION (volume reads): hops to follow `expand` edges. Default 4. Supplying `expand` or `depth` switches read into subtree mode.
            expand (list[string], optional): SUBTREE PROJECTION (volume reads): containment edge labels to follow from this node, e.g. ["contains","owns","has_step"]. Returns a hydrated, NESTED tree (each child under `children`, with `_via` = the label) instead of a flat node — the whole subtree in ONE call. Reference edges (depends_on, upholds, serves, …) are never expanded. If omitted but `depth` is set, defaults to the containment spine (contains/owns/has_step/has_part).
            fields (list[string], optional): SUBTREE PROJECTION: project each node's vals to this subset (id/name/shape always kept).
            view (dict, optional)
            volume (string, optional): Which Volume to read from. Defaults to "home". A mounted memex's volume_id targets that memex's pool.

        Examples:
            read({ id: "abc123" })
            read({ id: "roadmap", volume: "agentos-roadmap", depth: 4 })
        """
        return self._call("data.read", params)

    def list(self, **params: Any) -> Any:
        """List nodes by shape, user_tag, name match, FTS via `q`, system metadata, or skill membership.

        Args:
            about (string, optional): Engine introspection (e.g. "shapes").
            limit (int, optional): Max rows. Defaults vary per filter.
            name (string, optional): Substring match against node names.
            q (string, optional): FTS query — folds the previous `data.search` op.
            query (string, optional): Legacy alias for q. Prefer q.
            shape (string | list[string], optional): Shape name (e.g. "task") or array of shape names (union).
            skill (string, optional): List entities (or skill manifest with type="entity") for this skill.
            type (string, optional): Modifier for `skill`: list entities (vs. the skill manifest).
            user_tag (string | list[string], optional): User-tag name (or array — intersection).
            view (dict, optional)
            volume (string, optional): Which Volume to list from. Defaults to "home". Mutually exclusive with `volumes`.
            volumes (string | list[string], optional): Federation: union across multiple Volumes. Array of ids, or the string "all" for every mounted Volume.

        Examples:
            list({ shape: "task", priority: 1 })
            list({ user_tag: "follow-up" })
            list({ q: "meeting", limit: 10 })
            list({ about: "shapes" })
        """
        return self._call("data.list", params)

    def update(self, **params: Any) -> Any:
        """Set or delete vals on an existing node. `null` value deletes a val; non-null sets it. Unit auto-inferred from JSON type when not given.

        Args:
            vals (dict, required): Map of val key → value. `null` deletes (nodes only). Non-null sets. Object form `{value, unit}` overrides the inferred unit.
            id (string, optional): Node id to update.
            link (string, optional): Link id to update (writes link_vals — icon position, fares, etc.).
            volume (string, optional): Which Volume to write to. Defaults to "home". Errors on read-only mounts.

        Examples:
            update({ id: "abc123", vals: { "pref:ui": { themeId: "xp", fontSize: 14 } } })
            update({ id: "abc123", vals: { name: "Renamed" } })
            update({ id: "abc123", vals: { "pref:legacy": null } })
        """
        return self._call("data.update", params)

    def create(self, **params: Any) -> Any:
        """Create a node (`{shape, name?, vals?, identity?}`), or a relationship (`{from, label, to}`). With `identity`, an existing node is updated instead of duplicated (upsert semantics).

        Args:
            from (string, optional): Link form: source node id.
            identity (dict, optional): Node form: scalar (key, value) pairs. With `identity`, an existing match is updated instead of duplicated (upsert semantics).
            label (string, optional): Link form: relationship label.
            name (string, optional): Node form: display name for the node.
            shape (string, optional): Node form: shape name. Lazily registered on first use.
            to (string, optional): Link form: target node id. Accepts the qualified `"<volume_id>:<node_id>"` form to bridge into a mounted memex.
            vals (dict, optional): Node form: initial vals. Same shape as data.update vals.
            volume (string, optional): Which Volume to write the new node/link in. Defaults to "home". Errors on read-only mounts.

        Examples:
            create({ shape: "person", name: "Joe", identity: { email: "joe@example.com" } })
            create({ from: "abc123", label: "measures", to: "def456" })
            // bookmark: a named handle → any node, one atomic call
            create({ shape: "bookmark", vals: { handle: "home" }, links_out: [{ label: "points_to", target_id: "<node-id>" }] })
        """
        return self._call("data.create", params)

    def delete(self, **params: Any) -> Any:
        """Soft-delete a node or relationship. With `permanent: true`, hard-delete a soft-deleted node (purge).

        Args:
            id (string, required): Node or link id. Soft-delete.
            permanent (bool, optional): When true, hard-delete a soft-deleted node (purge from disk). Used by 'empty trash'.
            volume (string, optional): Which Volume to delete from. Defaults to "home". Errors on read-only mounts.

        Examples:
            delete({ id: "abc123" })
            delete({ id: "abc123", permanent: true })
        """
        return self._call("data.delete", params)

    def restore(self, **params: Any) -> Any:
        """Restore a soft-deleted node. Flips deleted_at back to null on the node and on the original cascade batch of links. Emits an activity record.

        Args:
            id (string, required): Soft-deleted node id. Flips deleted_at back to null on the node and on every link in the original cascade batch.

        Examples:
            restore({ id: "abc123" })
        """
        return self._call("data.restore", params)

    def export(self, **params: Any) -> Any:
        """Export a typed subgraph to a SQLite artifact. Writes _meta.schema_version pin for safe re-import.

        Args:
            description (string, required): One-paragraph human description of what this memex contains. Persisted to _meta.description.
            icon (string, required): Icon-shape `purpose` name (e.g. "book", "heart", "home"). Persisted to _meta.icon. Theme adapters resolve names to renderable assets.
            name (string, required): Display name for the memex — "Joe Health", "Bible", "US IP Law (2026)". Persisted to _meta.name.
            out_path (string, required): Destination path (~ expanded). Existing file is overwritten.
            selection (dict, required): One of {all: true} (full-DB backup — bypasses closure, includes orphans + trash by default), {shapes: [..]} (type-driven closure), or {nodes: [..]} (explicit seeds + closure).
            closure (dict, optional): Optional closure filters. V1 walks every link by default.

        Examples:
            export({ selection: { shapes: ["health-*"] }, out_path: "~/health.db", label: "Health profile" })
            export({ selection: { shapes: ["transaction", "account"] }, out_path: "~/finance.db", label: "Finance 2026" })
            export({ selection: { nodes: ["abc123"] }, out_path: "~/seed.db", closure: { max_depth: 2 } })
            export({ selection: { all: true }, out_path: "~/full.db" })
        """
        return self._call("data.export", params)

    def import_(self, **params: Any) -> Any:
        """Import a previously-exported artifact, replaying any migration chain from its pin to live SCHEMA_HASH.

        Args:
            in_path (string, required): Artifact path (~ expanded). SQLite for v1.
            on_id_collision (string, optional): Default merge: overwrite vals + ensure links/shapes/content on existing id.
            on_schema_drift (string, optional): Default migrate: replay chain from artifact pin to live.
            plan_only (bool, optional): Compute the diff + per-row category, do not write.

        Examples:
            import({ in_path: "~/health.db" })
            import({ in_path: "~/health.db", plan_only: true })
        """
        return self._call("data.import", params)

    def mount(self, **params: Any) -> Any:
        """Mount a memex `.db` file as a read-only Volume. Persists a volume node + emits a create activity. Survives engine restart.

        Args:
            path (string, required): Path to a memex `.db` file (~ expanded). Must carry _meta.type='memex'.

        Examples:
            mount({ path: "~/bible.db" })
            mount({ path: "/Users/joe/dev/agentos/_joe/health.db" })
        """
        return self._call("data.mount", params)

    def unmount(self, **params: Any) -> Any:
        """Detach a mounted Volume by volume_id (the slug). Soft-deletes the volume node + emits a delete activity. File on disk is untouched.

        Args:
            id (string, required): Volume id (the slug returned by data.mount), NOT the graph node id.

        Examples:
            unmount({ id: "joe-health" })
        """
        return self._call("data.unmount", params)

    def volume_stats(self, **params: Any) -> Any:
        """Disk + content statistics for a Volume: file size on disk, node count, shape histogram, schema version. Powers Properties' General tab (used space, node count) and the shape donut. Defaults to the home Volume when `id` is omitted.

        Args:
            id (string, optional): Volume id slug. Accepts "home" / "memex" for the home vault. Defaults to "home" when omitted.

        Examples:
            volume_stats({})                       // home
            volume_stats({ id: "joe-health" })     // a mounted pod
        """
        return self._call("data.volume_stats", params)


class _SkillsNamespace:
    """Proxy for the `skills` namespace."""

    def __init__(self, call):
        self._call = call

    def run(self, **params: Any) -> Any:
        """Execute a skill tool directly.

        Args:
            skill (string, required): Skill id (e.g. "exa").
            tool (string, required): Tool name within the skill (e.g. "search").
            account (string, optional): Force a specific credential/account when the skill has multiple.
            execute (Any, optional): Live-execution override; consult the skill manifest for accepted shapes.
            params (dict, optional): Op-level params forwarded to the skill.
            provider (string, optional): Force a cookie provider (e.g. "brave-browser").
            remember (bool, optional): Persist the live result to the graph. Default true.
            view (dict, optional)

        Examples:
            run({ skill: "exa", tool: "search", params: { query: "..." } })
        """
        return self._call("skills.run", params)

    def load(self, **params: Any) -> Any:
        """Load a skill manual (readme + tool list) before calling run.

        Args:
            skill (string, required): Skill id to load (readme + tool list).

        Examples:
            load({ skill: "exa" })
        """
        return self._call("skills.load", params)


class _SystemNamespace:
    """Proxy for the `system` namespace."""

    def __init__(self, call):
        self._call = call

    def status(self, **params: Any) -> Any:
        """Engine snapshot: version, uptime, PID, DB path, recent op stats.

        Args:
            recent (int, optional): Number of recent op events to include. Default 20, capped at the ring capacity.

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

    def schema_hash(self, **params: Any) -> Any:
        """Deterministic content hash of the AgentOS ontology — pinned in every data-porter export to detect schema drift on import.

        Examples:
            system.schema_hash()
        """
        return self._call("system.schema_hash", params)

    def schema_diff(self, **params: Any) -> Any:
        """Walk the migration chain from a given pin to the current SCHEMA_HASH. Returns the ordered list of migration ids that data.import would replay, or a no_chain result with the stuck hash when no migration exists from the current cursor.

        Args:
            pin (string, required): An ontology hash to diff against current — `sha256:<hex>` (typically from an export's `_meta.schema_version`).

        Examples:
            system.schema_diff({ pin: "sha256:abc..." })
        """
        return self._call("system.schema_diff", params)


class _ReadmeNamespace:
    """Proxy for the `readme` namespace."""

    def __init__(self, call):
        self._call = call

    def get(self, **params: Any) -> Any:
        """Identity, tools, and the roadmap for your working directory.

        Args:
            cwd (string, optional): Working directory to orient against. Optional — defaults to the session's directory (MCP clients supply it via roots; the CLI passes $PWD).

        Examples:
            readme()
            readme({ cwd: "/path/to/project" })
        """
        return self._call("readme.get", params)


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
        self.system = _SystemNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.readme = _ReadmeNamespace(lambda op, params: _sync_call(self._socket_path, op, params))


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
        self.system = _SystemNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.readme = _ReadmeNamespace(lambda op, params: _async_call(self._socket_path, op, params))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return None


