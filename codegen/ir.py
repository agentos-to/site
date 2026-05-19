#!/usr/bin/env python3
"""The ontology IR — one normalized tree, parsed + validated once.

The codegen pipeline is `YAML → IR → emitters`. This module owns the
first arrow: it parses `ontology/shapes/*.yaml` and
`ontology/auth-contracts/*.yaml`, resolves shape inheritance, normalizes
both into one `Ontology` tree, and validates it. Every emitter under
`emit/` is a dumb projection off this tree — it never re-reads YAML and
never re-derives. `serialize()` renders the tree to the checked-in
`ir.json`, which is the structural diff + lint surface.
"""

from __future__ import annotations

import json
import re
import sys
from dataclasses import asdict, dataclass, field
from pathlib import Path


# =============================================================================
# Naming transforms — shared by every emitter
# =============================================================================

def _camel_to_snake(name: str) -> str:
    """Convert camelCase to snake_case. Leaves snake_case unchanged."""
    return re.sub(r"([a-z])([A-Z])", r"\1_\2", name).lower()


def _to_camel(name: str) -> str:
    parts = name.split("_")
    return parts[0] + "".join(w.capitalize() for w in parts[1:])


def to_class_name(name: str) -> str:
    snake = _camel_to_snake(name).replace("-", "_")
    return "".join(w.capitalize() for w in snake.split("_"))


# =============================================================================
# IR — shapes
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
# IR — auth contracts
# =============================================================================
#
# `ontology/auth-contracts/{oauth,cookie}.yaml` declares what skills
# decorated `@provides(oauth_auth, ...)` / `@provides(cookie_auth, ...)`
# must return. The two contracts have different shapes by nature: an
# OAuth credential is a flat dict; a cookie credential is an envelope
# carrying an array of per-cookie elements. Both are normalized into a
# list of `AuthGroup`s keyed by `role`:
#
#   oauth  → [credential]
#   cookie → [envelope, element]


@dataclass
class AuthField:
    name: str
    type: str
    description: str = ""


@dataclass
class AuthGroup:
    role: str                                       # "credential" | "envelope" | "element"
    required: list[AuthField] = field(default_factory=list)
    recommended: list[AuthField] = field(default_factory=list)


@dataclass
class AuthContract:
    kind: str                                       # "oauth" | "cookie" (file's top-level key)
    description: str = ""
    groups: list[AuthGroup] = field(default_factory=list)
    forbidden_camel_case: dict[str, str] = field(default_factory=dict)

    def group(self, role: str) -> AuthGroup | None:
        for g in self.groups:
            if g.role == role:
                return g
        return None


# =============================================================================
# IR — the root
# =============================================================================


@dataclass
class Ontology:
    """The whole normalized contract — one tree, every emitter's input."""
    shapes: list[Shape] = field(default_factory=list)
    auth_contracts: list[AuthContract] = field(default_factory=list)

    def auth(self, kind: str) -> AuthContract | None:
        for c in self.auth_contracts:
            if c.kind == kind:
                return c
        return None


# =============================================================================
# Shape loader — YAML → Shape
# =============================================================================

def _strip_code_fences(text: str) -> str:
    """Strip markdown code fences from CLI JSON output."""
    if text.startswith("```"):
        text = "\n".join(text.split("\n")[1:])
    if text.endswith("```"):
        text = "\n".join(text.split("\n")[:-1])
    return text


def dump_yaml_from_api(agentos_bin: str, out_dir: Path) -> None:
    """Export each shape from the graph as a standalone YAML file (backup/restore)."""
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

        # Relations resolved up front so they can SHADOW a same-named
        # field: when a shape models a concept as an edge (`book
        # --author--> person`), the edge is the source of truth — the
        # generated type carries `author: Person`, never both a string
        # field and a relation. Without this, a standard field like
        # `author` and an `author` relation emit a duplicate identifier.
        relations = sorted(resolve_relations(shape_name).items())
        relation_labels = {label for label, _ in relations}

        # Standard fields — skipped when a relation shadows them.
        for wk_name, wk_type in STANDARD_FIELDS:
            if wk_name in relation_labels:
                continue
            s.fields.append(Field(wk_name, wk_type, False, False, None))

        # Shape-declared fields — skipped when a relation shadows them.
        for fname, ftype in sorted(resolve_fields(shape_name).items()):
            if any(sf[0] == fname for sf in STANDARD_FIELDS):
                continue
            if fname in relation_labels:
                continue
            is_array = ftype.endswith("[]")
            s.fields.append(Field(fname, ftype, False, is_array, None))

        # Relations
        for label, target in relations:
            is_array = target.endswith("[]")
            target_name = target.rstrip("[]")
            s.fields.append(Field(label, target, True, is_array, target_name))

        shapes.append(s)

    return shapes


