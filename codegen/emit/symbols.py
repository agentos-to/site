"""System Docs symbols — project the ontology (shapes + ops) into the same
compact symbol records the engine's build-time extractors emit.

The third System Docs producer: rustdoc covers the engine, ts-morph covers
the shell, this covers the contract itself. Output is one deterministic JSON
artifact — `core/crates/core/generated/yaml-symbols.json` — embedded by the
engine via `include_str!` and replayed through `agentos_volumes::write_nodes`
at boot, exactly like the Rust/TS artifacts (see `core/crates/core/src/
code_symbols.rs`; the artifact is the contract, not this script).

Ids are the urns (`shape:account`, `op:http.request`) — unlike the code
extractors' bare dotted paths — because bare names collide inside the one
System Docs pool (the SDK op group `services` vs the MCP `services`
namespace; a shape named `document` vs a concept doc). Display names stay
bare, so `[[account]]` still resolves by unique name.
"""

from __future__ import annotations

import json

from ir import STANDARD_FIELDS, Ontology, Op, Shape


def emit_yaml_symbols(onto: Ontology) -> str:
    records = [_shape_record(s, onto.shapes) for s in onto.shapes]
    groups: dict[str, list[Op]] = {}
    for op in onto.ops:
        groups.setdefault(op.group, []).append(op)
    for group, ops in groups.items():
        records.append(_group_record(group, ops))
        records.extend(_op_record(op) for op in ops)
    records.sort(key=lambda r: r["id"])
    return json.dumps(records, indent=1, sort_keys=True) + "\n"


# ── shapes ───────────────────────────────────────────────────────────────────

def _shape_ref(target: str) -> str:
    """A relation target as an intra-volume link. `node` is the universal
    target (any addressable graph node) and has no symbol — inline code."""
    base = target.rstrip("[]")
    if base == "node":
        return f"`{target}`"
    suffix = "[]" if target.endswith("[]") else ""
    return f"[[shape:{base}]]{suffix}"


def _shape_record(s: Shape, shapes: list[Shape]) -> dict:
    summary = s.leading_comment.split("\n")[0].strip() if s.leading_comment else ""
    own = [f.name for f in s.own_fields]
    signature = f"{s.name} {{ {', '.join(own)} }}" if own else s.name

    out = f"`{signature}`\n\n"
    if s.leading_comment:
        out += s.leading_comment.strip() + "\n\n"

    meta = []
    if s.plural:
        meta.append(("Plural", f"`{s.plural}`"))
    if s.identity:
        meta.append(("Identity", ", ".join(f"`{i}`" for i in s.identity)))
    if s.identity_any:
        meta.append(("Identity (any)", ", ".join(f"`{i}`" for i in s.identity_any)))
    if s.also:
        meta.append(("Also", " · ".join(_shape_ref(a) for a in s.also)))
    if meta:
        out += "| | |\n|---|---|\n"
        out += "".join(f"| **{k}** | {v} |\n" for k, v in meta) + "\n"

    if s.own_fields:
        out += "**Fields**\n\n| Field | Type |\n|---|---|\n"
        out += "".join(f"| `{f.name}` | `{f.type}` |\n" for f in s.own_fields) + "\n"
    if s.own_relations:
        out += "**Relations**\n\n| Relation | Target |\n|---|---|\n"
        for f in s.own_relations:
            tgt = (f.target or f.type.rstrip("[]")) + ("[]" if f.is_array else "")
            out += f"| `{f.name}` | {_shape_ref(tgt)} |\n"
        out += "\n"

    own_names = {f.name for f in s.own_fields} | {f.name for f in s.own_relations}
    std_names = {n for n, _ in STANDARD_FIELDS}
    inherited = [f for f in s.fields if f.name not in own_names and f.name not in std_names]
    if inherited:
        out += "**Inherited**\n\n| Field | Type |\n|---|---|\n"
        for f in inherited:
            if f.is_relation:
                tgt = (f.target or f.type.rstrip("[]")) + ("[]" if f.is_array else "")
                out += f"| `{f.name}` | {_shape_ref(tgt)} |\n"
            else:
                out += f"| `{f.name}` | `{f.type}` |\n"
        out += "\n"

    children = sorted(c.name for c in shapes if s.name in c.also)
    if children:
        out += "**Used as a base by:** " + " · ".join(_shape_ref(c) for c in children) + "\n\n"

    if s.prior_art:
        out += "**Prior art**\n\n"
        for entry in s.prior_art:
            head = f"[{entry['source']}]({entry['url']})" if entry.get("url") else entry["source"]
            notes = (entry.get("notes") or "").strip()
            out += f"- **{head}** — {notes}\n" if notes else f"- **{head}**\n"
        out += "\n"

    src = f"platform/ontology/shapes/{s.source_path}" if s.source_path else "platform/ontology/shapes"
    out += f"Source: `{src}`\n"

    return {
        "id": f"shape:{s.name}",
        "name": s.name,
        "kind": "shape",
        "lang": "yaml",
        "urn": f"shape:{s.name}",
        "signature": signature,
        "summary": summary,
        "sourcePath": src,
        "sourceLine": 1,
        "body": out,
        "contains": [],
        "returns": None,
    }


