---
title: airline
description: "A commercial airline. Created from flight search results."
sidebar:
  label: airline
---

A commercial airline. Created from flight search results.

| Metadata | Value |
|---|---|
| **Plural** | `airlines` |
| **Subtitle field** | `iataCode` |
| **Identity** | `iataCode` |
| **Also** | [`organization`](/shapes/reference/organization/) |

## Fields

| Field | Type |
|---|---|
| `iataCode` | `string` |
| `icaoCode` | `string` |
| `callsign` | `string` |
| `country` | `string` |
| `alliance` | `string` |

## Inherited

From [`organization`](/shapes/reference/organization/):

| Field | Type |
|---|---|
| `actorType` | `string` |
| `industry` | `string` |

| Relation | Target |
|---|---|
| `for` | [`person[]`](/shapes/reference/person/) |
| `headquartered_at` | [`place`](/shapes/reference/place/) |
| `on` | [`domain`](/shapes/reference/domain/) |
| `online_at` | [`website`](/shapes/reference/website/) |
| `subsidiary_of` | [`organization`](/shapes/reference/organization/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[IATA Airline Designators](https://www.iata.org/en/publications/directories/code-search/)** — iataCode is 2-letter (UA, DL); icaoCode is 3-letter (UAL, DAL); callsign is radio callsign (UNITED). Full IATA/ICAO alignment.
- **[schema.org/Airline](https://schema.org/Airline)** — schema.org's Airline is an Organization subtype. Our alliance is a free field; schema.org doesn't model it.
