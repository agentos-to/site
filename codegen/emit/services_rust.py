"""Rust services emitter — service registry YAML → compiled ServiceDef table.

Reads the `list[Service]` produced by `services.py` and projects the
engine's compiled registry: one `ServiceDef` row per canonical service.
The engine mints `shape:service` graph nodes from this table at boot
(content comes from here, existence is derived — never authored), and
validates each app's `provides` declarations against the known ids.

Params are carried as a JSON string (schema-ish map projected straight
from the YAML) — the engine stamps it onto the minted node's `params`
val; it does not interpret it.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import services as services_loader  # noqa: E402


def _rust_str(s: str) -> str:
    # ensure_ascii=False: Rust string literals take raw UTF-8, not \uXXXX
    return json.dumps(s, ensure_ascii=False)


def emit_services_rust(services: list[services_loader.Service]) -> str:
    lines: list[str] = [
        "// DO NOT EDIT — generated from platform/ontology/services/*.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "//",
        "// The canonical service registry — the interfaces the engine",
        "// brokers between apps. The engine mints `shape:service` graph",
        "// nodes from this table at boot and links providing apps to them",
        "// with `provides` edges derived from each app's declarations.",
        "",
        "#![allow(clippy::all)]",
        "",
        "/// One canonical service — id, contract, docs.",
        "pub struct ServiceDef {",
        "    /// The verb a caller asks for: `web_search`, `llm`, …",
        "    pub id: &'static str,",
        "    /// What the interface does — stamped onto the minted node.",
        "    pub description: &'static str,",
        "    /// Caller params as a JSON map (`{}` when unspecified).",
        "    pub params: &'static str,",
        "    /// Shape (or auth-contract) a provider's bound tool must",
        "    /// produce; `None` while the contract is loose.",
        "    pub returns: Option<&'static str>,",
        "}",
        "",
        "/// Alphabetical by id.",
        "pub static SERVICES: &[ServiceDef] = &[",
    ]
    for s in sorted(services, key=lambda x: x.name):
        params_json = json.dumps(s.params, sort_keys=True, ensure_ascii=False)
        returns = f"Some({_rust_str(s.returns)})" if s.returns else "None"
        lines += [
            "    ServiceDef {",
            f"        id: {_rust_str(s.name)},",
            f"        description: {_rust_str(s.description)},",
            f"        params: {_rust_str(params_json)},",
            f"        returns: {returns},",
            "    },",
        ]
    lines += [
        "];",
        "",
        "/// Registry lookup by id.",
        "pub fn service_def(id: &str) -> Option<&'static ServiceDef> {",
        "    SERVICES.iter().find(|s| s.id == id)",
        "}",
        "",
    ]
    return "\n".join(lines)
