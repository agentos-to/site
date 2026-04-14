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

Example sources: future (GTFS, flight timetables, Uber Eats store hours)

| | |
|---|---|
| **Plural** | `routes` |
| **Subtitle field** | `routeNumber` |
| **Also** | [`schedule`](/docs/reference/shapes/schedule/) |

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
| `stops` | [`place[]`](/docs/reference/shapes/place/) |
| `origin` | [`place`](/docs/reference/shapes/place/) |
| `destination` | [`place`](/docs/reference/shapes/place/) |
| `operator` | [`organization`](/docs/reference/shapes/organization/) |

## Inherited

From [`schedule`](/docs/reference/shapes/schedule/):

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
| `produces` | [`trip`](/docs/reference/shapes/trip/) |
| `provider` | [`skill`](/docs/reference/shapes/skill/) |
