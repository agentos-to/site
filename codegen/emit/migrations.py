"""Migrations emitter — `ontology/migrations/*.yaml` → Rust const.

Projects the loaded Migration IR into a single Rust file at
`core/crates/contract-generated/src/migrations.rs` containing the
`MigrationOp` enum + `MIGRATIONS: &[Migration]` const. Engine reads
this at runtime to walk the migration chain on `data.import`.
"""
from __future__ import annotations

import json

# Top-of-file Rust we always emit, then the per-migration data follows.
_PRELUDE = '''// DO NOT EDIT — generated from platform/ontology/migrations/ by platform/codegen/.
// Regen: `python3 platform/codegen/generate.py`.
//
// Schema migrations as data. Pinned by `data.export` in every artifact's
// `_meta.schema_version`; read by `data.import` to walk the chain
// `pin → SCHEMA_HASH` and replay the ops.
//
// Migrations are one-way (TerminusDB model). Downgrades are separate
// changesets. The op vocabulary mirrors TerminusDB's reference grammar
// plus three AgentOS-specific variants (rename_link, rename_link_val,
// move_to_event).

#![allow(clippy::all)]

/// W/S classification — whether an op is provably safe to auto-apply
/// under `on_schema_drift: migrate`.
#[derive(Debug, Clone, Copy, PartialEq, Eq)]
pub enum Severity {
    /// Cannot invalidate existing data. Auto-applies.
    Weakening,
    /// May invalidate existing data. Requires explicit ack or a
    /// `DefaultOrError::Default` resolution baked into the op.
    Strengthening,
}

/// Tagged union for narrow_field_type + required add_field defaults.
/// Encoding the choice in the op (rather than as a runtime flag) makes
/// the wrong thing impossible — the migration author has decided.
#[derive(Debug, Clone, Copy)]
pub enum DefaultOrError {
    /// Backfill with this JSON-encoded value.
    Default(&'static str),
    /// Abort the migration on any value that doesn't fit.
    Error,
}

/// One ordered op in a migration. Variants match the YAML op kinds in
/// `ontology/migrations/README.md` (the grammar spec).
#[derive(Debug, Clone)]
pub enum MigrationOp {
    // ─── Weakening (always safe) ─────────────────────────────────────
    AddNodeType { name: &'static str },
    WidenFieldType { shape: &'static str, field: &'static str, from: &'static str, to: &'static str },
    ExtendEnum { shape: &'static str, field: &'static str, add: &'static [&'static str] },
    SetMeta { shape: &'static str, key: &'static str, value: &'static str },
    SetDoc { shape: &'static str, value: &'static str },

    // ─── Parameterized — severity depends on optional/default ────────
    AddField {
        shape: &'static str,
        name: &'static str,
        ty: &'static str,
        optional: bool,
        default: Option<DefaultOrError>,
    },

    // ─── Strengthening (require ack) ─────────────────────────────────
    DropNodeType { name: &'static str, cascade: bool },
    RenameNodeType { from: &'static str, to: &'static str },
    DropField { shape: &'static str, name: &'static str },
    RenameField { shape: &'static str, from: &'static str, to: &'static str },
    NarrowFieldType {
        shape: &'static str,
        field: &'static str,
        from: &'static str,
        to: &'static str,
        default: DefaultOrError,
    },

    // ─── AgentOS-specific (always strengthening) ─────────────────────
    RenameLink { from: &'static str, to: &'static str },
    RenameLinkVal { link: &'static str, from: &'static str, to: &'static str },
    MoveToEvent { shape: &'static str },
    /// Direction-flip + rename. Rewrites every `links` row where
    /// `label = from` to `label = to` with `from_node` and `to_node`
    /// swapped. Used when an active-form label is dropped in favor of
    /// its past-participle canonical (e.g. `owns → owned_by`, where the
    /// canonical reads in the opposite direction).
    FlipLink { from: &'static str, to: &'static str },
}

impl MigrationOp {
    pub fn severity(&self) -> Severity {
        match self {
            MigrationOp::AddNodeType { .. }
            | MigrationOp::WidenFieldType { .. }
            | MigrationOp::ExtendEnum { .. }
            | MigrationOp::SetMeta { .. }
            | MigrationOp::SetDoc { .. } => Severity::Weakening,
            MigrationOp::AddField { optional, default, .. } => {
                if *optional
                    || matches!(default, Some(DefaultOrError::Default(_)))
                {
                    Severity::Weakening
                } else {
                    Severity::Strengthening
                }
            }
            _ => Severity::Strengthening,
        }
    }
}

#[derive(Debug, Clone)]
pub struct Migration {
    /// File basename without `.yaml` — `001-link-typing`, etc.
    pub id: &'static str,
    /// Source ontology hash — `sha256:<64hex>`.
    pub from: &'static str,
    /// Target ontology hash — `sha256:<64hex>`.
    pub to: &'static str,
    /// One-line author description.
    pub doc: &'static str,
    /// Ordered op list. Order is part of the migration's identity.
    pub ops: &'static [MigrationOp],
}

impl Migration {
    /// Migration is strengthening if any op is; otherwise weakening.
    pub fn severity(&self) -> Severity {
        if self.ops.iter().any(|op| op.severity() == Severity::Strengthening) {
            Severity::Strengthening
        } else {
            Severity::Weakening
        }
    }
}

'''


def _rust_str(s: str) -> str:
    """Emit a Rust &'static str literal — JSON encoding handles escapes."""
    return json.dumps(s, ensure_ascii=False)


def _rust_str_slice(items: list) -> str:
    return "&[" + ", ".join(_rust_str(str(s)) for s in items) + "]"


