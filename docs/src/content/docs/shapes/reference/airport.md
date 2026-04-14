---
title: airport
description: "An airport. Created from flight search results and linked to flights."
sidebar:
  label: airport
---

An airport. Created from flight search results and linked to flights.

| Metadata | Value |
|---|---|
| **Plural** | `airports` |
| **Subtitle field** | `iataCode` |
| **Identity** | `iataCode` |

## Fields

| Field | Type |
|---|---|
| `iataCode` | `string` |
| `icaoCode` | `string` |
| `city` | `string` |
| `country` | `string` |
| `countryCode` | `string` |
| `timezone` | `string` |
| `elevationFt` | `integer` |
| `terminalCount` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `location` | [`place`](/shapes/reference/place/) |
| `operator` | [`organization`](/shapes/reference/organization/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IATA/ICAO Airport Codes](https://www.iata.org/en/publications/directories/code-search/)** — iataCode is 3-letter (LAX, JFK); icaoCode is 4-letter (KLAX, KJFK). Canonical identifiers for global airport routing.
- **[schema.org/Airport](https://schema.org/Airport)** — Our iataCode/icaoCode = iataCode/icaoCode; city/country = address fields; elevationFt ≈ elevation. Direct alignment.
- **[OurAirports open dataset](https://ourairports.com/data/)** — Practical open dataset covering terminalCount, elevation, and country codes (ISO 3166-1) aligning with our countryCode field.
