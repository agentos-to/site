---
title: airline
description: "A commercial airline. Created from flight search results."
sidebar:
  label: airline
---

A commercial airline. Created from flight search results.

Example sources: SerpAPI (flight search)

| Metadata | Value |
|---|---|
| **Plural** | `airlines` |
| **Subtitle field** | `iataCode` |
| **Identity** | `iataCode` |
| **Also** | [`organization`](/docs/shapes/reference/organization/) |

## Fields

| Field | Type |
|---|---|
| `iataCode` | `string` |
| `icaoCode` | `string` |
| `callsign` | `string` |
| `country` | `string` |
| `alliance` | `string` |

## Inherited

From [`organization`](/docs/shapes/reference/organization/):

| Field | Type |
|---|---|
| `actorType` | `string` |
| `founded` | `datetime` |
| `industry` | `string` |

| Relation | Target |
|---|---|
| `domain` | [`domain`](/docs/shapes/reference/domain/) |
| `headquarters` | [`place`](/docs/shapes/reference/place/) |
| `member` | [`person[]`](/docs/shapes/reference/person/) |
| `website` | [`website`](/docs/shapes/reference/website/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[IATA Airline Designators](https://www.iata.org/en/publications/directories/code-search/)** — iataCode is 2-letter (UA, DL); icaoCode is 3-letter (UAL, DAL); callsign is radio callsign (UNITED). Full IATA/ICAO alignment.
- **[schema.org/Airline](https://schema.org/Airline)** — schema.org's Airline is an Organization subtype. Our alliance is a free field; schema.org doesn't model it.
