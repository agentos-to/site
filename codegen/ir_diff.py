#!/usr/bin/env python3
"""Breaking-change gate — structural diff of two contract IR snapshots.

The IR (`codegen/ir.json`) is the contract's normalized form. This module
diffs a baseline IR against the current one and classifies every change as
either a **break** (a removal, a rename — which reads as remove + add — a
retype, or a tightening) or a **note** (advisory: an addition, a loosening).
The gate fails on any break; pure additions pass untouched.

Rules follow protobuf / buf semantics: *addition is free*, the field name is
identity and is never reused for a different type. `generate.py
--breaking-check` is the entry point; this module is the differ it calls —
it is import-pure, no git, no I/O.
"""

from __future__ import annotations

# A change: (severity, path, message). severity ∈ {"break", "note"}.
Change = tuple[str, str, str]


def _index(items: list[dict], key: str = "name") -> dict[str, dict]:
    """List of dicts → `{item[key]: item}`."""
    return {it[key]: it for it in items}


def _diff_field_map(
    path: str, base: list[dict], cur: list[dict], *, request: bool
) -> list[Change]:
    """Diff a `[OpField]` list (op request/response, named record type).

    `request=True` applies caller-facing tightening rules: a field that
    stops being omittable (loses `optional`/`default`) breaks existing
    callers, and a brand-new non-omittable field is one they never sent.
    """
    changes: list[Change] = []
    bi, ci = _index(base), _index(cur)
    for name, bf in bi.items():
        cf = ci.get(name)
        if cf is None:
            changes.append(("break", f"{path}.{name}", "field removed"))
            continue
        if bf["type"] != cf["type"]:
            changes.append(("break", f"{path}.{name}",
                            f"type changed {bf['type']!r} → {cf['type']!r}"))
        if request:
            b_omit = bf.get("optional") or bf.get("has_default")
            c_omit = cf.get("optional") or cf.get("has_default")
            if b_omit and not c_omit:
                changes.append(("break", f"{path}.{name}",
                                "became required (was omittable)"))
    for name, cf in ci.items():
        if name in bi:
            continue
        omittable = cf.get("optional") or cf.get("has_default")
        if request and not omittable:
            changes.append(("break", f"{path}.{name}",
                            "new required request field — existing callers omit it"))
        else:
            changes.append(("note", f"{path}.{name}", "field added"))
    return changes


def _diff_response(path: str, base: dict | None, cur: dict | None) -> list[Change]:
    """Diff an `OpResponse` — a scalar or a field-map, never both."""
    if base is None and cur is None:
        return []
    if base is None or cur is None:
        return [("break", f"{path} response", "response presence changed")]
    if bool(base["scalar"]) != bool(cur["scalar"]):
        return [("break", f"{path} response", "scalar / field-map form changed")]
    if base["scalar"]:
        out: list[Change] = []
        if base["type"] != cur["type"]:
            out.append(("break", f"{path} response",
                        f"scalar type {base['type']!r} → {cur['type']!r}"))
        if base.get("type_optional") and not cur.get("type_optional"):
            out.append(("note", f"{path} response", "scalar optional → required"))
        return out
    return _diff_field_map(f"{path} response", base["fields"], cur["fields"],
                           request=False)


def _diff_ops(base: list[dict], cur: list[dict]) -> list[Change]:
    changes: list[Change] = []
    bi, ci = _index(base), _index(cur)
    for name, bop in bi.items():
        cop = ci.get(name)
        if cop is None:
            changes.append(("break", f"op {name}", "op removed"))
            continue
        p = f"op {name}"
        changes += _diff_field_map(f"{p} request", bop["request"], cop["request"],
                                   request=True)
        changes += _diff_response(p, bop.get("response"), cop.get("response"))
        bcap, ccap = set(bop.get("service") or []), set(cop.get("service") or [])
        for added in sorted(ccap - bcap):
            changes.append(("break", p,
                            f"new required service {added!r} — existing apps lack it"))
        for removed in sorted(bcap - ccap):
            changes.append(("note", p, f"service {removed!r} no longer required"))
        if bool(bop.get("fire_and_forget")) != bool(cop.get("fire_and_forget")):
            changes.append(("break", p, "fire_and_forget changed — wire-ack behavior differs"))
        be = {(e["verb"], e["target"]) for e in bop.get("effects") or []}
        ce = {(e["verb"], e["target"]) for e in cop.get("effects") or []}
        for v, t in sorted(ce - be):
            changes.append(("note", p, f"new declared effect: {v} {t}"))
        for v, t in sorted(be - ce):
            changes.append(("note", p, f"declared effect removed: {v} {t}"))
    for name in ci:
        if name not in bi:
            changes.append(("note", f"op {name}", "op added"))
    return changes


