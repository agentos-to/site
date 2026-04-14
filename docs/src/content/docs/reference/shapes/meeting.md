---
title: meeting
description: "A calendar meeting — an event with virtual meeting details and transcripts."
sidebar:
  label: meeting
---

A calendar meeting — an event with virtual meeting details and transcripts.
Querying by "event" returns meetings too.

Example sources: Google Calendar, Apple Calendar, Granola

| | |
|---|---|
| **Plural** | `meetings` |
| **Subtitle field** | `location` |
| **Also** | [`event`](/docs/reference/shapes/event/) |

## Fields

| Field | Type |
|---|---|
| `calendarLink` | `url` |
| `isVirtual` | `boolean` |
| `meetingUrl` | `url` |
| `conferenceProvider` | `string` |
| `phoneDialIn` | `string` |

## Relations

| Relation | Target |
|---|---|
| `transcribe` | [`transcript`](/docs/reference/shapes/transcript/) |

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

- [granola](/docs/reference/skills/granola/) — `op_list_meetings`
- [granola](/docs/reference/skills/granola/) — `op_get_meeting`
