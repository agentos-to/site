---
title: vehicle
description: "A vehicle — the physical object. VIN, specs, color."
sidebar:
  label: vehicle
---

A vehicle — the physical object. VIN, specs, color.
Ownership, registration, and purchase are events/relationships, not
properties of the vehicle. A car doesn't "become sold" — it changes
hands. Plates belong to a registration, not the car.

Ownership history: person --owns--> vehicle (edge with start/end dates)
Purchase: a transaction between buyer, seller, and vehicle
Registration: vehicle registered in a jurisdiction (edge with plate, dates)

Example sources: manual entry, document extraction

| Metadata | Value |
|---|---|
| **Plural** | `vehicles` |
| **Subtitle field** | `vin` |
| **Identity** | `vin` |
| **Also** | [`product`](/docs/shapes/reference/product/) |

## Fields

| Field | Type |
|---|---|
| `vin` | `string` |
| `year` | `integer` |
| `model` | `string` |
| `trim` | `string` |
| `bodyType` | `string` |
| `fuelType` | `string` |
| `transmission` | `string` |
| `drivetrain` | `string` |
| `color` | `string` |
| `odometer` | `integer` |

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
