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

- [`calendar[]`](/shapes/reference/calendar/) — from `list_calendars`
- [`event`](/shapes/reference/event/) — from `get_event`, `create_event`, `update_event`
- [`event[]`](/shapes/reference/event/) — from `list_events`, `search_events`

## Connections

- **`api`**
