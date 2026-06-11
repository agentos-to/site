"""Loader + validator for `platform/ontology/services/*.yaml`.

One file per service; the file stem is the service id (the verb a
caller asks for: `web_search`, `web_read`, `llm`, …). Each file:

    # <leading comment — surfaced in generated docs/constants>
    description: >-   (required) what the interface does
    params:           (optional) ops-style request map — name: {type, doc}
    returns: <name>   (optional) shape or auth-contract the provider's
                      bound tool must produce — the typed contract

This registry is the CONTRACT side of services. The graph side —
service nodes, `provides` edges from apps, the user's `defaults_to`
pick — is minted by the engine from this registry plus each app's own
declarations; nothing on the graph is authored by hand.
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

_ID_RE = re.compile(r"^[a-z][a-z0-9_]*$")


@dataclass
class Service:
    """One service declaration — the flattened form every emitter consumes."""
    name: str                              # the verb / id (file stem)
    description: str
    params: dict[str, Any] = field(default_factory=dict)   # name -> {type, doc, ...}
    returns: str | None = None             # shape or auth-contract name
    leading_comment: str = ""              # first comment block of the file


def _leading_comment(path: Path) -> str:
    lines = []
    for raw in path.read_text().splitlines():
        if raw.startswith("#"):
            lines.append(raw.lstrip("#").strip())
        else:
            break
    return "\n".join(lines).strip()


def load(services_dir: Path) -> list[Service]:
    """Load every `services/*.yaml` → sorted list of Service records.
    Skips `_`/`.`-prefixed files."""
    out: list[Service] = []
    for f in sorted(services_dir.glob("*.yaml")):
        if f.name.startswith(("_", ".")):
            continue
        try:
            data = yaml.safe_load(f.read_text())
        except yaml.YAMLError as e:
            raise ValueError(f"{f.name}: parse error: {e}")
        if not isinstance(data, dict):
            raise ValueError(f"{f.name}: expected a mapping at top level")
        out.append(Service(
            name=f.stem,
            description=str(data.get("description") or "").strip(),
            params=dict(data.get("params") or {}),
            returns=(str(data["returns"]).strip() if data.get("returns") else None),
            leading_comment=_leading_comment(f),
        ))
    return sorted(out, key=lambda s: s.name)


def validate(
    services: list[Service],
    shape_names: set[str],
    auth_contract_names: set[str],
) -> tuple[list[str], list[str]]:
    """Returns (errors, warnings). Errors fail codegen."""
    errors: list[str] = []
    warnings: list[str] = []
    returnable = shape_names | auth_contract_names
    for s in services:
        if not _ID_RE.match(s.name):
            errors.append(f"service `{s.name}`: id must be lower_snake_case")
        if not s.description:
            errors.append(f"service `{s.name}`: missing description")
        if s.returns and s.returns not in returnable:
            errors.append(
                f"service `{s.name}`: returns `{s.returns}` is neither a "
                f"shape nor an auth contract"
            )
        for pname, spec in s.params.items():
            if not isinstance(spec, dict) or "type" not in spec:
                errors.append(
                    f"service `{s.name}`: param `{pname}` needs a "
                    f"{{type, doc}} mapping"
                )
    return errors, warnings
