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
| `taught_by` | [`person`](/shapes/reference/person/) |
| `held_at` | [`place`](/shapes/reference/place/) |

## Inherited

From [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `properties` | `json` |
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
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `concerns` | [`person`](/shapes/reference/person/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/EducationEvent](https://schema.org/EducationEvent)** — schema.org's closest peer for a bookable class. Our instructor = performer; capacity = maximumAttendeeCapacity; spotsRemaining ≈ remainingAttendeeCapacity.
- **[schema.org/ExerciseAction](https://schema.org/ExerciseAction)** — Fitness-specific vocabulary: activityType ≈ exerciseType; venue matches directly as location.
- **[Mindbody Public API (class schedules)](https://developers.mindbodyonline.com/PublicDocumentation/V6)** — Practical API mirror. Our capacity/spotsRemaining/isFull come from Mindbody's MaxCapacity/TotalBooked/IsWaitlistAvailable.

## Apps that produce this shape

- [austin-boulder-project](/apps/reference/fitness/austin-boulder-project/) — `get_schedule`
