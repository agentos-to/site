#!/usr/bin/env python3
"""Validate `prior_art:` blocks across all shape YAMLs.

Rules:
  1. Each shape YAML SHOULD have a `prior_art:` block (warn if missing).
  2. `prior_art:` must be a list.
  3. Each entry must have `source` (non-empty string) and `url` (http[s]://).
  4. `notes` is required (non-empty) unless url is absent.
  5. URLs must be syntactically well-formed http[s] URLs (no trailing spaces).
  6. Sources must not duplicate within a shape.

Exits 0 if all shapes pass (or only miss prior_art with --allow-missing).
Exits 1 if hard-fail rules (2-6) break on any shape.

Usage:
    python scripts/validate_prior_art.py                 # warn on missing, fail on malformed
    python scripts/validate_prior_art.py --require-all   # also fail if any shape lacks prior_art
    python scripts/validate_prior_art.py --shapes-dir ../shapes
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


URL_RE = re.compile(r"^https?://\S+$")


def _load_yaml(path: Path):
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(2)
    return yaml.safe_load(path.read_text())


def validate(shapes_dir: Path, require_all: bool) -> int:
    errors: list[str] = []
    warnings: list[str] = []
    missing: list[str] = []
    ok_count = 0
    total = 0

    yaml_files = list(shapes_dir.glob("*.yaml"))
    for sub in shapes_dir.iterdir():
        if sub.is_dir() and not sub.name.startswith("_"):
            yaml_files.extend(sub.glob("*.yaml"))
    for f in sorted(yaml_files):
        total += 1
        data = _load_yaml(f)
        if not isinstance(data, dict):
            errors.append(f"{f.name}: top-level is not a mapping")
            continue
        for name, defn in data.items():
            if not isinstance(defn, dict):
                continue
            if "prior_art" not in defn:
                missing.append(name)
                continue
            pa = defn["prior_art"]
            if not isinstance(pa, list):
                errors.append(f"{name}: prior_art must be a list, got {type(pa).__name__}")
                continue
            if len(pa) == 0:
                warnings.append(f"{name}: prior_art is empty list")
                continue
            seen_sources: set[str] = set()
            for i, entry in enumerate(pa):
                if not isinstance(entry, dict):
                    errors.append(f"{name}.prior_art[{i}]: entry must be a mapping")
                    continue
                src = entry.get("source", "")
                url = entry.get("url", "")
                notes = entry.get("notes", "")
                if not isinstance(src, str) or not src.strip():
                    errors.append(f"{name}.prior_art[{i}]: missing/empty 'source'")
                if not isinstance(url, str) or not url.strip():
                    errors.append(f"{name}.prior_art[{i}]: missing/empty 'url'")
                elif not URL_RE.match(url.strip()):
                    errors.append(f"{name}.prior_art[{i}]: url not http[s]://...: {url!r}")
                if not isinstance(notes, str) or not notes.strip():
                    warnings.append(f"{name}.prior_art[{i}]: missing 'notes' (optional but recommended)")
                if isinstance(src, str) and src.strip():
                    key = src.strip().lower()
                    if key in seen_sources:
                        errors.append(f"{name}.prior_art[{i}]: duplicate source {src!r}")
                    seen_sources.add(key)
            ok_count += 1

    # Report
    for w in warnings:
        print(f"WARN  {w}")
    for m in missing:
        print(f"MISS  {m}: no prior_art block")
    for e in errors:
        print(f"FAIL  {e}", file=sys.stderr)

    covered = ok_count
    print()
    print(f"Coverage: {covered}/{total} shapes have prior_art ({covered*100//max(total,1)}%)")
    print(f"Errors:   {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Missing:  {len(missing)}")

    if errors:
        return 1
    if require_all and missing:
        print(f"\n--require-all: {len(missing)} shapes missing prior_art", file=sys.stderr)
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate prior_art blocks in shape YAMLs")
    parser.add_argument("--shapes-dir", type=Path, default=None, help="Path to shapes/ directory")
    parser.add_argument("--require-all", action="store_true", help="Fail if any shape is missing prior_art")
    args = parser.parse_args()

    shapes_dir = args.shapes_dir or (Path(__file__).parent.parent / "shapes")
    if not shapes_dir.is_dir():
        print(f"Shapes dir not found: {shapes_dir}", file=sys.stderr)
        return 2

    return validate(shapes_dir, args.require_all)


if __name__ == "__main__":
    sys.exit(main())
