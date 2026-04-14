---
title: event
description: "Something that happens — at a time, optionally at a place, involving people."
sidebar:
  label: event
---

Something that happens — at a time, optionally at a place, involving people.

The universal base for anything with a when: meetings, classes, parties,
conferences, concerts, life events. Subtypes extend via `also: [event]`.

Standard fields (inherited): id, name, url, image, published, content
published is when the event was *posted/announced* — NOT when it happens.
Use startDate / endDate for the actual event timing.

Example sources: Google Calendar, Apple Calendar, Partiful, Luma, Austin Boulder Project

| Metadata | Value |
|---|---|
| **Plural** | `events` |
| **Subtitle field** | `eventType` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `eventType` | `string` |
| `startDate` | `datetime` |
| `endDate` | `datetime` |
| `timezone` | `string` |
| `allDay` | `boolean` |
| `recurrence` | `string[]` |
| `status` | `string` |
| `visibility` | `string` |
| `showAs` | `string` |
| `dateUpdated` | `datetime` |
| `sourceUrl` | `url` |
| `sourceTitle` | `string` |
| `icalUid` | `string` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/reference/shapes/product/) |
| `involves` | [`person[]`](/docs/reference/shapes/person/) |
| `location` | [`place`](/docs/reference/shapes/place/) |
| `organizer` | [`person`](/docs/reference/shapes/person/) |
| `creator` | [`person`](/docs/reference/shapes/person/) |
| `attachments` | [`file[]`](/docs/reference/shapes/file/) |

## Used as a base by

- [`class`](/docs/reference/shapes/class/)
- [`meeting`](/docs/reference/shapes/meeting/)

## Skills that produce this shape

- [google-calendar](/docs/reference/skills/productivity/google-calendar/) — `list_events`, `search_events`
- [google-calendar](/docs/reference/skills/productivity/google-calendar/) — `get_event`, `create_event`, `update_event`
- [spacex](/docs/reference/skills/fun/spacex/) — `list_upcoming`, `list_past`
- [spacex](/docs/reference/skills/fun/spacex/) — `get_launch`
- [posthog](/docs/reference/skills/web/posthog/) — `list_events`
- [posthog](/docs/reference/skills/web/posthog/) — `get_event`
