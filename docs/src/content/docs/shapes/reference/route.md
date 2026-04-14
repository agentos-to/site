---
title: route
description: "A transport service that operates between places on a schedule."
sidebar:
  label: route
---

A transport service that operates between places on a schedule.
A route IS a schedule — it inherits recurrence fields and adds
transport-specific structure: stops, direction, route identifiers.

Each occurrence of the route produces a trip (with legs).

Examples:
Bus 29 Austin — route_type: bus, stops: [Congress, Riverside, ...]
UA 1234 LAX→JFK daily — route_type: flight, origin/destination airports
Amtrak Acela NYC→DC — route_type: train
Costco delivery (Sat 9:30a-7p) — route_type: delivery, store as origin

GTFS alignment: GTFS "route" = this shape. GTFS "trip" = our trip shape.
GTFS "stop_times" = our leg origins/destinations.

| Metadata | Value |
|---|---|
| **Plural** | `routes` |
| **Subtitle field** | `routeNumber` |
| **Also** | [`schedule`](/shapes/reference/schedule/) |

## Fields

| Field | Type |
|---|---|
| `routeType` | `string` |
| `routeNumber` | `string` |
| `direction` | `string` |
| `color` | `string` |

## Relations

| Relation | Target |
|---|---|
| `stops` | [`place[]`](/shapes/reference/place/) |
| `origin` | [`place`](/shapes/reference/place/) |
| `destination` | [`place`](/shapes/reference/place/) |
| `operator` | [`organization`](/shapes/reference/organization/) |

## Inherited

From [`schedule`](/shapes/reference/schedule/):

| Field | Type |
|---|---|
| `cronExpression` | `string` |
| `durability` | `string` |
| `enabled` | `boolean` |
| `hours` | `json` |
| `lastFiredAt` | `datetime` |
| `nextFireAt` | `datetime` |
| `prompt` | `string` |
| `providerJobId` | `string` |
| `rrule` | `string` |
| `scheduleType` | `string` |
| `timezone` | `string` |

| Relation | Target |
|---|---|
| `produces` | [`trip`](/shapes/reference/trip/) |
| `provider` | [`skill`](/shapes/reference/skill/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[GTFS routes.txt](https://gtfs.org/documentation/schedule/reference/#routestxt)** — Direct source. Our routeType maps to GTFS route_type (integer vocab); routeNumber = route_short_name; color = route_color.
- **[schema.org/BusOrCoach + FlightRoute](https://schema.org/BusOrCoach)** — Per-mode peers. Our stops[]/origin/destination are modeled separately per mode in schema.org.
