# Rust Shape-Producer Audit

Deterministic scan of `/Users/joe/dev/agentos/core/crates/**/*.rs` for
the four graph-tagging APIs defined in `graph/src/database.rs`:
`ensure_tag`, `find_tag_by_name`, `find_node_by_tag_and_val`, and
`create_tagged_node`.

## Totals

- **17 unique shapes** produced/referenced by the Rust engine
- **47 callsites** across 14 files
- Breakdown by API: `find_node_by_tag_and_val` 16, `create_tagged_node`
  12 (tag literals, from 11 calls — `identity.rs:48` emits both `agent`
  and `actor` from `&["agent", "actor"]`), `find_tag_by_name` 10,
  `ensure_tag` 9

## Full sorted list

```
account       conversation  image         shape
activity      folder        job           skill
actor         app           message       source
agent         album         person        task
                                          theme
```

## Surprises — Rust-produced shapes missing YAML definitions

Four shapes are created by the Rust engine but have no corresponding
file in `/Users/joe/dev/agentos/site/docs/shapes/`:

- **`album`** — `sources/wallpapers.rs:167, 261`
- **`app`** — `sources/apps.rs:366, 391`
- **`job`** — `jobs/lifecycle.rs:81, 179`, `engine/src/lib.rs:1135`
- **`shape`** — `shapes_graph.rs:28, 101, 141` (meta: the shape of
  shapes, used to hydrate the ShapeRegistry from the graph itself)

These are legitimate runtime entities but have no ontology YAML. Either
they should gain a shape file, or they are intentionally
engine-internal and should stay off-ontology. `shape` is likely
intentional (bootstrap / reflective); the other three look like gaps
worth filing.

The remaining 13 shapes (`account`, `activity`, `actor`, `agent`,
`conversation`, `folder`, `image`, `message`, `person`, `skill`,
`source`, `task`, `theme`) all have matching YAML files.

## Sanity check

The three `activity` references at `graph.rs:1251, 1323, 2934` are all
captured exactly as specified in the task brief.

## Ambiguity / unresolved

None. Every callsite matched was a bare string literal tag — no
`format!`, no constants, no dynamic dispatch. The only dynamic-tag
pattern in the codebase lives inside `graph/src/database.rs` itself
(e.g. `ensure_tag_on(conn, name)` where `name: &str` is a parameter),
and those are the *implementations* of the APIs we scan for — correctly
excluded because `name` is not a string literal. The script's
regex anchors on `\bensure_tag\s*\(`, which cleanly excludes the `_on`
variants (`ensure_tag_on`, `find_tag_by_name_on`,
`find_node_by_tag_and_val_on`) and the plural
`find_node_by_tag_and_vals`. One doc-comment example at
`database.rs:1704` is stripped by the comment-remover (`/// ...` is
treated as a `// ...` comment), so no false positive.

## Script

`/Users/joe/dev/agentos/skills/_sdk/agentos/audit_rust_producers.py`

- `scan_rust_producers(crates_root: Path) -> dict[str, list[tuple[Path, int, str]]]`
  — importable API
- `main()` — prints the sorted summary; run via
  `python3 audit_rust_producers.py`
