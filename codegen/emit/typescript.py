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
        "    labels?: Record<string, string>; // per-field display-label overrides for the preview card (e.g. {price: 'premium'}); humanized field name is the default",
        "    icon?: string;        // Material Symbols glyph name (outlined) for this shape's face",
        "    iconFrom?: string;    // enum field whose value IS the per-record icon slot (resolved engine-side)",
        "    /** The preview card's header composition — a bound portrait field",
        "     *  whose shape/size are a CLOSED enum resolving to theme tokens (never",
        "     *  raw px). A shape with `media` renders a contact-card header; one",
        "     *  without gets the icon + subtitle header. */",
        '    media?: { field: string; shape?: "circle" | "square" | "rounded"; size?: "sm" | "md" | "lg" };',
        "    lines?: string[];     // promoted header lines under the title (what `highlights` becomes for an image-bearing card)",
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
        if s.display.labels:     d["labels"]     = dict(s.display.labels)
        if s.display.icon:       d["icon"]       = s.display.icon
        if s.display.icon_from:  d["iconFrom"]   = s.display.icon_from
        if s.display.media:
            media = {"field": s.display.media.field}
            if s.display.media.shape: media["shape"] = s.display.media.shape
            if s.display.media.size:  media["size"]  = s.display.media.size
            d["media"] = media
        if s.display.lines:      d["lines"]      = list(s.display.lines)
        d["also"] = list(s.ancestors)
        # JSON ensures double-quoted keys/strings (valid TS object literal).
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(d)},")
    lines.append("};")
    lines.append("")

    # SHAPE_PLURAL — the authored `plural:` per shape. The display label for
    # a shape folder/group is the AUTHORED plural sentence-cased, never a
    # hand-rolled pluralizer (which mangles `settings` → `settingses`). One
    # source of truth: the ontology YAML.
    lines.extend([
        "// ─── Plural per shape — the authored `plural:` from the ontology ────────",
        "// Shape folders/group headers render this sentence-cased. Never re-derive",
        "// a plural in code — `settings` is its own plural, the YAML knows it.",
        "",
        "export const SHAPE_PLURAL: Record<string, string> = {",
    ])
    for s in shapes:
        if not s.plural:
            continue
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(s.plural)},")
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

    # SHAPE_IDENTITY — the `identity:` field list per shape. The preview card
    # renders these rows in bold — they are what uniquely names the record
    # (derived from the contract, never a hand-picked "important" flag). A
    # relation in the list (e.g. `underwritten_by`) bolds its relationship row.
    lines.extend([
        "// ─── Identity per shape — the `identity:` field list ───────────────────",
        "// The preview card bolds these rows — what uniquely names the record,",
        "// derived from the contract (never a hand-picked \"important\" flag).",
        "",
        "export const SHAPE_IDENTITY: Record<string, readonly string[]> = {",
    ])
    for s in shapes:
        ident = list(s.identity) + [f for f in s.identity_any if f not in s.identity]
        if not ident:
            continue
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(ident)},")
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
    if f.enum:
        return " | ".join(json.dumps(v) for v in f.enum)
    return _TS_TYPES.get(f.type, "unknown")
