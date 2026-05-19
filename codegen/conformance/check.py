#!/usr/bin/env python3
"""Cross-language conformance — the Python + TypeScript halves.

Reads `conformance/fixtures.json` — one fixture set, each entry a canonical
wire payload for some op request/response — and proves the Python op stubs
and the TypeScript op types project the same contract the Rust structs do.
The Rust half is `core/crates/contract-generated/tests/conformance.rs`,
run by `./dev.sh test`; this script is the other two halves plus an
IR cross-check.

  IR      — every fixture's op/kind/fields are checked against the ontology,
            so a stale fixture is caught before it can mask real drift.
  Python  — load each generated stub with a capturing `dispatch`, call it
            with the fixture as kwargs, assert the request dict it builds
            equals the fixture. The stub *is* the Python serializer.
  TS      — emit a `.ts` that assigns each fixture to its `ops.ts` type and
            run `tsc --noEmit`; the type system is the TS contract. Skipped
            with a notice when the TS SDK has no installed `tsc`.

Invoked by `generate.py --conformance`; also runnable standalone.
"""

from __future__ import annotations

import asyncio
import importlib.util
import json
import subprocess
import sys
import types
from pathlib import Path

CONFORMANCE_DIR = Path(__file__).parent
CODEGEN_DIR = CONFORMANCE_DIR.parent
PLATFORM_ROOT = CODEGEN_DIR.parent

sys.path.insert(0, str(CODEGEN_DIR))
import ir  # noqa: E402
from emit.ops_python import _PURE_OP_GROUPS  # noqa: E402


def load_fixtures() -> list[dict]:
    return json.loads((CONFORMANCE_DIR / "fixtures.json").read_text())


# ---------------------------------------------------------------------------
# IR cross-check — the fixture set must describe ops that actually exist.
# ---------------------------------------------------------------------------

def check_ir(fixtures: list[dict], ops: list[ir.Op]) -> list[str]:
    by_name = {o.name: o for o in ops}
    errors: list[str] = []
    for fx in fixtures:
        fid = f"{fx['op']}/{fx['kind']}/{fx['case']}"
        op = by_name.get(fx["op"])
        if op is None:
            errors.append(f"{fid}: no such op in the ontology")
            continue
        value, kind = fx["value"], fx["kind"]
        if kind == "request":
            names = {f.name for f in op.request}
            for k in value:
                if k not in names:
                    errors.append(f"{fid}: request key {k!r} is not a declared field")
            for f in op.request:
                if not f.optional and not f.has_default and f.name not in value:
                    errors.append(f"{fid}: required request field {f.name!r} missing")
        elif kind == "response":
            if op.response and not op.response.scalar:
                names = {f.name for f in op.response.fields}
                for k in value:
                    if k not in names:
                        errors.append(
                            f"{fid}: response key {k!r} is not a declared field")
        else:
            errors.append(f"{fid}: kind must be 'request' or 'response'")
    return errors


# ---------------------------------------------------------------------------
# Python half — drive each generated stub with a capturing dispatch.
# ---------------------------------------------------------------------------

class _Captured(Exception):
    """Raised by the fake `dispatch` once it has the request dict — short-
    circuits the stub before its (untyped) response handling runs."""


def _install_fake_agentos() -> dict:
    """Stub out the `agentos` package so a generated op module loads without
    running the SDK's heavy `__init__.py`. Returns the capture cell the fake
    `dispatch` writes into."""
    pkg = types.ModuleType("agentos")
    pkg.__path__ = [str(PLATFORM_ROOT / "sdk" / "python" / "agentos")]
    sys.modules["agentos"] = pkg

    captured: dict = {}

    async def dispatch(op, req):
        captured.clear()
        captured.update(op=op, req=req)
        raise _Captured

    bridge = types.ModuleType("agentos._bridge")
    bridge.dispatch = dispatch
    sys.modules["agentos._bridge"] = bridge
    return captured


