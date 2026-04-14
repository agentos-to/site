---
title: trip
description: "A directed journey from origin to destination — one direction of travel."
sidebar:
  label: trip
---

A directed journey from origin to destination — one direction of travel.
A round-trip booking produces two trips (outbound + return).
A single Uber ride is one trip. A connecting flight is one trip with multiple legs.
Multi-stop Uber rides have multiple legs (one per waypoint pair).

Terminology alignment:
Duffel/NDC "slice" = trip    |  "segment" = leg
SerpAPI result = trip        |  flights[] element = leg
Schema.org Trip > subTrip    |  Uber ride = trip (1+ legs)
Train journey = trip         |  each train boarded = leg

Example sources: Uber (rides), Uber Eats (delivery), SerpAPI (flights)

| Metadata | Value |
|---|---|
| **Plural** | `trips` |
| **Subtitle field** | `tripType` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `tripType` | `string` |
| `status` | `string` |
| `departureTime` | `datetime` |
| `arrivalTime` | `datetime` |
| `duration` | `string` |
| `durationMinutes` | `integer` |
| `distance` | `string` |
| `vehicleType` | `string` |
| `cabinClass` | `string` |
| `fare` | `string` |
| `fareAmount` | `number` |
| `currency` | `string` |
| `rating` | `string` |
| `trackingUrl` | `url` |
| `isSurge` | `boolean` |
| `isScheduled` | `boolean` |
| `stops` | `integer` |
| `bookingToken` | `string` |
| `carbonEmissions` | `json` |

## Relations

| Relation | Target |
|---|---|
| `origin` | [`place`](/docs/shapes/reference/place/) |
| `destination` | [`place`](/docs/shapes/reference/place/) |
| `legs` | [`leg[]`](/docs/shapes/reference/leg/) |
| `carrier` | [`organization`](/docs/shapes/reference/organization/) |
| `driver` | [`person`](/docs/shapes/reference/person/) |
| `order` | [`order`](/docs/shapes/reference/order/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Trip + subTrip](https://schema.org/Trip)** — Our origin/destination/departureTime/arrivalTime map exactly; legs[] ≈ subTrip or itinerary.
- **[IATA NDC Slice (airline itineraries)](https://www.iata.org/en/programs/airline-distribution/retailing/ndc/)** — NDC slice = our trip; NDC segment = our leg. cabinClass, bookingToken come from NDC offer items.
- **[Uber API — Trip resource](https://developer.uber.com/docs/riders/references/api)** — Practical source for ride trips. Our fare/fareAmount/ trackingUrl/isSurge/isScheduled lifted from Uber's Trip model.

## Skills that produce this shape

- [uber](/docs/skills/reference/logistics/uber/) — `list_trips`
- [uber](/docs/skills/reference/logistics/uber/) — `get_trip`
