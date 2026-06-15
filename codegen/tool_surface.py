"""Tool-surface registry loader — `agentos call --json system.schema`.

Per D11 (`_product/p1/unified-surface/unified-surface.md`) the registry in
`crates/core/src/tools.rs` is the single source of truth. This module fetches
it from a running engine for registry-driven codegen (`sdk_client.py`, the
`--sdk-client` path). The MCP tool registry's *docs* projection lives in the
engine itself (`crates/core/src/system_symbols.rs` → the System Docs volume),
not here.
"""

from __future__ import annotations

import json
import subprocess
import sys


def _strip_code_fences(text: str) -> str:
    """Strip a single markdown code fence from CLI JSON output."""
    if text.startswith("```"):
        text = "\n".join(text.split("\n")[1:])
    if text.endswith("```"):
        text = "\n".join(text.split("\n")[:-1])
    return text


def load_tool_surface(agentos_bin: str) -> list[dict]:
    """Fetch the tool surface registry from a running engine.

    Calls `agentos call --json system.schema` and parses the registry
    tree. Returns the list of namespace dicts. Exits with code 1 if the
    engine is unreachable — caller catches `SystemExit` to treat this
    as a soft skip.
    """
    try:
        result = subprocess.run(
            [agentos_bin, "call", "--json", "system.schema"],
            capture_output=True, text=True,
        )
    except FileNotFoundError:
        # No binary at all is the same condition as engine-unreachable —
        # the caller soft-skips registry-driven targets on SystemExit.
        print(f"Failed to load tool surface: {agentos_bin} not found", file=sys.stderr)
        sys.exit(1)
    if result.returncode != 0:
        print(f"Failed to load tool surface: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    lines = [ln for ln in result.stdout.splitlines() if not ln.startswith("[engine:")]
    body = _strip_code_fences("\n".join(lines).strip())
    data = json.loads(body)
    return data.get("namespaces", [])
