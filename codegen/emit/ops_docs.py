"""MDX emitter — op reference pages (Starlight-compatible).

One page per op group plus an index, projected off the `Op` / `OpType` IR.
The static counterpart to the registry-driven `tool-surface` docs: those
document the *live* engine; these document the *ontology* — the op contract
as authored. Not on the byte-identical `--check` path.
"""

from __future__ import annotations

from pathlib import Path

from ir import Op, OpType


def _flags(op: Op) -> str:
    badges = []
    if op.trace_span:
        badges.append("`trace_span`")
    if op.fire_and_forget:
        badges.append("`fire-and-forget`")
    return " · ".join(badges)


def _request_table(op: Op) -> list[str]:
    if not op.request:
        return ["_No parameters._", ""]
    out = [
        "| Field | Type | Required | Default | Description |",
        "|---|---|---|---|---|",
    ]
    for f in op.request:
        required = "no" if (f.optional or f.has_default) else "**yes**"
        default = "" if not f.has_default else f"`{f.default!r}`"
        ty = f"`{f.type}{'?' if f.optional else ''}`"
        out.append(f"| `{f.name}` | {ty} | {required} | {default} | {f.doc} |")
    out.append("")
    return out


def _response_block(op: Op) -> list[str]:
    resp = op.response
    if resp is None:
        return ["_No response._", ""]
    if resp.scalar:
        ty = f"{resp.type}{'?' if resp.type_optional else ''}"
        doc = f" — {resp.doc}" if resp.doc else ""
        return [f"Returns `{ty}`{doc}", ""]
    if not resp.fields:
        return ["_Empty object._", ""]
    out = ["| Field | Type | Description |", "|---|---|---|"]
    for f in resp.fields:
        ty = f"`{f.type}{'?' if f.optional else ''}`"
        out.append(f"| `{f.name}` | {ty} | {f.doc} |")
    out.append("")
    return out


def _op_section(op: Op) -> list[str]:
    out = [f"## `{op.name}`", ""]
    if op.doc:
        out += [op.doc, ""]
    meta_rows = []
    if op.capability:
        meta_rows.append(("Capability", ", ".join(f"`{c}`" for c in op.capability)))
    flags = _flags(op)
    if flags:
        meta_rows.append(("Flags", flags))
    if op.effects:
        meta_rows.append(("Effects", ", ".join(f"`{e}`" for e in op.effects)))
    if op.log_fields:
        lf = ", ".join(f"`{x.source}{x.path}` → `{x.key}`" for x in op.log_fields)
        meta_rows.append(("Audit log", lf))
    if meta_rows:
        out += ["| Metadata | Value |", "|---|---|"]
        out += [f"| **{k}** | {v} |" for k, v in meta_rows]
        out += [""]
    out += ["### Request", ""]
    out += _request_table(op)
    out += ["### Response", ""]
    out += _response_block(op)
    if op.doc_full and op.doc_full.strip() != op.doc.strip():
        out += ["### Notes", "", "```text", op.doc_full.rstrip(), "```", ""]
    return out


def _frontmatter(title: str, description: str, label: str) -> list[str]:
    desc = description.replace('"', "'").replace("`", "").strip()
    if len(desc) > 160:
        desc = desc[:157] + "..."
    return [
        "---",
        f"title: {title}",
        f'description: "{desc}"',
        "sidebar:",
        f"  label: {label}",
        "---",
        "",
    ]


def emit_op_docs(ops: list[Op], op_types: dict[str, OpType], out_dir: Path) -> None:
    """Write one MDX file per op group into `out_dir`, plus an index page."""
    out_dir.mkdir(parents=True, exist_ok=True)

    groups: dict[str, list[Op]] = {}
    for op in ops:
        groups.setdefault(op.group, []).append(op)

    for group, group_ops in sorted(groups.items()):
        lead = group_ops[0].leading_comment
        intro = lead.split("\n")[0] if lead else f"`{group}.*` engine ops."
        lines = _frontmatter(f"{group}.*", intro, group)
        if lead:
            lines += [lead, ""]
        for op in group_ops:
            lines += _op_section(op)
        (out_dir / f"{group}.mdx").write_text("\n".join(lines))

    # Named record types appendix — only when any are declared.
    type_lines: list[str] = []
    if op_types:
        for t in sorted(op_types.values(), key=lambda x: x.name):
            type_lines += [f"### `{t.name}`", "", "| Field | Type | Description |",
                           "|---|---|---|"]
            for f in t.fields:
                ty = f"`{f.type}{'?' if f.optional else ''}`"
                type_lines.append(f"| `{f.name}` | {ty} | {f.doc} |")
            type_lines.append("")

    # Index page.
    idx = _frontmatter("Ops", "The engine op contract — primitives skills call.", "Overview")
    idx += [
        "The op contract — the engine primitives skills call (`shell.run`,",
        "`http.request`, `sql.query`, …). Authored as YAML in",
        "`platform/ontology/ops/`, projected here and into every SDK.",
        "",
        "| Group | Ops |",
        "|---|---|",
    ]
    for group, group_ops in sorted(groups.items()):
        op_links = ", ".join(f"[`{o.name}`](/ops/reference/{group}/)" for o in group_ops)
        idx.append(f"| [`{group}`](/ops/reference/{group}/) | {op_links} |")
    idx.append("")
    if type_lines:
        idx += ["## Named record types", ""] + type_lines
    (out_dir / "index.mdx").write_text("\n".join(idx))
