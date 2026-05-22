"""Rust SDK emitter — shape YAML → ShapeDef constants + typed structs at
`platform/sdk/rust/src/shapes/`.

This is the post-shape-unification Rust emitter. The OLD `emit/rust.py`
emitted `core/crates/contract-generated/src/shapes.rs` with `pub static
<NAME>: ShapeHandle = ShapeHandle { ..., yaml_body: r#"..."# }` — YAML
strings baked into the engine binary. That apparatus is deleted; the
engine binary names ZERO shapes in Rust source.

The NEW emit:
- One file per shape at `platform/sdk/rust/src/shapes/<name>.rs`. Each
  file declares `pub static <NAME>: Lazy<ShapeDef>` and `pub struct
  <Name>` (the typed payload).
- `platform/sdk/rust/src/shapes/mod.rs` lists every submodule + the
  lookup tables (Display, ancestors, field order, event types, derived,
  shortcuts).

The engine `use agentos_sdk::shapes::VOLUME` and passes `&*VOLUME` to
`agentos_graph::database::create_shaped_node`. The schema travels with
the write; no `.ensure()`, no `__shape_yaml__` sidecar.
"""

from __future__ import annotations

import json
from pathlib import Path

from ir import Field, Ontology, Shape, _camel_to_snake


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


# YAML shape type → FieldType enum variant.
# `string` and `url` collapse to FieldType::String at the engine level;
# the YAML difference survives for SDK / docs but the storage datatype
# is the same.
_FIELD_TYPE = {
    "string":      "FieldType::String",
    "text":        "FieldType::Text",
    "url":         "FieldType::Url",
    "integer":     "FieldType::Integer",
    "number":      "FieldType::Number",
    "boolean":     "FieldType::Boolean",
    "json":        "FieldType::Json",
    "date":        "FieldType::Date",
    "datetime":    "FieldType::Datetime",
    "string[]":    "FieldType::StringList",
    "integer[]":   "FieldType::IntegerList",
}


# YAML shape type → Rust struct field type. Mirrors the Go/Swift maps;
# `date`/`datetime` carry as strings, `json` as serde_json::Value, arrays
# as Vec<T>.
_RUST_TYPES = {
    "string":      "String",
    "text":        "String",
    "url":         "String",
    "datetime":    "String",
    "date":        "String",
    "integer":     "i64",
    "number":      "f64",
    "boolean":     "bool",
    "json":        "serde_json::Value",
    "string[]":    "Vec<String>",
    "integer[]":   "Vec<i64>",
}


def _module_name(shape_name: str) -> str:
    """Shape name → Rust module name. `git-commit` → `git_commit`."""
    name = shape_name.replace("-", "_").replace(".", "_")
    if name in _RUST_RESERVED:
        name += "_"
    return name


def _const_ident(shape_name: str) -> str:
    """Shape name → SCREAMING_SNAKE Rust identifier. `git-commit` → `GIT_COMMIT`."""
    ident = shape_name.upper().replace("-", "_").replace(".", "_")
    if ident.lower() in _RUST_RESERVED:
        ident += "_"
    return ident


def _rust_field_name(name: str) -> str:
    ident = _camel_to_snake(name.replace(".", "_").replace("-", "_"))
    if ident in _RUST_RESERVED:
        ident += "_"
    return ident


def _rust_serde_camel(ident: str) -> str:
    """Reproduce serde's `rename_all = "camelCase"` transform."""
    words = [w for w in ident.split("_") if w]
    if not words:
        return ident
    return words[0] + "".join(w[:1].upper() + w[1:] for w in words[1:])


def _rust_field_type(f: Field, required: bool) -> str:
    base = _RUST_TYPES.get(f.type, "serde_json::Value")
    return base if required else f"Option<{base}>"


def _rust_str(s: str | None) -> str:
    if s is None:
        return "None"
    escaped = s.replace("\\", "\\\\").replace('"', '\\"')
    return f'Some("{escaped}".into())'


def _emit_field_def(f: Field, is_required: bool) -> str:
    ty = _FIELD_TYPE.get(f.type, "FieldType::Json")
    parts = [
        f'name: "{f.name}".into()',
        f"ty: {ty}",
        "description: None",
    ]
    if is_required:
        parts.append("required: true")
    return "FieldDef { " + ", ".join(parts) + ", ..FieldDef::optional(\"_unused\", FieldType::Json) }"


def _emit_shape_struct(s: Shape) -> list[str]:
    """The serde-friendly typed payload struct (one per shape)."""
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
            continue
        seen.add(ident)
        is_required = f.name == "name" or f.name in required
        if _rust_serde_camel(ident) != f.name:
            lines.append(f'    #[serde(rename = "{f.name}")]')
        lines.append(f"    pub {ident}: {_rust_field_type(f, is_required)},")
    lines.append("}")
    return lines


