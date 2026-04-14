---
title: organization
description: "A company, nonprofit, or other organization. Organizations are actors — they"
sidebar:
  label: organization
---

A company, nonprofit, or other organization. Organizations are actors — they
can be attributed as "who" in the graph alongside people and agents.

Example sources: extracted from various skills (email domains, product manufacturers, etc.)

| Metadata | Value |
|---|---|
| **Plural** | `organizations` |
| **Subtitle field** | `industry` |
| **Identity** | `url` |
| **Also** | [`actor`](/docs/shapes/reference/actor/) |

## Fields

| Field | Type |
|---|---|
| `industry` | `string` |
| `founded` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `member` | [`person[]`](/docs/shapes/reference/person/) |
| `domain` | [`domain`](/docs/shapes/reference/domain/) |
| `website` | [`website`](/docs/shapes/reference/website/) |
| `headquarters` | [`place`](/docs/shapes/reference/place/) |

## Inherited

From [`actor`](/docs/shapes/reference/actor/):

| Field | Type |
|---|---|
| `actorType` | `string` |

## Used as a base by

- [`airline`](/docs/shapes/reference/airline/)
