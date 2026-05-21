# Migrations — schema evolution as data

Each `*.yaml` file declares a content-addressed schema migration —
`from` ontology hash → `to` ontology hash, plus the ordered list of
ops the engine replays when importing data pinned at `from`.

Pinned in every `data.export` artifact via `_meta.schema_version`;
read by `data.import` to walk the chain `pin → current` and replay
the ops. The ontology hash itself is emitted by
`platform/codegen/schema_hash.py` into
`core/crates/contract-generated/src/schema_hash.rs` as `SCHEMA_HASH`.

## File grammar

```yaml
from: sha256:<hex>
to:   sha256:<hex>
doc:  "one-line description"
ops:
  - <op_kind>: { <params> }
  - <op_kind>: { <params> }
```

- **`from` / `to`** — full `sha256:<64hex>` pins.
- **`doc`** — one-line plain-English summary. Required.
- **`ops`** — ordered list. Order matters and is part of the migration's
  identity (canonicalisation preserves it).
- **File name** — `NNN-short-slug.yaml`. The `NNN` prefix is purely a
  filesystem convention for readable directory listings; the engine
  walks migrations by `from/to` hash, not filename.

## Op vocabulary

Thirteen ops. Each carries an implicit **W/S classification** —
*weakening* (cannot invalidate existing data, safe to auto-apply) or
*strengthening* (may invalidate, requires explicit ack or a tagged-union
default).

### Weakening — auto-applied under `on_schema_drift: migrate`

| op | params | notes |
|---|---|---|
| `add_node_type` | `{name}` | New shape with no instances yet. |
| `add_field` (optional) | `{shape, name, type: "..."?}` | New `field?: T` — old rows absent it. |
| `add_field` (with default) | `{shape, name, type, default: {type: Default, value: ...}}` | Required field with backfill. |
| `widen_field_type` | `{shape, field, from, to}` | `int → number`, `enum<a\|b> → string`, etc. |
| `extend_enum` | `{shape, field, add: [...]}` | New values for an existing enum. |
| `set_meta` | `{shape, key, value}` | Per-shape metadata edit. |
| `set_doc` | `{shape, value}` | Documentation edit. |

### Strengthening — require explicit user ack

| op | params | notes |
|---|---|---|
| `drop_node_type` | `{name, cascade: bool}` | All instances must be gone (or `cascade: true`). |
| `rename_node_type` | `{from, to}` | Rewrites instance ids; preserves attachment hashes. |
| `drop_field` | `{shape, name}` | Field disappears; existing values dropped. |
| `rename_field` | `{shape, from, to}` | Field renamed; values preserved under new key. |
| `narrow_field_type` | `{shape, field, from, to, default: DefaultOrError}` | `string → enum<...>`. Requires default resolution. |

### AgentOS-specific (always strengthening)

| op | params | notes |
|---|---|---|
| `rename_link` | `{from, to}` | Link label rename. Rewrites `links.label` rows. |
| `rename_link_val` | `{link, from, to}` | Rename a key on `link_vals` for one label. |
| `flip_link` | `{from, to}` | Direction-flip + rename. Rewrites every row where `label = from` to `label = to` with `from_node` and `to_node` swapped. Used when an active-form label drops in favor of its past-participle canonical (`owns → owned_by`). |
| `move_to_event` | `{shape}` | Adds `also: [event]`; folds onset/abatement-date fields into event start/end. |

Four of these (`rename_link`, `rename_link_val`, `flip_link`,
`move_to_event`) exist because AgentOS types links via a separate
registry (`platform/ontology/links/*.yaml`, Phase 1c) instead of
treating them as classes the way TerminusDB does. `flip_link` is the
shape-of-change the underscore-suffix audit produced: dropping an
active-form label like `owns` in favor of its past-participle peer
`owned_by` rewrites BOTH the label AND the direction-of-storage in
every existing row.

## `default: Default | Error` — the tagged union

For `narrow_field_type` and required `add_field`, the engine cannot
synthesise a value when the existing data doesn't fit. The migration
must declare what happens:

```yaml
- narrow_field_type:
    shape: task
    field: status
    from: string
    to: enum<todo|doing|done>
    default: {type: Default, value: "todo"}     # backfill non-matching rows
```

OR

```yaml
- narrow_field_type:
    shape: task
    field: status
    from: string
    to: enum<todo|doing|done>
    default: {type: Error}                       # abort import on non-matching rows
```

Encoding the choice in the op (rather than as a runtime flag) makes
the wrong thing impossible — the author has already decided.

## Authoring workflow

1. Edit the shape/op/link YAML in `platform/ontology/`.
2. Run `python3 platform/codegen/generate.py` → new `SCHEMA_HASH` lands
   in `core/crates/contract-generated/src/schema_hash.rs`.
3. `agentos call system '{"op":"schema_diff","params":{"pin":"sha256:<old>"}}'`
   → prints the chain (or a candidate template when no chain exists).
4. Save as `migrations/NNN-slug.yaml`, fill in the `ops:` list.
5. Re-run codegen → new `MIGRATIONS` entry lands in
   `contract-generated/src/migrations.rs`.
6. `data.import` will now auto-apply the chain when reading any
   artifact pinned at the `from` hash.

Migrations are **one-way**. Downgrades are separate changesets — if you
need to reverse a migration, write a new file with the inverse `from/to`
and the inverse ops. No engine auto-inverts.
