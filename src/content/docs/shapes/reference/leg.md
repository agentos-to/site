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
| `origin` | [`place`](/shapes/reference/place/) |
| `destination` | [`place`](/shapes/reference/place/) |
| `carrier` | [`organization`](/shapes/reference/organization/) |
| `aircraft` | [`aircraft`](/shapes/reference/aircraft/) |
| `trip` | [`trip`](/shapes/reference/trip/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IATA NDC "segment"](https://www.iata.org/en/programs/airline-distribution/retailing/ndc/)** — NDC segment = our leg. flightNumber, departureTime, arrivalTime, cabinClass come straight from NDC OfferItem Segment.
- **[GTFS stop_times.txt](https://gtfs.org/documentation/schedule/reference/#stop_timestxt)** — Transit leg model. Our sequence = stop_sequence; departureTime/ arrivalTime = arrival_time/departure_time.
- **[Google Encoded Polyline Algorithm](https://developers.google.com/maps/documentation/utilities/polylinealgorithmformat)** — Our polyline field is the standard Google encoded polyline. trace is a denser GPS breadcrumb alternative (GeoJSON-adjacent).
