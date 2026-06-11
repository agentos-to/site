#!/usr/bin/env python3
"""Deterministic content hash of the AgentOS ontology.

Pinned in every data-porter export so `data.import` can detect schema
drift on read. The hash covers the *structural* subset of the
ontology — anything that affects the wire shape of data, links, or
ops — and excludes documentation, display config, source paths, and
leading comments.

What's hashed (Phase 1a):
  - Shapes: name, fields (name/type/is_relation/is_array/target),
            identity, identity_any, also
  - Ops:    name, group, action, service, request, response,
            log_fields, effects
  - Services: name, params, returns (the brokered-interface registry)
  - OpTypes: name, fields
  - AuthContracts: kind, groups

Phase 1c will add the `links/` registry (one file per link label) to
the hash input; the projection function below already names a `links:`
key so the format-version pin doesn't need to change.

Algorithm:
  1. Project each top-level entity into its schema-relevant view.
  2. Sort entities by canonical key (name / kind).
  3. Sort dict keys recursively via json.dumps(sort_keys=True).
  4. Canonical JSON encoding: no whitespace, no escapes beyond ASCII fallback.
  5. sha256 → "sha256:<64 hex chars>".

The output is `sha256:<hex>`. Anything else (a different hash kind,
truncation) is reserved for the future; readers can split on `:`.
"""
from __future__ import annotations

import hashlib
import json
from typing import Any

# Format version — bump when the projection function changes shape.
# Included in the hash input so a projection-logic change ALSO produces
# a new hash even if the ontology is byte-identical.
SCHEMA_FORMAT_VERSION = "v1"


def _field_view(f) -> dict[str, Any]:
    return {
        "name": f.name,
        "type": f.type,
        "is_relation": f.is_relation,
        "is_array": f.is_array,
        "target": f.target,
    }


def _shape_view(shape) -> dict[str, Any]:
    return {
        "name": shape.name,
        "fields": sorted(
            [_field_view(f) for f in shape.fields],
            key=lambda f: f["name"],
        ),
        "identity": sorted(shape.identity),
        "identity_any": sorted(shape.identity_any),
        "also": sorted(shape.also),
    }


def _op_field_view(f) -> dict[str, Any]:
    return {
        "name": f.name,
        "type": f.type,
        "optional": f.optional,
        "has_default": f.has_default,
        "default": f.default,
    }


def _op_response_view(resp) -> dict[str, Any] | None:
    if resp is None:
        return None
    if resp.scalar:
        return {"scalar": True, "type": resp.type, "optional": resp.type_optional}
    return {
        "scalar": False,
        "fields": sorted(
            [_op_field_view(f) for f in resp.fields],
            key=lambda f: f["name"],
        ),
    }


def _log_field_view(f) -> dict[str, Any]:
    return {"source": f.source, "path": f.path, "key": f.key}


def _effect_view(e) -> dict[str, Any]:
    return {"verb": e.verb, "target": e.target}


def _op_view(op) -> dict[str, Any]:
    return {
        "name": op.name,
        "group": op.group,
        "action": op.action,
        "service": sorted(op.service),
        "request": sorted(
            [_op_field_view(f) for f in op.request],
            key=lambda f: f["name"],
        ),
        "response": _op_response_view(op.response),
        "log_fields": sorted(
            [_log_field_view(f) for f in op.log_fields],
            key=lambda f: (f["source"], f["path"]),
        ),
        "effects": sorted(
            [_effect_view(e) for e in op.effects],
            key=lambda e: (e["verb"], e["target"]),
        ),
    }


def _op_type_view(name: str, op_type) -> dict[str, Any]:
    return {
        "name": name,
        "fields": sorted(
            [_op_field_view(f) for f in op_type.fields],
            key=lambda f: f["name"],
        ),
    }


def _auth_field_view(f) -> dict[str, Any]:
    return {"name": f.name, "type": f.type}


def _auth_group_view(g) -> dict[str, Any]:
    return {
        "role": g.role,
        "required": sorted(
            [_auth_field_view(f) for f in g.required],
            key=lambda f: f["name"],
        ),
        "recommended": sorted(
            [_auth_field_view(f) for f in g.recommended],
            key=lambda f: f["name"],
        ),
    }


