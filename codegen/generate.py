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
import json
import subprocess
import sys
from pathlib import Path

import ir
import ir_diff
from emit import (
    build_skills_index,
    discover_skills,
    emit_contract_root,
    emit_links,
    emit_migrations,
    emit_op_docs,
    emit_ops_python,
    emit_ops_rust,
    emit_ops_ts,
    emit_python,
    emit_python_auth_contracts,
    emit_rust_auth_contracts,
    emit_shape_docs,
    emit_skill_docs,
    emit_typescript,
    write_rust_sdk,
)

# Registry-driven codegen — submodules alongside this file (D11). Each
# consumes the `system.schema` registry; only used on the `--docs` path.
from tool_surface import load_tool_surface, emit_tool_surface_docs  # noqa: E402
from sdk_client import emit_sdk_client  # noqa: E402


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
    parser.add_argument("--docs", action="store_true", help="Emit MDX reference pages for shapes + skills (Starlight)")
    parser.add_argument("--skills-root", type=Path, help="Path to skills/ tree for --docs (default: ../skills)")
    parser.add_argument("--docs-out", type=Path, help="Reference output root for --docs (default: src/content/docs/reference)")
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

    # Phase 1c.3 — typed link registry. One file per label declares
    # forward/inverse names + from_kind/to_kind + cardinality + link_vals.
    import links as _links
    links_dir = platform_root / "ontology" / "links"
    typed_links = _links.load(links_dir) if links_dir.is_dir() else []
    if typed_links:
        link_errors, link_warnings = _links.validate(typed_links, {s.name for s in shapes})
        for w in link_warnings:
            print(f"  lint [warn]: {w}", file=sys.stderr)
        for e in link_errors:
            print(f"  lint [error]: {e}", file=sys.stderr)
        if link_errors:
            sys.exit(1)
        print(f"Loaded {len(typed_links)} link declarations from {links_dir}")

    ontology = ir.build(shapes, auth_contracts, ops, op_types, links=typed_links)

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
    # packages; rust writes into `platform/sdk/rust/src/shapes/` (a tree of
    # files, one per shape — shape-unification Phase 1). Use --out-dir to
    # override (e.g. for Go/Swift one-off exports).
    contract_crate = workspace / "core" / "crates" / "contract-generated" / "src"
    targets = {
        "python": platform_root / "sdk" / "python" / "agentos" / "_generated.py",
        "typescript": platform_root / "sdk" / "typescript" / "src" / "shapes.ts",
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

        # SCHEMA_HASH — deterministic content hash of the ontology, pinned
        # in every data-porter export. See platform/codegen/schema_hash.py.
        import schema_hash
        drift |= _check_or_write(
            contract_crate / "schema_hash.rs", schema_hash.emit_rust(ontology),
            "schema-hash", check=args.check,
        )

        # Typed Link enum + reflection table — projected from
        # `ontology/links/*.yaml`. Indexed by `Link as usize`; engine
        # consumes via `agentos_contract_generated::links::Link`.
        if typed_links:
            drift |= _check_or_write(
                contract_crate / "links.rs", emit_links(typed_links),
                "links", check=args.check,
            )

        # Migrations — `ontology/migrations/*.yaml` → typed `MIGRATIONS`
        # const. Engine walks the chain on `data.import`. See
        # `platform/ontology/migrations/README.md` for the grammar.
        import migrations as migrations_loader
        migrations_dir = platform_root / "ontology" / "migrations"
        if migrations_dir.is_dir():
            ms = migrations_loader.load_migrations(migrations_dir)
            drift |= _check_or_write(
                contract_crate / "migrations.rs", emit_migrations(ms),
                "migrations", check=args.check,
            )

        # Op contract — projected into the `ops` module of the contract
        # crate, plus one TS module (ops.ts) and the per-group Python op
        # stubs into the SDK package.
        if ontology.ops:
            op_targets = {
                "ops-rust": (
                    emit_ops_rust(ontology),
                    contract_crate / "ops.rs",
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
