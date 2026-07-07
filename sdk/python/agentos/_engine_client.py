"""Auto-generated engine dispatch client — do not edit.

Generated from 9 namespaces, 48 ops.
Regenerate with: python3 codegen/generate.py

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
            read({ id: "roadmap", volume: "agentos-product", depth: 4 })
        """
        return self._call("data.read", params)

    def list(self, **params: Any) -> Any:
        """List nodes by shape, user_tag, name match, FTS via `q`, system metadata, or app membership.

        Args:
            about (string, optional): Engine introspection (e.g. "shapes").
            app (string, optional): List entities (or app manifest with type="entity") for this app.
            limit (int, optional): Max rows. Defaults vary per filter.
            name (string, optional): Substring match against node names.
            q (string, optional): FTS query — folds the previous `data.search` op.
            query (string, optional): Legacy alias for q. Prefer q.
            shape (string | list[string], optional): Shape name (e.g. "task") or array of shape names (union).
            type (string, optional): Modifier for `app`: list entities (vs. the app manifest).
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

    def set_icon(self, **params: Any) -> Any:
        """Give a node its own picture as its icon. `image` is an http(s) URL, a data: URI, or an absolute file path; the engine stores the bytes locally and the node wears that image everywhere. `image: null` removes it. Works on any node — an app, a person, an organization. For a brand/app logo, don't hand-build a CDN URL (a bare logo.dev URL 401s without a key) — get the ready-to-use URL from the logo-dev app: `apps.run({app:"logo-dev", tool:"logo_url", params:{domain:"<site>"}})`, then pass it here.

        Args:
            id (string, required): The node to give an icon (e.g. an app id like "gmail").
            image (Any, optional): http(s) URL, data: URI, or absolute file path to the image. null clears the icon.
            volume (string, optional): Optional — the engine finds which volume the node lives in automatically (apps are in "system"). Only pass this to disambiguate.

        Examples:
            set_icon({ id: "abc123", image: "https://upload.wikimedia.org/.../logo.png" })  // any public image URL
            set_icon({ id: "abc123", image: "/Users/me/Pictures/face.png" })  // a local file
            set_icon({ id: "gmail", image: null })  // back to the generic icon
        """
        return self._call("data.set_icon", params)

    def create(self, **params: Any) -> Any:
        """Create a node (`{shape, name?, vals?, identity?}`), or a relationship (`{from, label, to}`). With `identity`, an existing node is updated instead of duplicated (upsert semantics).

        Args:
            from (string, optional): LINK form: source node id.
            identity (dict, optional): NODE form: scalar upsert key. `{key: value}` pairs matched against existing node vals — a match is UPDATED in place instead of duplicated. The val-based natural key (e.g. `{url: "https://…"}`).
            identity_links (dict, optional): NODE form: relation-based upsert key. `{label: target_id}` matched against the node's outgoing links (e.g. `{points_to: "<node-id>"}` for a bookmark). When both `identity` and `identity_links` are given, the match must satisfy ALL conditions on one node. Honored at every nesting level.
            inverse (string, optional): LINK form: the reverse-reading verb. REQUIRED the first time `label` is seen in a volume; optional after.
            label (string, optional): LINK form: relationship verb.
            links_out (list[object], optional): NODE form: outgoing relationships, each creating or referencing a target node and wiring an edge. This is how a write lands wired in one atomic call. Recurses: a `target` is itself a full node-create (shape, vals, identity, its own links_out).
            name (string, optional): NODE form: display name (shorthand for the shape's title val).
            shape (string | dict, optional): NODE form. The shape — a STRING name (must already be registered in this volume), or a full ShapeDef OBJECT (`{name, fields:[{name, ty}], …}`) which registers/extends the shape on write. First write of a custom shape, or ANY write into a mounted pod where the shape isn't registered by name, MUST ship the object form — fetch it with `data.shape({name})`. (`ty` values: string|text|url|integer|number|boolean|json|date|datetime|stringlist|integerlist.)
            to (string, optional): LINK form: target node id. Accepts the qualified `"<volume_id>:<node_id>"` form to bridge into a mounted memex.
            vals (dict, optional): Initial vals — `{key: value}` or `{key: {value, unit}}`. NODE form: vals on the node (scalar/JSON only; for relationships use `links_out`). LINK form: vals stored on the edge (an event's time/place).
            volume (string, optional): Which Volume to write into. Defaults to "home". Errors on read-only mounts. The node + its whole `links_out` subtree land atomically in this volume.

        Examples:
            create({ shape: "person", name: "Joe", identity: { email: "joe@example.com" } })
            create({ from: "abc123", label: "measures", to: "def456" })
            // bookmark: a named handle → any node, one atomic call
            create({ shape: "bookmark", vals: { handle: "home" }, links_out: [{ label: "points_to", target_id: "<node-id>" }] })
        """
        return self._call("data.create", params)

    def write(self, **params: Any) -> Any:
        """Atomic bulk ingest — land many nodes (each with its wired `links_out`) into one Volume in a single transaction. ALL land or NONE do, so a dropped call is safe to retry verbatim; each node is idempotent via its own identity. Use this over N separate `create` calls to import a set.

        Args:
            nodes (list[object], required): The batch — each item is a NODE-form `data.create` payload (`{shape, name?, vals?, identity?, identity_links?, links_out?}`), same grammar as create. Writes into a pod where the shape isn't registered by name must ship the `shape` OBJECT (fetch with `data.shape({name})`).
            volume (string, required): Which Volume the whole batch writes into (e.g. "health"). Required — there is no silent home-default for a bulk write. Errors on read-only mounts.

        Examples:
            write({ volume: "health", nodes: [{ shape: "health-biomarker", name: "LDL", vals: { value: 99 } }, { shape: "health-biomarker", name: "HDL", vals: { value: 62 } }] })
            // each node may carry its own links_out subtree — the whole set lands wired, atomically
        """
        return self._call("data.write", params)

    def shape(self, **params: Any) -> Any:
        """Fetch a shape's ShapeDef by name — the write-side twin of `read({about:"shapes"})`. Returns the schema in the exact form `data.create` takes as its `shape` object, so you can write into a pod where the shape isn't registered by name without reading source.

        Args:
            name (string, required): Shape name (e.g. "person", "health-biomarker").
            volume (string, optional): Which Volume's registry to read the def from. Defaults to "home".

        Examples:
            shape({ name: "person" })
            shape({ name: "health-biomarker", volume: "health" })
        """
        return self._call("data.shape", params)

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

    def empty_trash(self, **params: Any) -> Any:
        """Purge every soft-deleted node across home and mounted volumes — the bulk hard-delete behind 'Empty Trash'. Reports live progress (current/total) and is cancelable mid-run (already-purged nodes stay purged); runs engine-side so it survives a tab reload. Returns {purged, total, cancelled}.

        Examples:
            empty_trash()
        """
        return self._call("data.empty_trash", params)

    def restore(self, **params: Any) -> Any:
        """Restore a soft-deleted node. Flips deleted_at back to null on the node and on the original cascade batch of links. Emits an activity record.

        Args:
            id (string, required): Soft-deleted node id. Flips deleted_at back to null on the node and on every link in the original cascade batch.

        Examples:
            restore({ id: "abc123" })
        """
        return self._call("data.restore", params)

    def split(self, **params: Any) -> Any:
        """Reverse a prior engine merge: restore the surviving node to its pre-merge state and reborn the absorbed person with its original identity set. Use when two contacts the engine merged on an identity collision turn out to be different people (a shared family email, a recycled handle). The mirror of the automatic merge on create/upsert.

        Args:
            id (string, required): The merged (surviving) node. Reverses the most recent engine merge folded into it.
            volume (string, optional): Which Volume the node lives in. Defaults to "home".

        Examples:
            split({ id: "abc123" })   // undo the latest merge folded into this node
        """
        return self._call("data.split", params)

    def resolve(self, **params: Any) -> Any:
        """Resolve an address (node/link id, or handle) to its target's identity — node_id, volume, shapes, listType, name, via — without reading content. The kernel resolver's public face: identity before acting.

        Args:
            address (string, required): Any address — a node/link id, or a handle. Resolved by the same kernel resolver every data op uses: literal id wins, then handle → bookmark → points_to target.

        Examples:
            resolve({ address: "desktop" })
            resolve({ address: "abc123" })
        """
        return self._call("data.resolve", params)

    def export(self, **params: Any) -> Any:
        """Export a typed subgraph to a self-describing SQLite artifact — embeds the shape-defs it uses, so the schema travels with the file.

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
        """Import a previously-exported artifact, merging its rows into the live graph under the identity policy.

        Args:
            in_path (string, required): Artifact path (~ expanded). SQLite for v1.
            on_id_collision (string, optional): Default merge: overwrite vals + ensure links/shapes/content on existing id.
            plan_only (bool, optional): Compute the per-row category, do not write.

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
        """Disk + content statistics for a Volume: file size on disk, node count, shape histogram, schema version. Powers the Properties inspector (used space, node count, shape histogram). Defaults to the home Volume when `id` is omitted.

        Args:
            id (string, optional): Volume id slug. Accepts "home" / "memex" for the home vault. Defaults to "home" when omitted.

        Examples:
            volume_stats({})                       // home
            volume_stats({ id: "joe-health" })     // a mounted pod
        """
        return self._call("data.volume_stats", params)

    def canonicalize_units(self, **params: Any) -> Any:
        """Back-canonicalize a Volume's stored units in place — rewrite every node_vals/link_vals unit through the write-boundary UCUM canonicalizer, retroactively. A migration (unit column only, atomic), not a reseed. Idempotent. Returns the before/after diff + residual audit set.

        Args:
            dry_run (bool, optional): Preview the diff without writing. Default false.
            id (string, optional): Volume id slug. Accepts "home" / "memex" for the home vault (default). A mounted-pod slug targets that pod.

        Examples:
            canonicalize_units({})                       // home vault
            canonicalize_units({ dry_run: true })        // preview only
            canonicalize_units({ id: "joe-health" })     // a mounted pod
        """
        return self._call("data.canonicalize_units", params)


class _PluginsNamespace:
    """Proxy for the `plugins` namespace."""

    def __init__(self, call):
        self._call = call

    def run(self, **params: Any) -> Any:
        """Execute a plugin tool directly.

        Args:
            app (string, required): Plugin id (e.g. "exa").
            tool (string, required): Tool name within the plugin (e.g. "search").
            account (string, optional): Force a specific credential/account when the plugin has multiple.
            execute (Any, optional): Live-execution override; consult the plugin manifest for accepted shapes.
            params (dict, optional): Op-level params forwarded to the plugin.
            provider (string, optional): Force a cookie provider (e.g. "brave-browser").
            remember (bool, optional): Persist the live result to the graph. Default true.
            view (dict, optional)

        Examples:
            run({ app: "exa", tool: "search", params: { query: "..." } })
        """
        return self._call("plugins.run", params)

    def load(self, **params: Any) -> Any:
        """Load a plugin manual (readme + tool list + per-connection auth state) before calling run.

        Args:
            app (string, required): Plugin id to load (readme + tool list).

        Examples:
            load({ app: "exa" })
        """
        return self._call("plugins.load", params)

    def connect(self, **params: Any) -> Any:
        """Store a credential for a plugin connection (api-key connections). Encrypted vault row + account node; the secret never lands in the graph. Returns the plugin's per-connection auth state.

        Args:
            app (string, required): Plugin id (e.g. "porkbun").
            connection (string, optional): Connection name. Optional when the plugin declares exactly one authenticated connection.
            identifier (string, optional): Account identity at the platform (email/handle), when known.
            key (string, optional): The API key/secret. For multi-part keys, use the format the plugin's manual states (e.g. porkbun: "apikey:secretapikey").
            label (string, optional): Display label for the credential.
            value (dict, optional): Alternative to key: explicit secret fields ({ field: secret, … }).

        Examples:
            connect({ app: "firecrawl", key: "fc-..." })
            connect({ app: "porkbun", key: "pk1_...:sk1_..." })
        """
        return self._call("plugins.connect", params)

    def disable(self, **params: Any) -> Any:
        """Switch a plugin off: it drops out of matchmaking, run, and readme()'s tool list. The graph node and any stored credentials stay; enable reverses it.

        Args:
            app (string, required): Plugin id to switch off — it drops out of matchmaking, run, and readme until re-enabled.

        Examples:
            disable({ app: "porkbun" })
        """
        return self._call("plugins.disable", params)

    def enable(self, **params: Any) -> Any:
        """Switch a disabled plugin back on.

        Args:
            app (string, required): Plugin id to switch back on.

        Examples:
            enable({ app: "porkbun" })
        """
        return self._call("plugins.enable", params)


class _AccountsNamespace:
    """Proxy for the `accounts` namespace."""

    def __init__(self, call):
        self._call = call

    def save(self, **params: Any) -> Any:
        """Save a login for a bare domain — the app-agnostic credential write door. Encrypted vault row + account node; the secret never returns. A website login is as first-class as an app api-key.

        Args:
            domain (string, required): Bare registrable domain the login is for (e.g. "prenuvo.com"). App-agnostic — a website is as first-class as an app.
            identifier (string, required): The account handle at that domain — usually the login email/username.
            value (dict, required): Secret fields. { username, password } for a login; { key } for an api-key. Never returned, encrypted at rest.
            itemType (string, optional): Credential kind. Defaults to "login_credentials". Use "api_key" for a pasted key.
            label (string, optional): Display label for the account.
            source (string, optional): Provenance of the secret. Defaults to "user".

        Examples:
            save({ domain: "prenuvo.com", identifier: "joe@contini.co", value: { username: "joe@contini.co", password: "<secret>" } })
            save({ domain: "openai.com", identifier: "joe", value: { key: "sk-..." }, itemType: "api_key" })
        """
        return self._call("accounts.save", params)

    def list(self, **params: Any) -> Any:
        """Every account + every app connection with auth kind, status, identifier, and freshness — the identity surface behind the apps and websites.

        Args:
            view (dict, optional)

        Examples:
            list()
        """
        return self._call("accounts.list", params)

    def forget(self, **params: Any) -> Any:
        """Forget a saved login — the inverse of save. Deletes the encrypted vault row(s) plus the credential + orphaned account graph nodes for a (domain, identifier). Idempotent: forgetting an unknown account is a no-op, not an error.

        Args:
            domain (string, optional): Bare registrable domain of the account to forget (e.g. "prenuvo.com"). The same value passed to accounts.save. Required unless `id` is given.
            id (string, optional): Account node id to forget — resolves (domain, identifier) off the node. Alternative to passing them directly; this is what the desktop's right-click → Forget uses.
            identifier (string, optional): The account handle at that domain — usually the login email/username. Required unless `id` is given.

        Examples:
            forget({ domain: "prenuvo.com", identifier: "joe@contini.co" })
        """
        return self._call("accounts.forget", params)


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

    def operations(self, **params: Any) -> Any:
        """Live background operations — what's running right now, shared with the desktop: label, progress (current/total), elapsed, ETA, and whether it's cancelable. The same set is appended to every tool result's footer, so you usually already know without calling. Pass `{cancel: "<act_id>"}` to cancel one (cooperative — see the field).

        Args:
            cancel (string, optional): act_id of a running operation to cancel. Cooperative by default — only ops that declare themselves cancelable honor it (others keep running and `cancelled` returns false). Omit to just list. The `how` field reports what happened: cooperative / hard_aborted / not_cancelled.
            hard (bool, optional): Force-abort a non-cooperative op that's wedged (a dead CDP target, a hung socket) — kills the Tokio task outright. Abrupt: it stops mid-flight, its request gets no reply, partial side effects stay. Reserve for stuck ops; cooperative cancel is preferred when it works.

        Examples:
            system.operations()
            system.operations({ cancel: "…" })
        """
        return self._call("system.operations", params)

    def subscriptions(self, **params: Any) -> Any:
        """Standing subscriptions — the durable streams the engine keeps live and re-arms at every boot (WhatsApp Live, …), the durable-axis sibling of `system.operations`. Each row carries the watching app (id, name, icon), the watched `target`, the arming `op`, and `armedAt`. Pass `{stop: "<id>"}` to stop one — tears the live stream down and removes the durable record so it won't re-arm.

        Args:
            stop (string, optional): Subscription node id to stop — tears the live stream down and removes the durable record so it won't re-arm at boot. Omit to just list.

        Examples:
            system.subscriptions()
            system.subscriptions({ stop: "…" })
        """
        return self._call("system.subscriptions", params)


class _WindowsNamespace:
    """Proxy for the `windows` namespace."""

    def __init__(self, call):
        self._call = call

    def surface(self, **params: Any) -> Any:
        """Ensure a desktop surface is up and rendering — launch the desktop app if none is connected, then (by default) wait until it actually connects. Idempotent; the dual of the headless ops. Call it before a DOM op (snapshot / ui.invoke) when working with no pixels up.

        Args:
            wait (bool, optional): Block until a surface actually connects (default true). false returns right after spawning the desktop app.

        Examples:
            surface({})
            surface({ wait: false })
        """
        return self._call("windows.surface", params)

    def list(self, **params: Any) -> Any:
        """Every open window: id, route, title, bounds, size policy, focused, minimized.

        Examples:
            list({})
        """
        return self._call("windows.list", params)

    def read(self, **params: Any) -> Any:
        """A window's content as a graph read — the window's route plus its hydrated subject node. No DOM scraping; views and apps have no subject (null).

        Args:
            id (string, required): Window id (from windows.list / windows.open).

        Examples:
            read({ id: "window-…" })
        """
        return self._call("windows.read", params)

    def snapshot(self, **params: Any) -> Any:
        """A window's full semantic state — view mode, every content row (label, icon, selection), table columns (id, width, and which is sorted) plus the overall sort, selected sidebar folder, details-pane visibility, toolbar nav state — read from the shell's DOM annotations, not pixels. Where windows.read returns the subject node, snapshot returns the rendered surface (listing routes have no subject). `rendered: false` (with `reason`: `reconnecting` mid-reload, `minimized`, or `no_surface`) means nothing painted the surface yet, so the empty content is honest — wait/retry or restore rather than trusting it.

        Args:
            id (string, required): Window id (from windows.list / windows.open).

        Examples:
            snapshot({ id: "window-…" })
        """
        return self._call("windows.snapshot", params)

    def open(self, **params: Any) -> Any:
        """Open a window at a route — the same spawn/dedup path a human launch takes. Returns the window id.

        Args:
            route (string, required): Shell route to open — `node/<id>`, `list/<id>`, an app id (`messaging`, `display?tab=Background`), or a view query (`?group=…`). Same dedup as a human launch: an existing window at the route is focused, not duplicated.
            bounds (dict, optional): Optional initial position/size. Omitted fields fall to saved position, then cascade.

        Examples:
            open({ route: "node/abc123" })
            open({ route: "display?tab=Background", bounds: { x: 200, y: 120 } })
        """
        return self._call("windows.open", params)

    def close(self, **params: Any) -> Any:
        """Close a window by id.

        Args:
            id (string, required): Window id (from windows.list / windows.open).

        Examples:
            close({ id: "window-…" })
        """
        return self._call("windows.close", params)

    def focus(self, **params: Any) -> Any:
        """Bring a window to the front (restores if minimized).

        Args:
            id (string, required): Window id (from windows.list / windows.open).

        Examples:
            focus({ id: "window-…" })
        """
        return self._call("windows.focus", params)

    def move(self, **params: Any) -> Any:
        """Move a window to (x, y).

        Args:
            id (string, required): Window id.
            x (float, required)
            y (float, required)

        Examples:
            move({ id: "window-…", x: 300, y: 160 })
        """
        return self._call("windows.move", params)

    def resize(self, **params: Any) -> Any:
        """Resize a free-sized window. Fit windows refuse — their size derives from content (policy is law).

        Args:
            height (float, required)
            id (string, required): Window id. Free-sized windows only — a fit window's size derives from its content and the shell refuses to override it.
            width (float, required)

        Examples:
            resize({ id: "window-…", width: 900, height: 640 })
        """
        return self._call("windows.resize", params)

    def respond(self, **params: Any) -> Any:
        """Shell-internal: the desktop delivers a command's result back to the engine. Agents never call this.

        Args:
            command (string, required): The shell_command event's command id.
            decline (bool, optional): This shell doesn't own the targeted window — another desktop's answer settles the command.
            error (string, optional): Why execution was refused, when it was.
            result (Any, optional): The executed command's result.
        """
        return self._call("windows.respond", params)

    def sync(self, **params: Any) -> Any:
        """Shell-internal: a surface pushes its full window set so the engine session mirrors it. Agents never call this.

        Args:
            focusedId (Any, required)
            windows (list[object], required)
        """
        return self._call("windows.sync", params)


class _UiNamespace:
    """Proxy for the `ui` namespace."""

    def __init__(self, call):
        self._call = call

    def invoke(self, **params: Any) -> Any:
        """Activate a labeled control (OK / Cancel / Apply) in a window. The real button is focused, pressed, and clicked — the human watches it happen. Minimized windows and disabled controls refuse (policy is law).

        Args:
            control (string, required): The control's visible label, case-insensitive — OK, Cancel, Apply, Browse…. A miss returns the window's labeled controls.
            windowId (string, required): Window id (from windows.list / windows.open).

        Examples:
            invoke({ windowId: "window-…", control: "OK" })
        """
        return self._call("ui.invoke", params)

    def click(self, **params: Any) -> Any:
        """Click any shell item by its visible label or its data-navigator-id — a list row, a tab, a sidebar entry, or a table column header (clicking a column name toggles its sort: ascending, then descending). The real element is scrolled into view and clicked, so the human watches it happen. Optional `in` scopes the search to one pane. Returns the window's fresh snapshot (the after-state — e.g. content.sort after a header click). A label/id miss returns the window's clickable items.

        Args:
            windowId (string, required): Window id (from windows.list / windows.open).
            in (string, optional): Optional region scope — resolve the label/navigatorId within just this pane (sidebar folder tree, content grid, or toolbar), so a label present in more than one pane is unambiguous. Omit to search the whole window body. A miss lists only that pane's items.
            label (string, optional): Click the item whose visible text matches, case-insensitive — a list row, a tab, a sidebar entry, a control. A miss returns the window's clickable items.
            navigatorId (string, optional): Click the item carrying this data-navigator-id (a node id) — the precise way to select a list row. A miss returns the window's clickable items.

        Examples:
            click({ windowId: "window-…", label: "Inbox" })
            click({ windowId: "window-…", navigatorId: "abc123" })
        """
        return self._call("ui.click", params)

    def contextMenu(self, **params: Any) -> Any:
        """Right-click a row and choose one menu entry — Open, Properties, Delete, Create Desktop Shortcut, a shape-scoped tool. The real menu mounts and the entry is clicked, so the human watches the gesture. Optional `in` scopes the row search to one pane. Returns the window's fresh snapshot (the after-state). A row or entry miss returns what was available.

        Args:
            select (string, required): The menu entry to choose, by its visible label — Open, Properties, Delete, Create Desktop Shortcut, a shape-scoped tool…. A miss returns the entries the menu offered.
            windowId (string, required): Window id (from windows.list / windows.open).
            in (string, optional): Optional region scope — resolve the label/navigatorId within just this pane (sidebar folder tree, content grid, or toolbar). Omit to search the whole window body. A miss lists only that pane's items.
            label (string, optional): Right-click the row whose visible text matches, case-insensitive. A miss returns the window's clickable items.
            navigatorId (string, optional): Right-click the row carrying this data-navigator-id (a node id) — the precise way to target a list row. A miss returns the window's clickable items.

        Examples:
            contextMenu({ windowId: "window-…", navigatorId: "abc123", select: "Properties" })
            contextMenu({ windowId: "window-…", label: "Inbox", select: "Open" })
        """
        return self._call("ui.contextMenu", params)

    def key(self, **params: Any) -> Any:
        """Press keys in a window the way a human types — arrows to walk a list or folder tree, Space to Quick Look the selection, Enter to open, Esc to close. Routes and labels can't express a keypress; this is the keyboard's first-class lever. Optionally focus a row first (label / navigatorId, with an optional `in` region scope), or compose after a ui.click. The window is focused and each key fires a real keydown+keyup on screen. Returns the window's fresh snapshot (the after-state) — e.g. ArrowDown shows the moved selection without a second call.

        Args:
            keys (list[string], required): Keys to press in order — each a real keydown+keyup. Named: ArrowUp, ArrowDown, ArrowLeft, ArrowRight, Enter, Escape, Space, Tab, Home, End, PageUp, PageDown, Backspace, Delete. Any single character types that character. e.g. ["ArrowDown", "ArrowDown", "Enter"].
            windowId (string, required): Window id (from windows.list / windows.open) to send the keys to. It's focused first, so window-level handlers (arrow selection, Space preview) act on it.
            in (string, optional): Optional region scope for the label/navigatorId focus target — resolve it within just this pane (sidebar folder tree, content grid, or toolbar). Omit to search the whole window body. A miss lists only that pane's items.
            label (string, optional): Optional — focus the item with this visible label first (e.g. a folder-tree row), then send the keys. Starts arrow-nav from a known row.
            navigatorId (string, optional): Optional — focus the item carrying this data-navigator-id first, then send the keys.

        Examples:
            key({ windowId: "window-…", keys: ["ArrowDown", "ArrowDown", "Enter"] })
            key({ windowId: "window-…", navigatorId: "abc123", keys: ["Space"] })
        """
        return self._call("ui.key", params)


class _TextNamespace:
    """Proxy for the `text` namespace."""

    def __init__(self, call):
        self._call = call

    def html_to_markdown(self, **params: Any) -> Any:
        """Convert an HTML string to Markdown — strip tags/styles down to prose and links. Browser-grade parsing tolerates malformed HTML. Pass `readable: true` (+ optional `url`) for reader mode: extract the main article first, dropping nav/ads/boilerplate. Pure transform; leaves no activity.

        Args:
            html (string, required): An HTML string to convert to Markdown.
            readable (bool, optional): Reader mode: extract the main article first (strip nav/ads/boilerplate), then convert. Default false (convert the whole document).
            url (string, optional): Source URL — lets reader mode resolve relative links. Only used with readable:true.

        Examples:
            html_to_markdown({ html: "<h1>Hi</h1><p>There</p>" })
        """
        return self._call("text.html_to_markdown", params)


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


class _ThemesNamespace:
    """Proxy for the `themes` namespace."""

    def __init__(self, call):
        self._call = call

    def list(self, **params: Any) -> Any:
        """Enumerate installed theme packages: every <source>/themes/<id>/theme.yaml across the registered sources. Returns [{id, name, path}].

        Examples:
            themes.list()
        """
        return self._call("themes.list", params)


class Client:
    """Engine dispatch client.

    Connects to the engine's MCP socket (~/.agentos/engine.sock
    unless $AGENTOS_ENGINE_SOCK overrides) and dispatches tool
    calls through `tools/call`. Namespaces are attributes:

        client.data.read(id="abc")
        client.system.status()
        client.apps.run(app="exa", tool="search", params={...})
    """

    def __init__(self, socket_path: Path | str | None = None):
        self._socket_path = (
            Path(socket_path) if socket_path else _default_socket_path()
        )
        self.data = _DataNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.plugins = _PluginsNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.accounts = _AccountsNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.system = _SystemNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.windows = _WindowsNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.ui = _UiNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.text = _TextNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.readme = _ReadmeNamespace(lambda op, params: _sync_call(self._socket_path, op, params))
        self.themes = _ThemesNamespace(lambda op, params: _sync_call(self._socket_path, op, params))


class AsyncClient:
    """Engine dispatch client (async).

    Connects to the engine's MCP socket (~/.agentos/engine.sock
    unless $AGENTOS_ENGINE_SOCK overrides) and dispatches tool
    calls through `tools/call`. Namespaces are attributes:

        client.data.read(id="abc")
        client.system.status()
        client.apps.run(app="exa", tool="search", params={...})
    """

    def __init__(self, socket_path: Path | str | None = None):
        self._socket_path = (
            Path(socket_path) if socket_path else _default_socket_path()
        )
        self.data = _DataNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.plugins = _PluginsNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.accounts = _AccountsNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.system = _SystemNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.windows = _WindowsNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.ui = _UiNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.text = _TextNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.readme = _ReadmeNamespace(lambda op, params: _async_call(self._socket_path, op, params))
        self.themes = _ThemesNamespace(lambda op, params: _async_call(self._socket_path, op, params))

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        return None