# =============================================================================
# Auth-contract loader — YAML → AuthContract
# =============================================================================

def _auth_fields(spec: dict | None) -> list[AuthField]:
    """A `{name: {type, description}}` YAML block → ordered AuthField list."""
    out = []
    for name, body in (spec or {}).items():
        body = body or {}
        out.append(AuthField(
            name=name,
            type=str(body.get("type", "string")),
            description=str(body.get("description", "")).strip(),
        ))
    return out


def load_auth_contracts(contracts_dir: Path) -> list[AuthContract]:
    """Load every `auth-contracts/*.yaml` into typed AuthContract IR.

    Glob order (`cookie.yaml`, `oauth.yaml`) is preserved — emitters that
    iterate the list (e.g. the Python `AUTH_CONTRACTS` dict) depend on it.
    """
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    contracts: list[AuthContract] = []
    for f in sorted(contracts_dir.glob("*.yaml")):
        data = yaml.safe_load(f.read_text())
        if not isinstance(data, dict):
            continue
        for kind, body in data.items():
            body = body or {}
            groups: list[AuthGroup] = []
            # oauth: a flat credential dict — top-level required/recommended.
            if "required" in body or "recommended" in body:
                groups.append(AuthGroup(
                    role="credential",
                    required=_auth_fields(body.get("required")),
                    recommended=_auth_fields(body.get("recommended")),
                ))
            # cookie: an envelope carrying a `cookies` array of elements.
            if "envelope" in body:
                env = body["envelope"] or {}
                groups.append(AuthGroup(
                    role="envelope",
                    required=_auth_fields(env.get("required")),
                    recommended=_auth_fields(env.get("recommended")),
                ))
            if "cookie_fields" in body:
                cf = body["cookie_fields"] or {}
                groups.append(AuthGroup(
                    role="element",
                    required=_auth_fields(cf.get("required")),
                    recommended=_auth_fields(cf.get("recommended")),
                ))
            contracts.append(AuthContract(
                kind=str(kind),
                description=str(body.get("description", "")).strip(),
                groups=groups,
                forbidden_camel_case=dict(body.get("forbidden_camel_case") or {}),
            ))
    return contracts


# =============================================================================
# Build + validate + serialize
# =============================================================================

# The shared type vocabulary. Shapes and auth contracts draw from one
# system; `validate()` flags anything outside it.
_SHAPE_TYPES = {
    "string", "text", "integer", "number", "boolean", "datetime", "date",
    "url", "json",
}
_AUTH_TYPES = {"string", "integer", "number", "boolean", "array", "json"}


def build(shapes: list[Shape], auth_contracts: list[AuthContract]) -> Ontology:
    """Assemble the normalized tree from already-loaded parts."""
    return Ontology(shapes=shapes, auth_contracts=auth_contracts)


def validate(onto: Ontology) -> list[str]:
    """Lint the normalized tree. Returns human-readable warnings.

    Phase 1 keeps this advisory — it reports, it does not transform, so
    it cannot change emitter output. The CI drift + breaking-change
    gates (Phases 3–4) build on top of it.
    """
    warnings: list[str] = []
    shape_names = {s.name for s in onto.shapes}

    for s in onto.shapes:
        for a in s.also:
            if a not in shape_names:
                warnings.append(f"shape {s.name!r}: `also` references unknown shape {a!r}")
        for r in s.own_relations:
            tgt = (r.target or "").rstrip("[]")
            if tgt and tgt != "node" and tgt not in shape_names:
                warnings.append(f"shape {s.name!r}: relation {r.name!r} targets unknown shape {tgt!r}")
        for f in s.own_fields:
            base = f.type.rstrip("[]")
            if base not in _SHAPE_TYPES:
                warnings.append(f"shape {s.name!r}: field {f.name!r} has unknown type {f.type!r}")

    for c in onto.auth_contracts:
        for g in c.groups:
            for f in g.required + g.recommended:
                if f.type not in _AUTH_TYPES:
                    warnings.append(f"auth {c.kind!r}: field {f.name!r} has unknown type {f.type!r}")

    return warnings


def serialize(onto: Ontology) -> str:
    """Render the tree to the checked-in `ir.json` — the structural diff
    + lint surface. Deterministic: shapes are name-sorted at build time,
    dataclass field order is fixed, dict order follows YAML insertion."""
    return json.dumps(asdict(onto), indent=2, ensure_ascii=False) + "\n"
