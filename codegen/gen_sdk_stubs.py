#!/usr/bin/env python3
"""Generate Python SDK stubs from core/codegen/ops-manifest.json.

The manifest is the source of truth — `gen_manifest` walks `agentos-ops`
meta statics and emits the JSON; this script turns each op into a typed
async function in the Python SDK. Pure-generated modules are rewritten
whole-file; modules with hand-written content use the
`<generated-begin hash=...>` / `<generated-end>` markers to swap just
the generated block in place.

Exit codes:
  0   All stubs regenerated successfully.
  1   Drift detected in --check mode (diff printed to stderr).
  2   Fatal codegen error (bad schema, marker corruption).

Usage:
  python3 platform/codegen/gen_sdk_stubs.py          Rewrite stubs in place.
  python3 platform/codegen/gen_sdk_stubs.py --check  Verify on-disk matches.
  python3 platform/codegen/gen_sdk_stubs.py --sdk /path/to/skills-sdk
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any

# Pure-generated modules — whole file is regenerated each run. Hand-written
# SDK modules (http, llm, …) are handled by a separate path introduced in
# Phase 5 via `<generated-begin hash=…>` / `<generated-end>` markers.
PURE_GENERATED = {"secrets", "crypto", "plist", "shell", "sql", "progress", "capability"}

# Top-of-file docstring per module. Keeps the generated prose consistent
# across regenerations without depending on any one op's `doc_full`.
MODULE_DOC = {
    "secrets": (
        "OS-level secret store access through the engine.\n\n"
        "Reads entries from the platform's secret store — macOS login "
        "keychain via the `security` CLI, Windows Credential Manager, "
        "or Linux Secret Service. The underlying platform is chosen by "
        "the Rust crate `agentos-secrets` at compile time via "
        "`#[cfg(target_os)]`. All calls are async and routed through "
        "the engine so every read is logged and auditable."
    ),
    "crypto": (
        "Cryptographic primitives — key derivation and symmetric decrypt.\n\n"
        "Used almost exclusively by browser cookie decryption "
        "(Brave/Chrome/Edge all share the PBKDF2 + AES-128-CBC recipe)."
    ),
    "plist": (
        "NSKeyedArchiver binary plist parsing.\n\n"
        "Used by browser skills to extract structured fields from "
        "keychain-stored NSKeyedArchiver blobs (Chrome Safe Storage, "
        "Mimestream OAuth entries, etc.)."
    ),
    "shell": (
        "Controlled binary execution through the engine.\n\n"
        "Shell interpreters (sh, bash, zsh, fish, etc.) are blocked "
        "at the handler. Every invocation is audited."
    ),
    "sql": (
        "SQLite query/execute through the engine.\n\n"
        "Replaces direct sqlite3 usage. All queries are routed for "
        "logging, path validation, and future permission controls."
    ),
    "progress": (
        "Job-progress updates — fire-and-forget.\n\n"
        "`progress.report` publishes on the job event bus and does "
        "not return a payload."
    ),
    "capability": (
        "Generic capability dispatch — one primitive over every "
        "`@provides(X)` skill.\n\n"
        "`capability.call(name, verb, params)` matchmakes a provider "
        "for the named capability and dispatches `verb` on it. "
        "`capability.list_providers(name)` enumerates candidates "
        "without dispatching. Replaces per-capability bespoke SDK "
        "wrappers — skills that need cross-skill access to a "
        "capability reach through this module, and the engine never "
        "needs bespoke Rust per new capability."
    ),
}

FILE_HEADER = (
    "# This file is AUTO-GENERATED. Do not edit.\n"
    "# Regenerate with `./dev.sh build` or "
    "`python3 codegen/gen_sdk_stubs.py`.\n"
)


def load_manifest(path: Path) -> dict[str, Any]:
    with path.open() as f:
        data = json.load(f)
    if data.get("version") != 1:
        raise SystemExit(
            f"[gen_sdk_stubs] unsupported manifest version: {data.get('version')}"
        )
    return data


def group_by_module(ops: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    groups: dict[str, list[dict[str, Any]]] = {}
    for op in ops:
        name = op["name"]
        if "." not in name:
            raise SystemExit(f"[gen_sdk_stubs] op name must be dotted: {name!r}")
        module, _action = name.split(".", 1)
        groups.setdefault(module, []).append(op)
    return groups


def py_name(action: str) -> str:
    return action


def action_of(op_name: str) -> str:
    return op_name.split(".", 1)[1]


# --------------------------------------------------------------------------
# Schema → Python type mapping (§6.4)
# --------------------------------------------------------------------------

_PRIMITIVE_MAP = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
}


def _resolve_ref(schema: dict[str, Any], defs: dict[str, Any]) -> dict[str, Any]:
    ref = schema.get("$ref")
    if not ref:
        return schema
    name = ref.rsplit("/", 1)[-1]
    resolved = defs.get(name)
    if resolved is None:
        raise SystemExit(f"[gen_sdk_stubs] unresolved $ref: {ref}")
    return resolved


def schema_to_py_type(
    schema: dict[str, Any] | bool,
    defs: dict[str, Any] | None = None,
) -> str:
    """Best-effort JSON Schema → Python type. Keeps it conservative — when
    in doubt, falls back to `Any` (typing import added by the emitter).
    """
    if defs is None:
        defs = {}
    if schema is True or schema is None:
        return "Any"
    if schema is False:
        return "None"

    schema = _resolve_ref(schema, defs)

    if isinstance(schema.get("anyOf"), list):
        parts = [schema_to_py_type(s, defs) for s in schema["anyOf"]]
        non_null = [p for p in parts if p != "None"]
        if len(parts) != len(non_null) and len(non_null) == 1:
            return f"{non_null[0]} | None"
        return " | ".join(parts) if parts else "Any"
    if isinstance(schema.get("oneOf"), list):
        parts = [schema_to_py_type(s, defs) for s in schema["oneOf"]]
        non_null = [p for p in parts if p != "None"]
        if len(parts) != len(non_null) and len(non_null) == 1:
            return f"{non_null[0]} | None"
        return " | ".join(parts) if parts else "Any"

    t = schema.get("type")
    if isinstance(t, list):
        parts = [_PRIMITIVE_MAP.get(x, "Any") for x in t if x != "null"]
        has_null = "null" in t
        base = " | ".join(dict.fromkeys(parts)) if parts else "Any"
        return f"{base} | None" if has_null else base

    if t == "string":
        return "str"
    if t == "integer":
        return "int"
    if t == "number":
        return "float"
    if t == "boolean":
        return "bool"
    if t == "array":
        items = schema.get("items", True)
        return f"list[{schema_to_py_type(items, defs)}]"
    if t == "object":
        additional = schema.get("additionalProperties")
        if additional and isinstance(additional, dict):
            return f"dict[str, {schema_to_py_type(additional, defs)}]"
        # Properties present → dict with Any values (TypedDict support
        # lands with hybrid mode in a later phase).
        return "dict[str, Any]"
    return "Any"


# --------------------------------------------------------------------------
# Stub emitters
# --------------------------------------------------------------------------


def _request_fields(
    request_schema: dict[str, Any]
) -> tuple[list[tuple[str, str, bool]], dict[str, Any]]:
    """Returns [(name, py_type, required)], plus the $defs table.

    Required fields come first, in `required` declaration order (so
    `sql.query` emits `sql, db` — matching the SQL-first mental model —
    rather than the alphabetical property order). Optional fields follow
    alphabetically for keyword-arg stability.
    """
    defs = request_schema.get("$defs", {})
    props = request_schema.get("properties", {}) or {}
    required_order = list(request_schema.get("required", []) or [])
    required_set = set(required_order)
    optional_names = sorted(n for n in props if n not in required_set)
    fields: list[tuple[str, str, bool]] = []
    for pname in required_order:
        if pname not in props:
            continue
        py_t = schema_to_py_type(props[pname], defs)
        fields.append((pname, py_t, True))
    for pname in optional_names:
        py_t = schema_to_py_type(props[pname], defs)
        fields.append((pname, py_t, False))
    return fields, defs


def _response_type(op: dict[str, Any]) -> str:
    resp = op.get("response_schema", {})
    unwrap = op.get("response_unwrap")
    decode = op.get("response_decode")
    if decode == "hex":
        return "bytes"
    if unwrap == "scalar":
        # Transparent newtype — wire shape is a bare primitive. schemars 0.9
        # drops the `extend` marker on transparent newtypes, so we fall back
        # to the raw type in the schema and keep conservative.
        t = schema_to_py_type(resp, resp.get("$defs", {}))
        return t
    # Object response — stubs return dict[str, Any] today. Hybrid mode in
    # Phase 5 will swap these to TypedDicts.
    return "dict[str, Any]"


def emit_op(op: dict[str, Any]) -> str:
    action = action_of(op["name"])
    fire_and_forget = op.get("fire_and_forget", False)
    fields, _defs = _request_fields(op.get("request_schema", {}))
    resp_t = "None" if fire_and_forget else _response_type(op)
    unwrap = op.get("response_unwrap")
    decode = op.get("response_decode")

    # Build signature: required fields positional, optional as kw-only with
    # `= None`. Keeps hand-written calls mostly source-compatible. If the
    # schema already admits null (so the type ends in ` | None`), don't
    # double-wrap — emit it verbatim.
    def _optional_annot(t: str) -> str:
        return t if t.endswith("| None") or t == "None" else f"{t} | None"

    pos_params = [f"{n}: {t}" for n, t, req in fields if req]
    kw_params = [f"{n}: {_optional_annot(t)} = None" for n, t, req in fields if not req]
    signature_parts = pos_params
    if kw_params:
        signature_parts.append("*")
        signature_parts.extend(kw_params)
    signature = ", ".join(signature_parts)

    doc_full = op.get("doc_full") or op.get("doc", "")
    # Indent the docstring uniformly by 4 spaces for the function body.
    doc_indented = "\n".join(
        ("    " + line) if line else line for line in doc_full.splitlines()
    )

    # Use an underscored local to avoid shadowing any op field literally
    # named `params` (e.g. `sql.query`).
    local = "_req"
    lines: list[str] = []
    lines.append(f"async def {action}({signature}) -> {resp_t}:")
    if doc_indented:
        lines.append('    """')
        lines.append(doc_indented.rstrip())
        lines.append('    """')
    lines.append(f"    {local}: dict[str, Any] = {{}}")
    for n, _t, req in fields:
        if req:
            lines.append(f"    {local}[{n!r}] = {n}")
        else:
            lines.append(f"    if {n} is not None:")
            lines.append(f"        {local}[{n!r}] = {n}")
    if fire_and_forget:
        lines.append(f"    await dispatch({op['name']!r}, {local})")
        lines.append("    return None")
    elif decode == "hex":
        lines.append(f"    hex_value = await dispatch({op['name']!r}, {local})")
        lines.append("    return bytes.fromhex(hex_value)")
    else:
        lines.append(f"    return await dispatch({op['name']!r}, {local})")
    lines.append("")
    return "\n".join(lines)


