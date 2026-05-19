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


# `display:` block — the per-shape spec the Finder card / EntityDetail /
# table / markdown preview all project. Five roles (`ROLE_REGISTRY`), each
# optional. `title` defaults to the standard `name` field when absent;
# everything not bound is *unpromoted* and renders at detail density in
# YAML declaration order. See `core/_roadmap/p1/shape-display/plan.md`.
DISPLAY_ROLES = {"title", "subtitle", "image", "highlights", "body"}


@dataclass
class Display:
    title: str | None = None         # → a field (default: `name`)
    subtitle: str | None = None      # → a field or relation
    image: str | None = None         # → a field (url) or a relation → node.image
    highlights: list[str] = field(default_factory=list)  # 0..4 fields/relations
    body: str | None = None          # detail-only: one long text field
    preview: dict[str, object] = field(default_factory=dict)  # per-field content policy at preview density


@dataclass
class Shape:
    name: str           # YAML name (snake_case)
    class_name: str     # PascalCase
    fields: list[Field] = field(default_factory=list)
    # Below fields are ignored by language emitters; used by the MDX doc emitter.
    also: list[str] = field(default_factory=list)           # raw `also:` list (tag chain)
    plural: str | None = None
    subtitle: str | None = None      # back-compat shortcut for display.subtitle
    display: Display | None = None   # per-shape display spec (shape-display plan)
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
# IR — ops
# =============================================================================
#
# `ontology/ops/*.yaml` declares the engine's op contract — the primitives
# skills call (`shell.run`, `http.request`, …). Each op has a typed request
# and a response that is either a field-map or a bare scalar. Op field types
# draw from a wider vocabulary than shapes (width-precise ints, `bytes`,
# `map<K,V>`, named record types) — see `parse_type`.


@dataclass
class OpField:
    name: str                       # field name (snake_case)
    type: str                       # type string, trailing `?` stripped
    optional: bool                  # was the type written with a `?` suffix
    has_default: bool               # was a `default:` key present in the YAML
    default: object = None          # the default value (None also = `default: null`)
    doc: str = ""


@dataclass
class OpType:
    """A named record type referenced by op req/resp — the `types:` block.
    The "every type named" rule: op payloads carry no anonymous structs."""
    name: str
    fields: list[OpField] = field(default_factory=list)


@dataclass
class OpResponse:
    """An op's response — exactly one of the two forms is populated.
    `scalar` → `response: { type, doc }` (a bare value, maybe a transparent
    newtype); otherwise → a field-map like `request:`."""
    scalar: bool
    type: str = ""                          # set when scalar
    type_optional: bool = False             # scalar optionality
    doc: str = ""                           # scalar doc
    fields: list[OpField] = field(default_factory=list)  # set when field-map


@dataclass
class OpLogField:
    source: str                     # "request" | "response"
    path: str                       # JSON pointer (RFC 6901)
    key: str                        # audit-log key


# The `effects:` vocabulary. An effect declares what graph data an op's
# handler may touch — `validate()` enforces the grammar, the Rust emitter
# projects it into `OpMeta.effects`, and the engine records it on every
# audit line. `[]` = a pure primitive that touches no graph data.
EFFECT_VERBS = {"creates", "mutates", "reads", "deletes"}
EFFECT_TARGET_PREFIXES = ("shape:", "edge:")


@dataclass
class Effect:
    """One declared data effect of an op — `{<verb>: <target>}` in YAML.

    `verb` ∈ `EFFECT_VERBS`; `target` is `shape:<name>` / `shape:<dynamic>`
    / `edge:<label>`. `<dynamic>` marks a target chosen at runtime (an op
    whose touched shape is a request parameter)."""
    verb: str
    target: str


@dataclass
class Op:
    name: str                       # wire name, e.g. "shell.run"
    group: str                      # "shell"
    action: str                     # "run"
    doc: str
    doc_full: str
    capability: list[str] = field(default_factory=list)   # required caps; [] = none
    trace_span: bool = False
    fire_and_forget: bool = False
    request: list[OpField] = field(default_factory=list)
    response: OpResponse | None = None
    log_fields: list[OpLogField] = field(default_factory=list)
    effects: list[Effect] = field(default_factory=list)    # graph data touched; [] = pure
    leading_comment: str = ""


# =============================================================================
# IR — the root
# =============================================================================


