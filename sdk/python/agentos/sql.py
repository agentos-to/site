# This file is AUTO-GENERATED. Do not edit.
# Regenerate with `./dev.sh build` or `python3 codegen/gen_sdk_stubs.py`.

"""SQLite query/execute through the engine.

Replaces direct sqlite3 usage. All queries are routed for logging, path validation, and future permission controls."""

from __future__ import annotations

from typing import Any

from agentos._bridge import dispatch


async def execute(sql: str, db: str) -> dict[str, Any]:
    """
    Run a writing SQL statement (INSERT/UPDATE/DELETE/DDL).

    Args:
        sql: SQL text to execute.
        db: Path to the SQLite file.

    Returns:
        {rows_affected, last_insert_rowid?}.
    """
    _req: dict[str, Any] = {}
    _req['sql'] = sql
    _req['db'] = db
    return await dispatch('sql.execute', _req)


async def query(sql: str, db: str, *, attach: dict[str, str] | None = None, params: dict[str, Any] | None = None) -> list[dict[str, Any]]:
    """
    Run a read-only SQL query against a named SQLite file.

    Args:
        sql: Parameterized SQL text. Use `:name` placeholders.
        db: Path to the SQLite file (`~` expands to $HOME).
        params: Named bind parameters (optional).
        attach: Alias → path map for ATTACH DATABASE (optional).

    Returns:
        List of row dicts keyed by column name.
    """
    _req: dict[str, Any] = {}
    _req['sql'] = sql
    _req['db'] = db
    if attach is not None:
        _req['attach'] = attach
    if params is not None:
        _req['params'] = params
    return await dispatch('sql.query', _req)
