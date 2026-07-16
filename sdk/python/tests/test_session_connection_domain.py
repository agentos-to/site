"""SDK guard: no-auth @account.check connections require explicit domain=."""

from __future__ import annotations

import textwrap
from pathlib import Path

from agentos.validate import check_session_connection_domain


def _write_app(tmp: Path, body: str) -> Path:
    app = tmp / "demo"
    app.mkdir()
    (app / "readme.md").write_text("---\nid: demo\nname: Demo\n---\n", encoding="utf-8")
    (app / "demo.py").write_text(textwrap.dedent(body), encoding="utf-8")
    return app


def test_requires_domain_on_none_connection(tmp_path: Path) -> None:
    app = _write_app(
        tmp_path,
        """
        from agentos import account, connection, returns

        connection("none", base_url="https://mail.google.com/")

        @account.check
        @returns("account")
        @connection("none")
        async def check_session(**params):
            return {"authenticated": False}
        """,
    )
    issues = check_session_connection_domain(app)
    assert any("omits domain=" in i for i in issues), issues


def test_domain_ok(tmp_path: Path) -> None:
    app = _write_app(
        tmp_path,
        """
        from agentos import account, connection, returns

        connection("none", domain="google.com")

        @account.check
        @returns("account")
        @connection("none")
        async def check_session(**params):
            return {"authenticated": False}
        """,
    )
    assert check_session_connection_domain(app) == []


def test_undeclared_none_flagged(tmp_path: Path) -> None:
    app = _write_app(
        tmp_path,
        """
        from agentos import account, connection, returns

        @account.check
        @returns("account")
        @connection("none")
        async def check_session(**params):
            return {"authenticated": False}
        """,
    )
    issues = check_session_connection_domain(app)
    assert any('connection("none", domain=' in i for i in issues), issues