def _emit_shape_const(s: Shape) -> list[str]:
    """The `pub static <NAME>: Lazy<ShapeDef>` constant."""
    ident = _const_ident(s.name)
    lines: list[str] = []
    lines.append(f"pub static {ident}: Lazy<ShapeDef> = Lazy::new(|| ShapeDef {{")
    lines.append(f'    name: "{s.name}".into(),')
    if s.plural:
        lines.append(f'    plural: Some("{s.plural}".into()),')
    if s.leading_comment:
        first = s.leading_comment.split("\n")[0].strip()
        if first:
            lines.append(f"    description: Some({_rust_string_literal(first)}.into()),")

    # icon — not yet in the IR; pulled from raw YAML if present.
    icon = _extract_icon(s.raw_body)
    if icon:
        lines.append(f"    icon: Some({_rust_string_literal(icon)}.into()),")

    # fields
    field_lines: list[str] = []
    required = set(s.identity)
    seen: set[str] = set()
    for f in s.fields:
        if f.is_relation:
            continue
        if f.name in seen:
            continue
        seen.add(f.name)
        is_required = f.name == "name" or f.name in required
        ty = _FIELD_TYPE.get(f.type, "FieldType::Json")
        if is_required:
            field_lines.append(
                f'        FieldDef::required("{f.name}", {ty}),'
            )
        else:
            field_lines.append(
                f'        FieldDef::optional("{f.name}", {ty}),'
            )
    if field_lines:
        lines.append("    fields: vec![")
        lines.extend(field_lines)
        lines.append("    ],")

    # out (relations) — `out:` block (Phase 2 will read `out:` blocks
    # from YAML directly; for now we project from `own_relations`).
    out_lines: list[str] = []
    for r in s.own_relations:
        is_many = r.is_array or (r.type or "").endswith("[]")
        target = (r.target or "").rstrip("[]")
        card = "Cardinality::Many" if is_many else "Cardinality::One"
        if target:
            out_lines.append(
                f'        EdgeDef {{ label: "{r.name}".into(), to: Some("{target}".into()), from: None, card: {card} }},'
            )
        else:
            out_lines.append(
                f'        EdgeDef {{ label: "{r.name}".into(), to: None, from: None, card: {card} }},'
            )
    if out_lines:
        lines.append("    out: vec![")
        lines.extend(out_lines)
        lines.append("    ],")

    # also (ancestry)
    if s.also:
        also = ", ".join(f'"{a}".into()' for a in s.also)
        lines.append(f"    also: vec![{also}],")

    # identity / identity_any
    if s.identity:
        ident_list = ", ".join(f'"{x}".into()' for x in s.identity)
        lines.append(f"    identity: vec![{ident_list}],")
    if s.identity_any:
        ident_any = ", ".join(f'"{x}".into()' for x in s.identity_any)
        lines.append(f"    identity_any: vec![{ident_any}],")

    # derived (JSON-opaque round-trip)
    if s.derived:
        derived_entries: list[str] = []
        for key, spec in sorted(s.derived.items()):
            json_str = json.dumps(spec).replace("\\", "\\\\").replace('"', '\\"')
            derived_entries.append(
                f'        DerivedBinding {{ key: "{key}".into(), '
                f'spec: serde_json::from_str("{json_str}").unwrap_or(serde_json::Value::Null) }},'
            )
        lines.append("    derived: vec![")
        lines.extend(derived_entries)
        lines.append("    ],")

    # shortcuts
    if s.shortcuts:
        shortcut_entries: list[str] = []
        for key, body in sorted(s.shortcuts.items()):
            if isinstance(body, dict) and "writes" in body:
                writes = str(body["writes"]).replace("\\", "\\\\").replace('"', '\\"')
                shortcut_entries.append(
                    f'        ShortcutDef {{ key: "{key}".into(), writes: "{writes}".into() }},'
                )
        if shortcut_entries:
            lines.append("    shortcuts: vec![")
            lines.extend(shortcut_entries)
            lines.append("    ],")

    # display
    if s.display:
        d = s.display
        any_set = (
            d.title or d.subtitle or d.image or d.body or d.highlights
        )
        if any_set:
            lines.append("    display: Some(DisplaySpec {")
            if d.title:
                lines.append(f'        title: Some("{d.title}".into()),')
            if d.subtitle:
                lines.append(f'        subtitle: Some("{d.subtitle}".into()),')
            if d.image:
                lines.append(f'        image: Some("{d.image}".into()),')
            if d.body:
                lines.append(f'        body: Some("{d.body}".into()),')
            if d.highlights:
                hl = ", ".join(f'"{h}".into()' for h in d.highlights)
                lines.append(f"        highlights: vec![{hl}],")
            lines.append("        ..DisplaySpec::default()")
            lines.append("    }),")

    lines.append("    ..ShapeDef::default()")
    lines.append("});")
    return lines