def _emit_default(d) -> str:
    """`{type: Default, value: V}` → `DefaultOrError::Default("<json>")`.
    `{type: Error}` → `DefaultOrError::Error`."""
    if not isinstance(d, dict):
        raise ValueError(f"default must be a mapping; got {d!r}")
    kind = d.get("type")
    if kind == "Error":
        return "DefaultOrError::Error"
    if kind == "Default":
        if "value" not in d:
            raise ValueError("default {type: Default} requires `value`")
        # JSON-encode the value, then Rust-string-literal it.
        json_value = json.dumps(d["value"], ensure_ascii=False, sort_keys=True)
        return f"DefaultOrError::Default({_rust_str(json_value)})"
    raise ValueError(f"default type must be 'Default' or 'Error'; got {kind!r}")


def _emit_op(op) -> str:
    p = op.params
    if op.kind == "add_node_type":
        return f"MigrationOp::AddNodeType {{ name: {_rust_str(p['name'])} }}"
    if op.kind == "widen_field_type":
        return (f"MigrationOp::WidenFieldType {{ shape: {_rust_str(p['shape'])}, "
                f"field: {_rust_str(p['field'])}, from: {_rust_str(p['from'])}, "
                f"to: {_rust_str(p['to'])} }}")
    if op.kind == "extend_enum":
        return (f"MigrationOp::ExtendEnum {{ shape: {_rust_str(p['shape'])}, "
                f"field: {_rust_str(p['field'])}, add: {_rust_str_slice(p['add'])} }}")
    if op.kind == "set_meta":
        return (f"MigrationOp::SetMeta {{ shape: {_rust_str(p['shape'])}, "
                f"key: {_rust_str(p['key'])}, value: {_rust_str(p['value'])} }}")
    if op.kind == "set_doc":
        return (f"MigrationOp::SetDoc {{ shape: {_rust_str(p['shape'])}, "
                f"value: {_rust_str(p['value'])} }}")
    if op.kind == "add_field":
        ty = p["type"]
        optional = bool(p.get("optional", False))
        # `string?` shorthand → optional + non-? type
        if isinstance(ty, str) and ty.endswith("?"):
            ty = ty[:-1]
            optional = True
        default_expr = "None"
        if "default" in p:
            default_expr = f"Some({_emit_default(p['default'])})"
        return (f"MigrationOp::AddField {{ shape: {_rust_str(p['shape'])}, "
                f"name: {_rust_str(p['name'])}, ty: {_rust_str(ty)}, "
                f"optional: {str(optional).lower()}, default: {default_expr} }}")
    if op.kind == "drop_node_type":
        return (f"MigrationOp::DropNodeType {{ name: {_rust_str(p['name'])}, "
                f"cascade: {str(bool(p.get('cascade', False))).lower()} }}")
    if op.kind == "rename_node_type":
        return (f"MigrationOp::RenameNodeType {{ from: {_rust_str(p['from'])}, "
                f"to: {_rust_str(p['to'])} }}")
    if op.kind == "drop_field":
        return (f"MigrationOp::DropField {{ shape: {_rust_str(p['shape'])}, "
                f"name: {_rust_str(p['name'])} }}")
    if op.kind == "rename_field":
        return (f"MigrationOp::RenameField {{ shape: {_rust_str(p['shape'])}, "
                f"from: {_rust_str(p['from'])}, to: {_rust_str(p['to'])} }}")
    if op.kind == "narrow_field_type":
        return (f"MigrationOp::NarrowFieldType {{ shape: {_rust_str(p['shape'])}, "
                f"field: {_rust_str(p['field'])}, from: {_rust_str(p['from'])}, "
                f"to: {_rust_str(p['to'])}, default: {_emit_default(p['default'])} }}")
    if op.kind == "rename_link":
        return (f"MigrationOp::RenameLink {{ from: {_rust_str(p['from'])}, "
                f"to: {_rust_str(p['to'])} }}")
    if op.kind == "rename_link_val":
        return (f"MigrationOp::RenameLinkVal {{ link: {_rust_str(p['link'])}, "
                f"from: {_rust_str(p['from'])}, to: {_rust_str(p['to'])} }}")
    if op.kind == "move_to_event":
        return f"MigrationOp::MoveToEvent {{ shape: {_rust_str(p['shape'])} }}"
    if op.kind == "flip_link":
        return (f"MigrationOp::FlipLink {{ from: {_rust_str(p['from'])}, "
                f"to: {_rust_str(p['to'])} }}")
    raise ValueError(f"unhandled op kind in emitter: {op.kind}")


def _emit_migration(m) -> str:
    ops_lit = ",\n            ".join(_emit_op(op) for op in m.ops)
    return (
        f"    Migration {{\n"
        f"        id: {_rust_str(m.id)},\n"
        f"        from: {_rust_str(m.from_hash)},\n"
        f"        to: {_rust_str(m.to_hash)},\n"
        f"        doc: {_rust_str(m.doc)},\n"
        f"        ops: &[\n"
        f"            {ops_lit},\n"
        f"        ],\n"
        f"    }}"
    )


def emit_migrations(migrations: list) -> str:
    """Render `core/crates/contract-generated/src/migrations.rs`."""
    body = ",\n".join(_emit_migration(m) for m in migrations) if migrations else ""
    return (
        _PRELUDE
        + "/// Every checked-in migration, in file-sorted order. The runtime\n"
        + "/// chain walker selects the path by `from → to` hash, not array index.\n"
        + "pub const MIGRATIONS: &[Migration] = &[\n"
        + (body + ",\n" if body else "")
        + "];\n"
    )
