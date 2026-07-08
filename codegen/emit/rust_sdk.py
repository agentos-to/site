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
        if f.description or f.enum:
            # Full struct literal — the `required`/`optional` constructors
            # hardcode `description: None` + empty `enum_values`, so a field
            # carrying guidance or a closed value set needs every slot spelled
            # out.
            req = "true" if is_required else "false"
            desc = (
                f"Some({_rust_string_literal(f.description)}.into())"
                if f.description else "None"
            )
            enum_vec = (
                "vec![" + ", ".join(f'"{v}".into()' for v in f.enum) + "]"
                if f.enum else "vec![]"
            )
            field_lines.append(
                f'        FieldDef {{ name: "{f.name}".into(), ty: {ty}, '
                f"description: {desc}, required: {req}, enum_values: {enum_vec} }},"
            )
        elif is_required:
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

    # also (ancestry)
    if s.also:
        also = ", ".join(f'"{a}".into()' for a in s.also)
        lines.append(f"    also: vec![{also}],")

    # timed (intrinsic time category — `self` = self-timed measurement)
    if s.timed:
        lines.append(f'    timed: Some("{s.timed}".into()),')

    # account_from (the field naming the account a record arrived on —
    # extraction resolves it and stamps `record —arrived_via→ account`)
    if s.account_from:
        lines.append(f'    account_from: Some("{s.account_from}".into()),')

    # membership ({service, key}) — how this shape's folder membership is
    # answered (a brokered service's mirror-lists); the data.list resolver reads
    # it here (directives live in the compiled registry, not the graph node).
    if s.membership:
        _svc = s.membership.get("service", "")
        _key = s.membership.get("key", "")
        lines.append(
            f'    membership: Some(agentos_graph::MembershipDef {{ '
            f'service: "{_svc}".into(), key: "{_key}".into() }}),'
        )

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
                if body.get("inverse"):
                    inv = str(body["inverse"]).replace("\\", "\\\\").replace('"', '\\"')
                    inverse = f'Some("{inv}".into())'
                else:
                    inverse = "None"
                shortcut_entries.append(
                    f'        ShortcutDef {{ key: "{key}".into(), '
                    f'writes: "{writes}".into(), inverse: {inverse} }},'
                )
        if shortcut_entries:
            lines.append("    shortcuts: vec![")
            lines.extend(shortcut_entries)
            lines.append("    ],")

    # display
    if s.display:
        d = s.display
        any_set = (
            d.title or d.subtitle or d.image or d.body or d.mono or d.highlights
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
            if d.mono:
                lines.append(f'        mono: Some("{d.mono}".into()),')
            if d.highlights:
                hl = ", ".join(f'"{h}".into()' for h in d.highlights)
                lines.append(f"        highlights: vec![{hl}],")
            lines.append("        ..DisplaySpec::default()")
            lines.append("    }),")

    # groups — ontology-declared card/detail sections.
    if s.groups:
        lines.append("    groups: vec![")
        for name, fields in s.groups:
            field_list = ", ".join(f'{_rust_string_literal(field)}.into()' for field in fields)
            lines.append(
                f"        FieldGroupDef {{ name: {_rust_string_literal(name)}.into(), fields: vec![{field_list}] }},"
            )
        lines.append("    ],")

    # prior_art — external standards this shape aligns with.
    if s.prior_art:
        lines.append("    prior_art: vec![")
        for entry in s.prior_art:
            source = _rust_string_literal(str(entry.get("source", "")))
            url = str(entry.get("url", ""))
            notes = str(entry.get("notes", ""))
            url_expr = f"Some({_rust_string_literal(url)}.into())" if url else "None"
            notes_expr = f"Some({_rust_string_literal(notes)}.into())" if notes else "None"
            lines.append(
                f"        PriorArtDef {{ source: {source}.into(), url: {url_expr}, notes: {notes_expr} }},"
            )
        lines.append("    ],")

    # prefs_schemas (JSON-opaque) — shape-level pref vocabulary
    # (`namespace → entries[]`). Settings reads it off the shape-def
    # node. Carried as `serde_json::Value` because each entry is a
    # discriminated union over `kind` (select/number/boolean/color)
    # with widely-varying field sets; typing it would freeze the
    # vocabulary at the SDK boundary.
    if s.prefs_schemas:
        json_str = json.dumps(s.prefs_schemas).replace("\\", "\\\\").replace('"', '\\"')
        lines.append(
            f'    prefs_schemas: serde_json::from_str("{json_str}").ok(),'
        )

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
    """Full source for `platform/sdk/rust/src/shapes/<name>.rs`.

    Every shape file pulls its types from the curated `sdk_prelude`
    module in `mod.rs` — one canonical import line, no per-file symbol
    list, no namespace leakage from mod.rs's internal lookup machinery
    (PreviewPolicy, Display, lookup_*, etc). Standard Rust prelude
    pattern — same as `serde::prelude`, `clap::prelude`, `bevy::prelude::*`.
    """
    lines: list[str] = [
        f"// DO NOT EDIT — generated from platform/ontology/shapes/{s.source_path or s.name + '.yaml'}.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "",
        "use super::sdk_prelude::*;",
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
    # Derive the prelude's contents from the ontology itself — re-export
    # only the agentos_graph symbols at least one shape actually
    # references, so adding/removing a YAML block (display, derived,
    # shortcuts) keeps the prelude honest with zero `unused import`
    # warnings. FieldDef + FieldType + ShapeDef are universal (every
    # shape declares fields).
    prelude_syms: list[str] = ["FieldDef", "FieldType", "ShapeDef"]
    if any(s.display for s in shapes_sorted):
        prelude_syms.append("DisplaySpec")
    if any(s.groups for s in shapes_sorted):
        prelude_syms.append("FieldGroupDef")
    if any(s.prior_art for s in shapes_sorted):
        prelude_syms.append("PriorArtDef")
    if any(s.derived for s in shapes_sorted):
        prelude_syms.append("DerivedBinding")
    if any(s.shortcuts for s in shapes_sorted):
        prelude_syms.append("ShortcutDef")
    prelude_syms.sort()

    lines: list[str] = [
        "// DO NOT EDIT — generated from platform/ontology/shapes/*.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "",
        "#![allow(non_upper_case_globals)]",
        "",
        "// Curated prelude for the generated shape files. Every shape file does",
        "// `use super::sdk_prelude::*;` — one canonical import line, no per-file",
        "// symbol list, no namespace leakage from mod.rs's own lookup machinery",
        "// below (PreviewPolicy, Display, lookup_*, etc). Standard Rust idiom:",
        "// `serde::prelude`, `clap::prelude`, `bevy::prelude::*` all work this way.",
        "//",
        "// Symbol set is derived from the ontology — only the types at least one",
        "// shape references are re-exported, so an unused-import warning here is",
        "// impossible by construction.",
        "pub(crate) mod sdk_prelude {",
        "    pub(crate) use agentos_graph::{",
        f"        {', '.join(prelude_syms)},",
        "    };",
        "    pub(crate) use once_cell::sync::Lazy;",
        "    pub(crate) use serde::{Deserialize, Serialize};",
        "}",
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

    # Def lookup by name — the engine's fallback when a write touches a
    # shape the wire carried no `__shape_def__` for (e.g. a nested child
    # entity whose shape was never a top-level `@returns`). The compiled
    # contract IS the def.
    lines += [
        "// ===========================================================",
        "// Def lookup — full compiled ShapeDef by shape name",
        "// ===========================================================",
        "",
        "pub fn lookup_def(shape: &str) -> Option<&'static agentos_graph::ShapeDef> {",
        "    match shape {",
    ]
    for s in shapes_sorted:
        lines.append(f'        "{s.name}" => Some(&{_const_ident(s.name)}),')
    lines += [
        "        _ => None,",
        "    }",
        "}",
        "",
    ]

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
        "/// The preview card's header composition — a bound portrait field whose",
        "/// shape/size are a CLOSED enum resolving to theme tokens (never raw px).",
        "#[derive(Debug, Clone)]",
        "pub struct Media {",
        "    pub field: &'static str,",
        "    pub shape: Option<&'static str>,",
        "    pub size: Option<&'static str>,",
        "}",
        "",
        "/// The closed roles every theme + renderer projects against.",
        "#[derive(Debug, Clone)]",
        "pub struct Display {",
        "    pub title: Option<&'static str>,",
        "    pub subtitle: Option<&'static str>,",
        "    pub image: Option<&'static str>,",
        "    pub highlights: &'static [&'static str],",
        "    pub body: Option<&'static str>,",
        "    pub mono: Option<&'static str>,",
        "    pub preview: &'static [(&'static str, PreviewPolicy)],",
        "    pub also: &'static [&'static str],",
        "    /// Material glyph for this shape's face (`display.icon`). The icon",
        "    /// resolver picks the most-specific shape carrying one; its slug is",
        "    /// the stamped `iconRole`, and the floor maps slug → this glyph.",
        "    pub icon: Option<&'static str>,",
        "    /// `display.iconFrom` — an enum field whose value IS the per-record",
        "    /// icon slot (device.formFactor → router/tv/…). Resolved engine-side.",
        "    pub icon_from: Option<&'static str>,",
        "    /// `display.labels` — per-field display-label overrides for the preview",
        "    /// card (e.g. `price` → \"premium\"); the humanized field name is the default.",
        "    pub labels: &'static [(&'static str, &'static str)],",
        "    /// `display.media` — the contact-card portrait binding + shape/size enums.",
        "    pub media: Option<Media>,",
        "    /// `display.lines` — promoted header lines under the title.",
        "    pub lines: &'static [&'static str],",
        "}",
        "",
        "pub fn lookup_display(shape: &str) -> Option<&'static Display> {",
        "    SHAPE_DISPLAY.iter().find(|(name, _)| *name == shape).map(|(_, d)| d)",
        "}",
        "",
        "/// Per-shape display-label override (`display.labels`) — the humanized field",
        "/// name is the default when a field is absent from the returned slice.",
        "pub fn lookup_label(shape: &str, field: &str) -> Option<&'static str> {",
        "    lookup_display(shape)",
        "        .and_then(|d| d.labels.iter().find(|(k, _)| *k == field).map(|(_, v)| *v))",
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

    def _label_array(labels: dict) -> str:
        if not labels:
            return "&[]"
        return "&[" + ", ".join(f'("{k}", "{v}")' for k, v in labels.items()) + "]"

    def _media(m) -> str:
        if not m:
            return "None"
        return f"Some(Media {{ field: \"{m.field}\", shape: {_opt(m.shape)}, size: {_opt(m.size)} }})"

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
        lines.append(f"        mono: {_opt(d.mono)},")
        lines.append(f"        preview: {_preview(d.preview)},")
        lines.append(f"        also: {_str_array(list(s.ancestors))},")
        lines.append(f"        icon: {_opt(d.icon)},")
        lines.append(f"        icon_from: {_opt(d.icon_from)},")
        lines.append(f"        labels: {_label_array(d.labels)},")
        lines.append(f"        media: {_media(d.media)},")
        lines.append(f"        lines: {_str_array(list(d.lines))},")
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

    # Identity — the `identity:` field list per shape. The preview card
    # (both renderers) bolds these rows: what uniquely names the record,
    # derived from the contract. A relation in the list (e.g.
    # `underwritten_by`) bolds its relationship row, not a field row.
    lines += [
        "// ===========================================================",
        "// Identity — the `identity:` field list per shape",
        "// ===========================================================",
        "",
        "pub fn lookup_identity(shape: &str) -> &'static [&'static str] {",
        "    SHAPE_IDENTITY.iter().find(|(name, _)| *name == shape).map(|(_, i)| *i).unwrap_or(&[])",
        "}",
        "",
        "pub static SHAPE_IDENTITY: &[(&'static str, &'static [&'static str])] = &[",
    ]
    for s in shapes_sorted:
        ident = list(s.identity) + [f for f in s.identity_any if f not in s.identity]
        if not ident:
            continue
        lines.append(f'    ("{s.name}", {_str_array(ident)}),')
    lines.append("];")
    lines.append("")

    # Plurals.
    lines += [
        "// ===========================================================",
        "// Plurals — the ontology's `plural:` per shape",
        "// ===========================================================",
        "",
        "pub fn lookup_plural(shape: &str) -> Option<&'static str> {",
        "    SHAPE_PLURALS.iter().find(|(name, _)| *name == shape).map(|(_, p)| *p)",
        "}",
        "",
        "pub static SHAPE_PLURALS: &[(&'static str, &'static str)] = &[",
    ]
    for s in shapes_sorted:
        if not s.plural:
            continue
        lines.append(f'    ("{s.name}", "{s.plural}"),')
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