def _extract_icon(raw_body: str) -> str | None:
    """Pull the `icon:` value from the raw YAML body — parsed via
    `yaml.safe_load` so values like `"\\U0001F516"` materialise as the
    actual codepoint rather than the literal escape sequence."""
    if not raw_body:
        return None
    try:
        import yaml as _yaml
        doc = _yaml.safe_load(raw_body)
    except Exception:
        return None
    if not isinstance(doc, dict):
        return None
    icon = doc.get("icon")
    if icon is None:
        return None
    return str(icon)


def _rust_string_literal(s: str) -> str:
    """Render `s` as a Rust string literal (double-quoted). Escapes
    backslash, double quote, and control codes. Non-ASCII unicode flows
    through as UTF-8 — Rust string literals support arbitrary unicode."""
    out = ['"']
    for ch in s:
        if ch == "\\":
            out.append("\\\\")
        elif ch == '"':
            out.append('\\"')
        elif ch == "\n":
            out.append("\\n")
        elif ch == "\r":
            out.append("\\r")
        elif ch == "\t":
            out.append("\\t")
        else:
            out.append(ch)
    out.append('"')
    return "".join(out)


def _emit_shape_file(s: Shape) -> str:
    """Full source for `platform/sdk/rust/src/shapes/<name>.rs`."""
    lines: list[str] = [
        f"// DO NOT EDIT — generated from platform/ontology/shapes/{s.source_path or s.name + '.yaml'}.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "",
        "use agentos_graph::{",
        "    Cardinality, DerivedBinding, DisplaySpec, EdgeDef, FieldDef, FieldType,",
        "    ShapeDef, ShortcutDef,",
        "};",
        "use once_cell::sync::Lazy;",
        "use serde::{Deserialize, Serialize};",
        "",
    ]
    lines.extend(_emit_shape_struct(s))
    lines.append("")
    lines.extend(_emit_shape_const(s))
    lines.append("")
    return "\n".join(lines)


