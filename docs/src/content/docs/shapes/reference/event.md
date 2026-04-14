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
| `platform` | [`product`](/docs/shapes/reference/product/) |
| `involves` | [`person[]`](/docs/shapes/reference/person/) |
| `location` | [`place`](/docs/shapes/reference/place/) |
| `organizer` | [`person`](/docs/shapes/reference/person/) |
| `creator` | [`person`](/docs/shapes/reference/person/) |
| `attachments` | [`file[]`](/docs/shapes/reference/file/) |

## Used as a base by

- [`class`](/docs/shapes/reference/class/)
- [`meeting`](/docs/shapes/reference/meeting/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Event](https://schema.org/Event)** — Core event type. Our startDate/endDate map 1:1; eventType is free-form vs. schema.org's subtype hierarchy (Concert, Conference, BusinessEvent). organizer/location match directly.
- **[RFC 5545 (iCalendar) VEVENT](https://datatracker.ietf.org/doc/html/rfc5545)** — Our icalUid is their UID; recurrence is their RRULE; status maps to STATUS (TENTATIVE/CONFIRMED/CANCELLED); showAs ≈ TRANSP; involves[] ≈ ATTENDEE.
- **[ActivityStreams 2.0 Event](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-event)** — Fediverse inbox format. Thinner than iCal — no native recurrence or showAs; our involves[] ≈ attendees via as:Relationship.

## Skills that produce this shape

- [google-calendar](/docs/skills/reference/productivity/google-calendar/) — `list_events`, `search_events`
- [google-calendar](/docs/skills/reference/productivity/google-calendar/) — `get_event`, `create_event`, `update_event`
- [spacex](/docs/skills/reference/fun/spacex/) — `list_upcoming`, `list_past`
- [spacex](/docs/skills/reference/fun/spacex/) — `get_launch`
- [posthog](/docs/skills/reference/web/posthog/) — `list_events`
- [posthog](/docs/skills/reference/web/posthog/) — `get_event`