@dataclass
class Ontology:
    """The whole normalized contract — one tree, every emitter's input."""
    shapes: list[Shape] = field(default_factory=list)
    auth_contracts: list[AuthContract] = field(default_factory=list)
    ops: list[Op] = field(default_factory=list)
    op_types: dict[str, OpType] = field(default_factory=dict)

    def auth(self, kind: str) -> AuthContract | None:
        for c in self.auth_contracts:
            if c.kind == kind:
                return c
        return None

    def op(self, name: str) -> Op | None:
        for o in self.ops:
            if o.name == name:
                return o
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
        # `display:` block — new home for `subtitle:` and the other roles.
        # Legacy top-level `subtitle: X` is still accepted (back-compat); the
        # parser hoists it into `Display(subtitle=X)` so emit/docs.py keeps
        # reading `s.subtitle` while consumers move to `s.display`.
        disp_raw = defn.get("display") or {}
        if disp_raw:
            s.display = Display(
                title=disp_raw.get("title"),
                subtitle=disp_raw.get("subtitle"),
                image=disp_raw.get("image"),
                highlights=list(disp_raw.get("highlights") or []),
                body=disp_raw.get("body"),
                preview=dict(disp_raw.get("preview") or {}),
            )
        elif "subtitle" in defn:
            s.display = Display(subtitle=defn.get("subtitle"))
        s.subtitle = s.display.subtitle if s.display else None
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
# Op-field type grammar
# =============================================================================
#
# Op field types are richer than shape types: width-precise ints, `bytes`,
# `map<K,V>`, `list<T>`, `T[]`, and references to named record types. The
# grammar is parsed into a `TypeRef` tree so emitters project it without
# re-parsing the string.

# Op primitives. `number` / `boolean` / `string` / `json` are shared with
# shapes; the width-precise ints + `bytes` are the minimal op-only extension.
_OP_PRIMITIVES = {
    "string", "boolean", "number", "bytes", "json",
    "i32", "i64", "u16", "u32", "u64",
}


@dataclass
class TypeRef:
    """A parsed op-field type."""
    kind: str                       # "primitive" | "named" | "array" | "map" | "list"
    name: str = ""                  # primitive or named-type name
    elem: "TypeRef | None" = None   # array/list element type
    key: "TypeRef | None" = None    # map key type
    val: "TypeRef | None" = None    # map value type


def _split_generic_args(s: str) -> list[str]:
    """Split `K,V` (or `T`) at top-level commas, respecting `<>` nesting."""
    args, depth, cur = [], 0, ""
    for ch in s:
        if ch == "<":
            depth += 1
            cur += ch
        elif ch == ">":
            depth -= 1
            cur += ch
        elif ch == "," and depth == 0:
            args.append(cur)
            cur = ""
        else:
            cur += ch
    if cur:
        args.append(cur)
    return [a.strip() for a in args]


def parse_type(s: str) -> TypeRef:
    """Parse an op-field type string (trailing `?` already stripped) into a
    `TypeRef`. An unknown bare word is treated as a named-type reference;
    `validate()` is what flags it if no such type is declared."""
    s = s.strip()
    if s.endswith("[]"):
        return TypeRef("array", elem=parse_type(s[:-2]))
    if s.startswith("map<") and s.endswith(">"):
        parts = _split_generic_args(s[4:-1])
        if len(parts) == 2:
            return TypeRef("map", key=parse_type(parts[0]), val=parse_type(parts[1]))
    if s.startswith("list<") and s.endswith(">"):
        return TypeRef("list", elem=parse_type(s[5:-1]))
    if s in _OP_PRIMITIVES:
        return TypeRef("primitive", name=s)
    return TypeRef("named", name=s)


# =============================================================================
# Op loader — YAML → Op
# =============================================================================

def _op_field(name: str, spec: dict | None) -> OpField:
    spec = spec or {}
    t = str(spec.get("type", "json")).strip()
    optional = t.endswith("?")
    if optional:
        t = t[:-1].strip()
    return OpField(
        name=name,
        type=t,
        optional=optional,
        has_default="default" in spec,
        default=spec.get("default"),
        doc=str(spec.get("doc", "")).strip(),
    )


def _op_field_map(spec: dict | None) -> list[OpField]:
    return [_op_field(n, fd) for n, fd in (spec or {}).items()]


