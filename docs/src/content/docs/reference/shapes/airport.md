---
title: airport
description: "An airport. Created from flight search results and linked to flights."
sidebar:
  label: airport
---

An airport. Created from flight search results and linked to flights.

Example sources: SerpAPI (flight search)

| | |
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
| `location` | [`place`](/docs/reference/shapes/place/) |
| `operator` | [`organization`](/docs/reference/shapes/organization/) |
