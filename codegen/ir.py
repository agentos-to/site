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
DISPLAY_ROLES = {"title", "subtitle", "image", "highlights", "body", "mono"}


@dataclass
class Display:
    title: str | None = None         # → a field (default: `name`)
    subtitle: str | None = None      # → a field or relation
    image: str | None = None         # → a field (url) or a relation → node.image
    highlights: list[str] = field(default_factory=list)  # 0..4 fields/relations
    body: str | None = None          # detail-only: one long text field
    mono: str | None = None          # → a preformatted text field (Unicode QR
                                     #   block, ASCII art) — renderers must keep
                                     #   its geometry: monospace, no re-wrap,
                                     #   no newline-flattening
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
    ancestors: list[str] = field(default_factory=list)        # transitive `also:` closure — every shape this one inherits from, walk order (immediate parents first, then grandparents, deduped).
    field_order: list[str] = field(default_factory=list)      # YAML declaration order, this shape's own fields first, then inherited via `also:` (deduped). Drives `SHAPE_FIELD_ORDER` per the life-events plan — author order is meaning.
    derived: dict = field(default_factory=dict)               # `derived:` block — per-field read-side bindings. Values are raw dicts with `find` / `where` / `where_link` / `is` / `get` / `latest`. See event-derived-attributes plan §"The derived block".
    shortcuts: dict = field(default_factory=dict)             # `shortcuts:` block — per-flat-key write-side expansions. Each entry maps a flat create-key to a single canonical write target (e.g. `birthdate: {writes: born_in[is=birth].startDate}`).
    prefs_schemas: dict = field(default_factory=dict)         # `prefsSchemas:` block — shape-level pref vocabulary (namespace → entries[]). Settings reads it off the shape-def node to render its tabs. `user` is the canonical case; any shape can declare one.


# =============================================================================
# IR — auth contracts
# =============================================================================
#
# `ontology/auth-contracts/{oauth,cookie}.yaml` declares what apps
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
# apps call (`shell.run`, `http.request`, …). Each op has a typed request
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
EFFECT_TARGET_PREFIXES = ("shape:", "link:")


@dataclass
class Effect:
    """One declared data effect of an op — `{<verb>: <target>}` in YAML.

    `verb` ∈ `EFFECT_VERBS`; `target` is `shape:<name>` / `shape:<dynamic>`
    / `link:<label>`. `<dynamic>` marks a target chosen at runtime (an op
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
    service: list[str] = field(default_factory=list)    # required services; [] = none
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


# =============================================================================
# IR — event types
# =============================================================================
#
# Event types are first-class shapes. Each subtype (`birth`, `transition`,
# `launch`, `meeting`, ...) lives in its own `shapes/*.yaml` and chains
# `also: [event]`. The shape IS the type — no separate registry, no
# `eventType` string discriminator. `event_shape_names(ontology)`
# derives the list at codegen time from the shape graph.


@dataclass
class Ontology:
    """The whole normalized contract — one tree, every emitter's input."""
    shapes: list[Shape] = field(default_factory=list)
    auth_contracts: list[AuthContract] = field(default_factory=list)
    ops: list[Op] = field(default_factory=list)
    op_types: dict[str, OpType] = field(default_factory=dict)
    links: list = field(default_factory=list)  # list[links.Link] — Phase 1c.3
    services: list = field(default_factory=list)  # list[services.Service]

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

    def event_shape_names(self) -> list[str]:
        """Names of every shape whose `also:` chain transitively includes
        `event`, plus `event` itself. Sorted. Drives `EVENT_TYPES` emission
        per language — the shape IS the type."""
        out = [s.name for s in self.shapes
               if s.name == "event" or "event" in s.ancestors]
        return sorted(out)


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


