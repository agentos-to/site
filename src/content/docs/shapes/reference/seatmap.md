---
title: seatmap
description: "A seat map for a specific flight + cabin, returned by an airline skill."
sidebar:
  label: seatmap
---

A seat map for a specific flight + cabin, returned by an airline skill.

A seatmap is the RENDERABLE STATE of a cabin at a moment in time:
which seats exist, which are available, their prices, and the
physical structure (aisles, exits, galleys, wings). It's bound to a
specific flight + fare because availability + prices depend on both.

Distinct from `aircraft` — aircraft describes the airplane TYPE
(model, variant, manufacturer); seatmap describes the cabin INSTANCE
at booking time (with occupancy, live pricing, per-fare eligibility).
The same 737-800 has different seatmaps for different flights (and
for different fare classes on the same flight, since Basic Economy
typically can't pick seats at all).

Distinct from a `pass.seatAssignment` — the assignment is the single
seat a passenger occupies; the seatmap is the whole cabin they
chose from.

Not itself a commerce primitive — the *selection* of a seat is a
purchase decision that lands on a `pass`. The seatmap is the catalog
that decision ranges over.

Prior art:
- IATA PADIS Seat Map Response (ATAMSM). Our schema mirrors the
cabin > row > seat hierarchy; flags like isExit / isBulkhead /
isBlocked map to PADIS characteristic codes.
- IATA AIRIMP codes for seat characteristics (e.g. "1A" = window,
"8" = no recline) — captured in iataAttributes when available.
- Duffel seat_maps endpoint. Their cabin > deck > rows > seats tree
flattens to our cabins[] > rows[] > seats[].
- schema.org has no seat-map primitive; closest is Event/Place/Ticket
but none fit cabin-with-aisles. Airlines universally use the IATA
shape; we follow.

Identity: the tuple (flight, fareBasisCode) — a seatmap is scoped to
one flight AND one fare (different fares yield different eligibility).
id is a synthetic string the skill composes.

| Metadata | Value |
|---|---|
| **Plural** | `seatmaps` |
| **Subtitle field** | `cabinBrand` |
| **Identity** | `id` |

## Fields

| Field | Type |
|---|---|
| `flightNumber` | `string` |
| `origin` | `string` |
| `destination` | `string` |
| `departureTime` | `datetime` |
| `fareBasisCode` | `string` |
| `classOfService` | `string` |
| `aircraftCode` | `string` |
| `totalSeats` | `integer` |
| `availableSeats` | `integer` |
| `cabins` | `json` |
| `tiers` | `json` |
| `hasExitRow` | `boolean` |
| `hasFreeSeats` | `boolean` |
| `hasPaidSeats` | `boolean` |
| `basicEconomyLocked` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `flight` | [`flight`](/shapes/reference/flight/) |
| `aircraft` | [`aircraft`](/shapes/reference/aircraft/) |
| `reservation` | [`reservation`](/shapes/reference/reservation/) |

## Skills that produce this shape

- [united](/skills/reference/logistics/united/) — `get_seatmap`
