"""TypeScript emitter — shape YAML → interfaces + display spec map."""

from __future__ import annotations

import json

from ir import Field, Ontology, _to_camel, to_class_name

_TS_TYPES = {
    "string": "string", "text": "string", "integer": "number",
    "number": "number", "boolean": "boolean", "datetime": "string",
    "url": "string", "json": "unknown",
    "string[]": "string[]", "integer[]": "number[]",
}


def emit_typescript(onto: Ontology) -> str:
    shapes = onto.shapes
    lines = [
        "// Auto-generated from shape YAML — do not edit.",
        f"// Generated from {len(shapes)} shapes.",
        "// Regenerate with: python generate.py --lang typescript",
        "",
    ]

    for s in shapes:
        lines.append(f"export interface {s.class_name} {{")
        for f in s.fields:
            name = _ts_field_name(f.name)
            ty = _ts_type(f)
            lines.append(f"    {name}?: {ty};")
        lines.append("}")
        lines.append("")

    # --- Display spec (shape-display plan) -----------------------------------
    # One closed role vocabulary; per-shape role bindings. The frontend's
    # `resolveDisplay()` reads `SHAPE_DISPLAY[shape]` and projects a
    # `DisplayModel` from a node + the bindings.
    lines.extend([
        "// ─── Display spec — `display:` block per shape ──────────────────────────",
        "// The closed role vocabulary every theme renders against; the frontend's",
        "// `resolveDisplay()` reads `SHAPE_DISPLAY[shape]` and projects a",
        "// `DisplayModel` from a node. See core/_product/p1/shape-display/plan.md.",
        "",
        "export interface Display {",
        "    title?: string;       // → a field (default: `name`)",
        "    subtitle?: string;    // → a field or relation",
        "    image?: string;       // → a field (url) or a relation → node.image",
        "    highlights?: string[];// 0..4 fields/relations",
        "    body?: string;        // detail-only: one long text field",
        "    mono?: string;        // → a preformatted text field (QR block, ASCII",
        "                          //   art): monospace, no re-wrap, keep geometry",
        '    preview?: Record<string, "clip" | "full" | { max_chars: number }>;',
        "    icon?: string;        // Material Symbols glyph name (outlined) for this shape's face",
        "    /** Transitive `also:` closure — the chain this shape inherits from.",
        "     *  The resolver uses it to pick the most-specific shape on a",
        "     *  multi-shape node (`shape[]` is alphabetical, not inheritance). */",
        "    also: string[];",
        "}",
        "",
        "export const SHAPE_DISPLAY: Record<string, Display> = {",
    ])
    for s in shapes:
        if not s.display:
            continue
        d = {}
        if s.display.title:      d["title"]      = s.display.title
        if s.display.subtitle:   d["subtitle"]   = s.display.subtitle
        if s.display.image:      d["image"]      = s.display.image
        if s.display.highlights: d["highlights"] = list(s.display.highlights)
        if s.display.body:       d["body"]       = s.display.body
        if s.display.mono:       d["mono"]       = s.display.mono
        if s.display.preview:    d["preview"]    = dict(s.display.preview)
        if s.display.icon:       d["icon"]       = s.display.icon
        d["also"] = list(s.ancestors)
        # JSON ensures double-quoted keys/strings (valid TS object literal).
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(d)},")
    lines.append("};")
    lines.append("")

    # SHAPE_FIELD_ORDER — YAML declaration order per shape, so detail
    # panels render rows in the author's order (e.g. given → middle →
    # family on person, not the alphabetised graph order).
    lines.extend([
        "// ─── Field order — YAML declaration order per shape ────────────────────",
        "// Detail panels iterate this list and look up `node.vals[key]`. Own",
        "// fields first, then inherited via `also:` deduped.",
        "",
        "export const SHAPE_FIELD_ORDER: Record<string, readonly string[]> = {",
    ])
    for s in shapes:
        if not s.field_order:
            continue
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(list(s.field_order))},")
    lines.append("};")
    lines.append("")

    # SHAPE_FIELD_GROUPS — the ontology `groups:` block: ordered property
    # sections for the detail pane / card. The pane renders these sections
    # in order, each listing the named fields the node actually carries;
    # any val no section names trails in a default "Other" section.
    lines.extend([
        "// ─── Property sections per shape — ontology `groups:` block ─────────────",
        "// The detail pane (NodeMetadata) renders these sections in order; the",
        "// section name renders verbatim. Vals no section names fall to \"Other\".",
        "",
        "export interface FieldGroup { name: string; fields: readonly string[] }",
        "export const SHAPE_FIELD_GROUPS: Record<string, readonly FieldGroup[]> = {",
    ])
    for s in shapes:
        if not s.groups:
            continue
        secs = [{"name": name, "fields": fields} for name, fields in s.groups]
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(secs)},")
    lines.append("};")
    lines.append("")

    # EVENT_TYPES — every shape whose `also:` chain includes `event` (plus
    # `event` itself). Derived from the shape graph — the shape IS the type.
    lines.extend([
        "// ─── Event types — shapes whose `also:` chain includes `event` ──────────",
        "// Derived from the shape graph — the shape IS the type.",
        "",
        "export const EVENT_TYPES: readonly string[] = [",
    ])
    for name in onto.event_shape_names():
        lines.append(f"    {json.dumps(name)},")
    lines.append("] as const;")
    lines.append("")

    # SHAPE_DERIVED + SHAPE_SHORTCUTS — see python emitter / ir.Shape for
    # binding grammar. The TS resolver mirrors the Rust one (Phase 3).
    lines.extend([
        "// ─── Derived bindings per shape — read-side resolver input ──────────────",
        "// Binding grammar: {find, where, where_link, is, get} | {latest: [...]} | dotted string.",
        "",
        "export const SHAPE_DERIVED: Record<string, Record<string, unknown>> = {",
    ])
    for s in shapes:
        if not s.derived:
            continue
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(s.derived)},")
    lines.append("};")
    lines.append("")

    lines.extend([
        "// ─── Shortcuts per shape — write-side flat-create expansion table ───────",
        "// Each entry: flat_key -> {writes: <link>[is=<shape>].<field>}",
        "",
        "export const SHAPE_SHORTCUTS: Record<string, Record<string, unknown>> = {",
    ])
    for s in shapes:
        if not s.shortcuts:
            continue
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(s.shortcuts)},")
    lines.append("};")
    lines.append("")

    return "\n".join(lines)


def _ts_field_name(name: str) -> str:
    if "." in name:
        return _to_camel(name.replace(".", "_"))
    return _to_camel(name)


def _ts_type(f: Field) -> str:
    if f.is_relation:
        if f.target == "node":
            return "unknown[]" if f.is_array else "unknown"
        cls = to_class_name(f.target)
        return f"{cls}[]" if f.is_array else cls
    return _TS_TYPES.get(f.type, "unknown")
