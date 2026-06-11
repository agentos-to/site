"""Multi-attribute shape classifier.

A single shape can be many things at once:

  - produced by one or more **apps** (`@returns("foo")` in Python)
  - produced by one or more **engine** callsites (`ensure_tag("foo")` etc. in Rust)
  - a **relation target** — pointed to by another shape's `relations:` block
  - **embedded** — used as a nested field type inside another shape
  - **inherited via `also:`** — another shape declares `also: [foo]`

These are independent facts. A shape is only an **orphan** when *all five*
lists are empty — nobody produces it, nobody references it.

This module is the single source of truth for "who uses this shape";
`validate.py` calls into `classify(...)` and renders the union output.

Importable API:
    classify(
        shapes_dir: Path,
        apps_roots: Iterable[Path] | None = None,
        crates_roots: Iterable[Path] | None = None,
    ) -> dict[str, ShapeClassification]

CLI:
    python3 classify_orphans.py [shapes_dir]
"""

from __future__ import annotations

import ast
import glob
import os
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

import yaml

try:
    # Inside the `agentos` package (e.g. `python3 -m agentos.classify_orphans`).
    from .audit_embedded_shapes import scan_embedded_types
    from .audit_rust_const_usage import scan_const_usage
    from .audit_rust_producers import scan_rust_producers
    from .audit_shape_relations import scan_relation_targets
except ImportError:
    # Direct script invocation (`python3 classify_orphans.py`).
    from audit_embedded_shapes import scan_embedded_types  # type: ignore[no-redef]
    from audit_rust_const_usage import scan_const_usage  # type: ignore[no-redef]
    from audit_rust_producers import scan_rust_producers  # type: ignore[no-redef]
    from audit_shape_relations import scan_relation_targets  # type: ignore[no-redef]


# ─────────────────────────────────────────────────────────────────────────────
# Types
# ─────────────────────────────────────────────────────────────────────────────

# App decorators that mark a function as a tool. Mirrors validate.py.
_TOOL_MARKERS = {"run", "returns", "setup", "on_event", "provides"}

# Strings that appear in `@returns(...)` but are not shape names.
_NON_SHAPE_RETURNS = {
    "bool", "int", "float", "str", "string", "list", "dict", "any", "none",
    "binary", "bytes", "void",
}


@dataclass
class AppProducer:
    """One `@returns("shape")` callsite in an app."""
    app_id: str        # directory name of the app root
    file_rel: str        # path relative to app root, e.g. "operations.py"
    function: str        # function name
    line: int


@dataclass
class EngineProducer:
    """One Rust graph-API callsite in the engine."""
    file_rel: str        # e.g. "core/src/graph.rs"
    line: int
    api: str             # "ensure_tag" | "create_tagged_node" | etc.


@dataclass
class ShapeClassification:
    """Per-shape union of every place the name appears."""
    name: str
    app_producers: list[AppProducer] = field(default_factory=list)
    engine_producers: list[EngineProducer] = field(default_factory=list)
    relation_sources: list[str] = field(default_factory=list)   # "host.field"
    embedded_in: list[tuple[str, str]] = field(default_factory=list)  # (host, field)
    inherited_via: list[str] = field(default_factory=list)      # child shape names

    @property
    def is_orphan(self) -> bool:
        return not (
            self.app_producers
            or self.engine_producers
            or self.relation_sources
            or self.embedded_in
            or self.inherited_via
        )


# ─────────────────────────────────────────────────────────────────────────────
# App producer scan (AST over `@returns("...")`)
# ─────────────────────────────────────────────────────────────────────────────

def _decorator_name(dec: ast.expr) -> str | None:
    if isinstance(dec, ast.Name):
        return dec.id
    if isinstance(dec, ast.Attribute):
        return dec.attr
    if isinstance(dec, ast.Call):
        return _decorator_name(dec.func)
    return None


