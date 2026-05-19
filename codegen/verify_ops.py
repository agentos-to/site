#!/usr/bin/env python3
"""Phase 2 op-equivalence gate.

Proves the ontology-driven op path is behaviour-equivalent to the
hand-written one, on two surfaces:

  1. **Manifest** — runs the `contract_manifest` bin (which walks the
     generated `OpMeta` statics) and structurally diffs its output against
     the committed `core/codegen/ops-manifest.json`. Cosmetic schema keys
     (`title`, `description`, `default`, `$schema`) and struct-naming are
     normalised away; `$ref`s are resolved; behaviour — field types,
     `required`, capabilities, log fields, flags, unwrap/decode — is not.

  2. **Python stubs** — emits the op stubs from the IR and diffs them
     against the committed `sdk/python/agentos/{group}.py`. The file header
     (regen hint) and the module docstring are sourced differently in the
     new path and are reported as benign; every `async def` — signature,
     docstring, body — must be byte-identical.

Exit 0 ⇒ equivalent. Exit 1 ⇒ a behavioural difference (a real
regression) was found. Phase 3 replaces this with the CI drift gate.
"""

from __future__ import annotations

import difflib
import json
import subprocess
import sys
from pathlib import Path

import ir
from emit import emit_ops_python

_CODEGEN = Path(__file__).resolve().parent
_PLATFORM = _CODEGEN.parent
_WORKSPACE = _PLATFORM.parent
_CORE = _WORKSPACE / "core"

_COSMETIC_KEYS = {"$schema", "title", "description", "default", "examples",
                  "deprecated", "$defs", "definitions"}


# ---------------------------------------------------------------------------
# Manifest equivalence
# ---------------------------------------------------------------------------

def _resolve_ref(schema: dict, defs: dict) -> dict:
    ref = schema.get("$ref")
    if not ref:
        return schema
    name = ref.rsplit("/", 1)[-1]
    return defs.get(name, {})


def _canon(schema, defs: dict):
    """Strip a JSON schema down to its behavioural skeleton.

    `$ref`s are inlined; cosmetic keys dropped; `required` sorted. An
    unconstrained value (`true`, `{}`) and an open object
    (`{type:object, additionalProperties:true}` with no `properties`)
    both fold to the sentinel `"ANY"` — schemars renders a passthrough
    `Value` as the former, a hand-written passthrough as the latter, and
    they mean the same thing.
    """
    if schema is True or schema == {}:
        return "ANY"
    if schema is False:
        return "NEVER"
    if not isinstance(schema, dict):
        return schema

    schema = _resolve_ref(schema, defs)
    out: dict = {}
    for k, v in schema.items():
        if k in _COSMETIC_KEYS:
            continue
        out[k] = v

    if isinstance(out.get("properties"), dict):
        out["properties"] = {k: _canon(v, defs) for k, v in out["properties"].items()}
    if "items" in out:
        out["items"] = _canon(out["items"], defs)
    if isinstance(out.get("additionalProperties"), (dict, bool)):
        out["additionalProperties"] = _canon(out["additionalProperties"], defs)
    if isinstance(out.get("required"), list):
        out["required"] = sorted(out["required"])
    for comb in ("anyOf", "oneOf", "allOf"):
        if isinstance(out.get(comb), list):
            out[comb] = [_canon(x, defs) for x in out[comb]]

    if not out:
        return "ANY"
    if (out.get("type") == "object"
            and out.get("additionalProperties") in (True, "ANY")
            and "properties" not in out):
        return "ANY"
    return out


def _canon_schema(schema: dict):
    defs = schema.get("$defs") or schema.get("definitions") or {}
    return _canon(schema, defs)


def _op_behaviour(op: dict) -> dict:
    """The behavioural projection of one manifest op entry."""
    return {
        "request": _canon_schema(op.get("request_schema", {})),
        "response": _canon_schema(op.get("response_schema", {})),
        "log_fields": op.get("log_fields", []),
        "fire_and_forget": op.get("fire_and_forget", False),
        "trace_span": op.get("trace_span", False),
        "required_capabilities": op.get("required_capabilities", []),
        "response_unwrap": op.get("response_unwrap"),
        "response_decode": op.get("response_decode"),
    }


