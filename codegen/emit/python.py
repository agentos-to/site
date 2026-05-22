"""Python emitter — shape YAML → TypedDict classes + SDK sidecars."""

from __future__ import annotations

from ir import Field, Ontology, Shape, to_class_name

_PY_TYPES = {
    "string": "str", "text": "str", "integer": "int", "number": "float",
    "boolean": "bool", "datetime": "str", "url": "str", "json": "Any",
    "string[]": "list[str]", "integer[]": "list[int]",
}


# Map IR field-type strings to the FieldType enum variant the Rust
# ShapeDef wire format expects (serialised as lowercase by serde).
_WIRE_FIELD_TYPES = {
    "string":      "string",
    "text":        "text",
    "url":         "url",
    "integer":     "integer",
    "number":      "number",
    "boolean":     "boolean",
    "json":        "json",
    "date":        "date",
    "datetime":    "datetime",
    "string[]":    "stringlist",
    "integer[]":   "integerlist",
}


def _shape_to_wire_def(s: Shape) -> dict:
    """Convert IR Shape → a wire-format dict that deserialises into the
    Rust `ShapeDef`. Mirrors `agentos_graph::ShapeDef` exactly: name,
    plural, description, icon, fields (list of FieldDef), out / in
    (list of EdgeDef), derived (list of DerivedBinding), shortcuts
    (list of ShortcutDef), also, identity, identity_any, display.

    Skill workers attach the matching entry as `__shape_def__` on every
    `@returns(shape)` response. The engine deserialises it server-side
    and upserts the shape-def before landing the data node — every
    write carries its schema (shape-unification Phase 1)."""
    required = set(s.identity)
    seen: set[str] = set()
    fields_out: list[dict] = []
    for f in s.fields:
        if f.is_relation or f.name == "id" or f.name in seen:
            continue
        seen.add(f.name)
        ty = _WIRE_FIELD_TYPES.get(f.type, "json")
        is_required = f.name == "name" or f.name in required
        fd = {"name": f.name, "ty": ty}
        if is_required:
            fd["required"] = True
        fields_out.append(fd)

    out_edges: list[dict] = []
    for r in s.own_relations:
        is_many = r.is_array or (r.type or "").endswith("[]")
        target = (r.target or "").rstrip("[]")
        edge = {"label": r.name, "card": "many" if is_many else "one"}
        if target:
            edge["to"] = target
        out_edges.append(edge)

    derived = [{"key": k, "spec": v} for k, v in sorted(s.derived.items())]
    shortcuts = [
        {"key": k, "writes": str(v.get("writes", ""))}
        for k, v in sorted(s.shortcuts.items())
        if isinstance(v, dict) and "writes" in v
    ]

    out: dict = {"name": s.name}
    if s.plural:
        out["plural"] = s.plural
    if s.leading_comment:
        first = s.leading_comment.split("\n")[0].strip()
        if first:
            out["description"] = first
    icon = _extract_icon(s.raw_body)
    if icon:
        out["icon"] = icon
    if fields_out:
        out["fields"] = fields_out
    if out_edges:
        out["out"] = out_edges
    if derived:
        out["derived"] = derived
    if shortcuts:
        out["shortcuts"] = shortcuts
    if s.also:
        out["also"] = list(s.also)
    if s.identity:
        out["identity"] = list(s.identity)
    if s.identity_any:
        out["identity_any"] = list(s.identity_any)
    if s.display:
        d = s.display
        disp: dict = {}
        if d.title:
            disp["title"] = d.title
        if d.subtitle:
            disp["subtitle"] = d.subtitle
        if d.image:
            disp["image"] = d.image
        if d.body:
            disp["body"] = d.body
        if d.highlights:
            disp["highlights"] = list(d.highlights)
        if disp:
            out["display"] = disp
    return out


def _extract_icon(raw_body: str) -> str | None:
    for line in raw_body.splitlines():
        if line.startswith("icon:"):
            return line.split(":", 1)[1].strip()
    return None

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

    # SHAPE_DEFS: per-shape structured schema. The skill worker attaches
    # the matching entry as `__shape_def__` on every @returns(shape)
    # response; the Rust engine deserialises it directly into
    # `agentos_graph::ShapeDef` and upserts the shape-def alongside the
    # data write (shape-unification Phase 1). Replaces the legacy
    # `SHAPE_YAMLS` apparatus — engine no longer carries any YAML parser.
    lines.append("# Structured shape defs — consumed by the skill worker to attach")
    lines.append("# `__shape_def__` on every @returns(shape) response. Wire-equivalent")
    lines.append("# to `agentos_graph::ShapeDef`.")
    lines.append("SHAPE_DEFS: dict[str, dict] = {")
    for s in shapes:
        defn = _shape_to_wire_def(s)
        lines.append(f"    {s.name!r}: {defn!r},")
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
