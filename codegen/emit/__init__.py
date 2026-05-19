"""Emitters — dumb projections off the ontology IR.

Each module here takes the `Ontology` tree (built by `ir.py`) and
renders one target. Adding a language is one new file: write
`emit_<lang>(onto) -> str`, re-export it here, wire it in `generate.py`.
"""

from .auth import emit_python_auth_contracts, emit_rust_auth_contracts
from .docs import build_skills_index, discover_skills, emit_shape_docs, emit_skill_docs
from .python import emit_python
from .rust import emit_rust
from .typescript import emit_typescript

__all__ = [
    "emit_python",
    "emit_typescript",
    "emit_rust",
    "emit_python_auth_contracts",
    "emit_rust_auth_contracts",
    "emit_shape_docs",
    "emit_skill_docs",
    "discover_skills",
    "build_skills_index",
]
