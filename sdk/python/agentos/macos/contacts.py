"""Resolve macOS handles (phone / email) to contact names from AddressBook.

Local Apple databases (Messages `chat.db`, `CallHistory.storedata`, …) only store
raw handles — a phone number or an email. The human-readable name lives in
Contacts. This module globs every AddressBook source DB (local, iCloud, Exchange,
…), building a `{match-key -> display name}` map so a handle resolves regardless
of how it was formatted.

    from agentos.macos import contacts

    names = await contacts.load()
    name  = contacts.resolve("+1 (555) 123-4567", names)   # → "Jane Doe" | None

Apps importing this must declare `platform: macos` in their `readme.md`.
"""

from __future__ import annotations

import glob
import os
import re

from agentos import sql


_AB_GLOB = "~/Library/Application Support/AddressBook/**/*.abcddb"

# Phone + email rows from one AddressBook source DB. Each tuple is (sql, is_phone).
_QUERIES = (
    ("SELECT r.ZFIRSTNAME f, r.ZLASTNAME l, r.ZORGANIZATION o, p.ZFULLNUMBER v "
     "FROM ZABCDPHONENUMBER p JOIN ZABCDRECORD r ON p.ZOWNER=r.Z_PK "
     "WHERE p.ZFULLNUMBER IS NOT NULL", True),
    ("SELECT r.ZFIRSTNAME f, r.ZLASTNAME l, r.ZORGANIZATION o, e.ZADDRESS v "
     "FROM ZABCDEMAILADDRESS e JOIN ZABCDRECORD r ON e.ZOWNER=r.Z_PK "
     "WHERE e.ZADDRESS IS NOT NULL", False),
)


def phone_key(s: str | None) -> str:
    """Reduce a phone string to its last 10 digits — a format-insensitive match key."""
    d = re.sub(r"\D", "", s or "")
    return d[-10:] if len(d) >= 10 else d


def handle_key(handle: str | None) -> str | None:
    """Normalize a handle to its AddressBook match key: email lowercased, phone → last-10."""
    if not handle:
        return None
    return handle.strip().lower() if "@" in handle else phone_key(handle)


async def load() -> dict[str, str]:
    """Build a `{match-key -> display name}` map from every macOS AddressBook source.

    Phones are keyed by their last 10 digits and emails by lowercased address, so
    a stored handle matches whatever formatting the source app used. First name
    wins on collision (`setdefault`).
    """
    names: dict[str, str] = {}
    for path in glob.glob(os.path.expanduser(_AB_GLOB), recursive=True):
        for query, is_phone in _QUERIES:
            try:
                rows = await sql.query(query, db=path, params={})
            except Exception:
                continue
            for r in rows:
                name = (" ".join(x for x in (r.get("f"), r.get("l")) if x).strip()
                        or (r.get("o") or "").strip())
                if not name:
                    continue
                key = phone_key(r.get("v")) if is_phone else (r.get("v") or "").strip().lower()
                if key:
                    names.setdefault(key, name)
    return names


def resolve(handle: str | None, names: dict[str, str]) -> str | None:
    """Resolve a handle (phone / email) to a contact display name, if known."""
    key = handle_key(handle)
    return names.get(key) if key else None
