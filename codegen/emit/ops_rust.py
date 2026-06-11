"""Rust op emitter — ops YAML → the `ops` module of the contract crate.

Projects the `Op` / `OpType` IR into `core/crates/contract-generated/src/ops.rs`:
per op a Request/Response struct pair (deriving `serde`) and an `OpMeta`
static, plus the named record types from the `types:` blocks. The `OpMeta`
type itself is *not* generated — it lives in `agentos-ops` and the generated
crate links it. The typed structs are the contract; `serde` deserialization
in the op handlers is the enforcement — no JSON Schema, no `schemars`.
"""

from __future__ import annotations

from ir import Op, OpField, Ontology, TypeRef, parse_type, to_class_name

# Op primitive → Rust type. `bytes` rides the wire as a hex string; `json`
# is an untyped `serde_json::Value`. Mirrors the hand-written op structs.
_RUST_PRIMITIVES = {
    "string": "String",
    "boolean": "bool",
    "number": "f64",
    "bytes": "String",
    "json": "serde_json::Value",
    "i32": "i32",
    "i64": "i64",
    "u16": "u16",
    "u32": "u32",
    "u64": "u64",
}

# Rust 2024 keywords that can't be bare field identifiers. Op field names are
# authored snake_case, so a clash is unlikely — but guard anyway.
_RUST_RESERVED = {
    "as", "break", "const", "continue", "crate", "dyn", "else", "enum",
    "extern", "false", "fn", "for", "if", "impl", "in", "let", "loop",
    "match", "mod", "move", "mut", "pub", "ref", "return", "self", "Self",
    "static", "struct", "super", "trait", "true", "type", "unsafe", "use",
    "where", "while", "async", "await", "abstract", "become", "box", "do",
    "final", "macro", "override", "priv", "try", "typeof", "unsized",
    "virtual", "yield", "union",
}


def _rust_type(t: TypeRef) -> str:
    """A parsed op-field type → its Rust spelling."""
    if t.kind == "primitive":
        return _RUST_PRIMITIVES[t.name]
    if t.kind == "named":
        return to_class_name(t.name)
    if t.kind in ("array", "list"):
        return f"Vec<{_rust_type(t.elem)}>"
    if t.kind == "map":
        return f"HashMap<{_rust_type(t.key)}, {_rust_type(t.val)}>"
    raise ValueError(f"unrenderable type: {t.kind}")


def _rust_ident(name: str) -> str:
    return f"{name}_" if name in _RUST_RESERVED else name


def _rust_str(s: str) -> str:
    """A Python string → a Rust `"..."` literal. UTF-8 is kept verbatim."""
    out = (
        s.replace("\\", "\\\\")
        .replace('"', '\\"')
        .replace("\n", "\\n")
        .replace("\t", "\\t")
        .replace("\r", "\\r")
    )
    return f'"{out}"'


def _struct_base(op: Op) -> str:
    """Op `group.action` → the PascalCase struct stem (e.g. `ShellRun`)."""
    return to_class_name(op.group) + to_class_name(op.action)


def _meta_ident(op: Op) -> str:
    return f"{op.group}_{op.action}".upper() + "_META"


def _effects_block(op: Op) -> str:
    """The `OpMeta.effects` slice literal — `&[]` for a pure primitive."""
    if not op.effects:
        return "&[]"
    items = [
        f"        Effect {{ verb: EffectVerb::{to_class_name(e.verb)}, "
        f"target: {_rust_str(e.target)} }},"
        for e in op.effects
    ]
    return "&[\n" + "\n".join(items) + "\n    ]"


# --------------------------------------------------------------------------
# Type vocabulary footprint — which std imports the output needs
# --------------------------------------------------------------------------

def _walk_types(onto: Ontology):
    """Yield every TypeRef referenced by any op or named type."""
    for t in onto.op_types.values():
        for f in t.fields:
            yield parse_type(f.type)
    for op in onto.ops:
        for f in op.request:
            yield parse_type(f.type)
        if op.response and op.response.scalar:
            yield parse_type(op.response.type)
        elif op.response:
            for f in op.response.fields:
                yield parse_type(f.type)