def _returns_shape(node: ast.FunctionDef | ast.AsyncFunctionDef) -> str | None:
    """Extract the shape name from `@returns("shape")` or `@returns("shape[]")`.
    Returns None for inline-dict schemas, primitives, or missing decorator."""
    for dec in node.decorator_list:
        if not isinstance(dec, ast.Call):
            continue
        if _decorator_name(dec) != "returns":
            continue
        if not dec.args:
            continue
        arg = dec.args[0]
        if isinstance(arg, ast.Constant) and isinstance(arg.value, str):
            base = arg.value.strip().rstrip("[]").rstrip()
            if base and base.lower() not in _NON_SHAPE_RETURNS:
                return base
        return None
    return None


def _is_tool(node: ast.AST) -> bool:
    if not isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
        return False
    if node.name.startswith("_"):
        return False
    for dec in node.decorator_list:
        if _decorator_name(dec) in _TOOL_MARKERS:
            return True
    return False


def _discover_app_roots(apps_dir: Path) -> list[Path]:
    """Every directory with a readme.md; skip `_`-prefixed trees."""
    roots: list[Path] = []
    for root, dirs, files in os.walk(apps_dir):
        dirs[:] = [d for d in dirs if not d.startswith("_")]
        if "readme.md" in files:
            roots.append(Path(root))
    return sorted(roots)


def _iter_app_py(app_dir: Path):
    for py in sorted(glob.glob(os.path.join(str(app_dir), "**", "*.py"), recursive=True)):
        rel = os.path.relpath(py, app_dir)
        if rel.startswith("_") or "/_" in rel or "/vendor/" in rel:
            continue
        try:
            with open(py, encoding="utf-8") as f:
                src = f.read()
            tree = ast.parse(src, filename=py)
        except (SyntaxError, UnicodeDecodeError, OSError):
            continue
        yield rel, tree


def scan_app_producers(
    apps_roots: Iterable[Path],
) -> dict[str, list[AppProducer]]:
    """Return {shape_name: [AppProducer, ...]}."""
    out: dict[str, list[AppProducer]] = {}
    for root in apps_roots:
        if not root or not Path(root).is_dir():
            continue
        for app_dir in _discover_app_roots(Path(root)):
            app_id = app_dir.name
            for rel, tree in _iter_app_py(app_dir):
                for node in tree.body:
                    if not _is_tool(node):
                        continue
                    shape = _returns_shape(node)
                    if not shape:
                        continue
                    out.setdefault(shape, []).append(
                        AppProducer(
                            app_id=app_id,
                            file_rel=rel,
                            function=node.name,
                            line=node.lineno,
                        )
                    )
    for shape in out:
        out[shape].sort(key=lambda p: (p.app_id, p.file_rel, p.line))
    return out


# ─────────────────────────────────────────────────────────────────────────────
# Path discovery
# ─────────────────────────────────────────────────────────────────────────────

def _find_workspace_root() -> Path | None:
    """Walk up from this file until we find `<root>/site/docs/shapes`."""
    here = Path(__file__).resolve()
    for ancestor in here.parents:
        if (ancestor / "site" / "docs" / "shapes").is_dir():
            return ancestor
        if (ancestor.parent / "site" / "docs" / "shapes").is_dir():
            return ancestor.parent
    return None


def _default_shapes_dir() -> Path | None:
    root = _find_workspace_root()
    return (root / "site" / "docs" / "shapes") if root else None


def _default_apps_roots() -> list[Path]:
    root = _find_workspace_root()
    if not root:
        return []
    candidates = [root / "apps"]
    return [p for p in candidates if p.is_dir()]


def _default_crates_roots() -> list[Path]:
    root = _find_workspace_root()
    if not root:
        return []
    candidates = [root / "core" / "crates"]
    return [p for p in candidates if p.is_dir()]


def _generated_rs_for(crates_root: Path) -> Path | None:
    """Find the generated `shapes` module of the contract crate, relative to
    a crates root."""
    candidate = Path(crates_root) / "contract-generated" / "src" / "shapes.rs"
    return candidate if candidate.is_file() else None


# ─────────────────────────────────────────────────────────────────────────────
# Shape files
# ─────────────────────────────────────────────────────────────────────────────

