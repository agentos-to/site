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
        "// `DisplayModel` from a node. See core/_roadmap/p1/shape-display/plan.md.",
        "",
        "export interface Display {",
        "    title?: string;       // → a field (default: `name`)",
        "    subtitle?: string;    // → a field or relation",
        "    image?: string;       // → a field (url) or a relation → node.image",
        "    highlights?: string[];// 0..4 fields/relations",
        "    body?: string;        // detail-only: one long text field",
        '    preview?: Record<string, "clip" | "full" | { max_chars: number }>;',
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
        if s.display.preview:    d["preview"]    = dict(s.display.preview)
        # JSON ensures double-quoted keys/strings (valid TS object literal).
        lines.append(f"    {json.dumps(s.name)}: {json.dumps(d)},")
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