def _shape_yaml_loader():
    """A SafeLoader that keeps `on`/`off`/`yes`/`no` as strings.

    YAML 1.1 resolves those words as booleans, but they appear as LINK
    LABELS in shape files (`email —on→ domain`) where a `True:` key
    silently corrupts the relation map. `true`/`false` still parse as
    booleans — only the ambiguous English words become strings."""
    import yaml

    class ShapeLoader(yaml.SafeLoader):
        pass

    bool_tag = "tag:yaml.org,2002:bool"
    import re as _re
    strict_bool = _re.compile(r"^(?:true|True|TRUE|false|False|FALSE)$")
    for ch in list("oOyYnNtTfF"):
        existing = ShapeLoader.yaml_implicit_resolvers.get(ch, [])
        replaced = []
        for tag, regexp in existing:
            if tag == bool_tag:
                replaced.append((tag, strict_bool))
            else:
                replaced.append((tag, regexp))
        ShapeLoader.yaml_implicit_resolvers[ch] = replaced
    return ShapeLoader


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
    loader = _shape_yaml_loader()
    for f in sorted(yaml_files):
        text = f.read_text()
        data = yaml.load(text, Loader=loader)
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
        for label, target in (defn.get("links") or {}).items():
            rels[label] = str(target)
        return rels

    def resolve_display(name: str, seen: set | None = None) -> Display | None:
        """Walk `also:` and deep-merge `display:` per role — most-specific
        wins. Mirrors `resolve_fields` / `resolve_relations`. Scalar roles
        (title/subtitle/image/body) override; `highlights` replaces the
        whole list when re-declared (a child opts-in to parent highlights
        by re-listing them); `preview` merges per-field key.

        Returns None when no shape in the chain declared a `display:` (or
        legacy top-level `subtitle:`)."""
        if seen is None:
            seen = set()
        if name in seen or name not in raw:
            return None
        seen.add(name)
        defn = raw.get(name, {})

        merged: Display | None = None
        for also in defn.get("also", []):
            parent = resolve_display(also, seen)
            if parent is None:
                continue
            if merged is None:
                merged = Display(
                    title=parent.title,
                    subtitle=parent.subtitle,
                    image=parent.image,
                    highlights=list(parent.highlights),
                    body=parent.body,
                    mono=parent.mono,
                    preview=dict(parent.preview),
                )
            else:
                # Later parent overrides earlier (sibling parents): the
                # rightmost `also:` entry is the closer relative.
                if parent.title is not None:    merged.title = parent.title
                if parent.subtitle is not None: merged.subtitle = parent.subtitle
                if parent.image is not None:    merged.image = parent.image
                if parent.body is not None:     merged.body = parent.body
                if parent.mono is not None:     merged.mono = parent.mono
                if parent.highlights:           merged.highlights = list(parent.highlights)
                for k, v in parent.preview.items():
                    merged.preview[k] = v

        # Own display — legacy top-level `subtitle:` accepted as shorthand.
        disp_raw = defn.get("display") or {}
        if not disp_raw and "subtitle" in defn:
            disp_raw = {"subtitle": defn.get("subtitle")}

        if disp_raw:
            if merged is None:
                merged = Display(
                    title=disp_raw.get("title"),
                    subtitle=disp_raw.get("subtitle"),
                    image=disp_raw.get("image"),
                    highlights=list(disp_raw.get("highlights") or []),
                    body=disp_raw.get("body"),
                    mono=disp_raw.get("mono"),
                    preview=dict(disp_raw.get("preview") or {}),
                )
            else:
                if disp_raw.get("title") is not None:    merged.title = disp_raw["title"]
                if disp_raw.get("subtitle") is not None: merged.subtitle = disp_raw["subtitle"]
                if disp_raw.get("image") is not None:    merged.image = disp_raw["image"]
                if disp_raw.get("body") is not None:     merged.body = disp_raw["body"]
                if disp_raw.get("mono") is not None:     merged.mono = disp_raw["mono"]
                if disp_raw.get("highlights"):           merged.highlights = list(disp_raw["highlights"])
                for k, v in (disp_raw.get("preview") or {}).items():
                    merged.preview[k] = v

        return merged

    def resolve_field_order(name: str, seen: set | None = None) -> list[str]:
        """Per-shape declaration-order field list, this shape's fields first,
        then each `also:` parent's fields appended (deduped). Drives
        SHAPE_FIELD_ORDER per the life-events plan — author order is meaning."""
        if seen is None:
            seen = set()
        if name in seen or name not in raw:
            return []
        seen.add(name)
        defn = raw.get(name, {})
        out: list[str] = []
        for fname in (defn.get("fields") or {}).keys():
            if fname not in out:
                out.append(fname)
        for also in defn.get("also") or []:
            for fname in resolve_field_order(also, seen):
                if fname not in out:
                    out.append(fname)
        return out

    def resolve_ancestors(name: str, seen: set | None = None) -> list[str]:
        """Transitive `also:` closure for one shape. Walk order: immediate
        parents first (in declaration order), then their parents, deduped.
        Used by the display resolver to pick the most-specific shape when
        a node carries multiple `shape[]` members."""
        if seen is None:
            seen = set()
        if name in seen or name not in raw:
            return []
        seen.add(name)
        defn = raw.get(name, {})
        out: list[str] = []
        for also in defn.get("also", []):
            if also not in raw:
                continue
            if also not in out:
                out.append(also)
            for a in resolve_ancestors(also, seen):
                if a not in out:
                    out.append(a)
        return out

    shapes = []
    for shape_name in sorted(raw.keys()):
        defn = raw.get(shape_name, {})
        s = Shape(name=shape_name, class_name=to_class_name(shape_name))

        # Metadata used by the doc emitter
        s.also = list(defn.get("also") or [])
        s.plural = defn.get("plural")
        # `display:` block — resolved through the `also:` chain so a child
        # shape inherits its parents' role bindings unless it re-declares
        # them. `s.display` is the *merged* spec; the emitters carry it to
        # the SDKs so both resolvers stay one-line lookups. Legacy
        # top-level `subtitle: X` is accepted inside resolve_display().
        s.display = resolve_display(shape_name)
        s.subtitle = s.display.subtitle if s.display else None
        s.ancestors = resolve_ancestors(shape_name)
        s.field_order = resolve_field_order(shape_name)
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

        # `derived:` + `shortcuts:` blocks — raw dicts, validated by
        # `validate()` against the relation graph (any `find:` must be a
        # known relation label; any `is:` must be a known shape name; any
        # `shortcuts.X.writes:` must resolve to a valid link label).
        derived = defn.get("derived") or {}
        if isinstance(derived, dict):
            s.derived = derived
        shortcuts = defn.get("shortcuts") or {}
        if isinstance(shortcuts, dict):
            s.shortcuts = shortcuts

        # `prefsSchemas:` block — shape-level pref vocabulary. Carried
        # through to the Rust/TS SDKs so Settings can render its tabs
        # off the shape-def node without a second source of truth.
        prefs_schemas = defn.get("prefsSchemas") or {}
        if isinstance(prefs_schemas, dict):
            s.prefs_schemas = prefs_schemas

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
        for label, target in (defn.get("links") or {}).items():
            tgt_s = str(target)
            is_array = tgt_s.endswith("[]")
            s.own_relations.append(Field(label, tgt_s, True, is_array, tgt_s.rstrip("[]")))

        # Relations resolved up front so they can SHADOW a same-named
        # field: when a shape models a concept as an link (`book
        # --author--> person`), the link is the source of truth — the
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

            cap = body.get("service")
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
                service=cap,
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


