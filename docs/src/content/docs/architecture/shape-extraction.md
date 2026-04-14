---
title: Shape coercion & entity extraction
description: How a skill's return dict turns into a graph node — the extraction pipeline, type coercion, identity-based upsert, and the self-identity guard that keeps your own person node from being overwritten.
---

A skill returns a Python dict. Some milliseconds later, that dict has become one or more nodes in `~/.agentos/data/agentos.db`, with declared field types coerced, identity keys checked against existing nodes, and a provenance edge back to the skill. This page is the close-up of that exchange.

This page assumes the [data model](/docs/architecture/data-model/) — the three primitives, shapes as schema, why identity-based dedup exists at all. It goes one layer down: into the Rust extraction module that turns dicts into graph mutations.

## From dict to node

The pipeline is a single function — `extract_entities_from_response` (`crates/core/src/execution/extraction.rs:114`) — invoked after every successful skill operation. The `tag` argument is the shape name from the operation's `@returns("book")` decorator. Items are unwrapped (single-object responses and `_items`-wrapped arrays are both handled, lines 129-140), then each item walks through `extract_single_node` (line 572).

```
skill returns dict ─┐
                    │
@returns("book") ───┤  tag = "book"
                    │
                    ▼
       ┌─────────────────────────────┐
       │ shape registry lookup       │  shapes::registry().get("book")
       │ (also-chain expansion)      │  also: [product]  →  fields merge
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │ shape relations stripped    │  nested dicts → recursed as child nodes
       │ from field data             │  (lines 590-599)
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │ typed_val() per field       │  "495" → ("495", "integer")
       │ (shape-driven coercion)     │  shapes/registry.rs:491
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │ identity keys assembled     │  build_identity_keys()
       │ (vals + relation edges)     │  extraction.rs:410
       └──────────────┬──────────────┘
                      │
                      ▼
       ┌─────────────────────────────┐
       │ upsert_by_identity_on()     │  match → UPDATE, else CREATE
       │ + imported_from edge        │  graph/database.rs:1923
       └─────────────────────────────┘
```

Everything happens inside one SQLite transaction (`begin_transaction` at line 159, `commit` at line 191) — partial extraction never lands.

## Type coercion

Each declared field gets a `FieldType` from the shape registry (`crates/shapes/src/registry.rs:64`). The full enum:

| YAML type    | `FieldType`     | Storage `unit` | Coercion behavior on a wrong-shape input                                                  |
|--------------|-----------------|----------------|-------------------------------------------------------------------------------------------|
| `string`     | `String`        | `text`         | Anything stringifies. `null` → empty string.                                              |
| `text`       | `Text`          | `text`         | Same as `string`; the Text marker tells the UI it's long-form / FTS-eligible.             |
| `integer`    | `Integer`       | `integer`      | `"495"` → `495`. Floats truncated with warning. `true`/`false` → `1`/`0`. `"abc"` → stored as `text` with warning, **not rejected** (registry.rs:565). |
| `number`     | `Number`        | `number`       | Numeric strings parsed; non-numeric strings stored as `text` with warning.                |
| `boolean`    | `Boolean`       | `bool`         | `1`/`0`, `"yes"`/`"no"`, `"true"`/`"false"` all coerce. Anything else falls through to `text`. |
| `datetime`   | `Datetime`      | `datetime`     | RFC 3339, RFC 2822, bare `YYYY-MM-DD`, `YYYY-MM`, `YYYY`, common human formats. Unix timestamps in s or ms auto-detected by magnitude (registry.rs:712). Non-parseable → `text` with warning. |
| `url`        | `Url`           | `url`          | Stored as text with the `url` unit hint; no validation.                                   |
| `enum`       | `Enum(values)`  | `text`         | Stored as-is; warning if value isn't in the declared set.                                 |
| `string[]`   | `StringArray`   | `json`         | Each element coerced to string; bare strings get wrapped in a single-element array.       |
| `integer[]`  | `IntegerArray`  | `json`         | Each element coerced to integer.                                                          |
| `json`       | `Json`          | `json`         | Stored verbatim. No coercion, no inspection.                                              |

