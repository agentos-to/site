"""Date parsing utilities for apps.

Converts display dates, fuzzy dates, and timestamps to ISO 8601.

**Instant contract (graph + UI):**
  - ``datetime`` fields are always absolute — UTC with an explicit ``Z``
    (or a numeric offset that ``canonicalize_datetime`` folds to ``Z``).
  - Offset-less / space-separated strings fed to ``canonicalize_datetime``
    are treated as **UTC wall clock** (Gmail, SQLite ``unixepoch``).
  - Provider APIs that speak **venue-local** naive ISO must go through
    ``wall_to_utc(local, iana_tz)`` before return. Never emit naive
    ``startDate`` + ``timezone`` and hope the consumer reinterprets —
    ``timezone`` is display/recurrence only.

**Write-back:** ``utc_to_wall(utc, iana_tz)`` for APIs that want local naive
(e.g. Skedda bookings).
"""

from __future__ import annotations

import re
from datetime import datetime, timezone
from typing import Any
from zoneinfo import ZoneInfo

_MONTHS = {
    "january": "01", "february": "02", "march": "03", "april": "04",
    "may": "05", "june": "06", "july": "07", "august": "08",
    "september": "09", "october": "10", "november": "11", "december": "12",
}

_AWARE_TAIL = re.compile(r"(?:Z|[+-]\d{2}:?\d{2})$")


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

    For venue-local naive strings from a booking provider, use
    ``wall_to_utc`` instead — this helper will mis-stamp them as UTC.
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


def _normalize_iso_sep(raw: str) -> str:
    s = raw.strip()
    if len(s) > 10 and s[10] == " ":
        s = s[:10] + "T" + s[11:]
    return s


def wall_to_utc(value: str | None, tz_name: str | None) -> str | None:
    """Venue-local (or already-aware) ISO → UTC instant with ``Z``.

    Use this when a provider returns offset-less wall clocks in a known
    IANA zone (Skedda ``start``, store hours, …). Aware inputs (``Z`` /
    numeric offset) are folded to UTC; ``tz_name`` is ignored for those.

    Naive + missing ``tz_name`` falls through to ``canonicalize_datetime``
    (UTC wall) — prefer always passing the venue zone.
    """
    if not value:
        return None
    raw = _normalize_iso_sep(str(value))
    if not raw:
        return None

    if raw.endswith("Z") or _AWARE_TAIL.search(raw):
        return canonicalize_datetime(raw)

    if not tz_name:
        return canonicalize_datetime(raw)

    naive = raw[:19]
    if len(naive) == 16:  # YYYY-MM-DDTHH:MM
        naive += ":00"
    try:
        dt = datetime.fromisoformat(naive)
    except ValueError:
        return canonicalize_datetime(raw)

    try:
        aware = dt.replace(tzinfo=ZoneInfo(tz_name))
    except Exception:
        aware = dt.replace(tzinfo=timezone.utc)
    return aware.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def utc_to_wall(value: str | None, tz_name: str | None) -> str | None:
    """UTC/aware ISO → venue-local naive ``YYYY-MM-DDTHH:MM:SS`` for provider writes.

    Naive inputs are returned trimmed (already wall). Missing ``tz_name`` with
    an aware instant yields UTC wall clock digits (no conversion).
    """
    if not value:
        return None
    raw = _normalize_iso_sep(str(value))
    if not raw:
        return None

    if raw.endswith("Z") or _AWARE_TAIL.search(raw):
        try:
            dt = datetime.fromisoformat(raw.replace("Z", "+00:00"))
        except ValueError as e:
            raise ValueError(f"invalid datetime: {value!r}") from e
        if tz_name:
            try:
                return dt.astimezone(ZoneInfo(tz_name)).strftime("%Y-%m-%dT%H:%M:%S")
            except Exception:
                pass
        return dt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S")

    # Already naive — assume venue-local.
    if len(raw) == 16:
        raw = raw + ":00"
    return raw[:19]


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
