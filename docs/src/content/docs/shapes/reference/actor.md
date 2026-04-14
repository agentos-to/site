---
title: actor
description: "Base type for anything that can be attributed as 'who did this' in the graph."
sidebar:
  label: actor
---

Base type for anything that can be attributed as "who did this" in the graph.
Not used directly — person, organization, and agent extend it via `also`.

| Metadata | Value |
|---|---|
| **Plural** | `actors` |
| **Subtitle field** | `actorType` |

## Fields

| Field | Type |
|---|---|
| `actorType` | `string` |

## Used as a base by

- [`agent`](/docs/shapes/reference/agent/)
- [`organization`](/docs/shapes/reference/organization/)
- [`person`](/docs/shapes/reference/person/)
