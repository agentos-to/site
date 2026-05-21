"""Python emitter — shape YAML → TypedDict classes + SDK sidecars."""

from __future__ import annotations

from ir import Field, Ontology, Shape, to_class_name

_PY_TYPES = {
    "string": "str", "text": "str", "integer": "int", "number": "float",
    "boolean": "bool", "datetime": "str", "url": "str", "json": "Any",
    "string[]": "list[str]", "integer[]": "list[int]",
}

_PY_RESERVED = {
    "from", "import", "class", "return", "def", "if", "else", "for",
    "while", "with", "as", "try", "except", "finally", "raise", "pass",
    "break", "continue", "and", "or", "not", "in", "is", "lambda",
    "global", "nonlocal", "yield", "assert", "del", "True", "False", "None",
}


def emit_python(onto: Ontology) -> str:
    shapes = onto.shapes
    lines = [
        '"""Auto-generated TypedDict classes from shape YAML — do not edit.',
        "",
        f"Generated from {len(shapes)} shapes.",
        "Regenerate with: python generate.py --lang python",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, TypedDict",
        "",
    ]

    for s in shapes:
        lines.append(f"class {s.class_name}(TypedDict, total=False):")
        for f in s.fields:
            safe = _py_field_name(f.name)
            comment = f"  # {f.name}" if safe != f.name else ""
            ty = _py_type(f, s)
            lines.append(f"    {safe}: {ty}{comment}")
        lines.append("")
        lines.append("")

    # SHAPE_YAMLS: raw YAML body per shape. The skill worker attaches the
    # matching entry as `__shape_yaml__` on every @returns(shape) response so
    # the Rust engine can upsert the definition on the graph with a single
    # byte-compare — no reparse, no field-by-field merger. The body matches
    # what the Rust ShapeHandle carries via include_str!, so SHAPE_YAMLS is
    # the Python mirror of the contract crate's `shapes` module.
    lines.append("# Raw YAML bodies — consumed by the skill worker to attach")
    lines.append("# `__shape_yaml__` on every @returns(shape) response.")
    lines.append("SHAPE_YAMLS: dict[str, str] = {")
    for s in shapes:
        if not s.raw_body:
            continue
        lines.append(f"    {s.name!r}: {s.raw_body!r},")
    lines.append("}")
    lines.append("")

    # Identity sidecars — the skill worker attaches these as
    # `__shape_identity__` and `__shape_identity_any__` next to
    # `__shape_yaml__` on every @returns(shape) response, so the Rust
    # engine can drive identity-based upserts without parsing YAML or
    # consulting any in-process registry.
    lines.append("# Identity keys per shape — sidecars for the skill worker.")
    lines.append("SHAPE_IDENTITIES: dict[str, list[str]] = {")
    for s in shapes:
        if not s.identity:
            continue
        lines.append(f"    {s.name!r}: {list(s.identity)!r},")
    lines.append("}")
    lines.append("")
    lines.append("SHAPE_IDENTITIES_ANY: dict[str, list[str]] = {")
    for s in shapes:
        if not s.identity_any:
            continue
        lines.append(f"    {s.name!r}: {list(s.identity_any)!r},")
    lines.append("}")
    lines.append("")

    # SHAPE_FIELD_ORDER — YAML declaration order per shape (own fields
    # first, then inherited via `also:` deduped). Detail panels render
    # fields in this order so the author's editorial decision (e.g.
    # given → middle → family on person) survives end to end.
    lines.append("# YAML declaration order per shape — author order is meaning.")
    lines.append("SHAPE_FIELD_ORDER: dict[str, list[str]] = {")
    for s in shapes:
        if not s.field_order:
            continue
        lines.append(f"    {s.name!r}: {list(s.field_order)!r},")
    lines.append("}")
    lines.append("")

    # EVENT_TYPES — every shape whose `also:` chain includes `event` (plus
    # `event` itself). Derived from the shape graph — no separate registry.
    # `agent-sdk validate` uses this to recognise event-shape returns.
    lines.append("# Every shape whose `also:` chain includes `event` (plus `event` itself).")
    lines.append("# Derived from the shape graph — the shape IS the type.")
    lines.append("EVENT_TYPES: list[str] = [")
    for name in onto.event_shape_names():
        lines.append(f"    {name!r},")
    lines.append("]")
    lines.append("")

    # SHAPE_DERIVED — per-shape `derived:` bindings. Read-side resolver
    # walks these at read time and projects computed values onto the node
    # JSON. Each entry maps a derived-field name to a binding dict (see
    # ir.Shape.derived for the binding grammar).
    lines.append("# `derived:` bindings per shape — read-side resolver input.")
    lines.append("# Binding grammar: {find, where, where_link, is, get} | {latest: [...]} | dotted string.")
    lines.append("SHAPE_DERIVED: dict[str, dict] = {")
    for s in shapes:
        if not s.derived:
            continue
        lines.append(f"    {s.name!r}: {s.derived!r},")
    lines.append("}")
    lines.append("")

    # SHAPE_SHORTCUTS — per-shape `shortcuts:` block, the flat-create
    # expansion table. Engine reads this on create() to rewrite a flat
    # payload into the canonical nested links_out form.
    lines.append("# `shortcuts:` per shape — write-side flat-create expansion table.")
    lines.append("# Each entry: flat_key -> {writes: <link>[is=<shape>].<field>}")
    lines.append("SHAPE_SHORTCUTS: dict[str, dict] = {")
    for s in shapes:
        if not s.shortcuts:
            continue
        lines.append(f"    {s.name!r}: {s.shortcuts!r},")
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def _py_field_name(name: str) -> str:
    if "." in name:
        return name.replace(".", "_")
    if name in _PY_RESERVED:
        return f"{name}_"
    return name


def _py_type(f: Field, s: Shape) -> str:
    if f.is_relation:
        # `node` is the universal relation target — any addressable graph node.
        # Used by list.contains (anything addressable) and bookmark.target.
        if f.target == "node":
            return "list[Any]" if f.is_array else "Any"
        cls = to_class_name(f.target)
        return f"list[{cls}]" if f.is_array else cls
    return _PY_TYPES.get(f.type, "Any")
