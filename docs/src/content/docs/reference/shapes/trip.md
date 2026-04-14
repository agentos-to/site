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
| `origin` | [`place`](/docs/reference/shapes/place/) |
| `destination` | [`place`](/docs/reference/shapes/place/) |
| `legs` | [`leg[]`](/docs/reference/shapes/leg/) |
| `carrier` | [`organization`](/docs/reference/shapes/organization/) |
| `driver` | [`person`](/docs/reference/shapes/person/) |
| `order` | [`order`](/docs/reference/shapes/order/) |

## Skills that produce this shape

- [uber](/docs/reference/skills/logistics/uber/) — `list_trips`
- [uber](/docs/reference/skills/logistics/uber/) — `get_trip`
