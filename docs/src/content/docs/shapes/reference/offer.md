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
| **Also** | [`event`](/shapes/reference/event/) |

## Fields

| Field | Type |
|---|---|
| `price` | `number` |
| `currency` | `string` |
| `offerType` | `string` |
| `availability` | `string` |
| `bookingToken` | `string` |
| `departureToken` | `string` |

## Relations

| Relation | Target |
|---|---|
| `offered_for` | [`product`](/shapes/reference/product/) |
| `offered_by` | [`organization`](/shapes/reference/organization/) |
| `covers_trip` | [`trip[]`](/shapes/reference/trip/) |

## Inherited

From [`event`](/shapes/reference/event/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `distinctId` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `visibility` | `string` |

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `concerns` | [`person`](/shapes/reference/person/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Offer](https://schema.org/Offer)** — Our price = price; currency = priceCurrency; availability = availability; validFrom/validUntil match directly.
- **[IATA NDC OfferItem](https://www.iata.org/en/programs/airline-distribution/retailing/ndc/)** — Our bookingToken ≈ OfferItemID; validUntil ≈ TimeLimits/ OfferExpirationDateTime; trips[] ≈ Itinerary.
- **[schema.org/AggregateOffer](https://schema.org/AggregateOffer)** — For price-range offers (SerpAPI flight results). offerType is AgentOS-specific.

## Apps that produce this shape

- [united](/apps/reference/logistics/united/) — `search_flights`
- [serpapi](/apps/reference/web/serpapi/) — `search_offers`, `list_offers`, `get_offer`
