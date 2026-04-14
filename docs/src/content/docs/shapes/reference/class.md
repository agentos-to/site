---
title: class
description: "A scheduled, bookable group activity — gym classes, workshops, courses."
sidebar:
  label: class
---

A scheduled, bookable group activity — gym classes, workshops, courses.
Has capacity (how many can attend) and optionally tracks spots remaining.

Not to be confused with a meeting (1:1 or small group, calendar-driven)
or a conference (large, multi-track). A class has an instructor, a fixed
capacity, and is typically part of a recurring schedule.

Example sources: Austin Boulder Project, Mindbody, future gym/studio integrations

| Metadata | Value |
|---|---|
| **Plural** | `classes` |
| **Subtitle field** | `activityType` |
| **Also** | [`event`](/docs/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `activityType` | `string` |
| `capacity` | `integer` |
| `spotsRemaining` | `integer` |
| `isFull` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `instructor` | [`person`](/docs/shapes/reference/person/) |
| `venue` | [`place`](/docs/shapes/reference/place/) |

## Inherited

From [`event`](/docs/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `dateUpdated` | `datetime` |
| `endDate` | `datetime` |
| `eventType` | `string` |
| `icalUid` | `string` |
| `recurrence` | `string[]` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |

| Relation | Target |
|---|---|
| `attachments` | [`file[]`](/docs/shapes/reference/file/) |
| `creator` | [`person`](/docs/shapes/reference/person/) |
| `involves` | [`person[]`](/docs/shapes/reference/person/) |
| `location` | [`place`](/docs/shapes/reference/place/) |
| `organizer` | [`person`](/docs/shapes/reference/person/) |
| `platform` | [`product`](/docs/shapes/reference/product/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/EducationEvent](https://schema.org/EducationEvent)** — schema.org's closest peer for a bookable class. Our instructor = performer; capacity = maximumAttendeeCapacity; spotsRemaining ≈ remainingAttendeeCapacity.
- **[schema.org/ExerciseAction](https://schema.org/ExerciseAction)** — Fitness-specific vocabulary: activityType ≈ exerciseType; venue matches directly as location.
- **[Mindbody Public API (class schedules)](https://developers.mindbodyonline.com/PublicDocumentation/V6)** — Practical API mirror. Our capacity/spotsRemaining/isFull come from Mindbody's MaxCapacity/TotalBooked/IsWaitlistAvailable.

## Skills that produce this shape

- [austin-boulder-project](/docs/skills/reference/fun/austin-boulder-project/) — `op_get_schedule`