def _auth_contract_view(c) -> dict[str, Any]:
    return {
        "kind": c.kind,
        "groups": sorted(
            [_auth_group_view(g) for g in c.groups],
            key=lambda g: g["role"],
        ),
    }


def _link_view(link) -> dict[str, Any]:
    """Project one typed link's structural surface for the hash.

    v2 Link dataclass shape: name, from_kind, to_kind, cardinality, link_vals,
    inverse_of, plus provenance fields (group_file, verb_root,
    preposition_root) that are intentionally excluded — file reorganization
    must NOT bump the schema hash, only semantic changes should.
    """
    return {
        "name": link.name,
        "from_kind": link.from_kind,
        "to_kind": link.to_kind,
        "cardinality": link.cardinality,
        "link_vals": dict(sorted((link.link_vals or {}).items())),
        "inverse_of": link.inverse_of,
    }


def _service_view(s) -> dict[str, Any]:
    """One service's structural surface: id, params, returns. Description
    and leading comments are docs — excluded, like everywhere else."""
    return {
        "name": s.name,
        "params": json.loads(json.dumps(s.params, sort_keys=True)),
        "returns": s.returns,
    }


def schema_view(ontology) -> dict[str, Any]:
    """The schema-relevant projection of the ontology, deterministic order."""
    return {
        "schema_format_version": SCHEMA_FORMAT_VERSION,
        "shapes": sorted(
            [_shape_view(s) for s in ontology.shapes],
            key=lambda s: s["name"],
        ),
        "links": sorted(
            [_link_view(l) for l in (ontology.links or [])],
            key=lambda l: l["name"],
        ),
        "ops": sorted(
            [_op_view(o) for o in ontology.ops],
            key=lambda o: o["name"],
        ),
        "op_types": sorted(
            [_op_type_view(name, t) for name, t in ontology.op_types.items()],
            key=lambda t: t["name"],
        ),
        "auth_contracts": sorted(
            [_auth_contract_view(c) for c in ontology.auth_contracts],
            key=lambda c: c["kind"],
        ),
        "services": sorted(
            [_service_view(s) for s in (ontology.services or [])],
            key=lambda s: s["name"],
        ),
    }


def compute(ontology) -> str:
    """Return `sha256:<hex>` for the ontology's schema-relevant view."""
    view = schema_view(ontology)
    canonical = json.dumps(view, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    return f"sha256:{digest}"


def emit_rust(ontology) -> str:
    """Render `core/crates/contract-generated/src/schema_hash.rs`."""
    hash_value = compute(ontology)
    return (
        "// DO NOT EDIT — generated from platform/ontology/ by platform/codegen/.\n"
        "// Regen: `python3 platform/codegen/generate.py`.\n"
        "//\n"
        "// Deterministic content hash of the AgentOS ontology — pinned in\n"
        "// every data-porter export to detect schema drift on import.\n"
        "// Computed by `platform/codegen/schema_hash.py` over a canonical\n"
        "// JSON projection that excludes documentation, display config,\n"
        "// and leading comments.\n"
        "\n"
        "#![allow(clippy::all)]\n"
        "\n"
        "/// Content hash of the structural ontology (`sha256:<hex>`).\n"
        f'pub const SCHEMA_HASH: &str = "{hash_value}";\n'
        "\n"
        "/// Format version of the projection that produced `SCHEMA_HASH`.\n"
        "/// Bumped when `platform/codegen/schema_hash.py` changes shape.\n"
        f'pub const SCHEMA_FORMAT_VERSION: &str = "{SCHEMA_FORMAT_VERSION}";\n'
    )


if __name__ == "__main__":
    # `python3 schema_hash.py` from inside platform/codegen prints the
    # current hash without writing anything.
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).parent))
    import ir
    import links as _links
    platform_root = Path(__file__).parent.parent
    shapes = ir.load_shapes(platform_root / "ontology" / "shapes")
    auth_contracts = ir.load_auth_contracts(platform_root / "ontology" / "auth-contracts")
    ops, op_types = ir.load_ops(platform_root / "ontology" / "ops")
    typed_links = _links.load(platform_root / "ontology" / "links")
    ontology = ir.build(shapes, auth_contracts, ops, op_types, links=typed_links)
    print(compute(ontology))
