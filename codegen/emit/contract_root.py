"""Crate-root emitter — the `agentos-contract-generated` `lib.rs`.

The generated contract crate has one module per ontology branch with a Rust
face. Their bodies are emitted into sibling files (`shapes.rs`, `ops.rs`);
this projects only the crate root that ties them together — module
declarations plus a crate-wide lint allowance. Trivial, but generated like
everything else, so the drift gate covers the crate root too.
"""

from __future__ import annotations

# Ontology branches with a Rust module in the contract crate. `auth-contracts`
# is intentionally absent — those contracts have a single consumer and stay
# in the `auth` crate (see phase5-contract-crate.md).
_MODULES = ("ops", "schema_hash", "shapes")


def emit_contract_root() -> str:
    """Render `core/crates/contract-generated/src/lib.rs`."""
    lines = [
        "// DO NOT EDIT — generated from platform/ontology/ by platform/codegen/.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "//",
        "// The crate root of the generated contract: one module per ontology",
        "// branch with a Rust face. Module bodies live in the sibling files.",
        "",
        "#![allow(clippy::all)]",
        "",
        *(f"pub mod {m};" for m in _MODULES),
        "",
    ]
    return "\n".join(lines)
