---
title: offer
description: "A purchasable offer — typically a flight itinerary with a price."
sidebar:
  label: offer
---

A purchasable offer — typically a flight itinerary with a price.
An offer wraps one or more flights into a bookable unit.

Example sources: SerpAPI (Google Flights)

| | |
|---|---|
| **Plural** | `offers` |

## Fields

| Field | Type |
|---|---|
| `price` | `number` |
| `currency` | `string` |
| `offerType` | `string` |
| `availability` | `string` |
| `validFrom` | `datetime` |
| `validUntil` | `datetime` |
| `bookingToken` | `string` |

## Relations

| Relation | Target |
|---|---|
| `for` | [`product`](/docs/reference/shapes/product/) |
| `offeredBy` | [`organization`](/docs/reference/shapes/organization/) |
| `trips` | [`trip[]`](/docs/reference/shapes/trip/) |

## Skills that produce this shape

- [serpapi](/docs/reference/skills/serpapi/) — `search_offers`, `list_offers`, `get_offer`
