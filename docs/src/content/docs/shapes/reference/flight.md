---
title: flight
description: "A flight — a specific leg of air travel. A flight IS a leg."
sidebar:
  label: flight
---

A flight — a specific leg of air travel. A flight IS a leg.
A nonstop itinerary has one flight. A connection has multiple flights.

| Metadata | Value |
|---|---|
| **Plural** | `flights` |
| **Subtitle field** | `airline` |
| **Also** | [`leg`](/docs/shapes/reference/leg/) |

## Fields

| Field | Type |
|---|---|
| `flightNumber` | `string` |
| `departureTime` | `datetime` |
| `arrivalTime` | `datetime` |
| `durationMinutes` | `integer` |
| `cabinClass` | `string` |
| `stops` | `integer` |
| `carbonEmissions` | `json` |

## Relations

| Relation | Target |
|---|---|
| `airline` | [`airline`](/docs/shapes/reference/airline/) |
| `departsFrom` | [`airport`](/docs/shapes/reference/airport/) |
| `arrivesAt` | [`airport`](/docs/shapes/reference/airport/) |
| `aircraft` | [`aircraft`](/docs/shapes/reference/aircraft/) |

## Inherited

From [`leg`](/docs/shapes/reference/leg/):

| Field | Type |
|---|---|
| `duration` | `string` |
| `layoverMinutes` | `integer` |
| `polyline` | `string` |
| `sequence` | `integer` |
| `trace` | `json` |
| `tracePointCount` | `integer` |
| `vehicleType` | `string` |

| Relation | Target |
|---|---|
| `carrier` | [`organization`](/docs/shapes/reference/organization/) |
| `destination` | [`place`](/docs/shapes/reference/place/) |
| `origin` | [`place`](/docs/shapes/reference/place/) |
| `trip` | [`trip`](/docs/shapes/reference/trip/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IATA Resolution 753 / Flight Codeshare](https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/)** — Our flightNumber follows IATA carrier-code + digits format (UA 1234). Canonical for cross-carrier flight identity.
- **[Duffel / IATA NDC Slice+Segment](https://duffel.com/docs/api/v2/overview)** — NDC models a trip (slice) as multiple flights (segments). Our flight shape = NDC segment; our trip = NDC slice.
- **[schema.org/Flight](https://schema.org/Flight)** — Our flightNumber = flightNumber; departsFrom/arrivesAt = departureAirport/arrivalAirport; departureTime/arrivalTime match directly; carbonEmissions ≈ estimatedFlightDuration + emissions extensions.
