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
| **Also** | [`leg`](/shapes/reference/leg/) |

## Fields

| Field | Type |
|---|---|
| `flightNumber` | `string` |
| `durationMinutes` | `integer` |
| `cabinClass` | `string` |
| `stops` | `integer` |
| `carbonEmissions` | `json` |

## Relations

| Relation | Target |
|---|---|
| `operated_by` | [`airline`](/shapes/reference/airline/) |
| `departs_from` | [`airport`](/shapes/reference/airport/) |
| `arrives_at` | [`airport`](/shapes/reference/airport/) |
| `flown_with` | [`aircraft`](/shapes/reference/aircraft/) |

## Inherited

From [`leg`](/shapes/reference/leg/):

| Field | Type |
|---|---|
| `allDay` | `boolean` |
| `arrivalTime` | `datetime` |
| `currentUrl` | `string` |
| `dateUpdated` | `datetime` |
| `departureTime` | `datetime` |
| `distinctId` | `string` |
| `duration` | `string` |
| `endDate` | `datetime` |
| `icalUid` | `string` |
| `layoverMinutes` | `integer` |
| `polyline` | `string` |
| `properties` | `json` |
| `recurrence` | `string[]` |
| `sequence` | `integer` |
| `showAs` | `string` |
| `sourceTitle` | `string` |
| `sourceUrl` | `url` |
| `startDate` | `datetime` |
| `status` | `string` |
| `timezone` | `string` |
| `trace` | `json` |
| `tracePointCount` | `integer` |
| `vehicleType` | `string` |
| `visibility` | `string` |

| Relation | Target |
|---|---|
| `at_namespace` | [`actor`](/shapes/reference/actor/) |
| `concerns` | [`person`](/shapes/reference/person/) |
| `created_by` | [`person`](/shapes/reference/person/) |
| `ends_at` | [`place`](/shapes/reference/place/) |
| `held_at` | [`place`](/shapes/reference/place/) |
| `in` | [`trip`](/shapes/reference/trip/) |
| `involves` | [`person[]`](/shapes/reference/person/) |
| `organized_by` | [`person`](/shapes/reference/person/) |
| `starts_at` | [`place`](/shapes/reference/place/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IATA Resolution 753 / Flight Codeshare](https://www.iata.org/en/programs/ops-infra/baggage/baggage-tracking/)** — Our flightNumber follows IATA carrier-code + digits format (UA 1234). Canonical for cross-carrier flight identity.
- **[Duffel / IATA NDC Slice+Segment](https://duffel.com/docs/api/v2/overview)** — NDC models a trip (slice) as multiple flights (segments). Our flight shape = NDC segment; our trip = NDC slice.
- **[schema.org/Flight](https://schema.org/Flight)** — Our flightNumber = flightNumber; departsFrom/arrivesAt = departureAirport/arrivalAirport; departureTime/arrivalTime match directly; carbonEmissions ≈ estimatedFlightDuration + emissions extensions.
