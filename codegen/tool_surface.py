"""Tool-surface codegen — registry → Astro MDX pages.

Reads the registry from a running engine via `agentos call --json schema`
and emits one MDX page per namespace to
`docs/src/content/docs/tool-surface/<name>.mdx`. Per D11
(`_roadmap/p1/unified-surface/unified-surface.md`) the registry in
`crates/core/src/tools.rs` is the single source of truth; this module
is one consumer of that source.

Future siblings under `docs/codegen/`:
- `sdk_client.py` — emits `sdk-skills/agentos/_engine_client.py` from
  the same registry dump.
- `mcp_bundled.py` — helper for the MCP adapter's bundled-tool
  descriptions (if we decide to hoist the MCP rendering here).
"""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def _strip_code_fences(text: str) -> str:
    """Strip a single markdown code fence from CLI JSON output."""
    if text.startswith("```"):
        text = "\n".join(text.split("\n")[1:])
    if text.endswith("```"):
        text = "\n".join(text.split("\n")[:-1])
    return text


def load_tool_surface(agentos_bin: str) -> list[dict]:
    """Fetch the tool surface registry from a running engine.

    Calls `agentos call --json schema`, which dispatches `system.schema`
    and emits the registry tree. Returns the list of namespace dicts.
    Exits with code 1 if the engine is unreachable — caller catches
    `SystemExit` to treat this as a soft skip.
    """
    result = subprocess.run(
        [agentos_bin, "call", "--json", "schema"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Failed to load tool surface: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    lines = [ln for ln in result.stdout.splitlines() if not ln.startswith("[engine:")]
    body = _strip_code_fences("\n".join(lines).strip())
    data = json.loads(body)
    return data.get("namespaces", [])


def emit_tool_surface_docs(namespaces: list[dict], out_dir: Path) -> None:
    """Write one MDX file per namespace into `tool-surface/<name>.mdx`.

    Each page lists every op in that namespace with description,
    examples, and input schema. Also writes `tool-surface/index.md`
    linking to all namespaces.
    """
    out_dir.mkdir(parents=True, exist_ok=True)

    for ns in namespaces:
        (out_dir / f"{ns.get('name', '?')}.md").write_text(
            _emit_namespace_page(ns).rstrip() + "\n"
        )

    (out_dir / "index.md").write_text(_emit_index_page(namespaces) + "\n")


def _emit_namespace_page(ns: dict) -> str:
    name = ns.get("name", "?")
    ns_desc = ns.get("description", "")
    ops = ns.get("ops", [])

    # Short description for sidebar/meta — first sentence, ≤160 chars.
    sidebar_desc = ns_desc.split(".")[0][:160].strip()

    lines = [
        "---",
        f"title: {name}",
        f'description: "{sidebar_desc}"',
        "sidebar:",
        f"  label: {name}",
        "---",
        "",
        f"# `{name}` namespace",
        "",
        ns_desc,
        "",
    ]

    if not ops:
        # Namespaces declared per D7 but whose handlers land in later
        # stages — document this honestly.
        lines.append(
            "*No ops registered yet.* This namespace is declared in the registry "
            "but its handlers land in a later stage of the unified-surface refactor "
            "(see [`_roadmap/p1/unified-surface/unified-surface.md`](https://github.com/agentos-to))."
        )
        lines.append("")
        return "\n".join(lines)

    # Table of contents at the top.
    lines.append("## Ops")
    lines.append("")
    for op in ops:
        op_name = op.get("name", "?")
        op_desc = op.get("description", "").split(".")[0]
        lines.append(f"- [`{op_name}`](#{op_name}) — {op_desc}")
    lines.append("")

    # One section per op.
    for op in ops:
        lines.extend(_emit_op_section(op))

    return "\n".join(lines)


def _emit_op_section(op: dict) -> list[str]:
    op_name = op.get("name", "?")
    op_desc = op.get("description", "")
    examples = op.get("examples") or []
    schema = op.get("input_schema")

    out = [f"## `{op_name}`", "", op_desc, ""]

    if examples:
        out += ["### Examples", "", "```js"]
        out += list(examples)
        out += ["```", ""]

    if schema:
        out += ["### Input schema", "", "```json", json.dumps(schema, indent=2), "```", ""]

    return out


def _emit_index_page(namespaces: list[dict]) -> str:
    lines = [
        "---",
        "title: Tool surface",
        'description: "Every tool the AgentOS engine exposes — 8 namespaces, one registry."',
        "---",
        "",
        "The engine's tool surface is organized into **8 namespaces**. The registry "
        "in `crates/core/src/tools.rs` is the single source of truth — this page, "
        "the MCP `tools/list`, and the Python `Client` SDK are all generated from it.",
        "",
        "See [`_roadmap/p1/unified-surface/unified-surface.md`](https://github.com/agentos-to) "
        "for the architecture.",
        "",
        "## Namespaces",
        "",
    ]
    for ns in namespaces:
        name = ns.get("name", "?")
        desc = ns.get("description", "").split(".")[0]
        op_count = len(ns.get("ops", []))
        count_str = (
            f" ({op_count} op{'s' if op_count != 1 else ''})"
            if op_count else " *(empty)*"
        )
        lines.append(f"- [`{name}`](/tool-surface/{name}/){count_str} — {desc}")
    return "\n".join(lines)
