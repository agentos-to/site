---
title: Wire shape
description: "The contract between every interface (HTTP, MCP, CLI) and the engine — request body, observer event shape, mutation_id round-trip."
sidebar:
  label: Wire shape
---

# Engine wire shape

The engine speaks one protocol — dotted-namespace ops with JSON params — through four interfaces ([HTTP bridge](/interfaces/http/), [MCP](/interfaces/mcp/), [CLI](/interfaces/cli/), in-process). This page is the authoritative description of what flows over those wires: the request body, what comes back, and the observer event every call emits.

It's the contract the frontend's [reactive graph cache](https://github.com/agentos-to/core/blob/main/_roadmap/p1/reactive-graph-cache.md) is built on, and the contract that lets external writers (skills, cron, CLI scripts) drive the same UI invalidation any other client gets.

## POST `/call` — request body

The HTTP bridge accepts JSON of the form:

```json
{
  "op": "data.update",
  "params": {
    "id": "abc123",
    "vals": { "pref:ui": "{\"fontSize\":14}" },
    "mutation_id": "1a2b3c4d-…",
    "view": { "format": "json" }
  }
}
```

| Field | Required | Notes |
|---|---|---|
| `op` | yes | Dotted op identity — `data.read`, `data.list`, `data.update`, `data.create`, `data.delete`, `skills.run`, `skills.load`, `system.{boot,status,schema}`, or any `tools.<capability>` contributed by an installed skill's `@provides`. |
| `params` | no | Op-specific arguments. Op pages under [`tool-surface/`](/tool-surface/) document each schema. |
| `params.mutation_id` | no | Client-minted UUID. The engine strips it from arguments before tool dispatch (no effect on tool behavior) and round-trips it into the observer event so the originating client can dedupe its own echo. Required only when the caller wants optimistic-UX dedupe (see below). |
| `params.view` | no | Output projection. The bridge auto-fills `{format: "json"}` when omitted; the CLI defaults to markdown for human readability. All ops accept it. |
| `params.__raw_json__` | no | When `true`, the MCP `content[0].text` field is the JSON-stringified result instead of pre-rendered markdown. The bridge auto-sets this so HTTP responses round-trip cleanly back to `Value`. Callers rarely need it. |

The bridge holds **one persistent MCP connection** to `~/.agentos/engine.sock` and forwards every `POST /call` as an MCP `tools/call`. There is no in-process dispatch on the bridge side. This is what makes UI writes emit observer events on the same bus as MCP / CLI / cron writes — see [the round-1 reactive-cache plan](https://github.com/agentos-to/core/blob/main/_roadmap/p1/reactive-graph-cache.md) for the architectural rationale ("one bus, one bridge").

## Observer event shape

Every tool dispatch — regardless of caller — emits two events on `~/.agentos/observer.sock`: one `phase: "started"` and one `phase: "completed"` (or `"failed"`). The HTTP bridge tails the socket and re-broadcasts events over [`/observer/stream`](/interfaces/http/#observer-live-activity) as SSE.

```jsonc
{
  "ts": "2026-05-12T08:44:31.196",
  "request_id": "2",
  "phase": "completed",
  "tool": "data.create",
  "operation": "data.create",
  "session_id": null,
  "client": "agentos-call",
  "working_dir": "/Users/joe/…",
  "arguments": { "shape": "task", "name": "Buy milk" },
  "display": { "title": "graph · data.create", "body_markdown": "…", "icon": "✏️", "address": "…" },
  "latency_ms": 5,
  "result": { "id": "hpefiq", "created": true },
  "error": null,
  "entities": { "nodes": ["hpefiq"], "edges": [], "shapes": ["task"] },
  "mutation_id": null,
  "skill": null
}
```

| Field | Notes |
|---|---|
| `phase` | `"started"` (dispatch begins) → `"completed"` or `"failed"` (terminal). The reactive bridge only acts on `"completed"`. |
| `tool` / `operation` | Same value — the dotted op identity. Both fields exist for cross-interface debugging without translating between bare and dotted forms. |
| `arguments` | The full input the engine saw, **including** `mutation_id`. |
| `result` | Tool result on `"completed"`, `null` otherwise. |
| `entities.nodes` / `entities.edges` | Graph IDs this call touched. `data.update` / `data.delete` echo the target id (or edge id). `data.create` echoes the new node's id on `"completed"`. The frontend invalidates every TanStack query bound to any of these IDs. |
| `entities.shapes` | Shape tags this call touched. Echoed on `data.create` (the explicit `shape` argument). Drives invalidation of open list queries (`useEntities({shape: X})`) whose new row hasn't been bound yet. Shape echo on update/delete is intentionally deferred — id binding already invalidates the lists that contain the row. |
| `mutation_id` | Echoes the client-supplied `params.mutation_id`; `null` for callers (MCP / CLI / cron) that don't mint one. The reactive bridge uses this to skip invalidating queries the local client has already patched optimistically. |
| `client` | Identifier the caller set on its session (`agentos-call`, `agentos-mcp`, `agentos-web-bridge`, etc.). Useful for filtering activity feeds by origin. |
| `latency_ms`, `request_id`, `session_id`, `working_dir` | Standard observability fields — same across all interfaces. |

`entities` is always present; an empty `{nodes: [], edges: [], shapes: []}` means "this call touched no entities" (most read ops, all `system.*` ops, etc.).

## `mutation_id` round-trip

The `mutation_id` is the dedupe primitive that lets the frontend patch its cache synchronously without later double-applying when the SSE echo arrives. The contract:

1. Client mints a UUID and embeds it in `params.mutation_id`.
2. Client patches its local cache via `registry.optimisticPatch(mutationId, …)`.
3. Engine strips `mutation_id` before tool dispatch (no effect on tool behavior) and includes it in both `arguments` and the top-level `mutation_id` field of the observer event.
4. SSE event arrives at every connected client. Each client calls `registry.consumeEcho(mutationId)`:
   - The originating client returns `true` (cache already patched) → skip invalidation.
   - Every other client returns `false` (the id was never registered locally) → invalidate normally.

The `useGraphMutation` hook + `graphCall` helper in the host app SDK handle all four steps automatically. External writers (MCP / CLI / cron) never set `mutation_id` and never need to.

## Escape hatches

The reactive substrate is opt-in. Two paths bypass it cleanly:

- **Raw `apiPost('/call', {op, params})` without `mutation_id`.** The write goes through, the observer event fires, every other reader's cache invalidates. The local caller just doesn't get the optimistic-UX path — its own cache waits for the SSE echo + invalidation roundtrip.
- **`window.__AGENTOS_SDK__.useQuery` (community-app back-compat).** Same — works, no auto-invalidation on the calling component. The cache itself still reacts to writes the host app makes via `useGraphQuery`; only the raw-`useQuery` component misses out on shape-tag and id-tag binding. New community apps should prefer `useGraphQuery` + `useGraphMutation` + `graphCall` (also on the SDK global).

## What does *not* go over this wire

- **Read-set tracking.** The engine doesn't tell the client what entity IDs a given `data.read` / `data.list` response depends on — the client deep-walks the response itself (`defaultExtractIds` in `entity-registry.ts`). The wire is one-way for reads: response in, IDs out, register the binding client-side.
- **Bulk / batch invalidation.** Every observer event is one tool call. There is no "shape X was reindexed, invalidate everything" superseding event. Skills that mutate many rows emit many events.
- **Per-field invalidation.** Echoed entities are whole nodes — there's no "node X's `pref:ui` field changed but its `name` didn't" granularity. The frontend treats any `entities.nodes: [X]` echo as "refetch any query bound to X".

These are deliberate — see the "Why this and not the alternatives" tables in the [round-1](https://github.com/agentos-to/core/blob/main/_roadmap/p1/reactive-graph-cache.md) and [round-2](https://github.com/agentos-to/core/blob/main/_roadmap/p2/reactive-graph-cache-followups.md) reactive-cache plans for the trade-offs.