def _all_shape_names(shapes_dir: Path) -> set[str]:
    """Shapes at the top level + namespacing subdirs (e.g. `agentos/`).
    Anything under `_`-prefixed subdirs (e.g. `_draft/`) is excluded —
    those are speculative/not-yet-wired."""
    names: set[str] = set()
    for p in shapes_dir.glob("*.yaml"):
        if p.is_file():
            names.add(p.stem)
    for sub in shapes_dir.iterdir():
        if sub.is_dir() and not sub.name.startswith("_"):
            for p in sub.glob("*.yaml"):
                if p.is_file():
                    names.add(p.stem)
    return names


def _find_shape_path(shapes_dir: Path, shape: str) -> Path:
    """Resolve a shape name to its YAML path, checking subdirs."""
    direct = shapes_dir / f"{shape}.yaml"
    if direct.is_file():
        return direct
    for sub in shapes_dir.iterdir():
        if sub.is_dir() and not sub.name.startswith("_"):
            candidate = sub / f"{shape}.yaml"
            if candidate.is_file():
                return candidate
    return direct  # caller will hit OSError on read; preserves error path


def _read_description(shapes_dir: Path, shape: str) -> str:
    path = _find_shape_path(shapes_dir, shape)
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError:
        return "(file unreadable)"
    try:
        data = yaml.safe_load(raw)
    except yaml.YAMLError:
        data = None
    if isinstance(data, dict):
        body = data.get(shape, data)
        if isinstance(body, dict):
            desc = body.get("description")
            if isinstance(desc, str) and desc.strip():
                return desc.strip().splitlines()[0]
    for line in raw.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            text = s[1:].lstrip()
            if text:
                return text
        else:
            break
    return "(no description)"


# ─────────────────────────────────────────────────────────────────────────────
# Main classifier
# ─────────────────────────────────────────────────────────────────────────────

def classify(
    shapes_dir: Path,
    apps_roots: Iterable[Path] | None = None,
    crates_roots: Iterable[Path] | None = None,
) -> dict[str, ShapeClassification]:
    """Build a per-shape classification record.

    Every shape defined in `shapes_dir` gets a record. Producer lists are
    populated from every `apps_roots` tree (Python AST) and every
    `crates_roots` tree (Rust scanner). Relation/embedded/inheritance
    come from the shape YAMLs themselves.
    """
    apps = list(apps_roots) if apps_roots is not None else _default_apps_roots()
    crates = list(crates_roots) if crates_roots is not None else _default_crates_roots()

    all_shapes = _all_shape_names(shapes_dir)

    app_map = scan_app_producers(apps)
    engine_map: dict[str, list[EngineProducer]] = {}
    for crates_root in crates:
        crates_root = Path(crates_root)
        # 1) Literal callsites — `ensure_tag("foo")`, etc. Remaining after
        #    the Phase 1 const migration will be a small set (newly-added
        #    code or shapes not yet in the generated `shapes.rs`).
        for tag, sites in scan_rust_producers(crates_root).items():
            bucket = engine_map.setdefault(tag, [])
            for file_path, line, api in sites:
                try:
                    rel = str(Path(file_path).relative_to(crates_root.parent))
                except ValueError:
                    rel = str(file_path)
                bucket.append(EngineProducer(file_rel=rel, line=line, api=api))

        # 2) Const references — `shapes::FOO`. These resolve to shape
        #    names via the generated const table (`FOO → "foo"`).
        generated = _generated_rs_for(crates_root)
        if generated is not None:
            report = scan_const_usage(crates_root, generated)
            const_to_value: dict[str, str] = report.get("_const_to_value", {})
            usage: dict[str, list[tuple[Path, int, str]]] = report.get("usage", {})
            for const_name, sites in usage.items():
                shape = const_to_value.get(const_name)
                if not shape:
                    continue
                bucket = engine_map.setdefault(shape, [])
                for file_path, line, text in sites:
                    try:
                        rel = str(Path(file_path).relative_to(crates_root.parent))
                    except ValueError:
                        rel = str(file_path)
                    bucket.append(EngineProducer(file_rel=rel, line=line, api=text))
    for shape in engine_map:
        # Dedup + stable order. (file, line, api) identifies a callsite.
        seen: set[tuple[str, int, str]] = set()
        unique: list[EngineProducer] = []
        for p in sorted(engine_map[shape], key=lambda p: (p.file_rel, p.line, p.api)):
            key = (p.file_rel, p.line, p.api)
            if key in seen:
                continue
            seen.add(key)
            unique.append(p)
        engine_map[shape] = unique

    relation_map = scan_relation_targets(shapes_dir)
    embedded_map = scan_embedded_types(shapes_dir)

    out: dict[str, ShapeClassification] = {}
    for shape in sorted(all_shapes):
        rec = ShapeClassification(name=shape)
        rec.app_producers = app_map.get(shape, [])
        rec.engine_producers = engine_map.get(shape, [])

        # Split relation sources: `.also` entries are inheritance, not
        # relation-target references. The scanner unions them — separate.
        for ref in relation_map.get(shape, []):
            if ref.endswith(".also"):
                child = ref[: -len(".also")]
                rec.inherited_via.append(child)
            else:
                rec.relation_sources.append(ref)
        rec.relation_sources.sort()
        rec.inherited_via.sort()

        rec.embedded_in = sorted(embedded_map.get(shape, []))
        out[shape] = rec
    return out