def _diff_op_types(base: dict, cur: dict) -> list[Change]:
    """Diff the `types:` block. A named record may back a request, so its
    fields are diffed with the conservative caller-facing rules."""
    changes: list[Change] = []
    for name, bt in base.items():
        ct = cur.get(name)
        if ct is None:
            changes.append(("break", f"op-type {name}", "named type removed"))
            continue
        changes += _diff_field_map(f"op-type {name}", bt["fields"], ct["fields"],
                                   request=True)
    for name in cur:
        if name not in base:
            changes.append(("note", f"op-type {name}", "named type added"))
    return changes


def _diff_shapes(base: list[dict], cur: list[dict]) -> list[Change]:
    changes: list[Change] = []
    bi, ci = _index(base), _index(cur)
    for name, bs in bi.items():
        cs = ci.get(name)
        if cs is None:
            changes.append(("break", f"shape {name}", "shape removed"))
            continue
        bf, cf = _index(bs["fields"]), _index(cs["fields"])
        for fn, bfd in bf.items():
            cfd = cf.get(fn)
            if cfd is None:
                changes.append(("break", f"shape {name}.{fn}", "field removed"))
                continue
            if bfd["type"] != cfd["type"]:
                changes.append(("break", f"shape {name}.{fn}",
                                f"type {bfd['type']!r} → {cfd['type']!r}"))
            if bool(bfd["is_relation"]) != bool(cfd["is_relation"]):
                changes.append(("break", f"shape {name}.{fn}",
                                "field ⇄ relation kind changed"))
        for fn in cf:
            if fn not in bf:
                changes.append(("note", f"shape {name}.{fn}", "field added"))
    for name in ci:
        if name not in bi:
            changes.append(("note", f"shape {name}", "shape added"))
    return changes


def _diff_auth(base: list[dict], cur: list[dict]) -> list[Change]:
    changes: list[Change] = []
    bi = {c["kind"]: c for c in base}
    ci = {c["kind"]: c for c in cur}
    for kind, bc in bi.items():
        cc = ci.get(kind)
        if cc is None:
            changes.append(("break", f"auth {kind}", "contract removed"))
            continue
        bg = {g["role"]: g for g in bc["groups"]}
        cg = {g["role"]: g for g in cc["groups"]}
        for role, bgrp in bg.items():
            cgrp = cg.get(role)
            if cgrp is None:
                changes.append(("break", f"auth {kind}.{role}", "group removed"))
                continue
            breq, creq = _index(bgrp["required"]), _index(cgrp["required"])
            for fn, bfd in breq.items():
                cfd = creq.get(fn)
                if cfd is None:
                    changes.append(("break", f"auth {kind}.{role}.{fn}",
                                    "required field removed"))
                elif bfd["type"] != cfd["type"]:
                    changes.append(("break", f"auth {kind}.{role}.{fn}",
                                    f"type {bfd['type']!r} → {cfd['type']!r}"))
            for fn in creq:
                if fn not in breq:
                    changes.append(("break", f"auth {kind}.{role}.{fn}",
                                    "new required field — skills must now return it"))
    for kind in ci:
        if kind not in bi:
            changes.append(("note", f"auth {kind}", "contract added"))
    return changes


def diff(baseline: dict, current: dict) -> list[Change]:
    """Diff two IR trees (parsed `ir.json`). Deterministic, append-ordered:
    shapes, then ops, then named types, then auth contracts."""
    return (
        _diff_shapes(baseline.get("shapes", []), current.get("shapes", []))
        + _diff_ops(baseline.get("ops", []), current.get("ops", []))
        + _diff_op_types(baseline.get("op_types", {}), current.get("op_types", {}))
        + _diff_auth(baseline.get("auth_contracts", []),
                     current.get("auth_contracts", []))
    )


def breaks(changes: list[Change]) -> list[Change]:
    """The breaking subset — what fails the gate."""
    return [c for c in changes if c[0] == "break"]
