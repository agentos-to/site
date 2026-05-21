"""Rust emitter — link YAML registry → typed Link enum + per-link LinkVals structs.

Reads the flattened `list[Link]` produced by `links.py` (one record per
storage label) and projects:

  1. `pub enum Cardinality` — closed enum mirroring the YAML `card:` values.

  2. `pub enum Link` — one variant per storage label, PascalCase from
     snake_case. The enum is `#[repr(usize)]`-compatible (variants are
     auto-numbered in source order); the reflection table `LINK_REGISTRY`
     is indexed by variant ordinal.

  3. `LINK_REGISTRY: &[LinkSpec]` — one row per variant, in the SAME
     source order as the enum. Carries label, kinds, cardinality, and
     the optional reverse-accessor name. All accessors on `Link` index
     this table by `*self as usize`.

  4. `link_for_reverse_name(name)` — reverse lookup driven by
     `LinkSpec.reverse_name`. Used by the engine's response processor to
     detect when a returned dict key on a parent shape is the active
     reading of a canonical past-participle link, so the writer can flip
     from/to and store against the canonical.

  5. Per-link `<Camel>LinkVals` structs — one per link with non-empty
     `link_vals`. Each `link_vals` field becomes an `Option<T>` so partial
     writes deserialize. Date/datetime carry as String (consistent with
     the shape emitter).

The whole emitter is order-stable: link records are loaded sorted by name,
LINK_REGISTRY rows are emitted in that order, and Link variants follow the
same order. That keeps generated Rust diff-friendly across re-runs.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Allow `emit/links.py` to import the sibling top-level `links.py` loader.
sys.path.insert(0, str(Path(__file__).parent.parent))
import links as links_loader  # noqa: E402


# Reserved Rust keywords. Variant identifiers are PascalCase from
# snake_case labels — none of our bare-preposition labels (`for`, `in`,
# `on`, `under`, `at`, `with`) collide as PascalCase, but keep the guard
# for future-proofing in case a single-word label like `await` lands.
_RUST_RESERVED = {
    "As", "Break", "Const", "Continue", "Crate", "Dyn", "Else", "Enum",
    "Extern", "False", "Fn", "For", "If", "Impl", "In", "Let", "Loop",
    "Match", "Mod", "Move", "Mut", "Pub", "Ref", "Return", "Self",
    "Static", "Struct", "Super", "Trait", "True", "Type", "Unsafe", "Use",
    "Where", "While", "Async", "Await", "Abstract", "Become", "Box", "Do",
    "Final", "Macro", "Override", "Priv", "Try", "Typeof", "Unsized",
    "Virtual", "Yield", "Union",
}

# PascalCase variant identifiers from snake_case labels. `For`, `In`,
# `On`, `Under` etc. are syntactically fine in Rust as identifiers (only
# lowercase forms are keywords); kept here for clarity and to honor
# the guard above.
_PASCAL_RESERVED = _RUST_RESERVED


def _pascal(snake: str) -> str:
    parts = [p for p in snake.replace("-", "_").split("_") if p]
    out = "".join(w[:1].upper() + w[1:] for w in parts)
    if out in _PASCAL_RESERVED:
        out += "_"
    return out


# YAML link_val type → Rust type. The link_val schema is open-ended
# (`"date | null"`, `"string"`, `"integer"`, `"number"`, `"boolean"`);
# the `| null` modifier is normalized away — every field is Option-wrapped
# regardless, since link_vals are inherently partial-writeable.
_LINK_VAL_TYPES = {
    "string":   "String",
    "text":     "String",
    "url":      "String",
    "date":     "String",
    "datetime": "String",
    "integer":  "i64",
    "number":   "f64",
    "boolean":  "bool",
    "json":     "serde_json::Value",
}


def _link_val_type(spec: str) -> str:
    """Resolve a link_val type spec to a Rust type. Strips `| null` —
    every link_val field is Option-wrapped so partial writes deserialize.
    Returns `serde_json::Value` for unrecognized specs (open-world)."""
    base = spec.split("|")[0].strip()
    return _LINK_VAL_TYPES.get(base, "serde_json::Value")


def _cardinality_variant(card: str) -> str:
    return {
        "one_to_one":   "Cardinality::OneToOne",
        "one_to_many":  "Cardinality::OneToMany",
        "many_to_many": "Cardinality::ManyToMany",
    }.get(card, "Cardinality::ManyToMany")


def _rust_opt_str(v: str | None) -> str:
    if v is None:
        return "None"
    return f'Some("{v}")'


def emit_links(typed_links: list[links_loader.Link]) -> str:
    """Render `core/crates/contract-generated/src/links.rs`."""
    # Stable order. `links_loader.load` already sorts by name, but be
    # defensive — the reflection table must match enum order exactly.
    ls = sorted(typed_links, key=lambda l: l.name)

    lines: list[str] = [
        "// DO NOT EDIT — generated from platform/ontology/links/*.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "//",
        "// One typed `Link` variant per storage label + a reflection",
        "// table (LINK_REGISTRY) carrying kinds, cardinality, and the",
        "// optional reverse-accessor name. Per-link `link_vals` structs",
        "// are emitted for the handful of links with edge-vals (rule 1).",
        "//",
        "// Open-world: callers may still pass arbitrary strings to",
        "// `database::create_link` / `get_links`. The Link enum is the",
        "// typed name when one is known; absence is not an error.",
        "",
        "#![allow(clippy::all)]",
        "#![allow(non_camel_case_types)]",
        "",
        "use serde::{Deserialize, Serialize};",
        "",
        "// ====================================================================",
        "// Cardinality",
        "// ====================================================================",
        "",
        "/// Mirrors the `card:` value on each link YAML. Default is",
        "/// `ManyToMany` when the YAML omits the field.",
        "#[derive(Debug, Clone, Copy, PartialEq, Eq)]",
        "pub enum Cardinality {",
        "    OneToOne,",
        "    OneToMany,",
        "    ManyToMany,",
        "}",
        "",
        "// ====================================================================",
        "// Link enum",
        "// ====================================================================",
        "",
        "/// One variant per storage label, in alphabetical order. The",
        "/// reflection table `LINK_REGISTRY` is indexed by `*self as",
        "/// usize` — adding/removing variants must regenerate both halves.",
        "#[derive(Debug, Clone, Copy, PartialEq, Eq, Hash)]",
        "pub enum Link {",
    ]
    for l in ls:
        lines.append(f"    {_pascal(l.name)},")
    lines += [
        "}",
        "",
        "// ====================================================================",
        "// LinkSpec + LINK_REGISTRY",
        "// ====================================================================",
        "",
        "/// One row of metadata per `Link` variant. Reflection-only —",
        "/// the engine doesn't enforce kind / cardinality at write time,",
        "/// codegen and validators do.",
        "pub struct LinkSpec {",
        "    pub link: Link,",
        "    pub label: &'static str,",
        "    pub from_kind: &'static str,",
        "    pub to_kind: &'static str,",
        "    pub cardinality: Cardinality,",
        "    /// Active-form reading of a past-participle canonical, when",
        "    /// one exists. E.g. `Link::OwnedBy.reverse_name() == Some(\"owns\")`.",
        "    /// Stative `_of`/`_at`/`_in` labels and labels with no clean",
        "    /// active reading leave this `None`.",
        "    pub reverse_name: Option<&'static str>,",
        "}",
        "",
        "/// Row count matches the `Link` enum size exactly. Order is the",
        "/// same alphabetical order, so `LINK_REGISTRY[link as usize]`",
        "/// addresses the right row.",
        "pub static LINK_REGISTRY: &[LinkSpec] = &[",
    ]
    for l in ls:
        variant = _pascal(l.name)
        lines.append(
            f'    LinkSpec {{ link: Link::{variant}, label: "{l.name}", '
            f'from_kind: "{l.from_kind}", to_kind: "{l.to_kind}", '
            f'cardinality: {_cardinality_variant(l.cardinality)}, '
            f'reverse_name: {_rust_opt_str(links_loader.derive_reverse_name(l))} }},'
        )
    lines += [
        "];",
        "",
        "impl Link {",
        "    /// Canonical string label as stored in the `links.label` column.",
        "    pub fn as_str(&self) -> &'static str {",
        "        LINK_REGISTRY[*self as usize].label",
        "    }",
        "    /// Resolve a string label back to its typed variant.",
        "    /// Returns `None` for labels not in the registry (open-world).",
        "    pub fn from_label(label: &str) -> Option<Self> {",
        "        LINK_REGISTRY.iter().find(|s| s.label == label).map(|s| s.link)",
        "    }",
        "    pub fn from_kind(&self) -> &'static str {",
        "        LINK_REGISTRY[*self as usize].from_kind",
        "    }",
        "    pub fn to_kind(&self) -> &'static str {",
        "        LINK_REGISTRY[*self as usize].to_kind",
        "    }",
        "    pub fn cardinality(&self) -> Cardinality {",
        "        LINK_REGISTRY[*self as usize].cardinality",
        "    }",
        "    /// Active-form reading of this canonical, if one was",
        "    /// annotated (`reverse_name:` on the YAML).",
        "    pub fn reverse_name(&self) -> Option<&'static str> {",
        "        LINK_REGISTRY[*self as usize].reverse_name",
        "    }",
        "}",
        "",
        "/// Reverse-accessor lookup. Given an active-form name like",
        "/// `\"owns\"` or `\"replies\"`, returns the canonical link whose",
        "/// `reverse_name` matches — drives the engine's response-processor",
        "/// rewrite path (a returned dict key matching this lookup writes",
        "/// to the canonical storage label with from/to flipped).",
        "pub fn link_for_reverse_name(name: &str) -> Option<&'static LinkSpec> {",
        "    LINK_REGISTRY.iter().find(|s| s.reverse_name == Some(name))",
        "}",
        "",
    ]

    # Per-link link_vals structs.
    lines += [
        "// ====================================================================",
        "// Per-link `link_vals` structs",
        "// ====================================================================",
        "//",
        "// Emitted only for links whose YAML declares a non-empty",
        "// `link_vals` block. Every field is Option-wrapped because",
        "// link_vals are inherently partial-writeable (a writer may set",
        "// `from` today and `to` later when the interval closes).",
        "",
    ]
    for l in ls:
        if not l.link_vals:
            continue
        struct_name = f"{_pascal(l.name)}LinkVals"
        lines += [
            f"/// link_vals for `{l.name}` (from YAML).",
            "#[derive(Debug, Clone, Default, Serialize, Deserialize)]",
            f"pub struct {struct_name} {{",
        ]
        for field_name, type_spec in l.link_vals.items():
            rust_ty = _link_val_type(str(type_spec))
            # Field names in YAML are already snake_case; collisions with
            # Rust keywords (e.g. `type`, `as`) get suffixed.
            ident = field_name
            if ident in {kw.lower() for kw in _RUST_RESERVED}:
                ident += "_"
            lines.append(f"    pub {ident}: Option<{rust_ty}>,")
        lines += ["}", ""]

    return "\n".join(lines)
