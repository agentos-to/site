---
title: calendar
description: "A calendar — container for events."
sidebar:
  label: calendar
---

A calendar — container for events.

Example sources: Google Calendar, Apple Calendar

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

## Skills that produce this shape

- [google-calendar](/docs/skills/reference/productivity/google-calendar/) — `list_calendars`
