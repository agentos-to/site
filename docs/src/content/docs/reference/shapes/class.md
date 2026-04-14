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

| | |
|---|---|
| **Plural** | `classes` |
| **Subtitle field** | `activityType` |
| **Also** | [`event`](/docs/reference/shapes/event/) |

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
| `instructor` | [`person`](/docs/reference/shapes/person/) |
| `venue` | [`place`](/docs/reference/shapes/place/) |

## Inherited

From [`event`](/docs/reference/shapes/event/):

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
| `attachments` | [`file[]`](/docs/reference/shapes/file/) |
| `creator` | [`person`](/docs/reference/shapes/person/) |
| `involves` | [`person[]`](/docs/reference/shapes/person/) |
| `location` | [`place`](/docs/reference/shapes/place/) |
| `organizer` | [`person`](/docs/reference/shapes/person/) |
| `platform` | [`product`](/docs/reference/shapes/product/) |

## Skills that produce this shape

- [austin-boulder-project](/docs/reference/skills/austin-boulder-project/) — `op_get_schedule`
