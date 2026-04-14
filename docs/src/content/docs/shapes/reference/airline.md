---
title: airline
description: "A commercial airline. Created from flight search results."
sidebar:
  label: airline
---

A commercial airline. Created from flight search results.

Example sources: SerpAPI (flight search)

| Metadata | Value |
|---|---|
| **Plural** | `airlines` |
| **Subtitle field** | `iataCode` |
| **Identity** | `iataCode` |
| **Also** | [`organization`](/docs/shapes/reference/organization/) |

## Fields

| Field | Type |
|---|---|
| `iataCode` | `string` |
| `icaoCode` | `string` |
| `callsign` | `string` |
| `country` | `string` |
| `alliance` | `string` |

## Inherited

From [`organization`](/docs/shapes/reference/organization/):

| Field | Type |
|---|---|
| `actorType` | `string` |
| `founded` | `datetime` |
| `industry` | `string` |

| Relation | Target |
|---|---|
| `domain` | [`domain`](/docs/shapes/reference/domain/) |
| `headquarters` | [`place`](/docs/shapes/reference/place/) |
| `member` | [`person[]`](/docs/shapes/reference/person/) |
| `website` | [`website`](/docs/shapes/reference/website/) |
