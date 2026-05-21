#!/usr/bin/env python3
"""Migration loader — `ontology/migrations/*.yaml` → typed Migration IR.

Each file declares one schema migration (`from` hash → `to` hash + an
ordered op list). The loader validates structure and op vocabulary;
detailed per-op param checking happens at emit time.

Output is a deterministic `list[Migration]` keyed by `from` hash so
the engine can walk a chain in O(N) by following `from → to` edges.
"""
from __future__ import annotations

import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


# Op vocabulary — the 13 known migration op kinds, each mapped to its
# W/S classification. `add_field` is classified at runtime based on
# `optional` / `default` params (W if either present; S otherwise).
WEAKENING_OPS = {
    "add_node_type",
    "widen_field_type",
    "extend_enum",
    "set_meta",
    "set_doc",
}
STRENGTHENING_OPS = {
    "drop_node_type",
    "rename_node_type",
    "drop_field",
    "rename_field",
    "narrow_field_type",
    "rename_link",
    "rename_link_val",
    "move_to_event",
    "flip_link",
}
PARAMETERIZED_OPS = {"add_field"}  # severity depends on params
KNOWN_OPS = WEAKENING_OPS | STRENGTHENING_OPS | PARAMETERIZED_OPS

# Param signatures per op kind. Each value is (required_keys, optional_keys).
OP_SIGNATURES: dict[str, tuple[set[str], set[str]]] = {
    "add_node_type":      ({"name"},                                set()),
    "add_field":          ({"shape", "name", "type"},               {"optional", "default"}),
    "widen_field_type":   ({"shape", "field", "from", "to"},        set()),
    "extend_enum":        ({"shape", "field", "add"},               set()),
    "set_meta":           ({"shape", "key", "value"},               set()),
    "set_doc":            ({"shape", "value"},                      set()),
    "drop_node_type":     ({"name"},                                {"cascade"}),
    "rename_node_type":   ({"from", "to"},                          set()),
    "drop_field":         ({"shape", "name"},                       set()),
    "rename_field":       ({"shape", "from", "to"},                 set()),
    "narrow_field_type":  ({"shape", "field", "from", "to", "default"}, set()),
    "rename_link":        ({"from", "to"},                          set()),
    "rename_link_val":    ({"link", "from", "to"},                  set()),
    "move_to_event":      ({"shape"},                               set()),
    "flip_link":          ({"from", "to"},                          set()),
}

HASH_RE = re.compile(r"^sha256:[0-9a-f]{64}$")


@dataclass
class MigrationOp:
    """One ordered op in a migration. `kind` ∈ KNOWN_OPS."""
    kind: str
    params: dict[str, Any] = field(default_factory=dict)


@dataclass
class Migration:
    """One migration file: `from → to` + ordered ops + provenance."""
    id: str                  # file basename without .yaml
    from_hash: str
    to_hash: str
    doc: str
    ops: list[MigrationOp] = field(default_factory=list)
    source_path: str = ""    # relative path for error messages


def _parse_op(spec: Any, file_id: str, idx: int) -> MigrationOp:
    if not isinstance(spec, dict) or len(spec) != 1:
        raise ValueError(
            f"{file_id}: op #{idx} must be a single-key dict "
            f"({{op_kind: {{params}}}}); got {spec!r}"
        )
    [(kind, params)] = spec.items()
    if kind not in KNOWN_OPS:
        raise ValueError(
            f"{file_id}: op #{idx} kind {kind!r} unknown. "
            f"Valid kinds: {sorted(KNOWN_OPS)}"
        )
    params = params or {}
    if not isinstance(params, dict):
        raise ValueError(
            f"{file_id}: op #{idx} ({kind}) params must be a mapping; "
            f"got {params!r}"
        )
    required, optional = OP_SIGNATURES[kind]
    keys = set(params.keys())
    missing = required - keys
    extra = keys - required - optional
    if missing:
        raise ValueError(f"{file_id}: op #{idx} ({kind}) missing required params: {sorted(missing)}")
    if extra:
        raise ValueError(f"{file_id}: op #{idx} ({kind}) unknown params: {sorted(extra)}")
    return MigrationOp(kind=kind, params=dict(params))


def load_migrations(migrations_dir: Path) -> list[Migration]:
    """Load every `migrations/*.yaml` into typed Migration IR.

    Files are read in sorted-name order (the `NNN-` prefix is a
    filesystem convention only — the runtime chain walks by `from/to`
    hash, not filename). Ops within a file keep YAML declaration order;
    that order is part of the migration's identity.
    """
    try:
        import yaml
    except ImportError:
        print("pyyaml required: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    out: list[Migration] = []
    for f in sorted(migrations_dir.glob("*.yaml")):
        file_id = f.stem
        try:
            data = yaml.safe_load(f.read_text())
        except yaml.YAMLError as exc:
            raise ValueError(f"{file_id}: invalid YAML — {exc}") from exc
        if not isinstance(data, dict):
            raise ValueError(f"{file_id}: top-level must be a mapping")

        for required_key in ("from", "to", "doc", "ops"):
            if required_key not in data:
                raise ValueError(f"{file_id}: missing required key {required_key!r}")

        from_hash = str(data["from"])
        to_hash = str(data["to"])
        if not HASH_RE.match(from_hash):
            raise ValueError(f"{file_id}: `from` must match sha256:<64hex>; got {from_hash!r}")
        if not HASH_RE.match(to_hash):
            raise ValueError(f"{file_id}: `to` must match sha256:<64hex>; got {to_hash!r}")
        if from_hash == to_hash:
            raise ValueError(f"{file_id}: `from` and `to` are identical — empty migration")

        doc = str(data["doc"]).strip()
        if not doc:
            raise ValueError(f"{file_id}: `doc` cannot be empty")

        raw_ops = data["ops"]
        if not isinstance(raw_ops, list) or not raw_ops:
            raise ValueError(f"{file_id}: `ops` must be a non-empty list")

        ops = [_parse_op(spec, file_id, idx) for idx, spec in enumerate(raw_ops)]

        out.append(Migration(
            id=file_id,
            from_hash=from_hash,
            to_hash=to_hash,
            doc=doc,
            ops=ops,
            source_path=str(f.relative_to(migrations_dir.parent.parent)),
        ))
    return out


def op_severity(op: MigrationOp) -> str:
    """Return 'weakening' or 'strengthening' for a single op."""
    if op.kind in WEAKENING_OPS:
        return "weakening"
    if op.kind in STRENGTHENING_OPS:
        return "strengthening"
    # add_field: W if optional OR has a non-Error default; S otherwise.
    assert op.kind == "add_field"
    if op.params.get("optional"):
        return "weakening"
    default = op.params.get("default")
    if isinstance(default, dict) and default.get("type") == "Default":
        return "weakening"
    return "strengthening"


def migration_severity(m: Migration) -> str:
    """A migration is strengthening if any op is; otherwise weakening."""
    return "strengthening" if any(op_severity(op) == "strengthening" for op in m.ops) else "weakening"
