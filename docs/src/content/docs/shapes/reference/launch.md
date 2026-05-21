---
title: launch
description: "A rocket launch event. Carries flight-specific fields that previously"
sidebar:
  label: launch
---

A rocket launch event. Carries flight-specific fields that previously
lived on `event.yaml` as per-eventType denormalization — moved here
now that event subtypes are first-class shapes via `also: [event]`.

This is the per-subtype pattern: any event type that needs typed
fields gets its own shape file. The base `event` shape stays the
universal when/where/who core; subtype shapes carry their own
vocabulary.

| Metadata | Value |
|---|---|
| **Plural** | `launches` |
| **Subtitle field** | `rocketId` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `flightNumber` | `integer` |
| `rocketId` | `string` |
| `launchpadId` | `string` |
| `crewIds` | `string[]` |
| `reusedBoosters` | `string[]` |
| `landingOutcomes` | `json` |
| `articleUrl` | `url` |
| `webcastUrl` | `url` |
| `wikipediaUrl` | `url` |
| `patchImage` | `url` |

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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[SpaceX r/SpaceX API v4](https://github.com/r-spacex/SpaceX-API)** — Original source of these fields. The fly-by-night-launch.com skill maps the v4 launches endpoint onto this shape; the per-booster landing outcomes JSON mirrors that API's `cores` sub-document.

## Skills that produce this shape

- [spacex](/skills/reference/logistics/spacex/) — `list_upcoming`, `list_past`, `get_launch`
