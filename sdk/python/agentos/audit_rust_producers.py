"""Audit the Rust engine for shape producers.

Walks `core/crates/**/*.rs` and finds every call to the four graph-shape
APIs from `graph/src/database.rs`:

    - `add_shape(node_id, "<shape>")`             — apply shape membership
    - `find_shape_node_by_name("<shape>")`        — resolves shape def node
    - `find_node_by_shape_and_val("<shape>", ...)` — lookup by shape + val
    - `create_shaped_node(&name, &vals, &[...])`  — shapes in slice arg

The Rust engine uses these with bare string literals (never `format!`,
never constants), so a regex/AST scan is tractable. For
`create_shaped_node` the shape slice can span multiple lines after the
opening paren, so we scan forward up to 10 lines for the `&[...]` slice
and extract every literal it contains.

Comments (`// ...`) are stripped before matching to avoid false
positives from commented-out code.

Run:
    python3 audit_rust_producers.py

Importable API:
    scan_rust_producers(crates_root: Path) -> dict[str, list[tuple[Path, int, str]]]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


_SKIP_DIRS = {"target", "node_modules", ".git"}

_RE_ADD_SHAPE = re.compile(
    r'\badd_shape(?:_on)?\s*\([^,]+,\s*"([a-z_]+)"\s*\)'
)
_RE_FIND_SHAPE_NODE_BY_NAME = re.compile(
    r'\bfind_shape_node_by_name(?:_on)?\s*\(\s*"([a-z_]+)"\s*\)'
)
_RE_FIND_NODE_BY_SHAPE_AND_VAL = re.compile(
    r'\bfind_node_by_shape_and_val(?:s_on|_on|s)?\s*\(\s*"([a-z_]+)"\s*,'
)

_RE_CREATE_SHAPED_NODE_CALL = re.compile(r'\bcreate_shaped_node(?:_on)?\s*\(')

_RE_STR_LITERAL = re.compile(r'"([a-z_]+)"')

_RE_LINE_COMMENT = re.compile(r'//.*$')


def _strip_comments(line: str) -> str:
    """Remove `// ...` trailing comments."""
    return _RE_LINE_COMMENT.sub('', line)


def _iter_rust_files(crates_root: Path):
    for path in crates_root.rglob("*.rs"):
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        yield path


def _scan_file(path: Path) -> list[tuple[str, int, str]]:
    """Returns list of (shape_name, line_number, api_call)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    lines = text.splitlines()
    stripped = [_strip_comments(ln) for ln in lines]
    out: list[tuple[str, int, str]] = []

    for i, line in enumerate(stripped, start=1):
        for shape in _RE_ADD_SHAPE.findall(line):
            out.append((shape, i, "add_shape"))
        for shape in _RE_FIND_SHAPE_NODE_BY_NAME.findall(line):
            out.append((shape, i, "find_shape_node_by_name"))
        for shape in _RE_FIND_NODE_BY_SHAPE_AND_VAL.findall(line):
            out.append((shape, i, "find_node_by_shape_and_val"))

    for i, line in enumerate(stripped):
        for m in _RE_CREATE_SHAPED_NODE_CALL.finditer(line):
            window_end = min(len(stripped), i + 10)
            window_lines = stripped[i:window_end]
            call_start = m.end()
            window_lines = [window_lines[0][call_start:]] + window_lines[1:]
            window = "\n".join(window_lines)

            for slice_match in re.finditer(
                r'&\[\s*([^\[\]]*?)\s*\]', window
            ):
                body = slice_match.group(1)
                if "(" in body:
                    continue
                shapes_in_slice = _RE_STR_LITERAL.findall(body)
                if not shapes_in_slice:
                    continue
                prefix = window[: slice_match.start()]
                line_offset = prefix.count("\n")
                abs_line = i + 1 + line_offset
                for shape in shapes_in_slice:
                    out.append((shape, abs_line, "create_shaped_node"))
                break

    return out


def scan_rust_producers(
    crates_root: Path,
) -> dict[str, list[tuple[Path, int, str]]]:
    """Scan every `.rs` file under `crates_root` for shape producer
    callsites.

    Returns a deterministic mapping of shape_name -> sorted list of
    (file, line, api_call) tuples.
    """
    crates_root = Path(crates_root)
    out: dict[str, list[tuple[Path, int, str]]] = {}

    for rs_path in _iter_rust_files(crates_root):
        for shape, line, api in _scan_file(rs_path):
            out.setdefault(shape, []).append((rs_path, line, api))

    for shape in out:
        out[shape].sort(key=lambda t: (str(t[0]), t[1], t[2]))

    return dict(sorted(out.items()))


def _format_rel(path: Path, crates_root: Path) -> str:
    try:
        return str(path.relative_to(crates_root.parent))
    except ValueError:
        return str(path)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    default_root = Path("/Users/joe/dev/agentos/core/crates")
    crates_root = Path(argv[0]) if argv else default_root

    if not crates_root.exists():
        print(f"error: crates root does not exist: {crates_root}", file=sys.stderr)
        return 2

    mapping = scan_rust_producers(crates_root)
    total_shapes = len(mapping)
    total_callsites = sum(len(sites) for sites in mapping.values())

    print(
        f"Rust-produced shapes ({total_shapes} unique, "
        f"{total_callsites} callsites):"
    )
    width = max((len(s) for s in mapping), default=0)
    for shape in sorted(mapping):
        sites = mapping[shape]
        print(f"  {shape:<{width}}  ({len(sites)} callsites)")
        for file_path, line, api in sites:
            rel = _format_rel(file_path, crates_root)
            print(f"    {rel}:{line}  {api}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
