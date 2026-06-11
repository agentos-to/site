---
title: HTTP
description: The web bridge — localhost HTTP + SSE at 127.0.0.1:3456 for the desktop shell. Read-only by default, reads from a separate SQLite connection.
---

The **web bridge** is how the browser-based desktop shell talks to AgentOS. Browsers can't open Unix sockets, so the bridge translates: it's a small HTTP/SSE server on `127.0.0.1:3456` that serves the graph, the observer event stream, shapes, user prefs, and static assets.

Run it with `agentos bridge`. It auto-starts the engine if needed (via `ensure_engine()`), opens its own read-only SQLite connection to `~/.agentos/data/agentos.db`, and binds to localhost only.

## Routes

### Liveness

| Method | Path | Purpose |
|---|---|---|
| GET | `/healthz` | Returns 200 OK if the bridge can reach the observer socket. |

### Tool surface

| Method | Path | Purpose |
|---|---|---|
| POST | `/call` | **The single front door** for every namespace in the unified tool surface. Body: `{"op": "<namespace>.<op>", "params": {...}}`. |

`/call` mirrors MCP's `tools/call` wire format: dotted op identity in, handler result out, dispatched through the same `tools::registry::dispatch` path that MCP, CLI, and the Python SDK use. One registry, four interfaces, identical behaviour:

- `data.read` — fetch one node by id (with relationships + content).
- `data.list` — list nodes by shape, user_tag, name, FTS via `q`, system metadata, or app membership.
- `data.update` — set or delete vals on an existing node, or set vals on an link (`{link: id, vals}`).
- `data.create` — create a node, or upsert if `identity` is provided.
- `data.delete` — soft-delete a node or link.
- `apps.run` — invoke an app tool.
- `apps.load` — fetch an app manual before calling `run`.
- `system.{status, schema}` — engine lifecycle + introspection.
- `services.<name>` — brokered service verbs contributed by installed apps' `@provides` (e.g. `services.web_search`).

See [`tool-surface/`](/tool-surface/) for the full op catalog (one page per namespace, generated from the registry). All ops accept `view: { format: "json" | "markdown" }` to override the per-interface default — HTTP defaults to JSON.

### Observer (live activity)

| Method | Path | Purpose |
|---|---|---|
| GET | `/observer/history` | One-shot query of past activity. Supports session and client filters. |
| GET | `/observer/stream` | **Server-Sent Events.** Live stream of tool-call activity as it happens. |

Observer events come from a separate socket (`~/.agentos/observer.sock`) that the engine writes to. The bridge tails that socket and forwards events to any connected SSE subscriber.

This is the primitive behind any "live activity feed" UI — you can see app invocations, graph writes, and auth resolutions as they happen.

### App metadata

| Method | Path | Purpose |
|---|---|---|
| GET | `/apps` | List installed app definitions (title, icon, contract metadata). |
| GET | `/user` | Unified user profile: person record + desktop prefs + theme. |
| GET | `/readme` | The engine's live readme — orientation for agents without MCP tools. |

User preferences are written through `POST /call` with `data.update` —
there's no separate `PUT /user/pref` shim. Settings writes
`pref:*` vals on the person node; the desktop folder writes positions
through `data.update {link: <id>, vals: {...}}` (the link branch).

### Static assets

| Method | Path | Purpose |
|---|---|---|
| GET | `/ui/wallpapers/*` | Theme wallpapers. |
| GET | `/content/:id` | Content for entities that reference local files. |
| GET | `/docs/*` | Rendered doc files. |

## Trust model

The bridge is **localhost only**. It binds to `127.0.0.1`, not `0.0.0.0`. Nothing from another machine can reach it without explicit tunneling.

Within localhost, there is no additional auth. Any process on the machine that can open a TCP connection to `:3456` can read the graph. This is the same trust model as the [CLI](/interfaces/cli/): if you're on the machine, you have access.

**Writes go through the engine, not the bridge.** The bridge's SQLite connection is opened read-only; mutating ops (`POST /call` with `data.update` / `data.create` / `data.delete` / `apps.run`) proxy to the engine socket, which enforces the usual dispatch and auth flow.

## SSE contract

The `/observer/stream` endpoint emits newline-delimited events in SSE format. Each event is one tool dispatch (started → completed/failed), shape documented in full at [`tool-surface/wire-shape`](/tool-surface/wire-shape/#observer-event-shape).

```
event: activity
data: {"phase":"completed","tool":"data.create","entities":{"nodes":["hpefiq"],"links":[],"shapes":["task"]},"mutation_id":null,…}
```

The `entities` field is what the frontend's reactive cache binds against — write `entities.nodes` invalidate queries bound to those ids, `entities.shapes` invalidate open list queries for those shapes. See the wire-shape page for the full field table and the `mutation_id` round-trip used for optimistic-UX dedupe.

Clients should use the browser `EventSource` API, not raw fetch. Reconnect is automatic; the server accepts `Last-Event-ID` for resumption (current implementation: the server keeps a small ring buffer of recent events for reconnect replay).

## How apps get a UI

There are no hand-written web apps and no TypeScript SDK. Every installed app renders in the desktop shell as a **generated window** — `core/web/src/views/AppWindow.tsx` builds the UI from the app's contract: its `@returns` shapes and the JSON-Schema input schemas derived from its tool signatures. The shell's own typed contract (`shapes.ts`) is codegen output, generated into `core/web/src/contract-generated/` from the same ontology that produces the Python SDK.

Writing an app means writing Python (see [Apps overview](/apps/overview/)); the window comes for free.

## Port configuration

Default is `3456`. Override with:

```bash
agentos bridge --port 3001
# or
AGENTOS_BRIDGE_PORT=3001 agentos bridge
```

If you change the port, anything that hardcodes `3456` will break. The shell reads the port from the page's origin, so pages served by the bridge itself are fine.

## Failure modes

- **Bridge won't start** — usually a port conflict. `lsof -i :3456` shows the culprit.
- **`/call` returns 500** — check `~/.agentos/logs/engine.log`. The bridge forwards mutating ops to the engine; engine errors surface as 500s.
- **SSE disconnects mid-session** — the observer socket was closed (engine restart). The browser `EventSource` will reconnect automatically.