def _mentions(t: TypeRef, kinds: set[str], names: set[str]) -> bool:
    if t.kind in kinds or (t.kind == "primitive" and t.name in names):
        return True
    for child in (t.elem, t.key, t.val):
        if child and _mentions(child, kinds, names):
            return True
    return False


# --------------------------------------------------------------------------
# Field rendering
# --------------------------------------------------------------------------

def _default_attr(op: Op, f: OpField, base: str) -> tuple[str, str | None]:
    """serde `default` attribute for a field with a `default:` in YAML.

    Returns `(attr, fn_code)`. Natural-empty defaults (`[]`, `{}`, `null`)
    use the type's `Default`; a specific value gets a named fn.
    """
    d = f.default
    if d is None or d == [] or d == {}:
        return "#[serde(default)]", None
    fn_name = f"default_{op.group}_{op.action}_{f.name}"
    lit = _default_literal(parse_type(f.type), d)
    return f'#[serde(default = "{fn_name}")]', f"fn {fn_name}() -> {base} {{ {lit} }}"


def _default_literal(t: TypeRef, d) -> str:
    if t.kind != "primitive":
        raise ValueError(f"non-primitive default: {t.kind}")
    n = t.name
    if n == "number":
        return repr(float(d))
    if n in ("i32", "i64", "u16", "u32", "u64"):
        return str(int(d))
    if n == "boolean":
        return "true" if d else "false"
    if n in ("string", "bytes"):
        return f"{_rust_str(str(d))}.to_string()"
    raise ValueError(f"unrenderable default for {n}")


def _emit_field(op: Op, f: OpField) -> tuple[list[str], str | None]:
    """One struct field. Returns `(lines, default_fn_code_or_None)`."""
    base = _rust_type(parse_type(f.type))
    ident = _rust_ident(f.name)
    lines: list[str] = []
    if f.doc:
        lines.append(f"    /// {f.doc}")
    fn_code: str | None = None
    if f.optional:
        lines.append('    #[serde(default, skip_serializing_if = "Option::is_none")]')
        ty = f"Option<{base}>"
    elif f.has_default:
        attr, fn_code = _default_attr(op, f, base)
        lines.append(f"    {attr}")
        ty = base
    else:
        ty = base
    if _rust_ident(f.name) != f.name:
        lines.append(f'    #[serde(rename = "{f.name}")]')
    lines.append(f"    pub {ident}: {ty},")
    return lines, fn_code


# --------------------------------------------------------------------------
# Struct + meta emission
# --------------------------------------------------------------------------

_DERIVE = "#[derive(Debug, Clone, Serialize, Deserialize)]"


def _emit_record(name: str, doc: str, fields: list[OpField], op: Op) -> list[str]:
    """A plain `serde`-deriving struct over a field list."""
    out: list[str] = []
    if doc:
        out.append(f"/// {doc}")
    out.append(_DERIVE)
    out.append(f"pub struct {name} {{")
    fns: list[str] = []
    for f in fields:
        flines, fn = _emit_field(op, f)
        out.extend(flines)
        if fn:
            fns.append(fn)
    out.append("}")
    out.append("")
    out.extend(fns)
    if fns:
        out.append("")
    return out


