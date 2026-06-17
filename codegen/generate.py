#!/usr/bin/env python3
"""Contract codegen — orchestrator for the `YAML → IR → emitters` pipeline.

`ir.py` parses `ontology/{shapes,auth-contracts}/*.yaml` into one
normalized `Ontology` tree and validates it. The emitters under `emit/`
are dumb projections off that tree. This file is just the conductor:
it builds the IR, runs validation, and drives each emitter to its SDK
target — or, with `--check`, compares without writing (the drift gate).

Usage:
    python generate.py                        # Python + TypeScript + Rust into SDK targets
    python generate.py --lang python          # one language, Python TypedDicts only
    python generate.py --check                # drift check — exit 1 if any target is stale
    python generate.py --from-api             # load shapes from the graph instead of YAML
    python generate.py --from-api --dump-yaml ./shapes  # export graph → YAML
    python generate.py --sdk-client           # Python engine client from the live registry
"""

from __future__ import annotations

import argparse
import difflib
import json
import subprocess
import sys
from pathlib import Path

import ir
import ir_diff
from emit import (
    emit_contract_root,
    emit_ops_python,
    emit_ops_rust,
    emit_python,
    emit_python_auth_contracts,
    emit_rust_auth_contracts,
    emit_typescript,
    emit_yaml_symbols,
    write_rust_sdk,
)

# Registry-driven codegen — consumes the live engine's `system.schema`
# registry; only used on the `--sdk-client` path.
from tool_surface import load_tool_surface  # noqa: E402
from sdk_client import emit_sdk_client  # noqa: E402


def _default_agentos_bin() -> str:
    """The engine CLI to query for registry-driven codegen.

    The engine builds into the sibling core repo's `target/`, and the
    bare `agentos` on PATH (if any) may be stale — prefer the workspace
    debug binary, fall back to PATH.
    """
    workspace_bin = Path(__file__).resolve().parent.parent.parent / "core" / "target" / "debug" / "agentos"
    return str(workspace_bin) if workspace_bin.is_file() else "agentos"


# The shape emitters — one per language with an SDK target. Adding a
# language is one new `emit/<lang>.py` plus an entry here and in `targets`.
#
# Rust is intentionally absent — its emitter (`emit/rust_sdk.py`) writes
# a *tree* of files under `platform/sdk/rust/src/shapes/`, not a single
# output, so it can't share the `(emitter, filename)` shape. Wired
# separately below the EMITTERS loop.
EMITTERS = {
    "python": (emit_python, "_generated.py"),
    "typescript": (emit_typescript, "shape.ts"),
}


def _check_or_write(out_path: Path, output: str, label: str, *, check: bool) -> bool:
    """Write `output` to `out_path`, or (with --check) compare. Returns True on drift."""
    if check:
        existing = out_path.read_text() if out_path.exists() else ""
        if existing != output:
            print(f"  {label}: DRIFT — {out_path} is stale", file=sys.stderr)
            diff = "".join(difflib.unified_diff(
                existing.splitlines(keepends=True),
                output.splitlines(keepends=True),
                fromfile=str(out_path),
                tofile="<generated>",
                n=2,
            ))
            if diff:
                sys.stderr.write(diff)
            return True
        print(f"  {label}: ok ({out_path})")
        return False
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(output)
    print(f"  {label}: {out_path}")
    return False


