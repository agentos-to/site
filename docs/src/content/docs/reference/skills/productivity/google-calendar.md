---
title: Google Calendar
description: "Read, create, update, and delete Google Calendar events — replaces apple-calendar with Google API + OAuth"
sidebar:
  label: google-calendar
---

| Metadata | Value |
|---|---|
| **Category** | `productivity` |
| **Capabilities** | `http` |
| **Website** | <https://calendar.google.com> |

## Returns shapes

- [`calendar[]`](/docs/reference/shapes/calendar/) — from `list_calendars`
- [`event`](/docs/reference/shapes/event/) — from `get_event`, `create_event`, `update_event`
- [`event[]`](/docs/reference/shapes/event/) — from `list_events`, `search_events`

## Connections

- **`api`**
