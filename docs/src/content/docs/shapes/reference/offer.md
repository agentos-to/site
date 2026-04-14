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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Offer](https://schema.org/Offer)** — Our price = price; currency = priceCurrency; availability = availability; validFrom/validUntil match directly.
- **[IATA NDC OfferItem](https://www.iata.org/en/programs/airline-distribution/retailing/ndc/)** — Our bookingToken ≈ OfferItemID; validUntil ≈ TimeLimits/ OfferExpirationDateTime; trips[] ≈ Itinerary.
- **[schema.org/AggregateOffer](https://schema.org/AggregateOffer)** — For price-range offers (SerpAPI flight results). offerType is AgentOS-specific.

## Skills that produce this shape

- [serpapi](/docs/skills/reference/web/serpapi/) — `search_offers`, `list_offers`, `get_offer`
