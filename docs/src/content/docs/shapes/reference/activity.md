---
title: activity
description: "An immutable change event — a graph mutation, skill run, search, or load."
sidebar:
  label: activity
---

An immutable change event — a graph mutation, skill run, search, or load.
Fields for what happened, relations for who/what/where.

| Metadata | Value |
|---|---|
| **Plural** | `activities` |
| **Subtitle field** | `action` |

## Fields

| Field | Type |
|---|---|
| `action` | `string` |
| `published` | `datetime` |
| `changedKeys` | `string[]` |
| `toolName` | `string` |
| `duration` | `number` |
| `success` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `session` | [`session`](/docs/shapes/reference/session/) |
| `folder` | [`folder`](/docs/shapes/reference/folder/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityStreams 2.0](https://www.w3.org/TR/activitystreams-core/)** — AS2's Create/Update/Delete activities match our action values. We diverge by tracking changedKeys explicitly instead of encoding full object replacement.
- **[OpenTelemetry Traces](https://opentelemetry.io/docs/concepts/signals/traces/)** — Closest fit for toolName/duration/success — span-shaped. Our activity is closer to a span event than a full span.
