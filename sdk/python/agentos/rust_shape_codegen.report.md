# Rust Shape Codegen — Prototype Report

## Proposed path

**`core/crates/shapes/src/generated.rs`**.

`agentos-shapes` already owns shape *semantics* (`registry.rs`, loaded
from YAML/graph at boot). The name mirror belongs next to it.
`lib.rs` is 13 lines; the codegen adds one sibling module. Placing it
under `crates/core/` would drag the consts through a re-export for no
benefit.

## Integration with `crates/shapes/`

`crates/shapes/src/lib.rs` needs **one hand-edit, once**:

```rust
pub mod registry;
pub mod generated;        // + added

pub use registry::*;
pub use generated::*;     // + added
```

After that, any consumer already saying `use crate::shapes::...`
(via the `agentos_core::shapes` facade at `core/src/lib.rs:127`)
gets `shapes::ACTIVITY` with no further wiring.

## No conflict with the runtime shape loader

`registry.rs::load_shapes_from_dirs` parses the same YAMLs at boot.
The consts duplicate *names only*, not fields/relations/identity — the
runtime registry stays the authority. A shape added at boot via the
graph but not in YAML simply won't have a const; callers fall back to
string literals. The const list is a compile-time convenience, not a
gate.

The generic-engine principle holds: names only. No fields, no
relations, no `enum Shape {}`, no matching behavior. The engine still
learns zero semantics. The module docstring in
`codegen_rust_shapes.py` lists what deliberately stays out.

## Callsite diff (not applied)

`core/crates/core/src/graph.rs:1251`:

```diff
 async fn boot_recent_activity() -> String {
     let mut md = String::new();

-    let activity_tag = match database::find_tag_by_name("activity").await.ok().flatten() {
+    let activity_tag = match database::find_tag_by_name(crate::shapes::ACTIVITY).await.ok().flatten() {
         Some(id) => id,
         None => return md,
     };
```

One-word substitution. A typo (`ACTIVITYY`) now fails at compile
instead of silently returning `None`. Mechanical across all 37
migration callsites.

## Integration point

**Add to `./dev.sh build` as a pre-compile check.** `dev.sh:77-112`
already runs `gen_manifest` and `gen_sdk_stubs.py --check` before
compile and fails on drift. One more line mirrors that pattern:

```sh
python3 -m agentos.codegen_rust_shapes --check || exit 1
```

Pre-commit alone is insufficient (agents can bypass hooks); the
build-time check is where correctness gets enforced. Secondary hook:
`agent-sdk validate --all` can call `generate_rust_shapes(check=True)`
to surface drift earlier.

## Findings from `audit_rust_const_usage.py`

- **81 consts defined, 0 currently used** (pre-migration baseline).
- **37 migration callsites across 13 shapes** ready to rewrite:
  `account` (3), `activity` (3), `actor` (1), `agent` (3),
  `conversation` (1), `folder` (5), `image` (2), `message` (1),
  `person` (7), `skill` (3), `source` (5), `task` (1), `theme` (2).
- **68 consts YAML-only from Rust's POV** — no Rust producer tags
  nodes with them (e.g. `book`, `email`, `flight`). Expected steady
  state: most shapes exist because *skills* produce them; the engine
  never creates those records. The audit doesn't flag these as dead
  YAML — that judgment needs cross-reference against `skills/`.
- **Out of scope**: relation names (`create_link("acted_on")`) and
  field names (`set_val(..., "changedKeys", ...)`). Giving them const
  treatment would start violating §1. Left as-is.
