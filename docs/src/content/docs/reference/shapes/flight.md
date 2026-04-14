---
title: flight
description: "A flight — a specific leg of air travel. A flight IS a leg."
sidebar:
  label: flight
---

A flight — a specific leg of air travel. A flight IS a leg.
A nonstop itinerary has one flight. A connection has multiple flights.

Example sources: SerpAPI (Google Flights)

| | |
|---|---|
| **Plural** | `flights` |
| **Subtitle field** | `airline` |
| **Also** | [`leg`](/docs/reference/shapes/leg/) |

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
| `airline` | [`airline`](/docs/reference/shapes/airline/) |
| `departsFrom` | [`airport`](/docs/reference/shapes/airport/) |
| `arrivesAt` | [`airport`](/docs/reference/shapes/airport/) |
| `aircraft` | [`aircraft`](/docs/reference/shapes/aircraft/) |

## Inherited

From [`leg`](/docs/reference/shapes/leg/):

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
| `carrier` | [`organization`](/docs/reference/shapes/organization/) |
| `destination` | [`place`](/docs/reference/shapes/place/) |
| `origin` | [`place`](/docs/reference/shapes/place/) |
| `trip` | [`trip`](/docs/reference/shapes/trip/) |
