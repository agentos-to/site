"""Audit the Rust engine for shape producers.

Walks `core/crates/**/*.rs` and finds every call to the four graph-tagging
APIs from `graph/src/database.rs`:

    - `ensure_tag("<tag>")`                          — registers a tag
    - `find_tag_by_name("<tag>")`                    — resolves tag id
    - `find_node_by_tag_and_val("<tag>", ...)`       — lookup by tag
    - `create_tagged_node(&name, &vals, &[...])`     — tags in slice arg

The Rust engine uses these with bare string literals (never `format!`,
never constants), so a regex/AST scan is tractable. For
`create_tagged_node` the tag slice can span multiple lines after the
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


# Skipped directory names (anywhere in the path).
_SKIP_DIRS = {"target", "node_modules", ".git"}

# Single-line patterns. Each captures one tag literal per match.
_RE_ENSURE_TAG = re.compile(r'\bensure_tag\s*\(\s*"([a-z_]+)"\s*\)')
_RE_FIND_TAG_BY_NAME = re.compile(r'\bfind_tag_by_name\s*\(\s*"([a-z_]+)"\s*\)')
_RE_FIND_NODE_BY_TAG_AND_VAL = re.compile(
    r'\bfind_node_by_tag_and_val\s*\(\s*"([a-z_]+)"\s*,'
)

# `create_tagged_node(` — the slice arg may be on a following line.
_RE_CREATE_TAGGED_NODE_CALL = re.compile(r'\bcreate_tagged_node\s*\(')

# Any `&[ "a" , "b" , ... ]` literal slice. We'll run findall over the
# joined lookahead window to extract all literals from the tag slice.
_RE_STR_LITERAL = re.compile(r'"([a-z_]+)"')

# Strip `// ...` comments (not `/* ... */` — rare in this codebase for
# inline-on-the-line-of-an-API-call, and stripping block comments
# safely would require a real tokenizer).
_RE_LINE_COMMENT = re.compile(r'//.*$')


def _strip_comments(line: str) -> str:
    """Remove `// ...` trailing comments. Leaves string-literal `//`
    inside `"..."` alone in the pathological case — but since our
    target APIs are called with single-token literals like `"activity"`,
    this is safe in practice for this codebase."""
    return _RE_LINE_COMMENT.sub('', line)


def _iter_rust_files(crates_root: Path):
    """Yield every `*.rs` file under crates_root, skipping build output."""
    for path in crates_root.rglob("*.rs"):
        # Skip any file whose path contains a skipped directory segment.
        if any(part in _SKIP_DIRS for part in path.parts):
            continue
        yield path


def _scan_file(
    path: Path,
) -> list[tuple[str, int, str]]:
    """Scan one file. Returns list of (shape_name, line_number, api_call)."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return []

    lines = text.splitlines()
    stripped = [_strip_comments(ln) for ln in lines]
    out: list[tuple[str, int, str]] = []

    # Single-line APIs — one regex sweep per line.
    for i, line in enumerate(stripped, start=1):
        for tag in _RE_ENSURE_TAG.findall(line):
            out.append((tag, i, "ensure_tag"))
        for tag in _RE_FIND_TAG_BY_NAME.findall(line):
            out.append((tag, i, "find_tag_by_name"))
        for tag in _RE_FIND_NODE_BY_TAG_AND_VAL.findall(line):
            out.append((tag, i, "find_node_by_tag_and_val"))

    # `create_tagged_node(...)` — find the opening call, then look
    # forward up to 10 lines for the first `&[ ... ]` slice literal.
    # The slice is always the 3rd arg (tag_names: &[&str]), and by
    # convention all prior args are the `name` and `vals` — `vals`
    # itself is `&[(&str, &str, &str)]` of *tuples*, not bare strings.
    # So the first `&[` containing only bare `"..."` (no parens) is
    # the tags slice.
    #
    # To be maximally robust: we grab the window after the opening
    # paren up to the matching close paren (or 10 lines, whichever is
    # first), then find every `&[...]` in it and skip any that contain
    # `(` (those are the vals slice of tuples).
    for i, line in enumerate(stripped):
        for m in _RE_CREATE_TAGGED_NODE_CALL.finditer(line):
            window_end = min(len(stripped), i + 10)
            window_lines = stripped[i:window_end]
            # Start the window at the character position of the
            # opening paren on the first line so we don't match an
            # earlier `&[...]` on the same line (unlikely but safe).
            call_start = m.end()  # position just after `(`
            window_lines = [window_lines[0][call_start:]] + window_lines[1:]
            window = "\n".join(window_lines)

            # Find every `&[ ... ]` literal (non-greedy, no nesting).
            for slice_match in re.finditer(
                r'&\[\s*([^\[\]]*?)\s*\]', window
            ):
                body = slice_match.group(1)
                # Tags slice contains only bare string literals and
                # commas/whitespace. The vals slice contains `(`/`)`
                # tuples. Skip anything with parens.
                if "(" in body:
                    continue
                # Extract every `"..."` literal from the slice body.
                tags_in_slice = _RE_STR_LITERAL.findall(body)
                if not tags_in_slice:
                    continue
                # Compute line number of this specific `&[` within the
                # file — we need the absolute line, not the window
                # offset. The slice_match.start() is relative to the
                # joined window string; count newlines before it to
                # find which window line it lands on.
                prefix = window[: slice_match.start()]
                line_offset = prefix.count("\n")
                abs_line = i + 1 + line_offset
                for tag in tags_in_slice:
                    out.append((tag, abs_line, "create_tagged_node"))
                # The FIRST non-tuple `&[...]` after `create_tagged_node(`
                # is the tags slice. Stop scanning this call.
                break

    return out


def scan_rust_producers(
    crates_root: Path,
) -> dict[str, list[tuple[Path, int, str]]]:
    """Scan every `.rs` file under `crates_root` for shape-tag producer
    callsites.

    Returns a deterministic mapping of shape_name -> sorted list of
    (file, line, api_call) tuples. File paths are returned as given
    (absolute if `crates_root` is absolute), sorted by (file, line, api)
    for stable output.
    """
    crates_root = Path(crates_root)
    out: dict[str, list[tuple[Path, int, str]]] = {}

    for rs_path in _iter_rust_files(crates_root):
        for tag, line, api in _scan_file(rs_path):
            out.setdefault(tag, []).append((rs_path, line, api))

    # Deterministic ordering: sort each shape's callsites by (path, line, api).
    for tag in out:
        out[tag].sort(key=lambda t: (str(t[0]), t[1], t[2]))

    # Return a dict sorted by shape name for deterministic iteration.
    return dict(sorted(out.items()))


def _format_rel(path: Path, crates_root: Path) -> str:
    """Render `path` relative to crates_root's parent (so the `core/`
    prefix shows) — matches the sample output in the task brief."""
    try:
        # Relative to the parent of crates_root, so we get `core/src/...`
        # when crates_root is `.../core/crates`.
        return str(path.relative_to(crates_root.parent))
    except ValueError:
        return str(path)


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    # Default crates root.
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
    # Width for shape-name column. Pad to longest name + a couple spaces.
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
