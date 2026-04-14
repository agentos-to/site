---
title: leg
description: "One continuous movement on a single vehicle — takeoff to landing,"
sidebar:
  label: leg
---

One continuous movement on a single vehicle — takeoff to landing,
boarding to alighting, pickup to dropoff. No transfers within a leg.

A nonstop flight is one leg. A connecting flight has one leg per segment.
A direct Uber ride is one leg. A multi-stop Uber ride has one leg per stop pair.

Example sources: SerpAPI (flight segments), Uber (ride waypoints)

| Metadata | Value |
|---|---|
| **Plural** | `legs` |
| **Subtitle field** | `flightNumber` |

## Fields

| Field | Type |
|---|---|
| `sequence` | `integer` |
| `departureTime` | `datetime` |
| `arrivalTime` | `datetime` |
| `duration` | `string` |
| `durationMinutes` | `integer` |
| `flightNumber` | `string` |
| `cabinClass` | `string` |
| `vehicleType` | `string` |
| `layoverMinutes` | `integer` |
| `carbonEmissions` | `json` |
| `trace` | `json` |
| `tracePointCount` | `integer` |
| `polyline` | `string` |

## Relations

| Relation | Target |
|---|---|
| `origin` | [`place`](/docs/reference/shapes/place/) |
| `destination` | [`place`](/docs/reference/shapes/place/) |
| `carrier` | [`organization`](/docs/reference/shapes/organization/) |
| `aircraft` | [`aircraft`](/docs/reference/shapes/aircraft/) |
| `trip` | [`trip`](/docs/reference/shapes/trip/) |

## Used as a base by

- [`flight`](/docs/reference/shapes/flight/)
