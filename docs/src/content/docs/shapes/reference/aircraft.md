---
title: aircraft
description: "An aircraft type (not an individual plane). Linked from flight search results."
sidebar:
  label: aircraft
---

An aircraft type (not an individual plane). Linked from flight search results.

Example sources: SerpAPI (flight search)

| Metadata | Value |
|---|---|
| **Plural** | `aircraft` |
| **Subtitle field** | `model` |
| **Identity** | `icaoCode` |
| **Also** | [`product`](/docs/shapes/reference/product/) |

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
| `manufacturer` | [`organization`](/docs/shapes/reference/organization/) |

## Inherited

From [`product`](/docs/shapes/reference/product/):

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
| `brand` | [`brand`](/docs/shapes/reference/brand/) |
| `tagged` | [`tag[]`](/docs/shapes/reference/tag/) |
