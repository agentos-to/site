# Orphan shape classification

`classify_orphans.py` against `site/docs/shapes/` (81 YAMLs).

## Counts

| Label | Count |
|---|---|
| `produced` (returned by ≥1 skill) | 43 |
| `schema_only` (relation/`also:` target) | 24 |
| `embedded` (field type on another shape) | 0 |
| `truly_orphan` (no producer, no referrer) | 14 |
| mixed non-produced | 0 |

38 validator orphans = 24 schema_only + 14 truly_orphan.

## Truly orphan — deletion candidates

One-liners from each YAML's header comment:

- **activity** — immutable change event (graph mutation, skill run, search, load).
- **analytics_event** — PostHog-tracked product analytics action.
- **article** — published written work (essay, news, blog, paper).
- **financial_account** — bank account, credit card, investment account.
- **flight** — specific leg of air travel. Flight IS a leg.
- **highlight** — personal extraction from a source (annotated passage).
- **report** — structured output of a research task, analysis, or agent run.
- **route** — transport service running between places on a schedule.
- **search** — a search query and its results.
- **shortcut** — named alias expanding to a location URI at parse time.
- **source** — content source (where skills, themes, shapes live).
- **theme** — OS theme (window chrome, taskbar, desktop styling).
- **vehicle** — physical vehicle (VIN, specs, color).
- **volume** — storage volume (local disk, external drive, network share).

Many look like forward-looking scaffolding — `activity`, `search`, `source`, `shortcut`, `theme`, `volume` are plausibly engine-level concepts the engine (not a skill) will produce.

## Surprises

1. **Embedded bucket is empty.** All `fields:` across 81 shapes use one of 8 primitives (`boolean`, `datetime`, `integer`, `json`, `number`, `string`, `text`, `url`). Scanner catches the first shape-typed field automatically.
2. **No dangling targets.** Every `relations.target:` and `also:` resolves to a real YAML. Shape graph is closed.
3. **`flight` is the oddest truly-orphan.** Declares `also: [leg]` (so `leg` gets a ref) but nothing refers to `flight` — a leaf supertype skills must opt into by returning `"flight"` explicitly.
4. **`financial_account` declares `also: [account]`** but nothing points at it. Engine-produced or dead?
5. **Top hubs:** `product` (20 incoming), `organization` (19), `person` (19), `account` (17), `place` (14).
6. **Self-referential shapes** (point at own shape): `memex`, `simulation`, `repository`, `document`, `note`, `spec`, `task`, `post`, `git_commit`, `tool_call`, `message`.

## Scripts

- `audit_shape_relations.py` — `relations:` + `also:` reverse index.
- `audit_embedded_shapes.py` — `fields:` scanner for shape-typed entries.
- `classify_orphans.py` — combines both with produced set.