def emit_module(module: str, ops: list[dict[str, Any]]) -> str:
    header = FILE_HEADER
    module_doc = MODULE_DOC.get(module, f"Generated stubs for `{module}` ops.")
    body = [
        header,
        f'"""{module_doc}"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from agentos._bridge import dispatch",
        "",
        "",
    ]
    ops_sorted = sorted(ops, key=lambda o: o["name"])
    for op in ops_sorted:
        body.append(emit_op(op))
        body.append("")
    text = "\n".join(body).rstrip() + "\n"
    return text


# --------------------------------------------------------------------------
# Hash / marker helpers — used by hybrid mode (Phase 5+)
# --------------------------------------------------------------------------


def block_hash(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:12]


MARKER_BEGIN_RE = re.compile(
    r"^# <generated-begin hash=(?P<hash>[a-f0-9]+)>\s*$", re.MULTILINE
)
MARKER_END_RE = re.compile(r"^# <generated-end>\s*$", re.MULTILINE)


# --------------------------------------------------------------------------
# Writers
# --------------------------------------------------------------------------


def write_file(path: Path, content: str, *, check: bool) -> bool:
    """Returns True on drift (check mode) or change (write mode)."""
    existing = path.read_text() if path.exists() else ""
    if existing == content:
        return False
    if check:
        sys.stderr.write(f"[gen_sdk_stubs] drift: {path}\n")
        return True
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    return True