def _emit_mod_rs(shapes_sorted: list[Shape], onto: Ontology) -> str:
    """The aggregate `mod.rs` — module list + lookup tables (Display,
    ancestors, field order, event types, derived, shortcuts).

    Display + the other tables stay in the SDK because read-side code
    in the engine projects nodes against them. Their entries name all
    shapes — the binary footprint is a few KB of string literals, not
    a YAML wall."""
    lines: list[str] = [
        "// DO NOT EDIT — generated from platform/ontology/shapes/*.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "",
        "#![allow(non_upper_case_globals)]",
        "",
    ]

    # Submodule declarations + re-exports.
    for s in shapes_sorted:
        mod = _module_name(s.name)
        lines.append(f"pub mod {mod};")
    lines.append("")
    for s in shapes_sorted:
        mod = _module_name(s.name)
        cls = s.class_name
        ident = _const_ident(s.name)
        # Re-export the typed struct + const at the `shapes::` level so
        # callers don't have to know the submodule path.
        lines.append(f"pub use {mod}::{{{ident}, {cls}}};")
    lines.append("")

    # Display lookups.
    lines += [
        "// ===========================================================",
        "// Display specs — `display:` block per shape",
        "// ===========================================================",
        "",
        "/// Per-field clip policy at preview/card density.",
        "#[derive(Debug, Clone, Copy, PartialEq, Eq)]",
        "pub enum PreviewPolicy {",
        "    Clip,",
        "    Full,",
        "    MaxChars(usize),",
        "}",
        "",
        "/// The five closed roles every theme + renderer projects against.",
        "#[derive(Debug, Clone)]",
        "pub struct Display {",
        "    pub title: Option<&'static str>,",
        "    pub subtitle: Option<&'static str>,",
        "    pub image: Option<&'static str>,",
        "    pub highlights: &'static [&'static str],",
        "    pub body: Option<&'static str>,",
        "    pub preview: &'static [(&'static str, PreviewPolicy)],",
        "    pub also: &'static [&'static str],",
        "}",
        "",
        "pub fn lookup_display(shape: &str) -> Option<&'static Display> {",
        "    SHAPE_DISPLAY.iter().find(|(name, _)| *name == shape).map(|(_, d)| d)",
        "}",
        "",
        "pub static SHAPE_DISPLAY: &[(&'static str, Display)] = &[",
    ]

    def _opt(v) -> str:
        return "None" if v is None else f'Some("{v}")'

    def _str_array(items) -> str:
        if not items:
            return "&[]"
        return "&[" + ", ".join(f'"{s}"' for s in items) + "]"

    def _preview(preview: dict) -> str:
        if not preview:
            return "&[]"
        parts = []
        for key, policy in preview.items():
            if policy == "full":
                p = "PreviewPolicy::Full"
            elif policy == "clip":
                p = "PreviewPolicy::Clip"
            elif isinstance(policy, dict) and "max_chars" in policy:
                p = f"PreviewPolicy::MaxChars({int(policy['max_chars'])})"
            else:
                continue
            parts.append(f'("{key}", {p})')
        return "&[" + ", ".join(parts) + "]"

    for s in shapes_sorted:
        if not s.display:
            continue
        d = s.display
        lines.append(f'    ("{s.name}", Display {{')
        lines.append(f"        title: {_opt(d.title)},")
        lines.append(f"        subtitle: {_opt(d.subtitle)},")
        lines.append(f"        image: {_opt(d.image)},")
        lines.append(f"        highlights: {_str_array(list(d.highlights))},")
        lines.append(f"        body: {_opt(d.body)},")
        lines.append(f"        preview: {_preview(d.preview)},")
        lines.append(f"        also: {_str_array(list(s.ancestors))},")
        lines.append("    }),")
    lines.append("];")
    lines.append("")

    # Field order.
    lines += [
        "// ===========================================================",
        "// Field order — YAML declaration order per shape",
        "// ===========================================================",
        "",
        "pub fn lookup_field_order(shape: &str) -> &'static [&'static str] {",
        "    SHAPE_FIELD_ORDER.iter().find(|(name, _)| *name == shape).map(|(_, o)| *o).unwrap_or(&[])",
        "}",
        "",
        "pub static SHAPE_FIELD_ORDER: &[(&'static str, &'static [&'static str])] = &[",
    ]
    for s in shapes_sorted:
        if not s.field_order:
            continue
        lines.append(f'    ("{s.name}", {_str_array(list(s.field_order))}),')
    lines.append("];")
    lines.append("")

    # Ancestors.
    lines += [
        "// ===========================================================",
        "// Ancestors — transitive `also:` closure per shape",
        "// ===========================================================",
        "",
        "pub fn lookup_ancestors(shape: &str) -> &'static [&'static str] {",
        "    SHAPE_ANCESTORS.iter().find(|(n, _)| *n == shape).map(|(_, a)| *a).unwrap_or(&[])",
        "}",
        "",
        "pub static SHAPE_ANCESTORS: &[(&'static str, &'static [&'static str])] = &[",
    ]
    for s in shapes_sorted:
        if not s.ancestors:
            continue
        lines.append(f'    ("{s.name}", {_str_array(list(s.ancestors))}),')
    lines.append("];")
    lines.append("")

    # Event types.
    lines += [
        "// ===========================================================",
        "// Event types — shapes whose `also:` chain includes `event`",
        "// ===========================================================",
        "",
        f"pub static EVENT_TYPES: &[&'static str] = {_str_array(onto.event_shape_names())};",
        "",
    ]

    # Derived / shortcuts JSON blobs.
    derived_obj = {s.name: s.derived for s in shapes_sorted if s.derived}
    shortcuts_obj = {s.name: s.shortcuts for s in shapes_sorted if s.shortcuts}
    lines += [
        "// ===========================================================",
        "// Derived bindings — per-shape `derived:` block as JSON",
        "// ===========================================================",
        "",
        f"pub static SHAPE_DERIVED_JSON: &str = r#\"{json.dumps(derived_obj)}\"#;",
        "",
        "// ===========================================================",
        "// Shortcuts — per-shape `shortcuts:` block as JSON",
        "// ===========================================================",
        "",
        f"pub static SHAPE_SHORTCUTS_JSON: &str = r#\"{json.dumps(shortcuts_obj)}\"#;",
        "",
    ]

    return "\n".join(lines)


def write_rust_sdk(onto: Ontology, root: Path) -> list[Path]:
    """Emit the full `platform/sdk/rust/src/shapes/` tree.

    `root` is `platform/sdk/rust/src/shapes/`. Writes one file per shape
    plus `mod.rs`. Returns the list of paths written (caller dedupes
    against existing for --check).
    """
    shapes_sorted = sorted(onto.shapes, key=lambda s: s.name)
    root.mkdir(parents=True, exist_ok=True)

    written: list[Path] = []
    seen_paths: set[Path] = set()
    for s in shapes_sorted:
        path = root / f"{_module_name(s.name)}.rs"
        path.write_text(_emit_shape_file(s))
        written.append(path)
        seen_paths.add(path.resolve())

    mod_path = root / "mod.rs"
    mod_path.write_text(_emit_mod_rs(shapes_sorted, onto))
    written.append(mod_path)
    seen_paths.add(mod_path.resolve())

    # Sweep stale shape files (a shape was removed from the YAML set).
    for existing in root.glob("*.rs"):
        if existing.resolve() not in seen_paths:
            existing.unlink()

    return written