# ── ops ──────────────────────────────────────────────────────────────────────

def _op_signature(op: Op) -> str:
    params = ", ".join(f.name + ("?" if f.optional or f.has_default else "")
                       for f in op.request)
    return f"{op.name}({{ {params} }})" if params else f"{op.name}()"


def _group_record(group: str, ops: list[Op]) -> dict:
    summary = ""
    for op in ops:
        if op.leading_comment:
            summary = op.leading_comment.split("\n")[0].strip()
            break
    body = f"`{group}.*` — engine op group.\n\n"
    if summary:
        body += summary + "\n\n"
    body += "**Ops:** " + " · ".join(f"[[op:{op.name}]]" for op in sorted(ops, key=lambda o: o.name)) + "\n\n"
    body += f"Source: `platform/ontology/ops/{group}.yaml`\n"
    return {
        "id": f"op:{group}",
        "name": group,
        "kind": "namespace",
        "lang": "yaml",
        "urn": f"op:{group}",
        "signature": f"{group}.*",
        "summary": summary,
        "sourcePath": f"platform/ontology/ops/{group}.yaml",
        "sourceLine": 1,
        "body": body,
        "contains": sorted(f"op:{op.name}" for op in ops),
        "returns": None,
    }


def _op_record(op: Op) -> dict:
    sig = _op_signature(op)
    out = f"`{sig}`\n\n"
    doc = (op.doc_full or op.doc or "").strip()
    if doc:
        out += doc + "\n\n"
    if op.service:
        out += "**Service:** " + ", ".join(f"`{s}`" for s in op.service) + "\n\n"
    if op.request:
        out += "**Request**\n\n| Param | Type | Default | |\n|---|---|---|---|\n"
        for f in op.request:
            default = "" if not f.has_default else f"`{json.dumps(f.default)}`"
            out += f"| `{f.name}` | `{f.type}{'?' if f.optional else ''}` | {default} | {f.doc} |\n"
        out += "\n"
    if op.response is not None:
        if op.response.scalar:
            opt = "?" if op.response.type_optional else ""
            out += f"**Response:** `{op.response.type}{opt}` — {op.response.doc}\n\n"
        elif op.response.fields:
            out += "**Response**\n\n| Field | Type | |\n|---|---|---|\n"
            for f in op.response.fields:
                out += f"| `{f.name}` | `{f.type}{'?' if f.optional else ''}` | {f.doc} |\n"
            out += "\n"
    out += f"Source: `platform/ontology/ops/{op.group}.yaml`\n"
    return {
        "id": f"op:{op.name}",
        "name": op.name,
        "kind": "op",
        "lang": "yaml",
        "urn": f"op:{op.name}",
        "signature": sig,
        "summary": (op.doc or "").split("\n")[0].strip(),
        "sourcePath": f"platform/ontology/ops/{op.group}.yaml",
        "sourceLine": 1,
        "body": out,
        "contains": [],
        "returns": None,
    }
