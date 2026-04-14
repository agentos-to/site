---
title: organization
description: "A company, nonprofit, or other organization. Organizations are actors — they"
sidebar:
  label: organization
---

A company, nonprofit, or other organization. Organizations are actors — they
can be attributed as "who" in the graph alongside people and agents.

Example sources: extracted from various skills (email domains, product manufacturers, etc.)

| | |
|---|---|
| **Plural** | `organizations` |
| **Subtitle field** | `industry` |
| **Identity** | `url` |
| **Also** | [`actor`](/docs/reference/shapes/actor/) |

## Fields

| Field | Type |
|---|---|
| `industry` | `string` |
| `founded` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `member` | [`person[]`](/docs/reference/shapes/person/) |
| `domain` | [`domain`](/docs/reference/shapes/domain/) |
| `website` | [`website`](/docs/reference/shapes/website/) |
| `headquarters` | [`place`](/docs/reference/shapes/place/) |

## Inherited

From [`actor`](/docs/reference/shapes/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Used as a base by

- [`airline`](/docs/reference/shapes/airline/)