def _emit_op(op: Op) -> list[str]:
    base = _struct_base(op)
    req_name, resp_name = f"{base}Request", f"{base}Response"
    out: list[str] = [
        f"// ── {op.name} " + "─" * max(0, 60 - len(op.name)),
        "",
    ]

    # Request struct — always a field-map.
    out.extend(_emit_record(req_name, f"Request parameters for `{op.name}`.",
                            op.request, op))

    # Response struct — field-map or a `#[serde(transparent)]` scalar newtype.
    resp = op.response
    if resp and resp.scalar:
        ty = _rust_type(parse_type(resp.type))
        if resp.type_optional:
            ty = f"Option<{ty}>"
        if resp.doc:
            out.append(f"/// {resp.doc}")
        out.append(_DERIVE)
        out.append("#[serde(transparent)]")
        out.append(f"pub struct {resp_name}(pub {ty});")
        out.append("")
    elif resp:
        out.extend(_emit_record(resp_name, f"Response payload for `{op.name}`.",
                                resp.fields, op))

    # OpMeta static.
    log = []
    for lf in op.log_fields:
        src = "Request" if lf.source == "request" else "Response"
        log.append(
            f"        LogField {{ source: LogFieldSource::{src}, "
            f"json_path: {_rust_str(lf.path)}, log_key: {_rust_str(lf.key)} }},"
        )
    if log:
        log_block = "&[\n" + "\n".join(log) + "\n    ]"
    else:
        log_block = "&[]"
    caps = ", ".join(_rust_str(c) for c in op.service)
    caps_block = f"&[{caps}]" if op.service else "&[]"

    out.append(f"/// `{op.name}`.")
    out.append(f"pub static {_meta_ident(op)}: OpMeta = OpMeta {{")
    out.append(f"    name: {_rust_str(op.name)},")
    out.append(f"    doc: {_rust_str(op.doc)},")
    out.append(f"    doc_full: {_rust_str(op.doc_full)},")
    out.append(f"    log_fields: {log_block},")
    out.append(f"    fire_and_forget: {'true' if op.fire_and_forget else 'false'},")
    out.append(f"    trace_span: {'true' if op.trace_span else 'false'},")
    out.append(f"    required_services: {caps_block},")
    out.append(f"    effects: {_effects_block(op)},")
    out.append("};")
    out.append("")
    return out


def emit_ops_rust(onto: Ontology) -> str:
    """Render the `ops` module of the contract crate (`ops.rs`)."""
    needs_hashmap = any(_mentions(t, {"map"}, set()) for t in _walk_types(onto))
    needs_value = any(_mentions(t, set(), {"json"}) for t in _walk_types(onto))
    needs_log = any(op.log_fields for op in onto.ops)
    needs_effects = any(op.effects for op in onto.ops)

    lines = [
        "// DO NOT EDIT — generated from platform/ontology/ops/*.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "//",
        "// Per op: a Request/Response struct pair and an `OpMeta` static.",
        "// The `OpMeta` type is linked from `agentos-ops` — this module is the",
        "// op *contract*, not the op *protocol*.",
        "",
        "#![allow(clippy::all)]",
        "",
    ]
    if needs_hashmap:
        lines.append("use std::collections::HashMap;")
        lines.append("")
    op_imports = ["OpMeta"]
    if needs_log:
        op_imports += ["LogField", "LogFieldSource"]
    if needs_effects:
        op_imports += ["Effect", "EffectVerb"]
    op_imports.sort()
    if len(op_imports) == 1:
        lines.append(f"use agentos_ops::{op_imports[0]};")
    else:
        lines.append("use agentos_ops::{" + ", ".join(op_imports) + "};")
    lines.append("use serde::{Deserialize, Serialize};")
    lines.append("")

    # Named record types — the `types:` blocks. Emitted first; ops reference them.
    if onto.op_types:
        lines.append("// ── Named record types " + "─" * 38)
        lines.append("")
        for t in onto.op_types.values():
            # A synthetic Op so `_emit_field` can name default fns; named-type
            # fields never carry defaults, so group/action are cosmetic.
            holder = Op(name=t.name, group=t.name, action="type", doc="",
                        doc_full="")
            lines.extend(_emit_record(
                to_class_name(t.name),
                f"Named record type `{t.name}`.",
                t.fields, holder,
            ))

    lines.append("// ── Ops " + "─" * 53)
    lines.append("")
    for op in onto.ops:
        lines.extend(_emit_op(op))

    if needs_value:
        # `serde_json::Value` is referenced by fully-qualified path; no `use`.
        pass

    return "\n".join(lines)