The dispatch lives in `coerce()` (`crates/shapes/src/registry.rs:468`) and the shape-aware entry point is `typed_val()` (line 491) — the function the extraction pipeline actually calls.

**The honest summary of every "wrong type" path: coerce if you can, store-as-text-with-warning if you can't.** Nothing is dropped, nothing is rejected. A skill that returns `pages: "many"` for an `integer` field gets a `node_val` row with value `"many"` and unit `text`, plus a `debug!` line. The graph keeps moving.

Fields not declared in any shape fall through to `json_val_infer` (registry.rs:511) — pure JSON-shape inference, no shape context needed. So extra keys don't break extraction; they just don't get the benefit of typed coercion.

## Identity resolution

After coercion, `build_identity_keys` (`extraction.rs:410`) walks the shape's `also` chain and pulls the identity field values out of the prepared vals. Two flavors, both declared in YAML, both resolved at upsert time.

### `identity: [issuer, identifier]` — compound key

All keys must match. The lookup is `find_node_by_tag_vals_and_edges_on` (`crates/graph/src/database.rs:1824`), which builds a SQL query with one `node_vals` self-join per identity field plus a tag-edge join:

```sql
SELECT nv0.node_id FROM node_vals nv0
JOIN node_vals nv1 ON nv1.node_id = nv0.node_id
                  AND nv1.key = ? AND nv1.value = ?    -- "identifier" = "joe@example.com"
JOIN edges e_tag   ON e_tag.from_node = nv0.node_id
                  AND e_tag.label = 'tagged_with'
                  AND e_tag.to_node = ?                -- account tag id
                  AND e_tag.deleted_at IS NULL
JOIN nodes n       ON n.id = nv0.node_id
                  AND n.deleted_at IS NULL
WHERE nv0.key = ? AND nv0.value = ?                    -- "issuer" = "gmail"
LIMIT 1
```

If `identity` includes a relation key (e.g. `identity: [platform, brand]` where `brand` is a relation), it becomes a join on `edges` instead of `node_vals` (database.rs:1863-1867). Pure relation identity is supported — the function falls back to anchoring on the edges table when there are no field vals (line 1846).

### `identity_any: [path, url]` — alternative key

Any single match wins. The resolver in `find_by_identity` (`crates/core/src/graph.rs:2295`) walks the list and returns the first hit:

```rust
if !shape.identity_any.is_empty() {
    for key in &shape.identity_any {
        if let Some(val) = params.get(key.as_str()).and_then(|v| v.as_str()) {
            if let Some(id) = database::find_node_by_tag_and_val(tag, key, val).await? {
                return Ok(Some(id));
            }
        }
    }
}
```

Iteration order = YAML declaration order. Put your most reliable disambiguator first.

## Upsert semantics

`upsert_by_identity_on` (`crates/graph/src/database.rs:1923`) is the single write path. It:

1. Tries identity lookup. If miss, falls back to **import provenance** (`imported_from` edge from the skill node with this `remote_id`) — line 1943.
2. **On hit (UPDATE):** bumps `updated_at`, calls `set_vals_on` to upsert each `(key, value, unit)` triple, ensures all tags are applied, ensures every relation identity edge exists. Existing vals not present in the new payload are **left in place**. (lines 1956-1987)
3. **On miss (CREATE):** mints a new node id, stores all vals, applies tags, creates relation edges, records provenance.
4. Either way: one `imported_from` edge per skill, with the skill's `remote_id` stored as an edge val. Re-importing the same record updates the timestamp on that edge (`record_import_on`, line 1980).

Critical consequence: **fields are merged, not replaced.** If skill A writes `{name, isbn, pages}` and skill B later writes `{name, isbn, cover_url}` for the same identity, the resulting node carries `name + isbn + pages + cover_url`. The provenance edges remember which skill contributed which write, but vals themselves don't carry per-field origin. Last writer wins per key.

