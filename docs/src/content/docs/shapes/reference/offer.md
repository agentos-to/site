---
title: offer
description: "A purchasable offer — typically a flight itinerary with a price."
sidebar:
  label: offer
---

A purchasable offer — typically a flight itinerary with a price.
An offer wraps one or more flights into a bookable unit.

| Metadata | Value |
|---|---|
| **Plural** | `offers` |
| **Subtitle field** | `price` |
| **Identity** | `id` |

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
| `departureToken` | `string` |

## Relations

| Relation | Target |
|---|---|
| `for` | [`product`](/shapes/reference/product/) |
| `offeredBy` | [`organization`](/shapes/reference/organization/) |
| `trips` | [`trip[]`](/shapes/reference/trip/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Offer](https://schema.org/Offer)** — Our price = price; currency = priceCurrency; availability = availability; validFrom/validUntil match directly.
- **[IATA NDC OfferItem](https://www.iata.org/en/programs/airline-distribution/retailing/ndc/)** — Our bookingToken ≈ OfferItemID; validUntil ≈ TimeLimits/ OfferExpirationDateTime; trips[] ≈ Itinerary.
- **[schema.org/AggregateOffer](https://schema.org/AggregateOffer)** — For price-range offers (SerpAPI flight results). offerType is AgentOS-specific.

## Skills that produce this shape

- [united](/skills/reference/logistics/united/) — `search_flights`
- [serpapi](/skills/reference/web/serpapi/) — `search_offers`, `list_offers`, `get_offer`
