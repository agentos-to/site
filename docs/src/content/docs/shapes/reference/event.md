---
title: event
description: "Something that happens — at a time, optionally at a place, involving people."
sidebar:
  label: event
---

Something that happens — at a time, optionally at a place, involving people.

The universal base for anything with a when: meetings, classes, parties,
conferences, concerts, life events. Subtypes extend via `also: [event]`
— each subtype is its own shape file carrying its own typed fields.
This base shape stays universal: when / where / who, nothing per-subtype.

Standard fields (inherited): id, name, url, image, published, content
published is when the event was *posted/announced* — NOT when it happens.
Use startDate / endDate for the actual event timing.

Per-subtype fields live on subtype shapes:
- birth.yaml      → name + gender particulars at birth
- transition.yaml → name/gender/etc. changes over a person's lifetime
- launch.yaml     → rocket-launch fields (SpaceX)
- meeting.yaml    → calendar-meeting fields
- ...

| Metadata | Value |
|---|---|
| **Plural** | `events` |
| **Subtitle field** | `startDate` |
| **Identity** | `at`, `id` |

## Fields

| Field | Type |
|---|---|
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
| `distinctId` | `string` |
| `currentUrl` | `string` |
| `properties` | `json` |

## Used as a base by

- [`activity`](/shapes/reference/activity/)
- [`birth`](/shapes/reference/birth/)
- [`booking_offer`](/shapes/reference/booking_offer/)
- [`class`](/shapes/reference/class/)
- [`conversion`](/shapes/reference/conversion/)
- [`git_commit`](/shapes/reference/git_commit/)
- [`health-condition`](/shapes/reference/health-condition/)
- [`health-immunization`](/shapes/reference/health-immunization/)
- [`health-observation`](/shapes/reference/health-observation/)
- [`health-panel`](/shapes/reference/health-panel/)
- [`health-procedure`](/shapes/reference/health-procedure/)
- [`health-reference-range`](/shapes/reference/health-reference-range/)
- [`invitation`](/shapes/reference/invitation/)
- [`launch`](/shapes/reference/launch/)
- [`leg`](/shapes/reference/leg/)
- [`loaded_model`](/shapes/reference/loaded_model/)
- [`meeting`](/shapes/reference/meeting/)
- [`membership`](/shapes/reference/membership/)
- [`offer`](/shapes/reference/offer/)
- [`order`](/shapes/reference/order/)
- [`pass`](/shapes/reference/pass/)
- [`reservation`](/shapes/reference/reservation/)
- [`role`](/shapes/reference/role/)
- [`task`](/shapes/reference/task/)
- [`transaction`](/shapes/reference/transaction/)
- [`transition`](/shapes/reference/transition/)
- [`trip`](/shapes/reference/trip/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Event](https://schema.org/Event)** — Core event type. Our startDate/endDate map 1:1; eventType is free-form vs. schema.org's subtype hierarchy (Concert, Conference, BusinessEvent). organizer/location match directly.
- **[RFC 5545 (iCalendar) VEVENT](https://datatracker.ietf.org/doc/html/rfc5545)** — Our icalUid is their UID; recurrence is their RRULE; status maps to STATUS (TENTATIVE/CONFIRMED/CANCELLED); showAs ≈ TRANSP; involves[] ≈ ATTENDEE.
- **[ActivityStreams 2.0 Event](https://www.w3.org/TR/activitystreams-vocabulary/#dfn-event)** — Fediverse inbox format. Thinner than iCal — no native recurrence or showAs; our involves[] ≈ attendees via as:Relationship.

## Skills that produce this shape

- [google-calendar](/skills/reference/productivity/google-calendar/) — `list_events`, `search_events`, `get_event`, `create_event`, `update_event`
- [posthog](/skills/reference/web/posthog/) — `list_events`, `get_event`
