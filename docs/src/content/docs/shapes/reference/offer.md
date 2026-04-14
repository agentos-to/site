---
title: offer
description: "A purchasable offer — typically a flight itinerary with a price."
sidebar:
  label: offer
---

A purchasable offer — typically a flight itinerary with a price.
An offer wraps one or more flights into a bookable unit.

Example sources: SerpAPI (Google Flights)

| Metadata | Value |
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
| `for` | [`product`](/docs/shapes/reference/product/) |
| `offeredBy` | [`organization`](/docs/shapes/reference/organization/) |
| `trips` | [`trip[]`](/docs/shapes/reference/trip/) |

## Skills that produce this shape

- [serpapi](/docs/skills/reference/web/serpapi/) — `search_offers`, `list_offers`, `get_offer`