# --------------------------------------------------------------------------
# Main
# --------------------------------------------------------------------------


def _default_sdk_root() -> Path:
    # codegen/ → core/ → workspace → sdk-skills/agentos
    here = Path(__file__).resolve().parent
    sdk = here.parent.parent / "sdk-skills" / "agentos"
    if not sdk.exists():
        raise SystemExit(
            f"expected skills SDK at {sdk} — clone sdk-skills/ next to core/"
        )
    return sdk.resolve()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--manifest",
        # platform/codegen/ → workspace → core/codegen/ops-manifest.json.
        # Still emitted by core's gen_manifest bin until Phase 3.
        default=str(
            Path(__file__).resolve().parent.parent.parent
            / "core" / "codegen" / "ops-manifest.json"
        ),
    )
    parser.add_argument(
        "--sdk",
        default=str(_default_sdk_root()),
        help="Path to sdk-skills/agentos (default: sibling repo)",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Exit 1 if on-disk stubs differ from what would be generated.",
    )
    parser.add_argument(
        "--smoke",
        action="store_true",
        help=(
            "Generate to a throwaway temp dir and verify the output is valid "
            "Python. Used by ./dev.sh build to catch codegen regressions "
            "without touching the SDK (which still dispatches via the "
            "pre-cutover wire names until Phase 5)."
        ),
    )
    parser.add_argument(
        "--modules",
        nargs="*",
        help="Only regenerate these modules (default: every PURE_GENERATED).",
    )
    args = parser.parse_args(argv)

    manifest = load_manifest(Path(args.manifest))
    grouped = group_by_module(manifest["ops"])

    if args.smoke:
        import py_compile
        import tempfile

        with tempfile.TemporaryDirectory(prefix="gen-sdk-smoke-") as tmp:
            tmp_root = Path(tmp)
            wanted_smoke = set(args.modules) if args.modules else PURE_GENERATED
            for module, ops in sorted(grouped.items()):
                if module not in wanted_smoke:
                    continue
                text = emit_module(module, ops)
                out_path = tmp_root / f"{module}.py"
                out_path.write_text(text)
                try:
                    py_compile.compile(str(out_path), doraise=True)
                except py_compile.PyCompileError as exc:
                    sys.stderr.write(
                        f"[gen_sdk_stubs] smoke: emitted {module}.py "
                        f"does not parse: {exc}\n"
                    )
                    return 1
        return 0

    sdk_root = Path(args.sdk)
    if not sdk_root.exists():
        print(
            f"[gen_sdk_stubs] SDK root not found: {sdk_root} "
            "(pass --sdk to override)",
            file=sys.stderr,
        )
        return 2

    wanted = set(args.modules) if args.modules else PURE_GENERATED
    drift_any = False

    for module, ops in sorted(grouped.items()):
        if module not in wanted:
            continue
        text = emit_module(module, ops)
        out_path = sdk_root / f"{module}.py"
        changed = write_file(out_path, text, check=args.check)
        drift_any = drift_any or changed
        if not args.check and changed:
            print(f"[gen_sdk_stubs] wrote {out_path}")

    if args.check and drift_any:
        print(
            "[gen_sdk_stubs] SDK stubs out of date. "
            "Run `./dev.sh build` (without --check).",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
