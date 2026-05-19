"""TypeScript op emitter — ops YAML → `sdk/typescript/src/ops.ts`.

Projects the `Op` / `OpType` IR into typed request/response interfaces plus
an `OpContracts` registry, so a TypeScript app calling an engine op gets the
payload typed both ways. New in Phase 2 — there is no prior TS op surface,
so there is nothing to diff against; the proof is `tsc` and the IR.

Field names are kept in the ontology's snake_case spelling: an op payload
is the wire contract, and the engine deserializes the snake_case keys
verbatim (unlike shape vals, which are camelCase on the graph).
"""

from __future__ import annotations

from ir import Op, Ontology, OpField, TypeRef, parse_type, to_class_name

_TS_PRIMITIVES = {
    "string": "string",
    "bytes": "string",
    "boolean": "boolean",
    "number": "number",
    "json": "unknown",
    "i32": "number",
    "i64": "number",
    "u16": "number",
    "u32": "number",
    "u64": "number",
}


def _ts_type(t: TypeRef) -> str:
    if t.kind == "primitive":
        return _TS_PRIMITIVES[t.name]
    if t.kind == "named":
        return to_class_name(t.name)
    if t.kind in ("array", "list"):
        elem = _ts_type(t.elem)
        # Parenthesise union elements so `A | B[]` doesn't mis-parse.
        return f"({elem})[]" if "|" in elem else f"{elem}[]"
    if t.kind == "map":
        return f"Record<{_ts_type(t.key)}, {_ts_type(t.val)}>"
    return "unknown"


def _struct_base(op: Op) -> str:
    return to_class_name(op.group) + to_class_name(op.action)


def _emit_interface(name: str, fields: list[OpField], *, request: bool) -> list[str]:
    """A field-map interface. Request fields with a `?` or a `default:` are
    optional for the caller; response fields are optional only on `?`."""
    out = [f"export interface {name} {{"]
    for f in fields:
        ty = _ts_type(parse_type(f.type))
        opt = f.optional or (request and f.has_default)
        if f.doc:
            out.append(f"    /** {f.doc} */")
        out.append(f"    {f.name}{'?' if opt else ''}: {ty};")
    out.append("}")
    out.append("")
    return out


def emit_ops_ts(onto: Ontology) -> str:
    lines = [
        "// DO NOT EDIT — generated from platform/ontology/ops/*.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "//",
        "// Typed request/response shapes for the engine's op contract, plus",
        "// the `OpContracts` registry mapping each op wire-name to its pair.",
        "",
    ]

    if onto.op_types:
        lines.append("// Named record types — referenced by op req/resp.")
        lines.append("")
        for t in onto.op_types.values():
            lines.extend(_emit_interface(to_class_name(t.name), t.fields, request=False))

    for op in onto.ops:
        base = _struct_base(op)
        lines.extend(_emit_interface(f"{base}Request", op.request, request=True))
        resp = op.response
        if resp and resp.scalar:
            ty = _ts_type(parse_type(resp.type))
            if resp.type_optional:
                ty = f"{ty} | null"
            doc = f"  // {resp.doc}" if resp.doc else ""
            lines.append(f"export type {base}Response = {ty};{doc}")
            lines.append("")
        elif resp:
            lines.extend(_emit_interface(f"{base}Response", resp.fields, request=False))

    # The registry — `OpContracts["shell.run"]["response"]` etc.
    lines.append("/** Every engine op, keyed by wire name. */")
    lines.append("export interface OpContracts {")
    for op in onto.ops:
        base = _struct_base(op)
        lines.append(
            f'    "{op.name}": {{ request: {base}Request; '
            f"response: {base}Response }};"
        )
    lines.append("}")
    lines.append("")
    lines.append("/** Op wire names. */")
    names = " | ".join(f'"{op.name}"' for op in onto.ops)
    lines.append(f"export type OpName = {names};")
    lines.append("")

    return "\n".join(lines)