def _verify_manifest() -> bool:
    """Returns True on a clean (behaviour-equivalent) manifest."""
    print("── Manifest equivalence " + "─" * 40)
    committed_path = _CORE / "codegen" / "ops-manifest.json"
    if not committed_path.exists():
        print(f"  FAIL: {committed_path} missing")
        return False
    committed = json.loads(committed_path.read_text())

    proc = subprocess.run(
        ["cargo", "run", "-q", "-p", "agentos-contract-generated",
         "--bin", "contract_manifest"],
        cwd=_CORE, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        print("  FAIL: contract_manifest bin did not run")
        print(proc.stderr.rstrip())
        return False
    generated = json.loads(proc.stdout)

    by_old = {o["name"]: o for o in committed["ops"]}
    by_new = {o["name"]: o for o in generated["ops"]}
    if set(by_old) != set(by_new):
        print(f"  FAIL: op set differs")
        print(f"    only committed: {sorted(set(by_old) - set(by_new))}")
        print(f"    only generated: {sorted(set(by_new) - set(by_old))}")
        return False

    behavioural_ok = True
    prose_notes: list[str] = []
    for name in sorted(by_old):
        old, new = by_old[name], by_new[name]
        ob, nb = _op_behaviour(old), _op_behaviour(new)
        if ob != nb:
            behavioural_ok = False
            print(f"  REGRESSION  {name}")
            for key in ob:
                if ob[key] != nb[key]:
                    print(f"    {key}:")
                    print(f"      committed: {json.dumps(ob[key], sort_keys=True)}")
                    print(f"      generated: {json.dumps(nb[key], sort_keys=True)}")
        else:
            print(f"  ok  {name}")
        for field in ("doc", "doc_full"):
            if old.get(field, "") != new.get(field, ""):
                prose_notes.append(f"{name}.{field}")

    if prose_notes:
        print(f"  note: prose differs (non-behavioural): {', '.join(prose_notes)}")
    return behavioural_ok


# ---------------------------------------------------------------------------
# Python-stub equivalence
# ---------------------------------------------------------------------------

_BODY_ANCHOR = "from __future__ import annotations"


def _behavioural_body(text: str) -> str:
    """Everything from the first import on — the file minus its header and
    module docstring (the two surfaces sourced differently in the new path)."""
    idx = text.find(_BODY_ANCHOR)
    return text[idx:] if idx != -1 else text


def _verify_python() -> bool:
    print("\n── Python stub equivalence " + "─" * 37)
    onto = _build_ontology()
    generated = emit_ops_python(onto)
    sdk_dir = _PLATFORM / "sdk" / "python" / "agentos"

    ok = True
    for module in sorted(generated):
        committed_path = sdk_dir / f"{module}.py"
        if not committed_path.exists():
            print(f"  FAIL  {module}.py — committed stub missing")
            ok = False
            continue
        committed = committed_path.read_text()
        gen = generated[module]
        if _behavioural_body(committed) == _behavioural_body(gen):
            note = "" if committed == gen else "  (header/docstring differ — benign)"
            print(f"  ok  {module}.py{note}")
        else:
            ok = False
            print(f"  REGRESSION  {module}.py — op surface differs")
            diff = difflib.unified_diff(
                _behavioural_body(committed).splitlines(keepends=True),
                _behavioural_body(gen).splitlines(keepends=True),
                fromfile=f"committed/{module}.py",
                tofile=f"generated/{module}.py",
                n=2,
            )
            sys.stdout.writelines(diff)
    return ok


# ---------------------------------------------------------------------------

def _build_ontology() -> ir.Ontology:
    shapes = ir.load_shapes(_PLATFORM / "ontology" / "shapes")
    contracts_dir = _PLATFORM / "ontology" / "auth-contracts"
    auth = ir.load_auth_contracts(contracts_dir) if contracts_dir.is_dir() else []
    ops, op_types = ir.load_ops(_PLATFORM / "ontology" / "ops")
    return ir.build(shapes, auth, ops, op_types)


def main() -> int:
    manifest_ok = _verify_manifest()
    python_ok = _verify_python()
    print()
    if manifest_ok and python_ok:
        print("✅ Op path is behaviour-equivalent to the hand-written path.")
        return 0
    print("❌ Behavioural divergence found — see REGRESSION lines above.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