# ─────────────────────────────────────────────────────────────────────────────
# CLI rendering
# ─────────────────────────────────────────────────────────────────────────────

def _render(records: dict[str, ShapeClassification], shapes_dir: Path) -> None:
    orphans = [r for r in records.values() if r.is_orphan]
    produced_by_app = [r for r in records.values() if r.app_producers]
    produced_by_engine = [r for r in records.values() if r.engine_producers]
    schema_only = [
        r for r in records.values()
        if not r.app_producers
        and not r.engine_producers
        and (r.relation_sources or r.embedded_in or r.inherited_via)
    ]

    print(f"Classified {len(records)} shapes in {shapes_dir}")
    print(
        f"  app-produced={len(produced_by_app)}  "
        f"engine-produced={len(produced_by_engine)}  "
        f"schema-only={len(schema_only)}  "
        f"orphan={len(orphans)}"
    )

    _print_section("ORPHAN (no producer, no reference)", orphans, shapes_dir)
    _print_section("SCHEMA-ONLY (referenced but not produced)", schema_only, shapes_dir)
    _print_detail(records, shapes_dir)


def _print_section(header: str, records: list[ShapeClassification], shapes_dir: Path) -> None:
    print(f"\n{header} ({len(records)}):")
    if not records:
        print("  (none)")
        return
    width = max((len(r.name) for r in records), default=0)
    for rec in sorted(records, key=lambda r: r.name):
        desc = _read_description(shapes_dir, rec.name)
        print(f"  {rec.name:<{width}}  {desc}")


def _print_detail(records: dict[str, ShapeClassification], shapes_dir: Path) -> None:
    print("\nPER-SHAPE DETAIL:")
    for shape in sorted(records):
        rec = records[shape]
        bits: list[str] = []
        if rec.app_producers:
            ids = sorted({p.app_id for p in rec.app_producers})
            bits.append(f"apps: {', '.join(ids)}")
        if rec.engine_producers:
            bits.append(f"engine: {len(rec.engine_producers)} callsites")
        if rec.relation_sources:
            bits.append(f"relations: {', '.join(rec.relation_sources)}")
        if rec.embedded_in:
            bits.append(
                "embedded: "
                + ", ".join(f"{h}.{f}" for h, f in rec.embedded_in)
            )
        if rec.inherited_via:
            bits.append(f"inherited: {', '.join(rec.inherited_via)}")
        suffix = "  [" + "; ".join(bits) + "]" if bits else "  [ORPHAN]"
        print(f"  {shape}{suffix}")


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

    records = classify(shapes_dir)
    _render(records, shapes_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
