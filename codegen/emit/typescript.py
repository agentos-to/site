"""TypeScript emitter — shape YAML → interfaces."""

from __future__ import annotations

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
