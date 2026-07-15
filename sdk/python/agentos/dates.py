"""Date parsing utilities for apps.

Converts display dates, fuzzy dates, and timestamps to ISO 8601.
Instants are always UTC with an explicit ``Z`` — naive / space-separated
forms from Gmail and SQLite ``unixepoch`` are treated as UTC wall clock.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any

_MONTHS = {
    "january": "01", "february": "02", "march": "03", "april": "04",
    "may": "05", "june": "06", "july": "07", "august": "08",
    "september": "09", "october": "10", "november": "11", "december": "12",
}


def parse_date(s: str | None) -> str | None:
    """Convert a display date to ISO 8601 partial date.

    'August 2010'       → '2010-08'
    'December 13, 2024' → '2024-12-13'
    'in January 2026'   → '2026-01'
    '2024'              → '2024'
    '2024-03-15'        → '2024-03-15'  (passthrough)
    'this month'        → None
    '3 days ago'        → None
    """
    if not s:
        return None
    s = s.strip()
    # Strip leading "in " (e.g. "in January 2026")
    s = re.sub(r"^in\s+", "", s, flags=re.I)

    # Already ISO? (starts with 4 digits)
    if re.match(r"^\d{4}(-\d{2})?(-\d{2})?(T|$)", s):
        return s

    # "Month YYYY"
    m = re.match(r"^([A-Za-z]+)\s+(\d{4})$", s)
    if m:
        month = _MONTHS.get(m.group(1).lower())
        if month:
            return f"{m.group(2)}-{month}"

    # "Month DD, YYYY" or "Month DD YYYY"
    m = re.match(r"^([A-Za-z]+)\s+(\d{1,2}),?\s+(\d{4})$", s)
    if m:
        month = _MONTHS.get(m.group(1).lower())
        if month:
            return f"{m.group(3)}-{month}-{int(m.group(2)):02d}"

    # Year only
    m = re.match(r"^(\d{4})$", s)
    if m:
        return m.group(1)

    return None


def canonicalize_datetime(s: str | None) -> str | None:
    """Normalize an instant to UTC RFC 3339 with ``Z``.

    Offset-less / space-separated strings are UTC wall clock (Gmail,
    SQLite ``datetime(..., 'unixepoch')``). Date-only stays date-only.
    """
    if not s:
        return None
    raw = s.strip()
    if not raw:
        return None

    # Date-only civil date.
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", raw):
        return raw

    # Space → T.
    if len(raw) > 10 and raw[10] == " ":
        raw = raw[:10] + "T" + raw[11:]

    # Already offset-aware.
    if raw.endswith("Z") or re.search(r"[+-]\d{2}:?\d{2}$", raw):
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
            return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        except ValueError:
            return s.strip()

    # Naive datetime → UTC.
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"):
        try:
            dt = datetime.strptime(raw, fmt).replace(tzinfo=timezone.utc)
            return dt.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
        except ValueError:
            continue

    return s.strip()


def iso_from_ms(value: Any) -> str | None:
    """Convert a millisecond Unix timestamp to UTC ISO 8601 with ``Z``."""
    if not isinstance(value, (int, float)):
        return None
    try:
        return (
            datetime.fromtimestamp(value / 1000, tz=timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
            + "Z"
        )
    except (ValueError, OSError):
        return None


def iso_from_seconds(value: Any) -> str | None:
    """Convert a second Unix timestamp to UTC ISO 8601 with ``Z``."""
    if not isinstance(value, (int, float)):
        return None
    try:
        return (
            datetime.fromtimestamp(value, tz=timezone.utc)
            .strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3]
            + "Z"
        )
    except (ValueError, OSError):
        return None
