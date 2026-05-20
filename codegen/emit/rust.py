"""Rust emitter — shape YAML → ShapeHandle statics + typed structs."""

from __future__ import annotations

from ir import Ontology, Shape, _camel_to_snake, Field

# Reserved Rust keywords that can't be used as identifiers directly.
# (2024 edition list; we prefix with `r#` where needed.)
_RUST_RESERVED = {
    "as", "break", "const", "continue", "crate", "dyn", "else", "enum",
    "extern", "false", "fn", "for", "if", "impl", "in", "let", "loop",
    "match", "mod", "move", "mut", "pub", "ref", "return", "self", "Self",
    "static", "struct", "super", "trait", "true", "type", "unsafe", "use",
    "where", "while", "async", "await", "abstract", "become", "box", "do",
    "final", "macro", "override", "priv", "try", "typeof", "unsized",
    "virtual", "yield", "union",
}


def _rust_ident(shape_name: str) -> str:
    """Convert a shape name to a SCREAMING_SNAKE_CASE Rust identifier."""
    # `git_commit` → `GIT_COMMIT`; `dns_record` → `DNS_RECORD`.
    ident = shape_name.upper().replace("-", "_").replace(".", "_")
    if ident.lower() in _RUST_RESERVED:
        ident = f"{ident}_"
    return ident


# Shape type → Rust type. Mirrors the Go/Swift maps; `date`/`datetime`
# carry as strings, `json` as serde_json::Value, arrays as Vec<T>.
_RUST_TYPES = {
    "string": "String", "text": "String", "url": "String",
    "datetime": "String", "date": "String",
    "integer": "i64", "number": "f64", "boolean": "bool",
    "json": "serde_json::Value",
    "string[]": "Vec<String>", "integer[]": "Vec<i64>",
}


def _rust_field_name(name: str) -> str:
    """YAML field name → snake_case Rust struct field identifier."""
    ident = _camel_to_snake(name.replace(".", "_").replace("-", "_"))
    if ident in _RUST_RESERVED:
        ident += "_"
    return ident


def _rust_serde_camel(ident: str) -> str:
    """Reproduce serde's `rename_all = "camelCase"` transform of a field
    identifier, so the emitter knows when an explicit `#[serde(rename)]`
    is needed to recover the original YAML key (dotted names, etc.)."""
    words = [w for w in ident.split("_") if w]
    if not words:
        return ident
    return words[0] + "".join(w[:1].upper() + w[1:] for w in words[1:])


def _rust_field_type(f: Field, required: bool) -> str:
    """Rust type for a non-relation field. Required (identity / `name`)
    fields get the bare type; every other field is `Option<...>` so a
    node carrying only a subset still deserializes, and absent fields
    serialize to nothing (`ShapeHandle::upsert_struct` skips nulls)."""
    base = _RUST_TYPES.get(f.type, "serde_json::Value")
    return base if required else f"Option<{base}>"


def _emit_rust_struct(s: Shape) -> list[str]:
    """One `#[derive(Serialize, Deserialize)]` struct for a shape — the
    typed payload for `ShapeHandle::upsert_struct`. Relations are edges,
    not vals, so they are omitted; `id` is the node identity, never a val.
    Generated from the field list, so a seeder upserting via this struct
    structurally cannot write a val the shape does not declare."""
    lines: list[str] = []
    if s.leading_comment:
        first = s.leading_comment.split("\n")[0].strip()
        if first:
            lines.append(f"/// {first}")
    lines.append("#[derive(Debug, Clone, Default, Serialize, Deserialize)]")
    lines.append('#[serde(rename_all = "camelCase", default)]')
    lines.append(f"pub struct {s.class_name} {{")
    required = set(s.identity)
    seen: set[str] = set()
    for f in s.fields:
        if f.is_relation or f.name == "id":
            continue
        ident = _rust_field_name(f.name)
        if ident in seen:
            continue  # dedupe post-snake-case collisions
        seen.add(ident)
        is_required = f.name == "name" or f.name in required
        if _rust_serde_camel(ident) != f.name:
            lines.append(f'    #[serde(rename = "{f.name}")]')
        lines.append(f"    pub {ident}: {_rust_field_type(f, is_required)},")
    lines.append("}")
    lines.append("")
    return lines


