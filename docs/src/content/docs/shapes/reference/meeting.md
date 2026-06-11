---
title: meeting
description: "A calendar meeting — an event with virtual meeting details and transcripts."
sidebar:
  label: meeting
---

A calendar meeting — an event with virtual meeting details and transcripts.
Querying by "event" returns meetings too.

| Metadata | Value |
|---|---|
| **Plural** | `meetings` |
| **Subtitle field** | `location` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `calendarLink` | `url` |
| `isVirtual` | `boolean` |
| `meetingUrl` | `url` |
| `conferenceProvider` | `string` |
| `phoneDialIn` | `string` |
| `meetingType` | `string` |

## Relations

| Relation | Target |
|---|---|
| `transcribed_by` | [`transcript`](/shapes/reference/transcript/) |

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
| `held_at` | [`place`](/shapes/reference/place/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[RFC 5545 VEVENT + conference property (RFC 7986)](https://datatracker.ietf.org/doc/html/rfc7986#section-5.11)** — Our meetingUrl ≈ CONFERENCE URI; phoneDialIn = tel: URI in CONFERENCE feature=PHONE; conferenceProvider ≈ CONFERENCE LABEL.
- **[schema.org/Event — location.VirtualLocation](https://schema.org/VirtualLocation)** — Our isVirtual triggers VirtualLocation; meetingUrl ≈ VirtualLocation.url.
- **[Google Calendar Event conferenceData](https://developers.google.com/calendar/api/v3/reference/events)** — Practical API mirror. Our conferenceProvider ≈ conferenceData.conferenceSolution.name; meetingUrl = entryPoints[uri].

## Skills that produce this shape

- [granola](/skills/reference/productivity/granola/) — `list_meetings`, `get_meeting`
