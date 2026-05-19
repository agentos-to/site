"""Tiny skill-result builders — pure data, no I/O.

Used to shape tool return values:

    return skill_error("missing user_id", code="NOT_FOUND")
    return skill_result(authenticated=True, identifier="joe@x")
    return {"__secrets__": skill_secret("exa.ai", "joe@x", "cognito", {...})}

Lives here (not in ``client`` or ``decorators``) because none of these
touch the network or the graph — they're just dict constructors that
carry the engine's reserved keys (``__result__``, ``__secrets__``).
"""

from __future__ import annotations


def skill_error(message: str, **extra) -> dict:
    """Return a structured error dict from a skill operation.

    The engine unwraps ``__result__`` into the caller's response — extra
    fields ride alongside ``error`` as context (``code``, ``hint``, …)."""
    result = {"error": message}
    result.update(extra)
    return {"__result__": result}


def skill_result(**fields) -> dict:
    """Return a structured result dict from a skill operation.

    Same unwrap semantics as ``skill_error`` — use when the skill has a
    shape it wants to return and would otherwise conflict with sidecar
    keys like ``__secrets__`` / ``__cookie_delta__``."""
    return {"__result__": fields}


def skill_secret(
    domain: str,
    identifier: str,
    item_type: str,
    value: dict,
    *,
    source: str | None = None,
    label: str | None = None,
    metadata: dict | None = None,
) -> dict:
    """Build a ``__secrets__`` entry for credential storage.

    Callers wrap these in a ``__secrets__`` list or dict on the result
    envelope; the engine's ``process_storage_writeback`` consumes and
    upserts them into the credential store."""
    entry = {
        "domain": domain,
        "identifier": identifier,
        "item_type": item_type,
        "value": value,
    }
    if source:
        entry["source"] = source
    if label:
        entry["label"] = label
    if metadata:
        entry["metadata"] = metadata
    return entry