def emit_rust(onto: Ontology) -> str:
    """Emit, per shape, two artifacts into the engine SDK crate:

      1. a `#[derive(Serialize, Deserialize)]` struct — the shape's node
         fields as a typed Rust value, for `ShapeHandle::upsert_struct`.
         Generated from the field list, so a seeder cannot write a val
         the shape does not declare.
      2. a `pub static` ShapeHandle — name + identity + raw YAML body,
         for lazy upsert. `yaml_body` is the INNER mapping (fields,
         identity, relations, also, ...) — not the outer `shape_name:`
         wrapper — so it round-trips through `serde_yaml`'s `RawShape`,
         byte-identical to Python's `SHAPE_YAMLS[name]`.
    """
    # Stable ordering by shape name.
    shapes_sorted = sorted(onto.shapes, key=lambda s: s.name)

    lines = [
        "// DO NOT EDIT — generated from platform/ontology/shapes/*.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "//",
        "// Per shape, two artifacts:",
        "//   • a struct — the shape's node fields as a typed Rust value,",
        "//     for `ShapeHandle::upsert_struct`. Generated from the field",
        "//     list, so a seeder cannot write an undeclared val.",
        "//   • a `pub static` ShapeHandle — name + identity + raw YAML",
        "//     body, for lazy upsert.",
        "//",
        "// Engine code imports both: `use agentos_contract_generated::shapes::{Theme, THEME};`.",
        "",
        "#![allow(non_upper_case_globals)]",
        "",
        "use agentos_shapes::ShapeHandle;",
        "use serde::{Deserialize, Serialize};",
        "",
        "// ===========================================================",
        "// Shape structs — typed node payloads (ShapeHandle::upsert_struct)",
        "// ===========================================================",
        "//",
        "// Fields are the shape's declared fields plus the universal",
        "// `name`; relations are edges (not vals) and are omitted.",
        "// Identity fields and `name` are required; every other field is",
        "// Option + #[serde(default)], so a node carrying a subset still",
        "// deserializes and absent fields serialize to nothing.",
        "",
    ]

    for s in shapes_sorted:
        lines.extend(_emit_rust_struct(s))

    lines += [
        "// ===========================================================",
        "// Shape handles — name + identity + raw YAML body (lazy upsert)",
        "// ===========================================================",
        "",
    ]

    def _rust_str_slice(items: list[str]) -> str:
        if not items:
            return "&[]"
        body = ", ".join(f'"{s}"' for s in items)
        return f"&[{body}]"

    for s in shapes_sorted:
        if not s.raw_body:
            # Shapes without a serialised body (e.g. loaded from the graph
            # API and failed to round-trip) can't be embedded. Skip — the
            # Rust SDK only emits YAML-sourced shapes, which is the common
            # path.
            continue
        ident = _rust_ident(s.name)
        # Use Rust raw string literal with enough `#` hashes to be unique.
        body = s.raw_body
        hashes = "#"
        while f'"{hashes}' in body:
            hashes += "#"
        lines.append(f"pub static {ident}: ShapeHandle = ShapeHandle {{")
        lines.append(f'    name: "{s.name}",')
        lines.append(f'    yaml_body: r{hashes}"{body}"{hashes},')
        lines.append(f"    identity: {_rust_str_slice(s.identity)},")
        lines.append(f"    identity_any: {_rust_str_slice(s.identity_any)},")
        lines.append("};")
        lines.append("")

    # ===========================================================
    # Display specs — `display:` block per shape (shape-display plan)
    # ===========================================================
    #
    # One closed role vocabulary; per-shape role bindings. The engine's
    # `view::display::resolve_display` reads `SHAPE_DISPLAY[shape]` and
    # projects a `DisplayModel` from a node — same projection as the
    # frontend `resolveDisplay()`. See core/_roadmap/p1/shape-display/plan.md.
    lines += [
        "// ===========================================================",
        "// Display specs — `display:` block per shape (shape-display plan)",
        "// ===========================================================",
        "//",
        "// One closed role vocabulary; per-shape role bindings. The",
        "// engine's `view::display::resolve_display` reads",
        "// `SHAPE_DISPLAY[shape]` and projects a `DisplayModel` from a",
        "// node — same projection as the frontend `resolveDisplay()`.",
        "",
        "/// Per-field clip policy at preview/card density.",
        "/// `Clip` (default) applies the global preview cap; `Full` never",
        "/// clips; `MaxChars(n)` is an explicit per-field cap.",
        "#[derive(Debug, Clone, Copy, PartialEq, Eq)]",
        "pub enum PreviewPolicy {",
        "    Clip,",
        "    Full,",
        "    MaxChars(usize),",
        "}",
        "",
        "/// The five closed roles every theme + renderer projects against.",
        "/// `title` defaults to the `name` field when absent; the other",
        "/// roles are simply absent if unbound.",
        "#[derive(Debug, Clone)]",
        "pub struct Display {",
        "    pub title: Option<&'static str>,",
        "    pub subtitle: Option<&'static str>,",
        "    pub image: Option<&'static str>,",
        "    pub highlights: &'static [&'static str],",
        "    pub body: Option<&'static str>,",
        "    pub preview: &'static [(&'static str, PreviewPolicy)],",
        "    /// Transitive `also:` closure — the chain this shape inherits",
        "    /// from. The resolver uses it to pick the most-specific shape",
        "    /// on a multi-shape node (`shape[]` is alphabetical, not",
        "    /// inheritance order).",
        "    pub also: &'static [&'static str],",
        "}",
        "",
        "/// Linear-scan lookup by shape name. ~100 shapes; binary search",
        "/// would shave microseconds and add ordering ceremony for no win.",
        "pub fn lookup_display(shape: &str) -> Option<&'static Display> {",
        "    SHAPE_DISPLAY.iter().find(|(name, _)| *name == shape).map(|(_, d)| d)",
        "}",
        "",
        "pub static SHAPE_DISPLAY: &[(&'static str, Display)] = &[",
    ]

    def _rust_opt_str(v) -> str:
        if v is None:
            return "None"
        return f'Some("{v}")'

    def _rust_str_array(items: list[str]) -> str:
        if not items:
            return "&[]"
        return "&[" + ", ".join(f'"{s}"' for s in items) + "]"

    def _rust_preview(preview: dict) -> str:
        if not preview:
            return "&[]"
        parts: list[str] = []
        for key, policy in preview.items():
            if policy == "full":
                p = "PreviewPolicy::Full"
            elif policy == "clip":
                p = "PreviewPolicy::Clip"
            elif isinstance(policy, dict) and "max_chars" in policy:
                p = f"PreviewPolicy::MaxChars({int(policy['max_chars'])})"
            else:
                # Unknown policy — skip rather than emit broken Rust.
                continue
            parts.append(f'("{key}", {p})')
        return "&[" + ", ".join(parts) + "]"

    for s in shapes_sorted:
        if not s.display:
            continue
        d = s.display
        lines.append(f'    ("{s.name}", Display {{')
        lines.append(f"        title: {_rust_opt_str(d.title)},")
        lines.append(f"        subtitle: {_rust_opt_str(d.subtitle)},")
        lines.append(f"        image: {_rust_opt_str(d.image)},")
        lines.append(f"        highlights: {_rust_str_array(list(d.highlights))},")
        lines.append(f"        body: {_rust_opt_str(d.body)},")
        lines.append(f"        preview: {_rust_preview(d.preview)},")
        lines.append(f"        also: {_rust_str_array(list(s.ancestors))},")
        lines.append("    }),")
    lines.append("];")
    lines.append("")

    return "\n".join(lines)
