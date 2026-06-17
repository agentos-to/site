"""Emitters — dumb projections off the ontology IR.

Each module here takes the `Ontology` tree (built by `ir.py`) and
renders one target. Adding a language is one new file: write
`emit_<lang>(onto) -> str`, re-export it here, wire it in `generate.py`.
"""

from .auth import emit_python_auth_contracts, emit_rust_auth_contracts
from .contract_root import emit_contract_root
from .ops_python import emit_ops_python
from .ops_rust import emit_ops_rust
from .python import emit_python
from .rust_sdk import write_rust_sdk
from .symbols import emit_yaml_symbols
from .typescript import emit_typescript

__all__ = [
    "emit_python",
    "emit_typescript",
    "write_rust_sdk",
    "emit_python_auth_contracts",
    "emit_rust_auth_contracts",
    "emit_ops_rust",
    "emit_ops_python",
    "emit_contract_root",
    "emit_yaml_symbols",
]
