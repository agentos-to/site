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
    python generate.py --docs                 # MDX reference pages (shapes + skills)
"""

from __future__ import annotations

import argparse
import difflib
import sys
from pathlib import Path

import ir
from emit import (
    build_skills_index,
    discover_skills,
    emit_op_docs,
    emit_ops_python,
    emit_ops_rust,
    emit_ops_ts,
    emit_python,
    emit_python_auth_contracts,
    emit_rust,
    emit_rust_auth_contracts,
    emit_shape_docs,
    emit_skill_docs,
    emit_typescript,
)

# Registry-driven codegen — submodules alongside this file (D11). Each
# consumes the `system.schema` registry; only used on the `--docs` path.
from tool_surface import load_tool_surface, emit_tool_surface_docs  # noqa: E402
from sdk_client import emit_sdk_client  # noqa: E402


# The shape emitters — one per language with an SDK target. Adding a
# language is one new `emit/<lang>.py` plus an entry here and in `targets`.
EMITTERS = {
    "python": (emit_python, "_generated.py"),
    "typescript": (emit_typescript, "shape.ts"),
    "rust": (emit_rust, "lib.rs"),
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


def main():
    parser = argparse.ArgumentParser(description="Generate typed contract code for Python, TypeScript, and Rust")
    parser.add_argument("--lang", choices=list(EMITTERS.keys()), help="Language to generate (default: all)")
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

    # generate.py lives at `platform/codegen/generate.py`.
    #   codegen_dir   = platform/codegen   — also home of the checked-in ir.json
    #   platform_root = platform/          — ontology, sdk, docs all live here
    #   workspace     = ~/dev/agentos/     — the only cross-repo target is core/
    codegen_dir = Path(__file__).parent
    platform_root = codegen_dir.parent
    workspace = platform_root.parent

    # ---- Stage 1: YAML → IR --------------------------------------------------
    if args.from_api:
        agentos_bin = args.agentos_bin or "agentos"
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

    ontology = ir.build(shapes, auth_contracts, ops, op_types)

    # Validation runs on every invocation. Advisory in Phase 1 — it
    # reports, never transforms, so it cannot change emitter output.
    for warning in ir.validate(ontology):
        print(f"  lint: {warning}", file=sys.stderr)

    # ---- Stage 2 (docs path) -------------------------------------------------
    if args.docs:
        skills_root = args.skills_root or (workspace / "skills").resolve()
        docs_out = args.docs_out or (platform_root / "docs" / "src" / "content" / "docs")
        if not skills_root.is_dir():
            print(f"Skills root not found: {skills_root}", file=sys.stderr)
            sys.exit(1)
        skills = discover_skills(skills_root)
        print(f"Discovered {len(skills)} skills in {skills_root}")
        known_shapes = {s.name for s in ontology.shapes}
        skills_index = build_skills_index(skills, known_shapes)
        emit_shape_docs(ontology.shapes, docs_out / "shapes" / "reference", skills_index)
        print(f"  shapes: {docs_out / 'shapes' / 'reference'} ({len(ontology.shapes)} pages + index)")
        emit_skill_docs(skills, docs_out / "skills" / "reference", known_shapes)
        print(f"  skills: {docs_out / 'skills' / 'reference'} ({len(skills)} pages + index)")

        emit_op_docs(ontology.ops, ontology.op_types, docs_out / "ops" / "reference")
        print(f"  ops: {docs_out / 'ops' / 'reference'} ({len(ontology.ops)} ops)")

        # Registry-driven codegen — both outputs read the same `system.schema`
        # dump. Opt out cleanly if the engine isn't running.
        agentos_bin = args.agentos_bin or "agentos"
        try:
            namespaces = load_tool_surface(agentos_bin)
        except SystemExit:
            print(f"  tool-surface + sdk-client: skipped (engine unreachable) — run `./dev.sh restart` and retry", file=sys.stderr)
            return

        emit_tool_surface_docs(namespaces, docs_out / "tool-surface")
        ops_total = sum(len(ns.get("ops", [])) for ns in namespaces)
        print(f"  tool-surface: {docs_out / 'tool-surface'} ({len(namespaces)} namespaces, {ops_total} ops)")

        sdk_out = platform_root / "sdk" / "python" / "agentos" / "_engine_client.py"
        sdk_out.write_text(emit_sdk_client(namespaces))
        print(f"  sdk-client: {sdk_out}")
        return

    # ---- Stage 2 (default path): IR → emitters -------------------------------
    # Output destinations per language — python/ts write into the in-repo SDK
    # packages; rust is the one cross-repo write, into core/. Use --out-dir to
    # override (e.g. for Go/Swift one-off exports).
    targets = {
        "python": platform_root / "sdk" / "python" / "agentos" / "_generated.py",
        "typescript": platform_root / "sdk" / "typescript" / "src" / "shapes.ts",
        "rust": workspace / "core" / "crates" / "shapes-generated" / "src" / "lib.rs",
    }

    langs = [args.lang] if args.lang else list(EMITTERS.keys())
    drift = False
    for lang in langs:
        emitter, filename = EMITTERS[lang]
        output = emitter(ontology)
        out_path = args.out_dir / filename if args.out_dir else targets[lang]
        drift |= _check_or_write(out_path, output, lang, check=args.check)

    # The auth contracts + the checked-in IR artifact are emitted only on a
    # full default run — `--lang` and `--from-api` are one-off / export modes.
    if not args.lang and not args.from_api:
        ir_path = codegen_dir / "ir.json"
        drift |= _check_or_write(ir_path, ir.serialize(ontology), "ir", check=args.check)

        # Op contract — projected beside the shape targets: one Rust crate
        # (contract-generated), one TS module (ops.ts), and the per-group
        # Python op stubs into the SDK package.
        if ontology.ops:
            op_targets = {
                "ops-rust": (
                    emit_ops_rust(ontology),
                    workspace / "core" / "crates" / "contract-generated" / "src" / "lib.rs",
                ),
                "ops-ts": (
                    emit_ops_ts(ontology),
                    platform_root / "sdk" / "typescript" / "src" / "ops.ts",
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