def _load_stub(group: str):
    pkg_dir = PLATFORM_ROOT / "sdk" / "python" / "agentos"
    spec = importlib.util.spec_from_file_location(
        f"agentos.{group}", pkg_dir / f"{group}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[f"agentos.{group}"] = mod
    spec.loader.exec_module(mod)
    return mod


def check_python(fixtures: list[dict]) -> tuple[int, int, list[str]]:
    """Returns `(checked, skipped, errors)`. Only request fixtures for
    pure-generated op groups have a Python stub to drive — the rest skip."""
    captured = _install_fake_agentos()
    checked = skipped = 0
    errors: list[str] = []
    stubs: dict[str, object] = {}

    for fx in fixtures:
        op_name, kind = fx["op"], fx["kind"]
        group, action = op_name.split(".", 1)
        fid = f"{op_name}/{kind}/{fx['case']}"
        if kind != "request" or group not in _PURE_OP_GROUPS:
            skipped += 1
            continue
        if group not in stubs:
            try:
                stubs[group] = _load_stub(group)
            except Exception as e:  # noqa: BLE001
                errors.append(f"{fid}: failed to load stub `agentos/{group}.py`: {e}")
                continue
        fn = getattr(stubs[group], action, None)
        if fn is None:
            errors.append(f"{fid}: stub `agentos/{group}.py` has no `{action}`")
            continue
        try:
            asyncio.run(fn(**fx["value"]))
        except _Captured:
            pass
        except TypeError as e:
            errors.append(f"{fid}: stub signature rejects the fixture — {e}")
            continue
        except Exception as e:  # noqa: BLE001
            errors.append(f"{fid}: stub raised {type(e).__name__}: {e}")
            continue
        if captured.get("op") != op_name:
            errors.append(f"{fid}: stub dispatched {captured.get('op')!r}")
        elif captured.get("req") != fx["value"]:
            errors.append(
                f"{fid}: request dict diverged\n    fixture: {fx['value']}\n"
                f"    built:   {captured.get('req')}")
        else:
            checked += 1
    return checked, skipped, errors


# ---------------------------------------------------------------------------
# TypeScript half — assign each fixture to its `ops.ts` type, run `tsc`.
# ---------------------------------------------------------------------------

def _ts_type(fx: dict) -> str:
    base = ir.to_class_name(fx["op"].split(".", 1)[0]) + \
        ir.to_class_name(fx["op"].split(".", 1)[1])
    return base + ("Request" if fx["kind"] == "request" else "Response")


def check_ts(fixtures: list[dict]) -> tuple[str, list[str]]:
    """Returns `(status, messages)` — status ∈ ok | skipped | fail."""
    ts_sdk = PLATFORM_ROOT / "sdk" / "typescript"
    tsc = ts_sdk / "node_modules" / ".bin" / "tsc"
    if not tsc.exists():
        return "skipped", [
            f"TS conformance skipped — no `tsc`. Run `npm install` in {ts_sdk}."]

    types_used = sorted({_ts_type(fx) for fx in fixtures})
    lines = [
        "// DO NOT EDIT — generated by conformance/check.py for `tsc --noEmit`.",
        "// Each fixture is assigned to its ops.ts type; tsc is the check.",
        "import type {",
        *(f"  {t}," for t in types_used),
        '} from "../../sdk/typescript/src/ops";',
        "",
    ]
    for i, fx in enumerate(fixtures):
        lines.append(f"const _f{i}: {_ts_type(fx)} = {json.dumps(fx['value'])};")
    lines += ["", "export {};", ""]

    conf_ts = CONFORMANCE_DIR / "_conformance.ts"
    conf_ts.write_text("\n".join(lines))

    result = subprocess.run(
        [str(tsc), "--noEmit", "--strict", "--target", "ES2022",
         "--module", "ES2022", "--moduleResolution", "Bundler",
         "--skipLibCheck", str(conf_ts)],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        return "fail", [(result.stdout + result.stderr).strip()]
    return "ok", []


# ---------------------------------------------------------------------------
# Entry point.
# ---------------------------------------------------------------------------

def run() -> int:
    fixtures = load_fixtures()
    ops, _op_types = ir.load_ops(PLATFORM_ROOT / "ontology" / "ops")

    ir_errors = check_ir(fixtures, ops)
    py_checked, py_skipped, py_errors = check_python(fixtures)
    ts_status, ts_msgs = check_ts(fixtures)

    print(f"conformance: {len(fixtures)} fixtures")
    for e in ir_errors:
        print(f"  ir   FAIL: {e}", file=sys.stderr)
    if not ir_errors:
        print(f"  ir   ok ({len(fixtures)} fixtures match the ontology)")

    for e in py_errors:
        print(f"  py   FAIL: {e}", file=sys.stderr)
    if not py_errors:
        print(f"  py   ok ({py_checked} stubs driven, {py_skipped} skipped — "
              f"response / hand-written group)")

    for m in ts_msgs:
        stream = sys.stderr if ts_status == "fail" else sys.stdout
        print(f"  ts   {ts_status}: {m}", file=stream)
    if ts_status == "ok":
        print(f"  ts   ok ({len(fixtures)} fixtures type-check against ops.ts)")

    failed = bool(ir_errors) or bool(py_errors) or ts_status == "fail"
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(run())
