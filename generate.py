#!/usr/bin/env python3
"""Shape codegen — YAML → typed code for SDK packages.

Reads shape definitions (from YAML files or the graph API), resolves
inheritance (`also` chains) and relations, then writes typed classes
directly into the SDK packages that use them.

Usage:
    python generate.py                        # Python + TypeScript into SDK packages
    python generate.py --lang python          # Python TypedDicts only
    python generate.py --from-api             # load shapes from graph instead of YAML
    python generate.py --from-api --dump-yaml ./shapes  # export graph → YAML
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# =============================================================================
# Intermediate representation
# =============================================================================

STANDARD_FIELDS = [
    ("id", "string"),
    ("name", "string"),
    ("text", "string"),
    ("url", "string"),
    ("image", "string"),
    ("author", "string"),
    ("datePublished", "string"),
    ("content", "string"),
]


@dataclass
class Field:
    name: str           # original YAML name (snake_case, may have dots)
    type: str           # shape type: string, integer, number, boolean, datetime, url, json, string[]
    is_relation: bool
    is_array: bool
    target: str | None  # for relations: target shape name (e.g. "author", "account")


@dataclass
class Shape:
    name: str           # YAML name (snake_case)
    class_name: str     # PascalCase
    fields: list[Field] = field(default_factory=list)
    # Below fields are ignored by language emitters; used by the MDX doc emitter.
    also: list[str] = field(default_factory=list)           # raw `also:` list (tag chain)
    plural: str | None = None
    subtitle: str | None = None
    identity: list[str] = field(default_factory=list)        # `identity:` field names (compound — all must match)
    identity_any: list[str] = field(default_factory=list)    # `identity_any:` field names (any one match suffices)
    leading_comment: str = ""                                # top-of-file `# ...` lines, stripped
    own_fields: list[Field] = field(default_factory=list)    # fields declared on THIS shape, not inherited
    own_relations: list[Field] = field(default_factory=list) # relations declared on THIS shape
    prior_art: list[dict] = field(default_factory=list)      # [{source, url, notes}, ...] — external standards this shape aligns with
    source_path: str | None = None                            # relative path of the YAML file that defined this shape (e.g. "account.yaml", "agentos/theme.yaml")
    raw_body: str = ""                                         # original YAML body as read from disk (or as serialised back from graph api). Used by SHAPE_YAMLS codegen.


# =============================================================================
# Loader — YAML → intermediate representation
# =============================================================================

def _camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case. Leaves snake_case unchanged."""
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", name).lower()


def to_class_name(name: str) -> str:
    snake = _camel_to_snake(name).replace("-", "_")
    return "".join(w.capitalize() for w in snake.split("_"))


def _strip_code_fences(text: str) -> str:
    """Strip markdown code fences from CLI JSON output."""
    if text.startswith("```"):
        text = "\n".join(text.split("\n")[1:])
    if text.endswith("```"):
        text = "\n".join(text.split("\n")[:-1])
    return text


