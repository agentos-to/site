//! # agentos-sdk — the build-time Rust SDK.
//!
//! Codegen output of `python3 platform/codegen/generate.py`. Every shape
//! in `platform/ontology/shapes/*.yaml` becomes a Rust module under
//! [`shapes`] with:
//!
//! - `pub static <NAME>: Lazy<ShapeDef>` — the schema, built once on
//!   first access. Callers pass `&*NAME` to [`agentos_graph::database::
//!   create_shaped_node`] so the schema ships with every write
//!   (shape-unification Phase 1 — "the graph IS the schema, totally").
//! - `pub struct <Name>` — a serde-friendly typed payload. Convenient
//!   for hand-authored seeders + reads; never the engine's primary
//!   contract.
//!
//! ## Engine ↔ SDK link-time pruning
//!
//! The Rust linker strips unreferenced `pub static`s on `cargo build
//! --release` with LTO. In `dev` builds, all SDK statics are linked.
//! The architectural property the engine cares about — *the engine
//! binary has zero compiled-in YAML strings* — holds in both profiles;
//! the symbol-table check (`VOLUME` present, `HEALTH_BIOMARKER`
//! absent) only matches under release+LTO.
//!
//! ## Hand-authored vs generated
//!
//! - `Cargo.toml`, `src/lib.rs` (this file): hand-authored.
//! - `src/shapes/`: every file in here is **generated**.
//!   `src/shapes/mod.rs` lists the modules; `src/shapes/<name>.rs` has
//!   the per-shape constant + struct. Never hand-edit those files;
//!   change the YAML in `platform/ontology/shapes/` and regenerate.

pub mod shapes;
