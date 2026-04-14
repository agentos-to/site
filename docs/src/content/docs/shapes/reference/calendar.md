---
title: calendar
description: "A calendar — container for events."
sidebar:
  label: calendar
---

A calendar — container for events.

| Metadata | Value |
|---|---|
| **Plural** | `calendars` |
| **Subtitle field** | `source` |
| **Identity** | `platform`, `calendarId` |

## Fields

| Field | Type |
|---|---|
| `calendarId` | `string` |
| `color` | `string` |
| `backgroundColor` | `string` |
| `foregroundColor` | `string` |
| `isPrimary` | `boolean` |
| `isReadonly` | `boolean` |
| `accessRole` | `string` |
| `source` | `string` |
| `timezone` | `string` |

## Relations

| Relation | Target |
|---|---|
| `owner` | [`person`](/docs/shapes/reference/person/) |
| `events` | [`event[]`](/docs/shapes/reference/event/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[RFC 5545 VCALENDAR](https://datatracker.ietf.org/doc/html/rfc5545)** — Our calendarId ≈ VCALENDAR's X-WR-CALID; timezone = X-WR-TIMEZONE; events relation mirrors VCALENDAR's VEVENT components.
- **[CalDAV (RFC 4791)](https://datatracker.ietf.org/doc/html/rfc4791)** — CalDAV calendar collections define accessRole semantics (owner/writer/reader) that match our field directly.
- **[Google Calendar API CalendarList](https://developers.google.com/calendar/api/v3/reference/calendarList)** — Practical API mirror. Our color/backgroundColor/foregroundColor, isPrimary, accessRole come from Google's CalendarList resource.

## Skills that produce this shape

- [google-calendar](/docs/skills/reference/productivity/google-calendar/) — `list_calendars`
