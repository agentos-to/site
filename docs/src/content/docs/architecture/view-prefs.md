---
title: View preferences
description: How AgentOS persists UI presentation state — view mode, column widths, sort order, theme knobs — as a single opaque `pref:ui` JSON val on the carrier node, with frontend-side resolution from instance → bookmark → shape → global.
---

UI presentation state — *what view mode is this folder in, how wide is the
"name" column on aircraft tables, what's my sort order on the trips
playlist* — lives as a single `pref:ui` json val on the carrier node. The
graph carries customisations; defaults are code-resident. Themes hang
their own knobs off `pref:ui.theme.<id>.*` and the engine never touches
the blob.

## The carrier is a node

Every "thing the user views" is already a graph node — a shape definition,
a folder, a playlist, a bookmark, a specific entity. We attach `pref:ui`
directly to those nodes. There is no separate `view_pref` shape, no
side table, no per-user join.

```
ANY node may carry:  pref:ui = { ...freeform UI blob }
```

Same val key, same `data.update` write path, different carrier nodes.

## The blob is opaque

The engine never reads, never validates, never indexes `pref:ui`. It
stores a json val and hands it back through normal node hydration.
Frontends and themes own the schema, documented advisorily here.

This means:

- New theme features need no engine change.
- Agents read & write prefs through the same `data.read` / `data.update`
  path as any other val.
- The convention can evolve in the frontend without migrations.

## Resolution chain

The frontend resolves prefs per render, deep-merging from least to most
specific:

```
1. GLOBAL_UI_DEFAULTS          (web/src/lib/ui-defaults.ts)
2. SHAPE_UI_DEFAULTS[shape]    (web/src/lib/ui-defaults.ts)
3. <shape def>.pref:ui         (graph-resident, when set)
4. <bookmark>.pref:ui          (when viewing through a bookmark)
5. <instance>.pref:ui          (when viewing one specific node)
```

`deepMerge(global, shapeDefault, shape, bookmark, instance)`. Last writer
wins per key path. Arrays replace wholesale (column orders are
sequences, not sets).

The merge happens entirely in the frontend (`web/src/hooks/useViewPrefs.ts`).
The engine returns whatever val each carrier carries; it does not pre-resolve.

This is the same mechanic as CSS: cascade by specificity. The graph
already says "shapes are nodes," so attaching prefs to a shape and
attaching prefs to a folder are *literally the same operation* —
`data.update({id, vals: {"pref:ui": {...}}})`.

## Setter targeting

The View menu writes to the *most-specific writable carrier*:

| Viewing | Edits target |
|---|---|
| A single named entity | That instance's `pref:ui` |
| A bookmark | The bookmark's `pref:ui` |
| All entities of a shape (no bookmark) | The shape def's `pref:ui` |
| FTS results, ad-hoc tag query | Disabled — no carrier |

Two explicit promote/reset actions are surfaced:

- **"Save as default for this shape"** — copies the resolved blob
  (everything more specific than the shape) onto the shape def.
- **"Reset to shape default"** — deletes `pref:ui` on the
  instance/bookmark carrier; the chain falls back to shape → global.

Promote and reset are the *only* shape-def writes a user makes
implicitly. Every other change targets the current carrier. This avoids
the "I customised one folder and it changed every folder" surprise.

## Reserved blob convention

Top-level keys split cleanly:

```jsonc
pref:ui = {
  // ── Universal — applies to any container, any view mode
  viewMode: 'details' | 'icons' | 'list' | 'thumbnails',
  sort:     { key: string, order: 'asc' | 'desc' },
  filter:   { /* freeform — TBD when first filter ships */ },

  // ── Mode-specific — namespaced by mode key
  details: {
    columnWidths:     { [colKey]: number },
    columnOrder:      string[],
    columnVisibility: { [colKey]: boolean },
    columnIncludes:   string[],   // view.include projections to request
  },
  icons: {
    iconSize: number,
    layout:   'grid' | 'flow',
  },
  list: {
    density: 'compact' | 'comfortable',
  },
  thumbnails: {
    tileSize: number,
  },

  // ── Theme-extension space — themes hang anything off `theme.<id>`
  theme: {
    xp:     { /* XP-specific knobs */ },
    aurora: { /* Aurora-specific knobs */ },
  },
}
```

Reserved top-level keys: `viewMode`, `sort`, `filter`, the mode-name keys
(`details`, `icons`, `list`, `thumbnails`), and `theme`. Everything else
is fair game during prototyping. Themes that introduce new keys document
them here when they stabilise.

## Defaults are code-resident

`GLOBAL_UI_DEFAULTS` and `SHAPE_UI_DEFAULTS` ship in the frontend at
[`web/src/lib/ui-defaults.ts`](https://github.com/agentos-to/core/blob/main/web/src/lib/ui-defaults.ts), not the graph. The graph only carries
*user customisations*.

Why: simpler bootstrap, themes can ship sensible starting points in
their YAML, no theme-switch write storm. The agent can still read what's
been customised — which is the meaningful subset. Promoting defaults
into the graph (so the agent sees baseline values too) is a future
opportunity, not a requirement.

## Engine surface

`pref:ui` is just a json val. It comes back through normal node
hydration:

```
data.read({id})              → entity.pref:ui in the response
data.list({shape})           → each row carries pref:ui (when set)
data.list({about: 'shapes'}) → each row carries shape_node_id, the
                                writable carrier for shape-default prefs
```

Writes:

```
data.update({
  id: <carrier-node-id>,
  vals: { 'pref:ui': { ...full blob... } }
})
```

Whole-blob writes. Last-write-wins. No JSONPath patches today —
single user, single window, blob is small (<1 KB). If contention shows
up later, `data.patch` is a 50-line addition.

To reset (delete `pref:ui` on the carrier), set the val to `null`:

```
data.update({ id, vals: { 'pref:ui': null } })
```

## What this unlocks

- Theme devs ship UI features without touching Rust.
- Agents can read & write view prefs through the regular graph API.
- Per-folder, per-playlist, per-bookmark customisation is free — the
  mechanic is the same as shape defaults.
- "Show me every shape I've customised" is a graph query.
- localStorage as UI persistence is gone.
- Multi-user (eventually) is a frontend overlay change, not a schema
  redesign.

## What this doesn't solve

- **Cross-machine sync.** Depends on database sync — separate problem.
- **Schema discipline within the blob.** Themes can collide; the
  convention here is advisory, not enforced. Namespace under
  `theme.<id>` if collisions become a problem.
- **Defaults as graph data.** Today defaults live in code. An agent
  inspecting `data.read({id: <shape def>})` sees only customisations,
  not the active default. Phase 3+ may promote defaults into the graph.

## Related

- [Data model](/architecture/data-model/) — the val/edge primitives that
  carry `pref:ui`.
- [Shapes](/architecture/shape-extraction/) — how shape defs become
  graph nodes (the carrier for shape-default prefs).
