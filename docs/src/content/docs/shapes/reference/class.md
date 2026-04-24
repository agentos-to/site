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

| Metadata | Value |
|---|---|
| **Plural** | `classes` |
| **Subtitle field** | `activityType` |
| **Also** | [`event`](/shapes/reference/event/) |

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
| `instructor` | [`person`](/shapes/reference/person/) |
| `venue` | [`place`](/shapes/reference/place/) |

## Inherited

From [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `articleUrl` | `url` |
| `crewIds` | `string[]` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `eventType` | `string` |
| `flightNumber` | `integer` |
| `icalUid` | `string` |
| `landingOutcomes` | `json` |
| `launchpadId` | `string` |
| `patchImage` | `url` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `reusedBoosters` | `string[]` |
| `rocketId` | `string` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |
| `webcastUrl` | `url` |
| `wikipediaUrl` | `url` |

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `attachments` | [`file[]`](/shapes/reference/file/) |
| `creator` | [`person`](/shapes/reference/person/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `location` | [`place`](/shapes/reference/place/) |
| `organizer` | [`person`](/shapes/reference/person/) |
| `person` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/EducationEvent](https://schema.org/EducationEvent)** — schema.org's closest peer for a bookable class. Our instructor = performer; capacity = maximumAttendeeCapacity; spotsRemaining ≈ remainingAttendeeCapacity.
- **[schema.org/ExerciseAction](https://schema.org/ExerciseAction)** — Fitness-specific vocabulary: activityType ≈ exerciseType; venue matches directly as location.
- **[Mindbody Public API (class schedules)](https://developers.mindbodyonline.com/PublicDocumentation/V6)** — Practical API mirror. Our capacity/spotsRemaining/isFull come from Mindbody's MaxCapacity/TotalBooked/IsWaitlistAvailable.

## Skills that produce this shape

- [austin-boulder-project](/skills/reference/fitness/austin-boulder-project/) — `get_schedule`
