"""Python services emitter — the one `agentos/services.py` module.

Two halves, one file:

  1. Service-name constants (from `ontology/services/*.yaml`) — the
     vocabulary apps use in `@provides(...)` declarations. Constants
     instead of strings: IDE autocomplete, typo detection at import
     time, one definition everywhere.

  2. The broker stubs (`call`, `list_providers`) — projected from the
     `services` op group exactly like every other generated op stub.

This module REPLACES the old hand-written `agentos/tools.py` constants
and the generated `agentos/capability.py` stubs.
"""

from __future__ import annotations

import sys
import textwrap
from pathlib import Path

from ir import Ontology

sys.path.insert(0, str(Path(__file__).parent.parent))
import services as services_loader  # noqa: E402

from .ops_python import FILE_HEADER, _emit_op  # noqa: E402

_MODULE_DOC = '''"""The service vocabulary + the broker.

A service is a named interface the engine brokers between strangers:
the caller names the interface, never the app. Use the constants in
`@provides` declarations —

    from agentos import provides
    from agentos.services import web_search

    @provides(web_search)
    def search(query: str, **params) -> list[dict]:
        ...

— and `call(...)` / `list_providers(...)` to consume a service across
app boundaries without naming the provider.

Contracts live in `platform/ontology/services/*.yaml`; the engine mints
the graph-side service nodes and `provides` edges from those contracts
plus each app's own declarations.
"""'''


def emit_services_python(
    services: list[services_loader.Service], onto: Ontology
) -> str:
    body: list[str] = [
        FILE_HEADER,
        _MODULE_DOC,
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any",
        "",
        "from agentos._bridge import dispatch",
        "",
        "# --- Service names ----------------------------------------------------",
        "# One constant per `ontology/services/*.yaml` entry, alphabetical.",
        "",
    ]
    for s in services:
        doc = s.leading_comment.splitlines()[0] if s.leading_comment else s.description
        for line in textwrap.wrap(doc, width=70):
            body.append(f"# {line}")
        body.append(f'{s.name} = "{s.name}"')
        body.append("")

    body += [
        "",
        "# --- The broker --------------------------------------------------------",
        "",
        "",
    ]
    broker_ops = sorted(
        (op for op in onto.ops if op.group == "services"), key=lambda o: o.name
    )
    for op in broker_ops:
        body.append(_emit_op(op))
        body.append("")
    return "\n".join(body).rstrip() + "\n"