def run_breaking_check(ontology: "ir.Ontology", codegen_dir: Path) -> int:
    """Breaking-change gate — diff the current IR against the last release
    tag's `codegen/ir.json`. Returns a process exit code.

    Dormant until a `v*` tag exists: with no tagged release there is no
    contract to break, so the gate passes and the first tag laid down
    becomes the baseline. Once tagged, any removal / rename / retype /
    tightening fails; pure additions pass.
    """
    platform_root = codegen_dir.parent
    tags = subprocess.run(
        ["git", "-C", str(platform_root), "tag", "-l", "v*",
         "--sort=-version:refname"],
        capture_output=True, text=True,
    )
    tag = ""
    if tags.returncode == 0:
        for line in tags.stdout.splitlines():
            if line.strip():
                tag = line.strip()
                break
    if not tag:
        print("breaking-check: no `v*` release tag — gate dormant. The first "
              "release tag becomes the contract baseline.")
        return 0

    show = subprocess.run(
        ["git", "-C", str(platform_root), "show", f"{tag}:codegen/ir.json"],
        capture_output=True, text=True,
    )
    if show.returncode != 0:
        print(f"breaking-check: {tag} carries no codegen/ir.json — nothing to "
              f"diff against; gate dormant.", file=sys.stderr)
        return 0

    baseline = json.loads(show.stdout)
    current = json.loads(ir.serialize(ontology))
    changes = ir_diff.diff(baseline, current)
    for severity, path, msg in changes:
        stream = sys.stderr if severity == "break" else sys.stdout
        print(f"  {severity}: {path} — {msg}", file=stream)

    breaking = ir_diff.breaks(changes)
    if breaking:
        print(f"\n❌ breaking-check: {len(breaking)} breaking change(s) vs {tag}. "
              f"The contract is append-only — a removal, rename, retype, or "
              f"tightening needs a new release line, not an edit to this one.",
              file=sys.stderr)
        return 1
    print(f"breaking-check: clean vs {tag} "
          f"({len(changes)} additive/advisory change(s)).")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Generate typed contract code for Python, TypeScript, and Rust")
    parser.add_argument("--lang", choices=list(EMITTERS.keys()), help="Language to generate (default: all)")
    parser.add_argument("--shapes-dir", type=Path, help="Path to shapes/ directory")
    parser.add_argument("--out-dir", type=Path, help="Output directory (default: target inside sibling SDK repo)")
    parser.add_argument("--from-api", action="store_true", help="Load shapes from graph via agentos CLI instead of YAML files")
    parser.add_argument("--agentos-bin", type=str, help="Path to agentos binary (default: agentos)")
    parser.add_argument("--dump-yaml", type=Path, help="With --from-api: also dump each shape as YAML to this directory (backup/export)")
    parser.add_argument("--sdk-client", action="store_true", help="Regenerate the Python SDK engine client from the live engine's registry")
    parser.add_argument("--check", action="store_true", help="Drift check: compare rendered output to files on disk; exit 1 if different")
    parser.add_argument("--breaking-check", action="store_true", help="Breaking-change gate: diff the IR against the last release tag; exit 1 on a removal/rename/retype/tightening")
    parser.add_argument("--conformance", action="store_true", help="Cross-language conformance: prove Python + TypeScript project the fixture set identically to Rust (the Rust half runs via `./dev.sh test`)")
    args = parser.parse_args()

    # generate.py lives at `platform/codegen/generate.py`.
    #   codegen_dir   = platform/codegen   — also home of the checked-in ir.json
    #   platform_root = platform/          — ontology, sdk, docs all live here
    #   workspace     = ~/dev/agentos/     — the only cross-repo target is core/
    codegen_dir = Path(__file__).parent
    platform_root = codegen_dir.parent
    workspace = platform_root.parent

    # ---- Stage 1: YAML → IR --------------------------------------------------
    if args.from_api:
        agentos_bin = args.agentos_bin or _default_agentos_bin()
        shapes = ir.load_shapes_from_api(agentos_bin)
        print(f"Loaded {len(shapes)} shapes from graph API")
        if args.dump_yaml:
            ir.dump_yaml_from_api(agentos_bin, args.dump_yaml)
    else:
        shapes_dir = args.shapes_dir or platform_root / "ontology" / "shapes"
        if not shapes_dir.is_dir():
            print(f"Shapes directory not found: {shapes_dir}", file=sys.stderr)
            sys.exit(1)
        shapes = ir.load_shapes(shapes_dir)
        print(f"Loaded {len(shapes)} shapes from {shapes_dir}")

    contracts_dir = platform_root / "ontology" / "auth-contracts"
    auth_contracts = ir.load_auth_contracts(contracts_dir) if contracts_dir.is_dir() else []

    ops_dir = platform_root / "ontology" / "ops"
    ops, op_types = ir.load_ops(ops_dir) if ops_dir.is_dir() else ([], {})

    # Services are not authored. A service exists because an app
    # `@provides` it — the engine self-registers a `shape:service` node
    # from the union of provider declarations at boot (see
    # `core/.../apps/seed.rs::mint_service_graph`). The SDK ships only
    # the broker (`services.call` / `list_providers`), generated from the
    # `services` op group like any other op stub — no registry, no
    # constants, no `returns:` contract. Same move as edges: the verb
    # space is emergent, never declared.

    ontology = ir.build(shapes, auth_contracts, ops, op_types)

    # Validation runs on every invocation. `warn` is advisory; `error`
    # means the ontology is structurally invalid (e.g. a malformed
    # `effects:` entry) — refuse to emit rather than project garbage.
    lint = ir.validate(ontology)
    for severity, msg in lint:
        print(f"  lint [{severity}]: {msg}", file=sys.stderr)
    if any(severity == "error" for severity, _ in lint):
        print("Ontology is invalid — fix the errors above before generating.",
              file=sys.stderr)
        sys.exit(1)

    # ---- Breaking-change gate ------------------------------------------------
    # Independent of emission — diffs the IR against the last release tag.
    if args.breaking_check:
        sys.exit(run_breaking_check(ontology, codegen_dir))

    # ---- Cross-language conformance ------------------------------------------
    # The Python + TypeScript halves; the Rust half is `./dev.sh test`.
    if args.conformance:
        sys.exit(subprocess.run(
            [sys.executable, str(codegen_dir / "conformance" / "check.py")],
        ).returncode)

    # ---- Stage 2 (sdk-client path) --------------------------------------------
    # Registry-driven codegen — reads the live engine's `system.schema` dump,
    # so it runs on demand, never on the drift-gated default path.
    if args.sdk_client:
        agentos_bin = args.agentos_bin or _default_agentos_bin()
        namespaces = load_tool_surface(agentos_bin)
        sdk_out = platform_root / "sdk" / "python" / "agentos" / "_engine_client.py"
        sdk_out.write_text(emit_sdk_client(namespaces))
        print(f"  sdk-client: {sdk_out}")
        return

    # ---- Stage 2 (default path): IR → emitters -------------------------------
    # Output destinations per language — python writes into the in-repo SDK
    # package; typescript writes the desktop shell's contract module
    # (core/web/src/contract-generated/ — the TS mirror of the
    # contract-generated crate); rust writes into
    # `platform/sdk/rust/src/shapes/` (a tree of files, one per shape —
    # shape-unification Phase 1). Use --out-dir to override (e.g. for
    # Go/Swift one-off exports).
    contract_crate = workspace / "core" / "crates" / "contract-generated" / "src"
    targets = {
        "python": platform_root / "sdk" / "python" / "agentos" / "_generated.py",
        "typescript": workspace / "core" / "web" / "src" / "contract-generated" / "shapes.ts",
    }

    langs = [args.lang] if args.lang else list(EMITTERS.keys()) + ["rust"]
    drift = False
    for lang in langs:
        if lang == "rust":
            # rust_sdk writes a tree, not a single file — no string-compare
            # against `targets` makes sense. With --check, we'd have to walk
            # the existing tree and diff each file; v1 just re-emits and
            # relies on git to flag drift.
            rust_sdk_root = (
                args.out_dir / "shapes"
                if args.out_dir
                else platform_root / "sdk" / "rust" / "src" / "shapes"
            )
            written = write_rust_sdk(ontology, rust_sdk_root)
            print(f"  rust: {rust_sdk_root} ({len(written)} files)")
            continue
        emitter, filename = EMITTERS[lang]
        output = emitter(ontology)
        out_path = args.out_dir / filename if args.out_dir else targets[lang]
        drift |= _check_or_write(out_path, output, lang, check=args.check)

    # The auth contracts + the checked-in IR artifact are emitted only on a
    # full default run — `--lang` and `--from-api` are one-off / export modes.
    if not args.lang and not args.from_api:
        ir_path = codegen_dir / "ir.json"
        drift |= _check_or_write(ir_path, ir.serialize(ontology), "ir", check=args.check)

        # The contract crate root — declares the `shapes` + `ops` modules
        # whose bodies the rust emitters wrote into the sibling files.
        drift |= _check_or_write(
            contract_crate / "lib.rs", emit_contract_root(),
            "contract-root", check=args.check,
        )

        # System Docs symbols — shapes + ops projected into the same compact
        # symbol records the engine's rustdoc/ts-morph extractors emit. The
        # engine embeds the artifact via `include_str!` and replays it into
        # the System Docs volume at boot (core/crates/core/src/code_symbols.rs).
        drift |= _check_or_write(
            workspace / "core" / "crates" / "core" / "generated" / "yaml-symbols.json",
            emit_yaml_symbols(ontology), "yaml-symbols", check=args.check,
        )

        # Op contract — projected into the `ops` module of the contract
        # crate, plus the per-group Python op stubs into the SDK package.
        # No TS projection: the shell consumes no op contract today; add a
        # target here the day a consumer exists.
        if ontology.ops:
            op_targets = {
                "ops-rust": (
                    emit_ops_rust(ontology),
                    contract_crate / "ops.rs",
                ),
            }
            for label, (output, out_path) in op_targets.items():
                drift |= _check_or_write(out_path, output, label, check=args.check)

            # Python op stubs — one agentos/<group>.py per pure-generated group.
            py_pkg = platform_root / "sdk" / "python" / "agentos"
            for group, body in sorted(emit_ops_python(ontology).items()):
                drift |= _check_or_write(
                    py_pkg / f"{group}.py", body, f"ops-python:{group}", check=args.check
                )

        if ontology.auth_contracts:
            ac_targets = {
                "auth-python": (
                    emit_python_auth_contracts(ontology),
                    platform_root / "sdk" / "python" / "agentos" / "_generated_auth_contracts.py",
                ),
                "auth-rust": (
                    emit_rust_auth_contracts(ontology),
                    workspace / "core" / "crates" / "auth" / "src" / "_generated_contracts.rs",
                ),
            }
            for label, (output, out_path) in ac_targets.items():
                drift |= _check_or_write(out_path, output, label, check=args.check)

    if args.check and drift:
        sys.exit(1)


if __name__ == "__main__":
    main()
