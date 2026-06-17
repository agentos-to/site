"""Python op emitter — ops YAML → typed async SDK stubs.

Projects the `Op` IR into one `agentos/<group>.py` per pure-generated op
group. A stub is a thin typed `async def` that builds the request dict and
`await dispatch(...)`s it. `generate.py` writes these straight into
`sdk/python/agentos/` — they are the SDK's op surface.
"""

from __future__ import annotations

from ir import Op, Ontology, TypeRef, parse_type

# Op groups whose entire SDK surface is generated stubs. `auth_store`, `http`,
# and `llm` are excluded — their SDK modules are hand-written (the HTTP
# client, the matchmaking loop), with ops called internally. `services` is
# just another pure-stub group: it ships the broker (`call` /
# `list_providers`) and nothing else — a service is named by its bare
# string, self-registered from each app's `@provides`, never a constant.
_PURE_OP_GROUPS = {"blobs", "crypto", "plist", "secrets", "services", "shell", "sql"}

FILE_HEADER = (
    "# This file is AUTO-GENERATED. Do not edit.\n"
    "# Regenerate with `python3 platform/codegen/generate.py`.\n"
)

_PY_PRIMITIVES = {
    "string": "str",
    "boolean": "bool",
    "number": "float",
    "json": "Any",
    "bytes": "bytes",
    "i32": "int",
    "i64": "int",
    "u16": "int",
    "u32": "int",
    "u64": "int",
}


def _py_type(t: TypeRef) -> str:
    """A parsed op-field type → its Python annotation."""
    if t.kind == "primitive":
        return _PY_PRIMITIVES[t.name]
    if t.kind == "named":
        return "Any"
    if t.kind in ("array", "list"):
        return f"list[{_py_type(t.elem)}]"
    if t.kind == "map":
        return f"dict[{_py_type(t.key)}, {_py_type(t.val)}]"
    return "Any"


def _response_type(op: Op) -> str:
    """The stub's return annotation."""
    if op.fire_and_forget:
        return "None"
    resp = op.response
    if resp and resp.scalar:
        t = parse_type(resp.type)
        if t.kind == "primitive" and t.name == "bytes":
            return "bytes"
        if t.kind == "primitive" and t.name == "json":
            # A bare-`json` passthrough response (services.call) — always an
            # object on the wire.
            return "dict[str, Any]"
        return _py_type(t)
    # Field-map response — typed `dict[str, Any]` until TypedDict mode lands.
    return "dict[str, Any]"


def _optional_annot(t: str) -> str:
    return t if t.endswith("| None") or t == "None" else f"{t} | None"


def _emit_op(op: Op) -> str:
    """One `async def` stub."""
    # Required fields (no `?`, no `default:`) keep YAML order; optional fields
    # follow alphabetically, so keyword-arg order is stable.
    required = [f for f in op.request if not f.optional and not f.has_default]
    optional = sorted(
        (f for f in op.request if f.optional or f.has_default),
        key=lambda f: f.name,
    )
    fields = [(f.name, _py_type(parse_type(f.type)), True) for f in required]
    fields += [(f.name, _py_type(parse_type(f.type)), False) for f in optional]

    resp_t = _response_type(op)
    pos_params = [f"{n}: {t}" for n, t, req in fields if req]
    kw_params = [f"{n}: {_optional_annot(t)} = None" for n, t, req in fields if not req]
    signature_parts = pos_params
    if kw_params:
        signature_parts.append("*")
        signature_parts.extend(kw_params)
    signature = ", ".join(signature_parts)

    doc_full = op.doc_full or op.doc
    doc_indented = "\n".join(
        ("    " + line) if line else line for line in doc_full.splitlines()
    )

    scalar_bytes = bool(
        op.response
        and op.response.scalar
        and parse_type(op.response.type).name == "bytes"
    )

    local = "_req"
    lines: list[str] = [f"async def {op.action}({signature}) -> {resp_t}:"]
    if doc_indented:
        lines.append('    """')
        lines.append(doc_indented.rstrip())
        lines.append('    """')
    lines.append(f"    {local}: dict[str, Any] = {{}}")
    for n, _t, req in fields:
        if req:
            lines.append(f"    {local}[{n!r}] = {n}")
        else:
            lines.append(f"    if {n} is not None:")
            lines.append(f"        {local}[{n!r}] = {n}")
    if op.fire_and_forget:
        lines.append(f"    await dispatch({op.name!r}, {local})")
        lines.append("    return None")
    elif scalar_bytes:
        lines.append(f"    hex_value = await dispatch({op.name!r}, {local})")
        lines.append("    return bytes.fromhex(hex_value)")
    else:
        lines.append(f"    return await dispatch({op.name!r}, {local})")
    lines.append("")
    return "\n".join(lines)


def _emit_module(group: str, ops: list[Op]) -> str:
    """One `agentos/<group>.py` file body."""
    # The module docstring is the op file's leading comment — the ontology's
    # per-group prose, sourced from one place.
    module_doc = ops[0].leading_comment or f"Generated stubs for `{group}` ops."
    body = [
        FILE_HEADER,
        f'"""{module_doc}"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from agentos._bridge import dispatch",
        "",
        "",
    ]
    for op in sorted(ops, key=lambda o: o.name):
        body.append(_emit_op(op))
        body.append("")
    return "\n".join(body).rstrip() + "\n"


def emit_ops_python(onto: Ontology) -> dict[str, str]:
    """Render every pure-generated op group → `{module_name: file_body}`."""
    groups: dict[str, list[Op]] = {}
    for op in onto.ops:
        if op.group in _PURE_OP_GROUPS:
            groups.setdefault(op.group, []).append(op)
    return {g: _emit_module(g, ops) for g, ops in sorted(groups.items())}
