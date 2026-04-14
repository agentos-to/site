---
title: aircraft
description: "An aircraft type (not an individual plane). Linked from flight search results."
sidebar:
  label: aircraft
---

An aircraft type (not an individual plane). Linked from flight search results.

Example sources: SerpAPI (flight search)

| | |
|---|---|
| **Plural** | `aircraft` |
| **Subtitle field** | `model` |
| **Identity** | `icaoCode` |
| **Also** | [`product`](/docs/reference/shapes/product/) |

## Fields

| Field | Type |
|---|---|
| `model` | `string` |
| `variant` | `string` |
| `seatCapacity` | `integer` |
| `rangeKm` | `integer` |
| `iataCode` | `string` |
| `icaoCode` | `string` |

## Relations

| Relation | Target |
|---|---|
| `manufacturer` | [`organization`](/docs/reference/shapes/organization/) |

## Inherited

From [`product`](/docs/reference/shapes/product/):

| Field | Type |
|---|---|
| `aisle` | `string` |
| `availability` | `string` |
| `barcode` | `string` |
| `calories` | `number` |
| `categories` | `string[]` |
| `currency` | `string` |
| `department` | `string` |
| `images` | `json` |
| `novaGroup` | `integer` |
| `nutritionScore` | `string` |
| `originalPrice` | `string` |
| `originalPriceAmount` | `number` |
| `price` | `string` |
| `priceAmount` | `number` |
| `quantity` | `integer` |
| `servingSize` | `string` |
| `sku` | `string` |
| `soldByWeight` | `boolean` |
| `weight` | `string` |
| `weightUnit` | `string` |
| `weightValue` | `number` |

| Relation | Target |
|---|---|
| `brand` | [`brand`](/docs/reference/shapes/brand/) |
| `tagged` | [`tag[]`](/docs/reference/shapes/tag/) |
