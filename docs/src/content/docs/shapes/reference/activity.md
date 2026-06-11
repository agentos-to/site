---
title: activity
description: "An immutable change event — a graph mutation, app run, search, or load."
sidebar:
  label: activity
---

An immutable change event — a graph mutation, app run, search, or load.
Fields for what happened, relations for who/what/where.

| Metadata | Value |
|---|---|
| **Plural** | `activities` |
| **Subtitle field** | `action` |
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `action` | `string` |
| `changedKeys` | `string[]` |
| `toolName` | `string` |
| `duration` | `number` |
| `success` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `in` | [`mcp_session`](/shapes/reference/mcp_session/) |
| `filed_in` | [`list`](/shapes/reference/list/) |

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

- **[ActivityStreams 2.0](https://www.w3.org/TR/activitystreams-core/)** — AS2's Create/Update/Delete activities match our action values. We diverge by tracking changedKeys explicitly instead of encoding full object replacement.
- **[OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)** — Closest fit for toolName/duration/success — span-shaped. Our activity is closer to a span event than a full span.
