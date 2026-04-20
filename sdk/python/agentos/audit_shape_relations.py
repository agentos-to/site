"""Audit shape-to-shape references via `relations:` and `also:` blocks.

Walks every `*.yaml` under a shapes directory and builds a reverse index
from *target* shape → list of *source* shapes (and the field/mechanism
that points to it). Answers the question: "which shapes are graph
targets pointed to by another shape, even if no skill directly produces
them?"

Two kinds of references are captured:

  1. `relations:` entries. Each is a shorthand `fieldName: target` or
     `fieldName: target[]`. The `[]` array marker is stripped. This is
     the dominant case.

  2. `also:` entries. Inheritance — `meeting:` declares `also: [event]`,
     meaning every meeting node IS-A event. Not a relation in the graph
     sense, but still introduces a hard reference from meeting → event
     that makes `event` a live part of the schema.

Run:
    python3 audit_shape_relations.py [shapes_dir]

Default shapes_dir = `<repo>/site/docs/shapes`, discovered by walking
up from this file until we find a sibling `site/` with `docs/shapes/`.

Importable API:
    scan_relation_targets(shapes_dir: Path) -> dict[str, list[str]]
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml


# Keyed references to source `shape.mechanism` (e.g. `account.owner`,
# `meeting.also`).
_SourceRef = str


def _strip_target(type_val: str) -> str:
    """Extract the bare target shape name from a relation shorthand.

    Relations in YAML look like:
        platform:   product       # inline comment
        follows:    account[]
        legs:       leg[]         # ordered sub-movements

    We take the first token, strip trailing `[]`, and ignore the rest.
    """
    if not isinstance(type_val, str):
        return ""
    first = type_val.strip().split()[0] if type_val.strip() else ""
    return first.rstrip("[]").rstrip()


def _default_shapes_dir() -> Path | None:
    """Find `<repo>/site/docs/shapes` by walking up from this file."""
    here = Path(__file__).resolve()
    for ancestor in here.parents:
        candidate = ancestor / "site" / "docs" / "shapes"
        if candidate.is_dir():
            return candidate
        # Sibling workspace layout: ~/dev/agentos/skills/... →
        # ~/dev/agentos/site/docs/shapes
        sibling = ancestor.parent / "site" / "docs" / "shapes"
        if sibling.is_dir():
            return sibling
    return None


def scan_relation_targets(shapes_dir: Path) -> dict[str, list[_SourceRef]]:
    """Scan shapes_dir and return a reverse index of relation/also targets.

    Returns a dict mapping target-shape-name → sorted list of source refs
    in the form `"<source_shape>.<field_name>"` (or `"<source>.also"`).

    Only references to names are captured — whether the target actually
    exists as a YAML file in shapes_dir is NOT checked here. Use the
    validator for that.
    """
    index: dict[str, list[_SourceRef]] = {}

    yaml_files = list(shapes_dir.glob("*.yaml"))
    for sub in shapes_dir.iterdir():
        if sub.is_dir() and not sub.name.startswith("_"):
            yaml_files.extend(sub.glob("*.yaml"))
    for path in sorted(yaml_files):
        source_name = path.stem
        try:
            data = yaml.safe_load(path.read_text(encoding="utf-8"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(data, dict):
            continue
        # Shape YAML convention: top-level key == filename stem. Fall
        # back to the whole doc if the body isn't nested.
        body = data.get(source_name, data)
        if not isinstance(body, dict):
            continue

        # ── relations: fieldName: target[]
        relations = body.get("relations") or {}
        if isinstance(relations, dict):
            for field_name, type_val in relations.items():
                target = _strip_target(type_val) if isinstance(type_val, str) else ""
                if not target:
                    continue
                index.setdefault(target, []).append(f"{source_name}.{field_name}")

        # ── also: [parent_shape, ...]
        also = body.get("also")
        if isinstance(also, list):
            for parent in also:
                if isinstance(parent, str) and parent.strip():
                    index.setdefault(parent.strip(), []).append(f"{source_name}.also")

    # Sort source-ref lists for stable output.
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

    index = scan_relation_targets(shapes_dir)
    print(f"Shape relation targets ({len(index)} unique):")
    if not index:
        print("  (none)")
        return 0

    # Column-align target names for a readable ragged-right table.
    name_width = max(len(k) for k in index)
    for target in sorted(index):
        sources = ", ".join(index[target])
        print(f"  {target:<{name_width}}  ← pointed to by: {sources}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