def _dump_yaml_from_api(agentos_bin: str, out_dir: Path) -> None:
    """Export each shape from the graph as a standalone YAML file (backup/restore)."""
    import json
    import subprocess
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    result = subprocess.run(
        [agentos_bin, "call", "read", json.dumps({"tags": "shape", "view": {"format": "json"}, "limit": 200})],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Failed to list shapes: {result.stderr}", file=sys.stderr)
        return

    listing = json.loads(_strip_code_fences(result.stdout.strip()))
    nodes = listing.get("data", [])
    out_dir.mkdir(parents=True, exist_ok=True)
    dumped = 0

    for node in nodes:
        name = node.get("name", "")
        node_id = node.get("id", "")
        if not name or not node_id:
            continue

        r = subprocess.run(
            [agentos_bin, "call", "read", json.dumps({"id": node_id, "view": {"format": "json"}})],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            continue

        node_data = json.loads(_strip_code_fences(r.stdout.strip()))
        content = node_data.get("content", "")
        if not content:
            continue

        # Wrap in top-level name key to match original YAML format
        defn = yaml.safe_load(content)
        yaml_out = yaml.dump({name: defn}, default_flow_style=False, sort_keys=False, allow_unicode=True)
        (out_dir / f"{name}.yaml").write_text(yaml_out)
        dumped += 1

    print(f"  Dumped {dumped} shape YAML files to {out_dir}")


def load_shapes_from_api(agentos_bin: str) -> list[Shape]:
    """Load shapes from the graph via `agentos call` CLI."""
    import json
    import subprocess
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    # List all shape-tagged nodes
    result = subprocess.run(
        [agentos_bin, "call", "read", json.dumps({"tags": "shape", "view": {"format": "json"}, "limit": 200})],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        print(f"Failed to list shapes: {result.stderr}", file=sys.stderr)
        sys.exit(1)

    listing = json.loads(_strip_code_fences(result.stdout.strip()))
    nodes = listing.get("data", [])
    print(f"Found {len(nodes)} shapes on graph")

    # Read each shape's content body
    raw: dict[str, dict] = {}
    for node in nodes:
        shape_name = node.get("name", "")
        node_id = node.get("id", "")
        if not shape_name or not node_id:
            continue

        r = subprocess.run(
            [agentos_bin, "call", "read", json.dumps({"id": node_id, "view": {"format": "json"}})],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(f"  Warning: failed to read {shape_name}: {r.stderr}", file=sys.stderr)
            continue

        node_data = json.loads(_strip_code_fences(r.stdout.strip()))
        content = node_data.get("content", "")
        if not content:
            print(f"  Warning: {shape_name} has no content body, skipping", file=sys.stderr)
            continue

        defn = yaml.safe_load(content)
        if isinstance(defn, dict):
            raw[shape_name] = defn

    return _build_shapes(raw, {})


def load_shapes(shapes_dir: Path) -> list[Shape]:
    """Load shapes from YAML files on disk."""
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    raw: dict[str, dict] = {}
    comments: dict[str, str] = {}
    source_paths: dict[str, str] = {}
    # Recurse one level into namespacing subdirs (e.g. `agentos/`) but skip
    # `_`-prefixed dirs (`_draft/`).
    yaml_files = list(shapes_dir.glob("*.yaml"))
    for sub in sorted(p for p in shapes_dir.iterdir() if p.is_dir() and not p.name.startswith("_")):
        yaml_files.extend(sub.glob("*.yaml"))
    for f in sorted(yaml_files):
        text = f.read_text()
        data = yaml.safe_load(text)
        if data and isinstance(data, dict):
            # Capture leading `# ...` comment block (before first non-comment, non-blank line).
            lead_lines = []
            for line in text.splitlines():
                stripped = line.strip()
                if stripped.startswith("#"):
                    lead_lines.append(stripped.lstrip("#").strip())
                elif stripped == "":
                    continue
                else:
                    break
            lead = "\n".join(lead_lines).strip()
            rel_path = f.relative_to(shapes_dir).as_posix()
            for name, defn in data.items():
                if isinstance(defn, dict):
                    raw[name] = defn
                    if lead:
                        comments[name] = lead
                    source_paths[name] = rel_path

    return _build_shapes(raw, comments, source_paths)


def _build_shapes(
    raw: dict[str, dict],
    comments: dict[str, str] | None = None,
    source_paths: dict[str, str] | None = None,
) -> list[Shape]:
    """Convert raw shape dicts into Shape objects with resolved inheritance."""
    comments = comments or {}
    source_paths = source_paths or {}

    def resolve_fields(name: str, seen: set | None = None) -> dict[str, str]:
        if seen is None:
            seen = set()
        if name in seen:
            return {}
        seen.add(name)
        defn = raw.get(name, {})
        fields = {}
        for also in defn.get("also", []):
            fields.update(resolve_fields(also, seen))
        for fname, ftype in (defn.get("fields") or {}).items():
            fields[fname] = str(ftype)
        return fields

    def resolve_relations(name: str, seen: set | None = None) -> dict[str, str]:
        if seen is None:
            seen = set()
        if name in seen:
            return {}
        seen.add(name)
        defn = raw.get(name, {})
        rels = {}
        for also in defn.get("also", []):
            rels.update(resolve_relations(also, seen))
        for label, target in (defn.get("relations") or {}).items():
            rels[label] = str(target)
        return rels

    shapes = []
    for shape_name in sorted(raw.keys()):
        defn = raw.get(shape_name, {})
        s = Shape(name=shape_name, class_name=to_class_name(shape_name))

        # Metadata used by the doc emitter
        s.also = list(defn.get("also") or [])
        s.plural = defn.get("plural")
        s.subtitle = defn.get("subtitle")
        if "identity" in defn:
            ident = defn["identity"]
            s.identity = ident if isinstance(ident, list) else [ident]
        if "identity_any" in defn:
            ident_any = defn["identity_any"]
            s.identity_any = ident_any if isinstance(ident_any, list) else [ident_any]
        s.leading_comment = comments.get(shape_name, "")
        s.source_path = source_paths.get(shape_name)

        # Raw YAML body for this shape — the inner mapping (fields, identity,
        # relations, also, ...), not the outer `shape_name:` wrapper. Rust's
        # `RawShape` deserialises from exactly this form, so we dump the
        # parsed defn back to YAML (canonicalised — key order comes from dict
        # insertion order, which Python preserves on py>=3.7).
        try:
            import yaml as _yaml
            s.raw_body = _yaml.safe_dump(defn, sort_keys=False, default_flow_style=False)
        except Exception:
            s.raw_body = ""

        # Prior art — optional list of external standards this shape aligns with.
        pa = defn.get("prior_art") or []
        if isinstance(pa, list):
            for entry in pa:
                if isinstance(entry, dict) and entry.get("source"):
                    s.prior_art.append({
                        "source": str(entry.get("source", "")).strip(),
                        "url": str(entry.get("url", "")).strip(),
                        "notes": str(entry.get("notes", "")).strip(),
                    })

        # Own fields — declared on THIS shape only (not inherited).
        for fname, ftype in (defn.get("fields") or {}).items():
            is_array = str(ftype).endswith("[]")
            s.own_fields.append(Field(fname, str(ftype), False, is_array, None))
        for label, target in (defn.get("relations") or {}).items():
            tgt_s = str(target)
            is_array = tgt_s.endswith("[]")
            s.own_relations.append(Field(label, tgt_s, True, is_array, tgt_s.rstrip("[]")))

        # Standard fields first
        for wk_name, wk_type in STANDARD_FIELDS:
            s.fields.append(Field(wk_name, wk_type, False, False, None))

        # Shape-declared fields
        for fname, ftype in sorted(resolve_fields(shape_name).items()):
            if any(sf[0] == fname for sf in STANDARD_FIELDS):
                continue
            is_array = ftype.endswith("[]")
            base = ftype.rstrip("[]") if is_array else ftype
            s.fields.append(Field(fname, ftype, False, is_array, None))

        # Relations
        for label, target in sorted(resolve_relations(shape_name).items()):
            is_array = target.endswith("[]")
            target_name = target.rstrip("[]")
            s.fields.append(Field(label, target, True, is_array, target_name))

        shapes.append(s)

    return shapes


# =============================================================================
# Python emitter — TypedDict
# =============================================================================

_PY_TYPES = {
    "string": "str", "text": "str", "integer": "int", "number": "float",
    "boolean": "bool", "datetime": "str", "url": "str", "json": "Any",
    "string[]": "list[str]", "integer[]": "list[int]",
}

_PY_RESERVED = {
    "from", "import", "class", "return", "def", "if", "else", "for",
    "while", "with", "as", "try", "except", "finally", "raise", "pass",
    "break", "continue", "and", "or", "not", "in", "is", "lambda",
    "global", "nonlocal", "yield", "assert", "del", "True", "False", "None",
}


def emit_python(shapes: list[Shape]) -> str:
    lines = [
        '"""Auto-generated TypedDict classes from shape YAML — do not edit.',
        "",
        f"Generated from {len(shapes)} shapes.",
        "Regenerate with: python generate.py --lang python",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, TypedDict",
        "",
    ]

    for s in shapes:
        lines.append(f"class {s.class_name}(TypedDict, total=False):")
        for f in s.fields:
            safe = _py_field_name(f.name)
            comment = f"  # {f.name}" if safe != f.name else ""
            ty = _py_type(f, s)
            lines.append(f"    {safe}: {ty}{comment}")
        lines.append("")
        lines.append("")

    # SHAPE_YAMLS: raw YAML body per shape. The skill worker attaches the
    # matching entry as `__shape_yaml__` on every @returns(shape) response so
    # the Rust engine can upsert the definition on the graph with a single
    # byte-compare — no reparse, no field-by-field merger. The body matches
    # what the Rust ShapeHandle carries via include_str!, so SHAPE_YAMLS is
    # the Python mirror of the shapes-generated crate.
    lines.append("# Raw YAML bodies — consumed by the skill worker to attach")
    lines.append("# `__shape_yaml__` on every @returns(shape) response.")
    lines.append("SHAPE_YAMLS: dict[str, str] = {")
    for s in shapes:
        if not s.raw_body:
            continue
        lines.append(f"    {s.name!r}: {s.raw_body!r},")
    lines.append("}")
    lines.append("")

    # Identity sidecars — the skill worker attaches these as
    # `__shape_identity__` and `__shape_identity_any__` next to
    # `__shape_yaml__` on every @returns(shape) response, so the Rust
    # engine can drive identity-based upserts without parsing YAML or
    # consulting any in-process registry.
    lines.append("# Identity keys per shape — sidecars for the skill worker.")
    lines.append("SHAPE_IDENTITIES: dict[str, list[str]] = {")
    for s in shapes:
        if not s.identity:
            continue
        lines.append(f"    {s.name!r}: {list(s.identity)!r},")
    lines.append("}")
    lines.append("")
    lines.append("SHAPE_IDENTITIES_ANY: dict[str, list[str]] = {")
    for s in shapes:
        if not s.identity_any:
            continue
        lines.append(f"    {s.name!r}: {list(s.identity_any)!r},")
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def _py_field_name(name: str) -> str:
    if "." in name:
        return name.replace(".", "_")
    if name in _PY_RESERVED:
        return f"{name}_"
    return name


def _py_type(f: Field, s: Shape) -> str:
    if f.is_relation:
        cls = to_class_name(f.target)
        return f"list[{cls}]" if f.is_array else cls
    return _PY_TYPES.get(f.type, "Any")


# =============================================================================
# TypeScript emitter — interfaces
# =============================================================================

_TS_TYPES = {
    "string": "string", "text": "string", "integer": "number",
    "number": "number", "boolean": "boolean", "datetime": "string",
    "url": "string", "json": "unknown",
    "string[]": "string[]", "integer[]": "number[]",
}


def emit_typescript(shapes: list[Shape]) -> str:
    lines = [
        "// Auto-generated from shape YAML — do not edit.",
        f"// Generated from {len(shapes)} shapes.",
        "// Regenerate with: python generate.py --lang typescript",
        "",
    ]

    for s in shapes:
        lines.append(f"export interface {s.class_name} {{")
        for f in s.fields:
            name = _ts_field_name(f.name)
            ty = _ts_type(f)
            lines.append(f"    {name}?: {ty};")
        lines.append("}")
        lines.append("")

    return "\n".join(lines)


def _ts_field_name(name: str) -> str:
    if "." in name:
        return _to_camel(name.replace(".", "_"))
    return _to_camel(name)


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(w.capitalize() for w in parts[1:])


def _ts_type(f: Field) -> str:
    if f.is_relation:
        cls = to_class_name(f.target)
        return f"{cls}[]" if f.is_array else cls
    return _TS_TYPES.get(f.type, "unknown")


# =============================================================================
# Swift emitter — Codable structs
# =============================================================================

_SWIFT_TYPES = {
    "string": "String", "text": "String", "integer": "Int",
    "number": "Double", "boolean": "Bool", "datetime": "String",
    "url": "String", "json": "AnyCodable",
    "string[]": "[String]", "integer[]": "[Int]",
}

_SWIFT_RESERVED = {
    "class", "struct", "enum", "protocol", "func", "var", "let", "import",
    "return", "if", "else", "for", "while", "switch", "case", "default",
    "break", "continue", "in", "as", "is", "self", "Self", "true", "false",
    "nil", "operator", "typealias", "associatedtype", "throw", "throws",
    "try", "catch", "where", "guard", "repeat", "defer", "do",
}


def emit_swift(shapes: list[Shape]) -> str:
    lines = [
        "// Auto-generated from shape YAML — do not edit.",
        f"// Generated from {len(shapes)} shapes.",
        "// Regenerate with: python generate.py --lang swift",
        "",
        "import Foundation",
        "",
    ]

    for s in shapes:
        lines.append(f"struct {s.class_name}: Codable {{")

        # Properties
        needs_coding_keys = False
        for f in s.fields:
            swift_name = _swift_field_name(f.name)
            ty = _swift_type(f)
            lines.append(f"    var {swift_name}: {ty}?")
            if swift_name != f.name:
                needs_coding_keys = True

        # CodingKeys enum (only if any field name differs)
        if needs_coding_keys:
            lines.append("")
            lines.append("    enum CodingKeys: String, CodingKey {")
            simple = []
            mapped = []
            for f in s.fields:
                swift_name = _swift_field_name(f.name)
                if swift_name == f.name:
                    simple.append(swift_name)
                else:
                    mapped.append((swift_name, f.name))
            if simple:
                lines.append(f"        case {', '.join(simple)}")
            for swift_name, orig in mapped:
                lines.append(f'        case {swift_name} = "{orig}"')
            lines.append("    }")

        lines.append("}")
        lines.append("")

    return "\n".join(lines)


def _swift_field_name(name: str) -> str:
    # Dots to camelCase
    if "." in name:
        name = name.replace(".", "_")
    # snake_case to camelCase
    name = _to_camel(name)
    if name in _SWIFT_RESERVED:
        return f"`{name}`"
    return name


def _swift_type(f: Field) -> str:
    if f.is_relation:
        cls = to_class_name(f.target)
        return f"[{cls}]" if f.is_array else cls
    return _SWIFT_TYPES.get(f.type, "AnyCodable")


# =============================================================================
# Go emitter — structs with json tags
# =============================================================================

_GO_TYPES = {
    "string": "string", "text": "string", "integer": "int",
    "number": "float64", "boolean": "bool", "datetime": "string",
    "url": "string", "json": "any",
    "string[]": "[]string", "integer[]": "[]int",
}

_GO_RESERVED = {
    "break", "case", "chan", "const", "continue", "default", "defer",
    "else", "fallthrough", "for", "func", "go", "goto", "if", "import",
    "interface", "map", "package", "range", "return", "select", "struct",
    "switch", "type", "var",
}


def emit_go(shapes: list[Shape]) -> str:
    lines = [
        "// Auto-generated from shape YAML — do not edit.",
        f"// Generated from {len(shapes)} shapes.",
        "// Regenerate with: python generate.py --lang go",
        "",
        "package shapes",
        "",
    ]

    for s in shapes:
        lines.append(f"type {s.class_name} struct {{")
        for f in s.fields:
            go_name = _go_field_name(f.name)
            ty = _go_type(f)
            tag = f.name
            lines.append(f'\t{go_name} {ty} `json:"{tag},omitempty"`')
        lines.append("}")
        lines.append("")

    return "\n".join(lines)


def _go_field_name(name: str) -> str:
    if "." in name:
        name = name.replace(".", "_")
    # Normalize camelCase to snake_case first, then PascalCase
    snake = _camel_to_snake(name)
    result = "".join(w.capitalize() for w in snake.split("_"))
    # Common initialisms
    for initialism in ("Id", "Url", "Html", "Http", "Isbn", "Dns", "Ip", "Ssh", "Ssl", "Tls", "Api"):
        if result.endswith(initialism) or result == initialism:
            result = result[: -len(initialism)] + initialism.upper()
    if result in _GO_RESERVED:
        result += "_"
    return result


def _go_type(f: Field) -> str:
    if f.is_relation:
        cls = to_class_name(f.target)
        return f"[]{cls}" if f.is_array else f"*{cls}"
    base = _GO_TYPES.get(f.type, "any")
    if f.is_array:
        return base  # already has [] prefix for known array types
    return f"*{base}"  # pointer for optional


# =============================================================================
# Rust emitter — ShapeHandle statics for the engine SDK crate
# =============================================================================

# Reserved Rust keywords that can't be used as identifiers directly.
# (2024 edition list; we prefix with `r#` where needed.)
_RUST_RESERVED = {
    "as", "break", "const", "continue", "crate", "dyn", "else", "enum",
    "extern", "false", "fn", "for", "if", "impl", "in", "let", "loop",
    "match", "mod", "move", "mut", "pub", "ref", "return", "self", "Self",
    "static", "struct", "super", "trait", "true", "type", "unsafe", "use",
    "where", "while", "async", "await", "abstract", "become", "box", "do",
    "final", "macro", "override", "priv", "try", "typeof", "unsized",
    "virtual", "yield", "union",
}


def _rust_ident(shape_name: str) -> str:
    """Convert a shape name to a SCREAMING_SNAKE_CASE Rust identifier."""
    # `git_commit` → `GIT_COMMIT`; `dns_record` → `DNS_RECORD`.
    ident = shape_name.upper().replace("-", "_").replace(".", "_")
    if ident.lower() in _RUST_RESERVED:
        ident = f"{ident}_"
    return ident


def emit_rust(shapes: list[Shape]) -> str:
    """Emit `pub static` ShapeHandle per shape with inline YAML body.

    The body embedded in each handle is the INNER mapping (fields, identity,
    relations, also, ...) — not the outer `shape_name: {...}` wrapper. That
    matches what Rust's `RawShape` deserialises from, and keeps the body
    byte-identical to Python's `SHAPE_YAMLS[name]` so lazy upsert from
    either side produces the same graph content.
    """
    # Stable ordering by shape name.
    shapes_sorted = sorted(shapes, key=lambda s: s.name)

    lines = [
        "// AUTO-GENERATED by docs/generate.py. DO NOT EDIT.",
        "//",
        "// Source: docs/shapes/*.yaml",
        "// Regen: `python3 docs/generate.py` (run from workspace root).",
        "//",
        "// One `pub static` per shape YAML. `yaml_body` carries the inner",
        "// mapping (fields/identity/relations/also) — not the outer",
        "// `shape_name:` wrapper — so the body round-trips through",
        "// `serde_yaml::from_str::<RawShape>` without reshaping. Engine",
        "// code imports these via `use agentos_shapes_generated::ACCOUNT;`.",
        "",
        "#![allow(non_upper_case_globals)]",
        "",
        "use agentos_shapes::ShapeHandle;",
        "",
    ]

    def _rust_str_slice(items: list[str]) -> str:
        if not items:
            return "&[]"
        body = ", ".join(f'"{s}"' for s in items)
        return f"&[{body}]"

    for s in shapes_sorted:
        if not s.raw_body:
            # Shapes without a serialised body (e.g. loaded from the graph
            # API and failed to round-trip) can't be embedded. Skip — the
            # Rust SDK only emits YAML-sourced shapes, which is the common
            # path.
            continue
        ident = _rust_ident(s.name)
        # Use Rust raw string literal with enough `#` hashes to be unique.
        body = s.raw_body
        hashes = "#"
        while f'"{hashes}' in body:
            hashes += "#"
        lines.append(f"pub static {ident}: ShapeHandle = ShapeHandle {{")
        lines.append(f'    name: "{s.name}",')
        lines.append(f'    yaml_body: r{hashes}"{body}"{hashes},')
        lines.append(f"    identity: {_rust_str_slice(s.identity)},")
        lines.append(f"    identity_any: {_rust_str_slice(s.identity_any)},")
        lines.append("};")
        lines.append("")

    return "\n".join(lines)


# =============================================================================
# MDX emitter — one doc page per shape (Starlight-compatible)
# =============================================================================

def _shape_link(target: str) -> str:
    """Produce a markdown link to another shape's reference page."""
    base = target.rstrip("[]")
    return f"[`{target}`](/shapes/reference/{base}/)"


def emit_shape_docs(shapes: list[Shape], out_dir: Path, skills_index: dict[str, list[dict]]) -> None:
    """Write one MDX file per shape into `out_dir`, plus an index page.

    skills_index maps shape-name → list of {skill_id, path, operations} dicts,
    so each shape page can show 'skills that produce this shape'.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    by_name = {s.name: s for s in shapes}

    for s in shapes:
        desc = s.leading_comment.split("\n")[0] if s.leading_comment else f"Shape reference for `{s.name}`."
        # Starlight YAML-safe description: single line, no backticks, no quotes.
        desc_safe = desc.replace('"', "'").replace("`", "").strip()
        if len(desc_safe) > 160:
            desc_safe = desc_safe[:157] + "..."

        lines = [
            "---",
            f"title: {s.name}",
            f'description: "{desc_safe}"',
            "sidebar:",
            f"  label: {s.name}",
            "---",
            "",
        ]

        # Leading comment as intro prose, if present
        if s.leading_comment:
            lines.append(s.leading_comment)
            lines.append("")

        # Metadata table: plural, subtitle, identity, also chain
        meta_rows = []
        if s.plural:
            meta_rows.append(("Plural", f"`{s.plural}`"))
        if s.subtitle:
            meta_rows.append(("Subtitle field", f"`{s.subtitle}`"))
        if s.identity:
            meta_rows.append(("Identity", ", ".join(f"`{i}`" for i in s.identity)))
        if s.identity_any:
            meta_rows.append(("Identity (any)", ", ".join(f"`{i}`" for i in s.identity_any)))
        if s.also:
            chain = " · ".join(_shape_link(a) for a in s.also)
            meta_rows.append(("Also", chain))
        if meta_rows:
            lines.append("| Metadata | Value |")
            lines.append("|---|---|")
            for k, v in meta_rows:
                lines.append(f"| **{k}** | {v} |")
            lines.append("")

        # Own fields
        if s.own_fields:
            lines.append("## Fields")
            lines.append("")
            lines.append("| Field | Type |")
            lines.append("|---|---|")
            for f in s.own_fields:
                lines.append(f"| `{f.name}` | `{f.type}` |")
            lines.append("")

        # Own relations
        if s.own_relations:
            lines.append("## Relations")
            lines.append("")
            lines.append("| Relation | Target |")
            lines.append("|---|---|")
            for f in s.own_relations:
                tgt = f.target or f.type.rstrip("[]")
                arr = "[]" if f.is_array else ""
                lines.append(f"| `{f.name}` | {_shape_link(tgt + arr)} |")
            lines.append("")

        # Inherited fields (resolved - own, minus standard)
        own_names = {f.name for f in s.own_fields}
        own_rel_names = {f.name for f in s.own_relations}
        std_names = {n for n, _ in STANDARD_FIELDS}
        inherited_fields = [
            f for f in s.fields
            if not f.is_relation and f.name not in own_names and f.name not in std_names
        ]
        inherited_rels = [
            f for f in s.fields if f.is_relation and f.name not in own_rel_names
        ]
        if inherited_fields or inherited_rels:
            lines.append("## Inherited")
            lines.append("")
            if s.also:
                chain = " · ".join(_shape_link(a) for a in s.also)
                lines.append(f"From {chain}:")
                lines.append("")
            if inherited_fields:
                lines.append("| Field | Type |")
                lines.append("|---|---|")
                for f in inherited_fields:
                    lines.append(f"| `{f.name}` | `{f.type}` |")
                lines.append("")
            if inherited_rels:
                lines.append("| Relation | Target |")
                lines.append("|---|---|")
                for f in inherited_rels:
                    tgt = f.target or f.type.rstrip("[]")
                    arr = "[]" if f.is_array else ""
                    lines.append(f"| `{f.name}` | {_shape_link(tgt + arr)} |")
                lines.append("")

        # Shapes that declare THIS shape in their `also:` chain (children)
        children = sorted([c.name for c in shapes if s.name in c.also])
        if children:
            lines.append("## Used as a base by")
            lines.append("")
            for child in children:
                lines.append(f"- {_shape_link(child)}")
            lines.append("")

        # Prior art — external standards this shape aligns with
        if s.prior_art:
            lines.append("## Prior art")
            lines.append("")
            lines.append("External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.")
            lines.append("")
            for entry in s.prior_art:
                src = entry["source"]
                url = entry["url"]
                notes = entry["notes"]
                heading = f"[{src}]({url})" if url else src
                lines.append(f"- **{heading}** — {notes}" if notes else f"- **{heading}**")
            lines.append("")

        # Skills that return this shape
        producers = skills_index.get(s.name, [])
        if producers:
            lines.append("## Skills that produce this shape")
            lines.append("")
            for p in producers:
                sid = p["skill_id"]
                cat = p.get("category", "")
                ops = ", ".join(f"`{op}`" for op in p["operations"])
                url = f"/skills/reference/{cat}/{sid}/" if cat else f"/skills/reference/{sid}/"
                lines.append(f"- [{sid}]({url}) — {ops}")
            lines.append("")

        (out_dir / f"{s.name}.md").write_text("\n".join(lines).rstrip() + "\n")

    # Index page — flat A-Z list with one-line descriptions
    idx = [
        "---",
        "title: Shapes",
        'description: "Every shape in the AgentOS ontology. Browse all 81, or follow a tag chain."',
        "---",
        "",
        f"The AgentOS ontology — **{len(shapes)}** shapes. Each shape defines what an entity *is* (fields, relations, display hints). Shapes can extend other shapes via `also:`, which makes that shape a **tag** on the entity — a person is also an actor; a book is also a product.",
        "",
        "See [Overview](/shapes/overview/) for the tactical reference and [Shape design principles](/shapes/shape-design-principles/) for the rules.",
        "",
        "## All shapes",
        "",
    ]
    for s in shapes:
        desc = (s.leading_comment.split("\n")[0] if s.leading_comment else "").strip().rstrip(".")
        also = ""
        if s.also:
            also = f" — also {', '.join(f'`{a}`' for a in s.also)}"
        desc_part = f" — {desc}" if desc else ""
        idx.append(f"- [`{s.name}`](/shapes/reference/{s.name}/){also}{desc_part}")
    (out_dir / "index.md").write_text("\n".join(idx) + "\n")


# =============================================================================
# Skill docs emitter — one MDX per skill, reading each skill's readme.md
# =============================================================================

_SKILL_IGNORE_DIRS = {"_sdk", "_prototype", "_code-reviews", "agent-sdk", "bin", "node_modules", "__pycache__"}


def _parse_readme_frontmatter(text: str) -> tuple[dict, str]:
    """Parse YAML frontmatter from a readme. Returns (meta, body)."""
    try:
        import yaml
    except ImportError:
        return {}, text
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    meta = yaml.safe_load(text[3:end]) or {}
    body = text[end + 4:].lstrip("\n")
    return (meta if isinstance(meta, dict) else {}), body


def _extract_returns(py_text: str) -> list[tuple[str, str]]:
    """Find @returns('shape') decorators over def/async-def. Returns [(func_name, shape), ...]."""
    import ast
    try:
        tree = ast.parse(py_text)
    except SyntaxError:
        return []
    out = []
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            for dec in node.decorator_list:
                if isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name) and dec.func.id == "returns":
                    if dec.args and isinstance(dec.args[0], ast.Constant) and isinstance(dec.args[0].value, str):
                        out.append((node.name, dec.args[0].value))
    return out


def discover_skills(skills_root: Path) -> list[dict]:
    """Walk skills/ looking for readme.md files. Return list of skill records."""
    records = []
    for readme in skills_root.rglob("readme.md"):
        rel = readme.parent.relative_to(skills_root)
        parts = rel.parts
        if any(p in _SKILL_IGNORE_DIRS or p.startswith(".") for p in parts):
            continue
        if readme.parent == skills_root:
            continue
        text = readme.read_text()
        meta, body = _parse_readme_frontmatter(text)
        skill_id = meta.get("id") or rel.name
        category = parts[0] if len(parts) > 1 else "misc"
        # Scan .py files for @returns shape names
        returns = {}  # shape → [func_name, ...]
        for py in readme.parent.glob("*.py"):
            for fn, shape in _extract_returns(py.read_text()):
                returns.setdefault(shape, []).append(fn)
        records.append({
            "skill_id": skill_id,
            "rel_path": str(rel),
            "category": category,
            "meta": meta,
            "body": body,
            "returns": returns,
        })
    return records


def emit_skill_docs(skills: list[dict], out_dir: Path, known_shapes: set[str]) -> None:
    """Write one MDX file per skill under `<category>/<id>.md` + an index page.

    Skills are laid out by **category** — the same taxonomy the skills/ tree
    uses on disk (comms/, web/, finance/, …). The sidebar mirrors this,
    giving agents a fast scan path: "where are the email skills?" → `comms/`.

    `known_shapes` is the set of shape names that have their own reference page;
    return-types outside this set (e.g. `void`) are rendered as plain code without
    a link so generated pages never produce dead `/shapes/reference/void/` URLs.
    """
    out_dir.mkdir(parents=True, exist_ok=True)
    # Group skills by category so we can emit per-category index pages below.
    by_cat: dict[str, list[dict]] = {}
    for rec in skills:
        by_cat.setdefault(rec["category"], []).append(rec)
    for rec in skills:
        meta = rec["meta"]
        sid = rec["skill_id"]
        name = meta.get("name", sid)
        desc = (meta.get("description") or "").replace('"', "'").strip()
        if len(desc) > 160:
            desc = desc[:157] + "..."

        lines = [
            "---",
            f"title: {name}",
            f'description: "{desc}"' if desc else f'description: "Skill reference for {sid}."',
            "sidebar:",
            f"  label: {sid}",
            "---",
            "",
        ]

        # Metadata table: category, capabilities, website
        meta_rows = [("Category", f"`{rec['category']}`")]
        if meta.get("capabilities"):
            caps = ", ".join(f"`{c}`" for c in meta["capabilities"])
            meta_rows.append(("Capabilities", caps))
        if meta.get("website"):
            meta_rows.append(("Website", f"<{meta['website']}>"))
        lines.append("| Metadata | Value |")
        lines.append("|---|---|")
        for k, v in meta_rows:
            lines.append(f"| **{k}** | {v} |")
        lines.append("")

        # Shapes produced
        if rec["returns"]:
            lines.append("## Returns shapes")
            lines.append("")
            for shape, fns in sorted(rec["returns"].items()):
                fn_list = ", ".join(f"`{fn}`" for fn in fns)
                bare = shape.rstrip("[]")
                if bare in known_shapes:
                    rendered = f"[`{shape}`](/shapes/reference/{bare}/)"
                else:
                    rendered = f"`{shape}`"
                lines.append(f"- {rendered} — from {fn_list}")
            lines.append("")

        # Connections block — just list connection names
        if meta.get("connections"):
            lines.append("## Connections")
            lines.append("")
            for cname, cval in meta["connections"].items():
                cdesc = cval.get("description") if isinstance(cval, dict) else ""
                if cdesc:
                    lines.append(f"- **`{cname}`** — {cdesc}")
                else:
                    lines.append(f"- **`{cname}`**")
            lines.append("")

        # Body (the agent-facing readme) — strip first H1 if any (title already in frontmatter)
        body = rec["body"].strip()
        if body.startswith("# "):
            body = body.split("\n", 1)[1].lstrip("\n") if "\n" in body else ""
        if body:
            lines.append("## Readme")
            lines.append("")
            lines.append(body)
            lines.append("")

        cat_dir = out_dir / rec["category"]
        cat_dir.mkdir(parents=True, exist_ok=True)
        (cat_dir / f"{sid}.md").write_text("\n".join(lines).rstrip() + "\n")

    # Top-level index — flat listing of all skills, grouped visually by category.
    idx = [
        "---",
        "title: Skills index",
        'description: "Every skill in the AgentOS catalog. Browse all or filter by category."',
        "---",
        "",
        f"The AgentOS skill catalog — **{len(skills)}** skills across **{len(by_cat)}** categories. Each skill is a Python adapter that connects to a service or provides a pure agent capability.",
        "",
        "See [Skills → Overview](/skills/overview/) for how to build one.",
        "",
    ]
    for cat in sorted(by_cat.keys()):
        idx.append(f"## [{cat}](/skills/reference/{cat}/)")
        idx.append("")
        for rec in sorted(by_cat[cat], key=lambda r: r["skill_id"]):
            name = rec["meta"].get("name", rec["skill_id"])
            desc = (rec["meta"].get("description") or "").strip().rstrip(".")
            desc_part = f" — {desc}" if desc else ""
            idx.append(f"- [**{name}**](/skills/reference/{cat}/{rec['skill_id']}/){desc_part}")
        idx.append("")
    (out_dir / "index.md").write_text("\n".join(idx) + "\n")

    # Per-category index pages — each category folder gets its own landing.
    for cat, recs in sorted(by_cat.items()):
        cat_lines = [
            "---",
            f"title: {cat}",
            f'description: "Skills in the {cat} category."',
            "sidebar:",
            "  label: Overview",
            "  order: -1",
            "---",
            "",
            f"**{len(recs)}** skills in `{cat}`.",
            "",
        ]
        for rec in sorted(recs, key=lambda r: r["skill_id"]):
            name = rec["meta"].get("name", rec["skill_id"])
            desc = (rec["meta"].get("description") or "").strip().rstrip(".")
            desc_part = f" — {desc}" if desc else ""
            cat_lines.append(f"- [**{name}**](/skills/reference/{cat}/{rec['skill_id']}/){desc_part}")
        (out_dir / cat / "index.md").write_text("\n".join(cat_lines).rstrip() + "\n")


def build_skills_index(skills: list[dict], known_shapes: set[str]) -> dict[str, list[dict]]:
    """Invert skills list into shape-name → skills that produce it (arrays stripped).

    Only keeps entries for shapes that have a reference page (`known_shapes`).
    Operations from multiple SOPs of the same skill are merged and deduped, so
    a skill appears at most once per shape.
    """
    # shape -> { skill_id -> {category, operations: [ordered unique]} }
    tmp: dict[str, dict[str, dict]] = {}
    for rec in skills:
        for shape in rec["returns"]:
            bare = shape.rstrip("[]")
            if bare not in known_shapes:
                continue
            bucket = tmp.setdefault(bare, {})
            entry = bucket.get(rec["skill_id"])
            if entry is None:
                entry = {
                    "skill_id": rec["skill_id"],
                    "category": rec["category"],
                    "operations": [],
                }
                bucket[rec["skill_id"]] = entry
            seen = set(entry["operations"])
            for op in rec["returns"][shape]:
                if op not in seen:
                    entry["operations"].append(op)
                    seen.add(op)

    idx: dict[str, list[dict]] = {
        shape: list(bucket.values()) for shape, bucket in tmp.items()
    }
    # Invariant: each skill appears at most once per shape. If this trips,
    # bucket aggregation above has regressed.
    for shape, entries in idx.items():
        seen: set[str] = set()
        for e in entries:
            if e["skill_id"] in seen:
                raise AssertionError(
                    f"build_skills_index: skill {e['skill_id']!r} listed twice for shape {shape!r}"
                )
            seen.add(e["skill_id"])
    return idx


# =============================================================================
# Tool surface codegen — lives in docs/codegen/tool_surface.py (D11)
# =============================================================================
#
# Kept modular: the registry is big enough to deserve its own module, and
# future SDK codegen (sdk-skills Client class) will sit next to it under
# docs/codegen/. generate.py stays the orchestrator.

from codegen.tool_surface import load_tool_surface, emit_tool_surface_docs  # noqa: E402


# =============================================================================
# Auth-contract loader + emitters
# =============================================================================
#
# `docs/auth-contracts/{oauth,cookie}.yaml` is the single source of truth for
# what skills decorated `@provides(oauth_auth, ...)` / `@provides(cookie_auth, ...)`
# must return. We codegen:
#
#   - Python: sdk-skills/agentos/_generated_auth_contracts.py
#       OAuthCredential / CookieCredential / Cookie TypedDicts +
#       AUTH_CONTRACTS dict consumed by agent-sdk validate.
#
#   - Rust:   core/crates/auth/src/_generated_contracts.rs
#       OAUTH_REQUIRED_FIELDS, OAUTH_RECOMMENDED_FIELDS,
#       COOKIE_ENVELOPE_REQUIRED, COOKIE_FIELDS_REQUIRED — replaces
#       the literal "access_token" string scattered through the
#       resolver and Session impl.
#
# Why: the mimestream camelCase / engine snake_case bug
# (_roadmap/p1/observability/panes.md). Implicit contracts → silent
# 401s. Explicit contracts → uncommittable bugs.

def load_auth_contracts(contracts_dir: Path) -> dict:
    """Load all *.yaml files under docs/auth-contracts/ as a dict."""
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)
    contracts = {}
    for f in sorted(contracts_dir.glob("*.yaml")):
        data = yaml.safe_load(f.read_text())
        if isinstance(data, dict):
            for name, body in data.items():
                contracts[name] = body
    return contracts


_PY_PRIMITIVE = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list[Any]",
    "json": "Any",
}


def _py_field(name: str, type_str: str) -> str:
    return f"    {name}: {_PY_PRIMITIVE.get(type_str, 'Any')}"


def emit_python_auth_contracts(contracts: dict) -> str:
    """Emit the Python auth contracts module — TypedDicts + AUTH_CONTRACTS dict."""
    lines = [
        '"""Auto-generated auth provider contracts — do not edit.',
        "",
        "Single source of truth: docs/auth-contracts/{oauth,cookie}.yaml.",
        "Regenerate with: python docs/generate.py",
        "",
        "Skills decorated `@provides(oauth_auth, ...)` should return a dict",
        "matching `OAuthCredential`. Skills decorated `@provides(cookie_auth, ...)`",
        "return `CookieCredential`. agent-sdk validate enforces this at commit",
        "time using the AUTH_CONTRACTS dict at the bottom of this file.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, TypedDict",
        "",
    ]

    if "oauth" in contracts:
        oauth = contracts["oauth"]
        lines += [
            "class OAuthCredential(TypedDict, total=False):",
            f'    """{oauth.get("description", "OAuth provider return shape.").strip()}',
            "",
            "    All fields snake_case to match the OAuth 2.0 spec (RFC 6749 §5.1)",
            "    and the engine resolver (crates/auth/src/types.rs). Required:",
            "    `access_token`. Strongly recommended for refresh:",
            "    `refresh_token`, `expires_in`, `client_id`, `token_url`.",
            '    """',
        ]
        for name, body in (oauth.get("required") or {}).items():
            lines.append(_py_field(name, body.get("type", "string")))
        for name, body in (oauth.get("recommended") or {}).items():
            lines.append(_py_field(name, body.get("type", "string")))
        lines += ["", ""]

    if "cookie" in contracts:
        cookie = contracts["cookie"]
        lines += [
            "class Cookie(TypedDict, total=False):",
            '    """A single cookie in a CookieCredential.cookies array."""',
        ]
        for name, body in (cookie.get("cookie_fields", {}).get("required") or {}).items():
            lines.append(_py_field(name, body.get("type", "string")))
        for name, body in (cookie.get("cookie_fields", {}).get("recommended") or {}).items():
            lines.append(_py_field(name, body.get("type", "string")))
        lines += ["", ""]

        lines += [
            "class CookieCredential(TypedDict, total=False):",
            f'    """{cookie.get("description", "Cookie provider return shape.").strip()}"""',
        ]
        for name, body in (cookie.get("envelope", {}).get("required") or {}).items():
            ty = "list[Cookie]" if name == "cookies" else _PY_PRIMITIVE.get(body.get("type", "string"), "Any")
            lines.append(f"    {name}: {ty}")
        for name, body in (cookie.get("envelope", {}).get("recommended") or {}).items():
            lines.append(_py_field(name, body.get("type", "string")))
        lines += ["", ""]

    # AUTH_CONTRACTS — what agent-sdk validate reads.
    lines += [
        "# Machine-readable contract — what agent-sdk validate enforces.",
        "# Every key here corresponds to a `@provides(<name>_auth, ...)`",
        "# decorator. Format:",
        "#   {'required': [field, ...], 'recommended': [field, ...],",
        "#    'forbidden_camel_case': {camelCase: snake_case_replacement, ...}}",
        "AUTH_CONTRACTS: dict[str, dict] = {",
    ]
    for kind, body in contracts.items():
        required = list((body.get("required") or {}).keys())
        recommended = list((body.get("recommended") or {}).keys())
        forbidden = body.get("forbidden_camel_case") or {}
        lines.append(f"    {kind!r}: {{")
        lines.append(f"        'required': {required!r},")
        lines.append(f"        'recommended': {recommended!r},")
        lines.append(f"        'forbidden_camel_case': {dict(forbidden)!r},")
        # Cookie has nested cookie_fields contract too — flatten under
        # a sibling key so the validator can check each Cookie dict.
        if "cookie_fields" in body:
            cf_required = list((body["cookie_fields"].get("required") or {}).keys())
            cf_recommended = list((body["cookie_fields"].get("recommended") or {}).keys())
            lines.append(f"        'cookie_fields_required': {cf_required!r},")
            lines.append(f"        'cookie_fields_recommended': {cf_recommended!r},")
        lines.append("    },")
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def emit_rust_auth_contracts(contracts: dict) -> str:
    """Emit Rust constants for the auth resolver."""
    lines = [
        "// AUTO-GENERATED by docs/generate.py. DO NOT EDIT.",
        "//",
        "// Source: docs/auth-contracts/{oauth,cookie}.yaml",
        "// Regen: `python3 docs/generate.py` (run from workspace root).",
        "//",
        "// Single source of truth for OAuth + cookie provider contracts.",
        "// Replaces literal field-name strings (\"access_token\", \"refresh_token\",",
        "// etc.) scattered through crates/auth/src/{types,resolve,source,cache}.rs.",
        "//",
        "// See _roadmap/p1/observability/panes.md for the bug that motivated this.",
        "",
        "#![allow(dead_code)]",
        "",
    ]

    def emit_const(name: str, items: list[str]) -> list[str]:
        body = ", ".join(f'"{i}"' for i in items)
        return [f"pub const {name}: &[&str] = &[{body}];"]

    if "oauth" in contracts:
        oauth = contracts["oauth"]
        required = list((oauth.get("required") or {}).keys())
        recommended = list((oauth.get("recommended") or {}).keys())
        forbidden = oauth.get("forbidden_camel_case") or {}
        lines += [
            "// ── OAuth provider contract ─────────────────────────────────────────",
            "",
        ]
        lines += emit_const("OAUTH_REQUIRED_FIELDS", required)
        lines += emit_const("OAUTH_RECOMMENDED_FIELDS", recommended)
        lines.append("")
        lines.append("/// camelCase variants the engine should warn loudly about when found")
        lines.append("/// in an OAuth provider response. (camel_case_form, snake_case_replacement).")
        lines.append("pub const OAUTH_FORBIDDEN_CAMEL_CASE: &[(&str, &str)] = &[")
        for camel, snake in forbidden.items():
            lines.append(f'    ("{camel}", "{snake}"),')
        lines.append("];")
        lines.append("")

    if "cookie" in contracts:
        cookie = contracts["cookie"]
        env_required = list((cookie.get("envelope", {}).get("required") or {}).keys())
        env_recommended = list((cookie.get("envelope", {}).get("recommended") or {}).keys())
        cf_required = list((cookie.get("cookie_fields", {}).get("required") or {}).keys())
        cf_recommended = list((cookie.get("cookie_fields", {}).get("recommended") or {}).keys())
        forbidden = cookie.get("forbidden_camel_case") or {}
        lines += [
            "// ── Cookie provider contract ────────────────────────────────────────",
            "",
        ]
        lines += emit_const("COOKIE_ENVELOPE_REQUIRED", env_required)
        lines += emit_const("COOKIE_ENVELOPE_RECOMMENDED", env_recommended)
        lines += emit_const("COOKIE_FIELDS_REQUIRED", cf_required)
        lines += emit_const("COOKIE_FIELDS_RECOMMENDED", cf_recommended)
        lines.append("")
        lines.append("/// camelCase variants flagged in cookie provider responses.")
        lines.append("pub const COOKIE_FORBIDDEN_CAMEL_CASE: &[(&str, &str)] = &[")
        for camel, snake in forbidden.items():
            lines.append(f'    ("{camel}", "{snake}"),')
        lines.append("];")
        lines.append("")

    return "\n".join(lines)


# =============================================================================
# CLI
# =============================================================================

# Emitters generated by default when you run `generate.py` with no --lang.
# Each has a default target path inside a sibling repo, wired up below.
EMITTERS = {
    "python": (emit_python, "_generated.py"),
    "typescript": (emit_typescript, "shape.ts"),
    "rust": (emit_rust, "lib.rs"),
}

# Available via --lang but not written to default targets — callers must
# supply --out-dir. Intended for one-off exports (docs examples, experiments).
_EXTRA_EMITTERS = {
    "swift": (emit_swift, "Shape.swift"),
    "go": (emit_go, "shape.go"),
}


ALL_EMITTERS = {**EMITTERS, **_EXTRA_EMITTERS}


def main():
    parser = argparse.ArgumentParser(description="Generate typed shapes for Python, TypeScript, and Rust")
    parser.add_argument("--lang", choices=list(ALL_EMITTERS.keys()), help="Language to generate (default: all in EMITTERS)")
    parser.add_argument("--shapes-dir", type=Path, help="Path to shapes/ directory")
    parser.add_argument("--out-dir", type=Path, help="Output directory (default: target inside sibling SDK repo)")
    parser.add_argument("--from-api", action="store_true", help="Load shapes from graph via agentos CLI instead of YAML files")
    parser.add_argument("--agentos-bin", type=str, help="Path to agentos binary (default: agentos)")
    parser.add_argument("--dump-yaml", type=Path, help="With --from-api: also dump each shape as YAML to this directory (backup/export)")
    parser.add_argument("--docs", action="store_true", help="Emit MDX reference pages for shapes + skills (Starlight)")
    parser.add_argument("--skills-root", type=Path, help="Path to skills/ tree for --docs (default: ../skills)")
    parser.add_argument("--docs-out", type=Path, help="Reference output root for --docs (default: src/content/docs/reference)")
    parser.add_argument("--check", action="store_true", help="Drift check: compare rendered output to files on disk; exit 1 if different")
    args = parser.parse_args()

    # generate.py lives at `docs/generate.py`; docs_dir = workspace/docs,
    # workspace = docs_dir.parent. Everything we emit lives in sibling repos.
    docs_dir = Path(__file__).parent
    workspace = docs_dir.parent

    if args.from_api:
        agentos_bin = args.agentos_bin or "agentos"
        shapes = load_shapes_from_api(agentos_bin)
        print(f"Loaded {len(shapes)} shapes from graph API")

        if args.dump_yaml:
            _dump_yaml_from_api(agentos_bin, args.dump_yaml)
    else:
        shapes_dir = args.shapes_dir or docs_dir / "shapes"
        if not shapes_dir.is_dir():
            print(f"Shapes directory not found: {shapes_dir}", file=sys.stderr)
            sys.exit(1)
        shapes = load_shapes(shapes_dir)
        print(f"Loaded {len(shapes)} shapes from {shapes_dir}")

    # Output destinations per language — write directly into sibling SDK packages.
    # Use --out-dir to override (e.g. for Go/Swift one-off exports).
    targets = {
        "python": workspace / "sdk-skills" / "agentos" / "_generated.py",
        "typescript": workspace / "sdk-apps" / "src" / "shapes.ts",
        "rust": workspace / "core" / "crates" / "shapes-generated" / "src" / "lib.rs",
    }

    if args.docs:
        skills_root = args.skills_root or (workspace / "skills").resolve()
        docs_out = args.docs_out or (docs_dir / "src" / "content" / "docs")
        if not skills_root.is_dir():
            print(f"Skills root not found: {skills_root}", file=sys.stderr)
            sys.exit(1)
        skills = discover_skills(skills_root)
        print(f"Discovered {len(skills)} skills in {skills_root}")
        known_shapes = {s.name for s in shapes}
        skills_index = build_skills_index(skills, known_shapes)
        emit_shape_docs(shapes, docs_out / "shapes" / "reference", skills_index)
        print(f"  shapes: {docs_out / 'shapes' / 'reference'} ({len(shapes)} pages + index)")
        emit_skill_docs(skills, docs_out / "skills" / "reference", known_shapes)
        print(f"  skills: {docs_out / 'skills' / 'reference'} ({len(skills)} pages + index)")

        # Tool surface — registry is single source of truth per D11. Opt
        # out cleanly if the engine isn't running; drift will surface next
        # time someone runs generate with the engine up.
        agentos_bin = args.agentos_bin or "agentos"
        try:
            namespaces = load_tool_surface(agentos_bin)
            emit_tool_surface_docs(namespaces, docs_out / "tool-surface")
            ops_total = sum(len(ns.get("ops", [])) for ns in namespaces)
            print(f"  tool-surface: {docs_out / 'tool-surface'} ({len(namespaces)} namespaces, {ops_total} ops)")
        except SystemExit:
            print(f"  tool-surface: skipped (engine unreachable) — run `./dev.sh restart` and retry", file=sys.stderr)
        return

    langs = [args.lang] if args.lang else list(EMITTERS.keys())
    drift = False
    for lang in langs:
        emitter, filename = ALL_EMITTERS[lang]
        output = emitter(shapes)

        if args.out_dir:
            out_path = args.out_dir / filename
        elif lang in targets:
            out_path = targets[lang]
        else:
            print(f"  {lang}: no SDK package — use --out-dir to write", file=sys.stderr)
            continue

        if args.check:
            existing = out_path.read_text() if out_path.exists() else ""
            if existing != output:
                drift = True
                print(f"  {lang}: DRIFT — {out_path} is stale", file=sys.stderr)
                # Show a compact diff to help the reader see what changed.
                import difflib
                diff = "".join(difflib.unified_diff(
                    existing.splitlines(keepends=True),
                    output.splitlines(keepends=True),
                    fromfile=str(out_path),
                    tofile="<generated>",
                    n=2,
                ))
                if diff:
                    sys.stderr.write(diff)
            else:
                print(f"  {lang}: ok ({out_path})")
        else:
            if args.out_dir:
                args.out_dir.mkdir(exist_ok=True)
            out_path.write_text(output)
            print(f"  {lang}: {out_path}")

    # Auth contracts — single source of truth for OAuth + cookie provider
    # return shapes (the mimestream snake_case bug fix). Always emitted in
    # the default run; --lang explicitly skips since auth contracts aren't
    # tied to any one language.
    if not args.lang:
        contracts_dir = docs_dir / "auth-contracts"
        if contracts_dir.is_dir():
            contracts = load_auth_contracts(contracts_dir)
            if contracts:
                ac_targets = {
                    "python": workspace / "sdk-skills" / "agentos" / "_generated_auth_contracts.py",
                    "rust":   workspace / "core" / "crates" / "auth" / "src" / "_generated_contracts.rs",
                }
                ac_outputs = {
                    "python": emit_python_auth_contracts(contracts),
                    "rust":   emit_rust_auth_contracts(contracts),
                }
                for lang, out_path in ac_targets.items():
                    output = ac_outputs[lang]
                    if args.check:
                        existing = out_path.read_text() if out_path.exists() else ""
                        if existing != output:
                            drift = True
                            print(f"  auth-{lang}: DRIFT — {out_path} is stale", file=sys.stderr)
                        else:
                            print(f"  auth-{lang}: ok ({out_path})")
                    else:
                        out_path.parent.mkdir(parents=True, exist_ok=True)
                        out_path.write_text(output)
                        print(f"  auth-{lang}: {out_path}")

    if args.check and drift:
        sys.exit(1)


if __name__ == "__main__":
    main()