def _op_effects(spec) -> list[Effect]:
    """Parse a YAML `effects:` list into `Effect`s. Each entry is a
    single-key `{<verb>: <target>}` mapping. Malformed entries become an
    `Effect` with a sentinel verb so `validate()` reports them as errors —
    parsing stays total; enforcement lives in one place."""
    out: list[Effect] = []
    for entry in spec or []:
        if isinstance(entry, dict) and len(entry) == 1:
            (verb, target), = entry.items()
            out.append(Effect(verb=str(verb), target=str(target)))
        else:
            out.append(Effect(verb="?malformed", target=repr(entry)))
    return out


def load_ops(ops_dir: Path) -> tuple[list[Op], dict[str, OpType]]:
    """Load every `ops/*.yaml` into typed Op IR + the named-type table.

    Files are read in sorted-name order; ops within a file keep YAML
    declaration order. Top-level keys: a dotted key is an op wire name;
    the `types:` key is the file's named-record-type block.
    """
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    ops: list[Op] = []
    op_types: dict[str, OpType] = {}
    for f in sorted(ops_dir.glob("*.yaml")):
        text = f.read_text()
        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            continue
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

        for key, body in data.items():
            body = body or {}
            if key == "types":
                for tname, tfields in body.items():
                    op_types[tname] = OpType(name=tname, fields=_op_field_map(tfields))
                continue
            if "." not in key:
                continue
            group, action = key.split(".", 1)

            resp_spec = body.get("response") or {}
            if "type" in resp_spec:
                rt = str(resp_spec["type"]).strip()
                ropt = rt.endswith("?")
                if ropt:
                    rt = rt[:-1].strip()
                response = OpResponse(
                    scalar=True, type=rt, type_optional=ropt,
                    doc=str(resp_spec.get("doc", "")).strip(),
                )
            else:
                response = OpResponse(scalar=False, fields=_op_field_map(resp_spec))

            cap = body.get("capability")
            if cap is None:
                cap = []
            elif isinstance(cap, str):
                cap = [cap]
            else:
                cap = list(cap)

            log_fields = [
                OpLogField(
                    source=str(lf.get("from", "")),
                    path=str(lf.get("path", "")),
                    key=str(lf.get("as", "")),
                )
                for lf in (body.get("log_fields") or [])
            ]

            ops.append(Op(
                name=key,
                group=group,
                action=action,
                doc=str(body.get("doc", "")).strip(),
                doc_full=body.get("doc_full") or body.get("doc", ""),
                capability=cap,
                trace_span=bool(body.get("trace_span", False)),
                fire_and_forget=bool(body.get("fire_and_forget", False)),
                request=_op_field_map(body.get("request")),
                response=response,
                log_fields=log_fields,
                effects=_op_effects(body.get("effects")),
                leading_comment=lead,
            ))

    return ops, op_types


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


def build(
    shapes: list[Shape],
    auth_contracts: list[AuthContract],
    ops: list[Op] | None = None,
    op_types: dict[str, OpType] | None = None,
) -> Ontology:
    """Assemble the normalized tree from already-loaded parts."""
    return Ontology(
        shapes=shapes,
        auth_contracts=auth_contracts,
        ops=ops or [],
        op_types=op_types or {},
    )


def _check_op_type(tref: TypeRef, known_types: set[str]) -> str | None:
    """Walk a parsed type; return the first unknown leaf name, or None."""
    if tref.kind == "primitive":
        return None
    if tref.kind == "named":
        return None if tref.name in known_types else tref.name
    if tref.kind in ("array", "list"):
        return _check_op_type(tref.elem, known_types) if tref.elem else None
    if tref.kind == "map":
        return (
            (_check_op_type(tref.key, known_types) if tref.key else None)
            or (_check_op_type(tref.val, known_types) if tref.val else None)
        )
    return None


