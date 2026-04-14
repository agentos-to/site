---
title: meeting
description: "A calendar meeting — an event with virtual meeting details and transcripts."
sidebar:
  label: meeting
---

A calendar meeting — an event with virtual meeting details and transcripts.
Querying by "event" returns meetings too.

Example sources: Google Calendar, Apple Calendar, Granola

| Metadata | Value |
|---|---|
| **Plural** | `meetings` |
| **Subtitle field** | `location` |
| **Also** | [`event`](/docs/shapes/reference/event/) |

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
| `transcribe` | [`transcript`](/docs/shapes/reference/transcript/) |

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

- **[RFC 5545 VEVENT + conference property (RFC 7986)](https://datatracker.ietf.org/doc/html/rfc7986#section-5.11)** — Our meetingUrl ≈ CONFERENCE URI; phoneDialIn = tel: URI in CONFERENCE feature=PHONE; conferenceProvider ≈ CONFERENCE LABEL.
- **[schema.org/Event — location.VirtualLocation](https://schema.org/VirtualLocation)** — Our isVirtual triggers VirtualLocation; meetingUrl ≈ VirtualLocation.url.
- **[Google Calendar Event conferenceData](https://developers.google.com/calendar/api/v3/reference/events)** — Practical API mirror. Our conferenceProvider ≈ conferenceData.conferenceSolution.name; meetingUrl = entryPoints[uri].

## Skills that produce this shape

- [granola](/docs/skills/reference/productivity/granola/) — `op_list_meetings`
- [granola](/docs/skills/reference/productivity/granola/) — `op_get_meeting`