# Rule 1 — an event is a relationship; time and place ride on it. A
# `datetime` on a non-event shape is a denormalization bug. This
# allowlist is the narrow exception: transaction-time stamps ("when
# AgentOS learned this fact") are fine on any node per rule 6 (two
# clocks). Everything else gets a warning that surfaces three fixes:
# (a) link val on a verb link, (b) promote to an event node, (c) add
# the field name here if it really is transaction-time.
TRANSACTION_TIME_ALLOWLIST = {
    # generic transaction-time stamps
    "recorded_at", "created_at", "updated_at", "dateUpdated",
    "lastSeen", "last_synced_at", "synced_at", "crawled_at",
    "fetched_at", "lastSynced",
    # auth / credential lifecycle (when AgentOS learned the creds)
    "lastVerified", "lastActive", "lastProfileFetch", "obtainedAt",
    # execution span — "when this process ran on this machine"
    "startedAt", "endedAt", "committedAt",
    # challenge lifecycle — when a login artifact (QR ref, mailed code)
    # stops being usable; an intrinsic TTL on a machine-minted ephemeral,
    # not a world-fact about another party (auth_challenge)
    "expiresAt",
    # search-index recency
    "indexedAt",
    # account onboarding-time
    "joinedDate",
}


def build(
    shapes: list[Shape],
    auth_contracts: list[AuthContract],
    ops: list[Op] | None = None,
    op_types: dict[str, OpType] | None = None,
    links: list | None = None,
    services: list | None = None,
) -> Ontology:
    """Assemble the normalized tree from already-loaded parts."""
    return Ontology(
        shapes=shapes,
        auth_contracts=auth_contracts,
        ops=ops or [],
        op_types=op_types or {},
        links=links or [],
        services=services or [],
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
        # Rule 1: orphan-datetime check. A `datetime` on a non-event shape
        # is a denormalized date for a relationship — should be an link
        # val or an event node. Skip event-derived shapes (the date lives
        # naturally on the event) and the transaction-time allowlist.
        # Hard error after the life-events migration — the ontology is
        # not allowed to grow a new orphan datetime without an explicit
        # decision (allowlist, event-derive, or migrate the field).
        is_event_derived = s.name == "event" or "event" in s.ancestors
        if not is_event_derived:
            for f in s.own_fields:
                if f.type == "datetime" and f.name not in TRANSACTION_TIME_ALLOWLIST:
                    err(f"shape {s.name!r}: field {f.name!r} is a datetime "
                        f"on a non-event shape (rule 1). Fix: (a) link val "
                        f"on the verb link that earns this date, (b) promote "
                        f"to an event node with `--<verb>--> event {{startDate}}`, "
                        f"or (c) add {f.name!r} to TRANSACTION_TIME_ALLOWLIST "
                        f"in ir.py if it's really 'when AgentOS learned this'.")
        # `display:` block — role bindings must reference a field or relation
        # this shape carries (resolved fields, includes inherited + standard +
        # relations). Unknown bindings are advisory warnings, not errors —
        # consistent with the rest of shape lint.
        #
        # A binding may also be dotted (`born_in.startDate`) — depth-1
        # recursion per the life-events plan. The relation half must be a
        # known relation label; the field half is not validated here
        # (resolved against the target's own shape at render time).
        if s.display:
            known = {f.name for f in s.fields}
            # Derived bindings are also valid as display references — they
            # project onto the node JSON at read time and look like plain
            # fields to the display resolver (Phase 3 of event-derived-attributes).
            known |= set((s.derived or {}).keys())

            def _known_binding(binding: str) -> bool:
                # Dotted bindings (`born_in.startDate`) walk a verb link.
                # Per rule 4, verb links aren't owned by shapes — `person`
                # declares no `born_in` even though the canonical home for
                # birthdate is `person --born_in--> event`. The validator
                # therefore accepts any dotted binding; the resolver
                # silently returns nothing if no matching link exists.
                if "." in binding:
                    return True
                return binding in known

            for role in ("title", "subtitle", "image", "body", "mono"):
                binding = getattr(s.display, role)
                if binding and not _known_binding(binding):
                    warn(f"shape {s.name!r}: display.{role} binds to "
                         f"unknown field/relation {binding!r}")
            for hi in s.display.highlights:
                if not _known_binding(hi):
                    warn(f"shape {s.name!r}: display.highlights includes "
                         f"unknown {hi!r}")
            if len(s.display.highlights) > 4:
                warn(f"shape {s.name!r}: display.highlights has "
                     f"{len(s.display.highlights)} entries; max is 4")
            for pk in s.display.preview:
                if pk not in known:
                    warn(f"shape {s.name!r}: display.preview key {pk!r} "
                         f"is not a declared field")

    # `derived:` + `shortcuts:` lint. Per rule 4 (links aren't owned by
    # shapes), verb labels like `born_in` / `lived_at` / `changed` are
    # NOT declared on any shape — they're just verbs. The resolver returns
    # None gracefully if a verb doesn't match any link, so we don't warn
    # on unknown `find:` / `writes:` verbs. Only the `is:` filter is
    # globally checkable: shapes ARE formally declared.

    def _check_binding(where: str, b: object) -> None:
        """Walk a single derived binding. String form: dotted sugar
        (`born_in.startDate`). Dict form: `{find, where, where_link, is, get}`."""
        if isinstance(b, str):
            return  # dotted sugar — no useful lint
        if not isinstance(b, dict):
            warn(f"{where}: binding must be a string or dict, got {type(b).__name__}")
            return
        is_ = b.get("is")
        if is_ and is_ not in shape_names:
            warn(f"{where}: `is: {is_!r}` references unknown shape")

    for s in onto.shapes:
        for field_name, binding in (s.derived or {}).items():
            where = f"shape {s.name!r}: derived.{field_name}"
            if isinstance(binding, dict) and "latest" in binding:
                arms = binding["latest"] or []
                if not isinstance(arms, list):
                    warn(f"{where}.latest: expected a list, got {type(arms).__name__}")
                    continue
                for i, arm in enumerate(arms):
                    _check_binding(f"{where}.latest[{i}]", arm)
            else:
                _check_binding(where, binding)
        for flat_key, entry in (s.shortcuts or {}).items():
            where = f"shape {s.name!r}: shortcuts.{flat_key}"
            if not isinstance(entry, dict):
                warn(f"{where}: expected a dict with `writes:`, got "
                     f"{type(entry).__name__}")
                continue
            writes = entry.get("writes")
            if not isinstance(writes, str):
                warn(f"{where}: missing or non-string `writes:` value")

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
