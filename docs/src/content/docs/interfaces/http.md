---
title: HTTP
description: The web bridge — localhost HTTP + SSE at 127.0.0.1:3456 for browser apps. Read-only by default, reads from a separate SQLite connection.
---

The **web bridge** is how browser-based apps talk to AgentOS. Browsers can't open Unix sockets, so the bridge translates: it's a small HTTP/SSE server on `127.0.0.1:3456` that serves the graph, the observer event stream, shapes, user prefs, and the static assets apps need.

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
| POST | `/graph` | Legacy — kept until the last `apiPost('/graph', ...)` caller in the frontend migrates to `/call`. New code must not call this. |

`/call` mirrors MCP's `tools/call` wire format: dotted op identity in, handler result out, dispatched through the same `tools::registry::dispatch` path that MCP, CLI, and the Python SDK use. One registry, four interfaces, identical behaviour:

- `data.read` — fetch one node by id (with relationships + content).
- `data.search` — full-text across content (FTS5 + BM25).
- `data.update` — set or delete vals on an existing node.
- `data.create` — create a node, or upsert if `identity` is provided.
- `data.delete` — soft-delete a node or edge.
- `skills.run` — invoke a skill tool.
- `skills.load` — fetch a skill manual before calling `run`.
- `system.{boot, status, schema}` — engine lifecycle + introspection.
- `tools.<capability>` — dynamic capability tools contributed by installed skills' `@provides` (e.g. `tools.web_search`).

See [`tool-surface/`](/tool-surface/) for the full op catalog (one page per namespace, generated from the registry). All ops accept `view: { format: "json" | "markdown" }` to override the per-interface default — HTTP defaults to JSON.

### Observer (live activity)

| Method | Path | Purpose |
|---|---|---|
| GET | `/observer/history` | One-shot query of past activity. Supports session and client filters. |
| GET | `/observer/stream` | **Server-Sent Events.** Live stream of tool-call activity as it happens. |

Observer events come from a separate socket (`~/.agentos/observer.sock`) that the engine writes to. The bridge tails that socket and forwards events to any connected SSE subscriber.

This is the primitive behind any "live activity feed" UI — you can see skills invocations, graph writes, and auth resolutions as they happen.

### App metadata

| Method | Path | Purpose |
|---|---|---|
| GET | `/apps` | List installed + bundled app definitions (title, icon path, manifest). |
| GET | `/user` | Unified user profile: person record + desktop prefs + theme. |
| PUT | `/user/pref` | Set a person-level preference value. |

### Static assets

| Method | Path | Purpose |
|---|---|---|
| GET | `/ui/*` | App bundles, themes, wallpapers, icons. |
| GET | `/files/*` | File previews for entities that reference local files. |

## Trust model

The bridge is **localhost only**. It binds to `127.0.0.1`, not `0.0.0.0`. Nothing from another machine can reach it without explicit tunneling.

Within localhost, there is no additional auth. Any process on the machine that can open a TCP connection to `:3456` can read the graph. This is the same trust model as the [CLI](/interfaces/cli/): if you're on the machine, you have access.

**Writes go through the engine, not the bridge.** The bridge's SQLite connection is opened read-only; mutating ops (`POST /call` with `data.update` / `data.create` / `data.delete` / `skills.run`) proxy to the engine socket, which enforces the usual dispatch and auth flow.

## SSE contract

The `/observer/stream` endpoint emits newline-delimited events in SSE format:

```
event: activity
data: {"kind":"skill_run","skill":"goodreads","op":"get_book","duration_ms":412,"ok":true}

event: activity
data: {"kind":"graph_write","shape":"book","count":1}
```

Clients should use the browser `EventSource` API, not raw fetch. Reconnect is automatic; the server accepts `Last-Event-ID` for resumption (current implementation: the server keeps a small ring buffer of recent events for reconnect replay).

## Building an app against the bridge

Apps are regular web pages that fetch from `http://127.0.0.1:3456/call` (and friends). The `sdk-apps/` sibling repo ships `@agentos/sdk`, a TypeScript wrapper around these endpoints — most apps use it rather than calling fetch directly.

A minimal app is:

1. An HTML entrypoint + bundle served from `/ui/your-app-id/`.
2. A manifest at `app.json` the bridge picks up via `/apps`.
3. JavaScript that calls `fetch('/call', { method: 'POST', body: JSON.stringify({op: 'data.read', params: {id: '...'}}) })`.

See [Apps overview](/apps/overview/) for the full shape.

## Port configuration

Default is `3456`. Override with:

```bash
agentos bridge --port 3001
# or
AGENTOS_BRIDGE_PORT=3001 agentos bridge
```

If you change the port, apps that hardcode `3456` will break. The SDK reads the port from the page's origin, so apps served by the bridge itself are fine.

## Failure modes

- **Bridge won't start** — usually a port conflict. `lsof -i :3456` shows the culprit.
- **`/call` returns 500** — check `~/.agentos/logs/engine.log`. The bridge forwards mutating ops to the engine; engine errors surface as 500s.
- **SSE disconnects mid-session** — the observer socket was closed (engine restart). The browser `EventSource` will reconnect automatically.
