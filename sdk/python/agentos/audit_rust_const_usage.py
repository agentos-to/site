"""Audit Rust callsite usage of the generated `shapes::*` consts.

Companion to `codegen_rust_shapes.py`. The codegen script emits one
`pub const NAME: &str = "name";` per shape so the engine can refer to
shapes symbolically (`shapes::ACTIVITY`) instead of by bare string
(`"activity"`). This script walks the Rust code and reports:

  1. **Defined but never used** — generated consts that no Rust file
     references. A const with zero callsites is either (a) a shape
     that's only used by skills (fine; the engine never sees it), or
     (b) a shape that used to be used and isn't anymore, which makes
     the YAML itself a delete candidate. The audit can't tell them
     apart — that's a human judgment call — so it just reports.

  2. **Literals ready to migrate** — bare `"shape_name"` string
     literals in the graph-tagging APIs (`ensure_tag`,
     `find_tag_by_name`, `find_node_by_tag_and_val`,
     `create_tagged_node`) where `shape_name` is a known shape that
     already has a generated const. These are the drop-in rewrites:
     `ensure_tag("activity")` → `ensure_tag(shapes::ACTIVITY)`.

Output is stable and sorted so diffs against the previous run
highlight real changes. Exit codes:
    0  Clean audit (or informational only).
    1  Reserved for future --strict mode; currently never returned.
    2  Fatal error (missing path, bad generated.rs parse).

Run:
    python3 -m agentos.audit_rust_const_usage

Importable API:
    scan_const_usage(...) -> dict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Reuse the producer scanner — it already knows how to find every
# `"shape_name"` literal inside the four graph-tagging APIs. No reason
# to duplicate that regex matrix here; we just run it and diff the
# result against the generated const list.
from agentos.audit_rust_producers import scan_rust_producers


# ─────────────────────────────────────────────────────────────────────
# Defaults — same workspace layout as codegen_rust_shapes.py.
# ─────────────────────────────────────────────────────────────────────

_WORKSPACE_ROOT = Path(__file__).resolve().parents[3]

DEFAULT_CRATES_ROOT = _WORKSPACE_ROOT / "core" / "crates"
DEFAULT_GENERATED_RS = (
    _WORKSPACE_ROOT / "core" / "crates" / "shapes" / "src" / "generated.rs"
)

# `_SKIP_DIRS` mirrors audit_rust_producers — we want the two scans to
# cover the same file set so their results line up.
_SKIP_DIRS = {"target", "node_modules", ".git"}

# Regex to extract the `NAME` of `pub const NAME: &str = "name";` from
# the generated file. Looser than the generator's output template
# (allows any whitespace, any single-line form) so hand-edits don't
# break the audit — though hand-edits to a generated file are a bug.
_RE_PUB_CONST = re.compile(
    r'^\s*pub\s+const\s+([A-Z][A-Z0-9_]*)\s*:\s*&str\s*=\s*"([^"]*)"\s*;\s*$',
    re.MULTILINE,
)

# Regex for `shapes::NAME` references in hand-written Rust. Captures
# the const name. Accepts any path prefix so both `shapes::ACTIVITY`
# and `agentos_shapes::ACTIVITY` / `crate::shapes::ACTIVITY` count.
_RE_SHAPES_USE = re.compile(r'\bshapes::([A-Z][A-Z0-9_]*)\b')

# Filtering: only SCREAMING_SNAKE that could plausibly be a shape
# const. Rust types like `HashMap::NEW` or custom consts with two-plus
# underscores match too, so we cross-reference against the actual
# const list before counting a match — the regex is a prefilter, the
# const set is the authority.


# ─────────────────────────────────────────────────────────────────────
# Core API
# ─────────────────────────────────────────────────────────────────────

def parse_generated_consts(generated_rs: Path) -> dict[str, str]:
    """Parse `generated.rs` into a `{CONST_NAME: "shape_value"}` dict.

    The shape-value side of the map lets the audit cross-check: a
    literal `"activity"` in hand-written code can be rewritten to
    `shapes::ACTIVITY` because the const's string IS `"activity"`.
    """
    if not generated_rs.exists():
        raise FileNotFoundError(
            f"generated.rs not found at {generated_rs}. "
            f"Run `python3 -m agentos.codegen_rust_shapes` first."
        )
    text = generated_rs.read_text()
    consts: dict[str, str] = {}
    for match in _RE_PUB_CONST.finditer(text):
        const_name, shape_value = match.group(1), match.group(2)
        consts[const_name] = shape_value
    if not consts:
        raise RuntimeError(
            f"{generated_rs} contains no `pub const` declarations — "
            f"did codegen succeed?"
        )
    return consts


def _iter_rust_files(crates_root: Path):
    """Yield every non-generated `*.rs` file under crates_root.

    The generated file itself defines the consts — referencing a const
    from its own definition doesn't count as "usage" — so we skip it.
    """
    generated_rs = (
        crates_root / "shapes" / "src" / "generated.rs"
    ).resolve()
    for path in crates_root.rglob("*.rs"):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        if path.resolve() == generated_rs:
            continue
        yield path


def scan_const_usage(
    crates_root: Path,
    generated_rs: Path,
) -> dict:
    """Run the audit. Returns a structured report dict.

    Return schema (all lists deterministically sorted):

        {
          "consts_total":  int,
          "consts_used":   [CONST_NAME, ...],
          "consts_unused": [CONST_NAME, ...],
          "usage": {
            CONST_NAME: [(path, line, matched_text), ...],
          },
          "migratable_literals": {
            shape_name: [(path, line, api_call), ...],
          },
        }
    """
    crates_root = Path(crates_root).resolve()
    consts = parse_generated_consts(generated_rs)
    # Reverse map: shape_value → const_name, for migration suggestions.
    value_to_const = {v: k for k, v in consts.items()}
    # Forward map is the authoritative const table (name → shape value).
    const_to_value = dict(consts)

    # 1. `shapes::NAME` references in hand-written Rust.
    usage: dict[str, list[tuple[Path, int, str]]] = {}
    for rs_path in _iter_rust_files(crates_root):
        try:
            text = rs_path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            for match in _RE_SHAPES_USE.finditer(line):
                const = match.group(1)
                if const in consts:
                    usage.setdefault(const, []).append(
                        (rs_path, i, match.group(0))
                    )

    for const in usage:
        usage[const].sort(key=lambda t: (str(t[0]), t[1]))

    consts_used = sorted(usage.keys())
    consts_unused = sorted(c for c in consts if c not in usage)

    # 2. Literals in graph-tagging APIs that could become const refs.
    #    `scan_rust_producers` already finds `ensure_tag("x")` and the
    #    other three APIs — its output is `{shape_name: [(path, line,
    #    api), ...]}`. We only surface the subset whose shape_name
    #    is a known generated const (i.e. a real shape in the
    #    ontology). Anything else is either a typo in Rust or a
    #    shape that exists only at runtime (e.g. user-added via the
    #    graph), which isn't the codegen's problem.
    producers = scan_rust_producers(crates_root)
    migratable: dict[str, list[tuple[Path, int, str]]] = {}
    for shape_name, sites in producers.items():
        if shape_name in value_to_const:
            migratable[shape_name] = sorted(
                sites, key=lambda t: (str(t[0]), t[1], t[2])
            )

    return {
        "consts_total": len(consts),
        "consts_used": consts_used,
        "consts_unused": consts_unused,
        "usage": usage,
        "migratable_literals": dict(sorted(migratable.items())),
        "_const_to_value": const_to_value,  # CONST_NAME → "shape_name"
        "_value_to_const": value_to_const,  # "shape_name" → CONST_NAME
    }


# ─────────────────────────────────────────────────────────────────────
# Report rendering
# ─────────────────────────────────────────────────────────────────────

def _rel(path: Path, crates_root: Path) -> str:
    """Render `path` relative to crates_root's parent (so the `core/`
    prefix shows). Mirrors audit_rust_producers."""
    try:
        return str(path.relative_to(crates_root.parent))
    except ValueError:
        return str(path)


def render_report(report: dict, crates_root: Path) -> str:
    """Format a report dict into a printable text summary."""
    crates_root = Path(crates_root).resolve()
    out: list[str] = []

    total = report["consts_total"]
    used = report["consts_used"]
    unused = report["consts_unused"]
    usage = report["usage"]
    migratable = report["migratable_literals"]
    const_to_value = report["_const_to_value"]
    value_to_const = report["_value_to_const"]

    out.append("=" * 72)
    out.append(
        f"shapes:: const usage audit — {total} consts defined, "
        f"{len(used)} used ({len(unused)} unused)"
    )
    out.append("=" * 72)
    out.append("")

    # Section 1: unused consts.
    out.append(
        f"## Unused consts ({len(unused)}) — no `shapes::NAME` reference in Rust"
    )
    if not unused:
        out.append("  (none — every generated const is referenced)")
    else:
        out.append(
            "  These shape names exist in the YAML ontology but the "
            "engine never"
        )
        out.append(
            "  references the const. That is fine if the shape is "
            "skill-only, or a"
        )
        out.append(
            "  candidate for YAML deletion if nothing else uses it "
            "either. Cross-"
        )
        out.append("  reference with skills / graph content before deleting.")
        out.append("")
        for const in unused:
            out.append(f"  - shapes::{const}  (\"{const_to_value[const]}\")")
    out.append("")

    # Section 2: used consts — short tally.
    out.append(f"## Used consts ({len(used)})")
    if not used:
        out.append("  (none — no hand-written Rust currently uses shapes::*)")
    else:
        width = max((len(c) for c in used), default=0)
        for const in used:
            sites = usage[const]
            out.append(f"  shapes::{const:<{width}}  ({len(sites)} callsites)")
            for path, line, text in sites:
                out.append(f"    {_rel(path, crates_root)}:{line}  {text}")
    out.append("")

    # Section 3: migration candidates — bare literals that could use
    # a const instead. This is the action list for the next commit.
    total_lit = sum(len(v) for v in migratable.values())
    out.append(
        f"## Literal → const migration candidates "
        f"({len(migratable)} shapes, {total_lit} callsites)"
    )
    if not migratable:
        out.append("  (none — every tagging-API callsite already uses a const)")
    else:
        out.append(
            "  Each callsite below uses a bare \"shape\" literal where a "
            "generated"
        )
        out.append(
            "  const exists. Rewrite to `shapes::NAME` for type safety."
        )
        out.append("")
        for shape_name in sorted(migratable):
            const = value_to_const[shape_name]
            sites = migratable[shape_name]
            out.append(
                f'  "{shape_name}" → shapes::{const}  '
                f"({len(sites)} callsites)"
            )
            for path, line, api in sites:
                out.append(
                    f"    {_rel(path, crates_root)}:{line}  {api}(\"{shape_name}\")"
                )
    out.append("")

    return "\n".join(out)


# ─────────────────────────────────────────────────────────────────────
# CLI entry
# ─────────────────────────────────────────────────────────────────────

def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="audit_rust_const_usage",
        description=(
            "Audit Rust callsite usage of the generated shapes:: consts."
        ),
    )
    parser.add_argument(
        "--crates-root",
        type=Path,
        default=DEFAULT_CRATES_ROOT,
        help=f"Rust crates root (default: {DEFAULT_CRATES_ROOT})",
    )
    parser.add_argument(
        "--generated-rs",
        type=Path,
        default=DEFAULT_GENERATED_RS,
        help=f"generated consts file (default: {DEFAULT_GENERATED_RS})",
    )
    args = parser.parse_args(argv)

    try:
        report = scan_const_usage(args.crates_root, args.generated_rs)
    except (FileNotFoundError, RuntimeError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    print(render_report(report, args.crates_root))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
