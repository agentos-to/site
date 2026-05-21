"""Audit shape-to-shape references embedded as field *types*.

Complements `audit_shape_relations.py`. Where that script reads
`relations:` (first-class links in the graph) and `also:` (inheritance),
this one reads `fields:` and asks: "is this field's declared type the
name of another shape?"

Example (hypothetical):
    leg:
      fields:
        departureAirport: airport    # `airport` is another defined shape
        sequence:         integer

Here `airport` is embedded as a nested field type, not a top-level
relation. Even if no skill returns `airport` standalone, it's clearly
part of the live schema.

In the current corpus every field uses a primitive type (string,
number, boolean, datetime, text, integer, url, json), so this scanner
is expected to emit zero embedded targets today — but we wire it in so
the classifier remains correct when a shape-typed field lands.

Run:
    python3 audit_embedded_shapes.py [shapes_dir]

Importable API:
    scan_embedded_types(shapes_dir: Path)
        -> dict[str, list[tuple[str, str]]]   # {embedded: [(host, field)]}
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


# Types we treat as non-shape. Everything else is a candidate for being
# an embedded shape reference (filtered against the actual set of
# defined shapes below). Kept lowercase — we normalize input.
_PRIMITIVES: frozenset[str] = frozenset({
    "string",
    "text",
    "number",
    "integer",
    "float",
    "double",
    "decimal",
    "boolean",
    "bool",
    "datetime",
    "date",
    "time",
    "timestamp",
    "duration",
    "url",
    "uri",
    "email",
    "phone",
    "json",
    "array",
    "object",
    "map",
    "dict",
    "any",
    "null",
    "binary",
    "blob",
    "bytes",
    "id",
    "uuid",
    "enum",
})


def _strip_type(raw: str) -> str:
    """Pull the bare type name off a field shorthand, stripping `[]` and
    trailing whitespace/comments."""
    if not isinstance(raw, str):
        return ""
    first = raw.strip().split()[0] if raw.strip() else ""
    return first.rstrip("[]").rstrip()


def _default_shapes_dir() -> Path | None:
    here = Path(__file__).resolve()
    for ancestor in here.parents:
        candidate = ancestor / "site" / "docs" / "shapes"
        if candidate.is_dir():
            return candidate
        sibling = ancestor.parent / "site" / "docs" / "shapes"
        if sibling.is_dir():
            return sibling
    return None


def _iter_yamls(shapes_dir: Path) -> list[Path]:
    """Yield shape YAMLs, recursing one level into namespacing subdirs
    (e.g. `agentos/`) but skipping `_`-prefixed dirs."""
    files = list(shapes_dir.glob("*.yaml"))
    for sub in shapes_dir.iterdir():
        if sub.is_dir() and not sub.name.startswith("_"):
            files.extend(sub.glob("*.yaml"))
    return files


def _known_shapes(shapes_dir: Path) -> set[str]:
    return {p.stem for p in _iter_yamls(shapes_dir)}


def scan_embedded_types(
    shapes_dir: Path,
) -> dict[str, list[tuple[str, str]]]:
    """Scan shapes_dir and return {embedded_shape: [(host_shape, field_name), ...]}.

    A field's type is counted as "embedded" when:
      - it's a string (shorthand type declaration),
      - the bare name (after stripping `[]`) is not a primitive,
      - and the bare name matches another shape in shapes_dir.
    """
    known = _known_shapes(shapes_dir)
    index: dict[str, list[tuple[str, str]]] = {}

    for path in sorted(_iter_yamls(shapes_dir)):
        host = path.stem
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(data, dict):
            continue
        body = data.get(host, data)
        if not isinstance(body, dict):
            continue

        fields = body.get("fields") or {}
        if not isinstance(fields, dict):
            continue

        for field_name, type_val in fields.items():
            # Some shapes may use the long form `field: {type: foo}`.
            # Support it for forward-compat even though it's unused now.
            if isinstance(type_val, dict):
                type_val = type_val.get("type")

            bare = _strip_type(type_val) if isinstance(type_val, str) else ""
            if not bare:
                continue
            if bare.lower() in _PRIMITIVES:
                continue
            if bare == host:
                # A field typed as its own parent — treat as self-ref,
                # don't count as embedded.
                continue
            if bare not in known:
                continue
            index.setdefault(bare, []).append((host, str(field_name)))

    # Sort entries for stable output.
    return {k: sorted(set(v)) for k, v in index.items()}


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)

    if argv:
        shapes_dir = Path(argv[0]).expanduser().resolve()
    else:
        discovered = _default_shapes_dir()
        if discovered is None:
            print(
                "error: could not find shapes directory. "
                "Pass its path as the first argument.",
                file=sys.stderr,
            )
            return 2
        shapes_dir = discovered

    if not shapes_dir.is_dir():
        print(f"error: {shapes_dir} is not a directory", file=sys.stderr)
        return 2

    index = scan_embedded_types(shapes_dir)
    print(f"Shapes embedded as field types ({len(index)} unique):")
    if not index:
        print("  (none)")
        return 0

    name_width = max(len(k) for k in index)
    for embedded in sorted(index):
        refs = ", ".join(f"{h}.{f}" for h, f in index[embedded])
        print(f"  {embedded:<{name_width}}  ← embedded in: {refs}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