This is also how a node survives skill churn. Uninstall the WhatsApp skill, the `imported_from(whatsapp)` edge stays, the vals stay. Reinstall it, identity lookup hits the same node, and updates resume on the same `id`.

## Collisions and self-identity

There's exactly one place the engine refuses to write a node: when extracting a *child* node whose identity matches the user.

`is_self_identity` (`crates/core/src/execution/extraction.rs:62`) reads the `self.identities` setting once, caches it in a `OnceLock<RwLock<Option<Vec<(String, String)>>>>` (line 56), and answers `(platform, identifier)` queries from that cache. The check fires inside `extract_linked_node_from_values` (line 1004):

```rust
for (key, value) in &filtered {
    if let Some(v) = value.as_str() {
        if is_self_identity(key, v).await {
            debug!("Skipping self identity: {}:{}", key, v);
            return Ok(None);
        }
    }
}
```

Returning `None` means: don't create the child node, don't create the edge to it. The parent record still lands.

The threat this closes: a Gmail skill returns an email with `from: { handle: "joe@gmail.com" }`. Without the guard, that nested dict becomes a fresh `account` node — identity `("email", "joe@gmail.com")` — and in the worst case, gets silently merged into the user's primary `person` via the `account` → `person` linkage (`link_account_to_primary_user`, line 360) using values the skill controls. With the guard, child extractions whose identity *is* the user are dropped before they can hijack the user's own node. The user's `person` is still authored only by the deterministic flow that runs at boot.

Note the asymmetry: the guard is on *child* extraction, not the top-level item. A skill that's explicitly tagged `person` and writes the user's identity isn't blocked here — that's a different layer's job.

## Where validation lives

The engine does type coercion. It does **not** enforce required fields, semantic constraints, or `@returns` shape conformance at runtime.

> *Schema validation lives elsewhere: `agent-sdk validate` (in
> `skills/_sdk/agentos/validate.py`) is the canonical static
> check for skill YAML/Python … These structs only describe the shape — they do not validate it.*
>
> — `crates/core/src/skills/types.rs:5-9`

In practice this means:

- **Static (pre-commit):** `agent-sdk validate` parses every `@returns("shape")` function, walks dict literals via AST, and warns on unknown keys, missing identity fields, and scalar-fields-that-should-be-relations. Runs on every commit.
- **Runtime (engine):** types get coerced; unknown keys get stored anyway; missing identity fields just mean the node falls back to import-provenance dedup; bad coercions become text with a warning.

The tradeoff is deliberate. The engine is generic — it doesn't know that `book` requires `isbn13`, and adding that knowledge would push entity-specific rules into Rust. Instead, conformance is a contract enforced at the SDK layer where shape semantics already live.

## Why shape-agnostic engine + shape-aware extraction

The extraction module imports exactly one piece of shape knowledge: `crate::shapes::registry()` (extraction.rs:415, 446, 471). Every shape-driven operation — identity resolution, relation processing, type coercion — is parameterized over a name string. The Rust code never says `if tag == "book"`.

That's the line. The engine is **shape-aware** (it consults the registry for field types, relations, identity) but **entity-agnostic** (it has no opinion about what `book` or `person` means). Adding a new shape is a YAML file, a graph seed, an engine restart. No Rust change, no recompile, no migration.

The day the engine learns that `book.pages` is sortable, every new entity becomes a Rust diff. That door is closed by architecture, not discipline.

## Further reading

- [Data model](/docs/architecture/data-model/) — the three primitives and why semantic type lives in data, not DDL.
- [Shapes overview](/docs/shapes/overview/) — authoring format, design principles, the review checklist.
- [Skill dispatch](/docs/architecture/skill-dispatch/) — what runs *before* extraction: the wire protocol that delivers the dict.
- [Identity & change](/docs/shapes/identity-and-change/) — identity across time, why every change is itself an entity.
