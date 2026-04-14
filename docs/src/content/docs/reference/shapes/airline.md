---
title: airline
description: "A commercial airline. Created from flight search results."
sidebar:
  label: airline
---

A commercial airline. Created from flight search results.

Example sources: SerpAPI (flight search)

| | |
|---|---|
| **Plural** | `airlines` |
| **Subtitle field** | `iataCode` |
| **Identity** | `iataCode` |
| **Also** | [`organization`](/docs/reference/shapes/organization/) |

## Fields

| Field | Type |
|---|---|
| `iataCode` | `string` |
| `icaoCode` | `string` |
| `callsign` | `string` |
| `country` | `string` |
| `alliance` | `string` |

## Inherited

From [`organization`](/docs/reference/shapes/organization/):

| Field | Type |
|---|---|
| `actorType` | `string` |
| `founded` | `datetime` |
| `industry` | `string` |

| Relation | Target |
|---|---|
| `domain` | [`domain`](/docs/reference/shapes/domain/) |
| `headquarters` | [`place`](/docs/reference/shapes/place/) |
| `member` | [`person[]`](/docs/reference/shapes/person/) |
| `website` | [`website`](/docs/reference/shapes/website/) |