def validate(onto: Ontology) -> list[tuple[str, str]]:
    """Lint the normalized tree. Returns `(severity, message)` pairs,
    severity ∈ `"error" | "warn"`.

    A `"warn"` is advisory — it reports, never transforms. An `"error"`
    means the ontology is structurally invalid; `generate.py` refuses to
    emit and exits non-zero. Shape/auth/type checks are advisory; the
    `effects:` grammar is enforced (Phase 4 — `effects` is load-bearing,
    so a malformed effect is a build failure, not a hint).
    """
    out: list[tuple[str, str]] = []
    warn = lambda m: out.append(("warn", m))    # noqa: E731
    err = lambda m: out.append(("error", m))    # noqa: E731
    shape_names = {s.name for s in onto.shapes}

    for s in onto.shapes:
        for a in s.also:
            if a not in shape_names:
                warn(f"shape {s.name!r}: `also` references unknown shape {a!r}")
        for r in s.own_relations:
            tgt = (r.target or "").rstrip("[]")
            if tgt and tgt != "node" and tgt not in shape_names:
                warn(f"shape {s.name!r}: relation {r.name!r} targets unknown shape {tgt!r}")
        for f in s.own_fields:
            base = f.type.rstrip("[]")
            if base not in _SHAPE_TYPES:
                warn(f"shape {s.name!r}: field {f.name!r} has unknown type {f.type!r}")
        # `display:` block — role bindings must reference a field or relation
        # this shape carries (resolved fields, includes inherited + standard +
        # relations). Unknown bindings are advisory warnings, not errors —
        # consistent with the rest of shape lint.
        if s.display:
            known = {f.name for f in s.fields}
            for role in ("title", "subtitle", "image", "body"):
                binding = getattr(s.display, role)
                if binding and binding not in known:
                    warn(f"shape {s.name!r}: display.{role} binds to "
                         f"unknown field/relation {binding!r}")
            for hi in s.display.highlights:
                if hi not in known:
                    warn(f"shape {s.name!r}: display.highlights includes "
                         f"unknown {hi!r}")
            if len(s.display.highlights) > 4:
                warn(f"shape {s.name!r}: display.highlights has "
                     f"{len(s.display.highlights)} entries; max is 4")
            for pk in s.display.preview:
                if pk not in known:
                    warn(f"shape {s.name!r}: display.preview key {pk!r} "
                         f"is not a declared field")

    for c in onto.auth_contracts:
        for g in c.groups:
            for f in g.required + g.recommended:
                if f.type not in _AUTH_TYPES:
                    warn(f"auth {c.kind!r}: field {f.name!r} has unknown type {f.type!r}")

    known_types = set(onto.op_types)

    def _check_op_field(where: str, f: OpField) -> None:
        unknown = _check_op_type(parse_type(f.type), known_types)
        if unknown:
            warn(f"{where}: field {f.name!r} references unknown type {unknown!r}")

    for t in onto.op_types.values():
        for f in t.fields:
            _check_op_field(f"op-type {t.name!r}", f)

    op_names: set[str] = set()
    for o in onto.ops:
        if o.name in op_names:
            err(f"op {o.name!r}: duplicate op name")
        op_names.add(o.name)
        for f in o.request:
            _check_op_field(f"op {o.name!r} request", f)
        if o.response and o.response.scalar:
            unknown = _check_op_type(parse_type(o.response.type), known_types)
            if unknown:
                warn(f"op {o.name!r} response: unknown type {unknown!r}")
        elif o.response:
            for f in o.response.fields:
                _check_op_field(f"op {o.name!r} response", f)
        for lf in o.log_fields:
            if lf.source not in ("request", "response"):
                warn(f"op {o.name!r}: log_field source {lf.source!r} not request/response")
        # `effects:` grammar — enforced. A bad verb or an unresolvable
        # `shape:` target fails the build: an effect the engine can't
        # interpret is worse than no effect at all.
        for e in o.effects:
            if e.verb not in EFFECT_VERBS:
                err(f"op {o.name!r}: effect verb {e.verb!r} not one of "
                    f"{sorted(EFFECT_VERBS)}")
            if not e.target.startswith(EFFECT_TARGET_PREFIXES):
                err(f"op {o.name!r}: effect target {e.target!r} must start with "
                    f"one of {list(EFFECT_TARGET_PREFIXES)}")
            elif e.target.startswith("shape:"):
                shape = e.target[len("shape:"):]
                if shape != "<dynamic>" and shape not in shape_names:
                    err(f"op {o.name!r}: effect targets unknown shape {shape!r}")

    return out


def serialize(onto: Ontology) -> str:
    """Render the tree to the checked-in `ir.json` — the structural diff
    + lint surface. Deterministic: shapes are name-sorted at build time,
    dataclass field order is fixed, dict order follows YAML insertion."""
    return json.dumps(asdict(onto), indent=2, ensure_ascii=False) + "\n"
