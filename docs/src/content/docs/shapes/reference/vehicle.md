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

| Metadata | Value |
|---|---|
| **Plural** | `vehicles` |
| **Subtitle field** | `vin` |
| **Identity** | `vin` |
| **Also** | [`product`](/shapes/reference/product/) |

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
| `manufacturer` | [`organization`](/shapes/reference/organization/) |

## Inherited

From [`product`](/shapes/reference/product/):

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
| `brand` | [`brand`](/shapes/reference/brand/) |
| `tagged` | [`tag[]`](/shapes/reference/tag/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ISO 3779 — VIN (Vehicle Identification Number)](https://www.iso.org/standard/52200.html)** — Canonical 17-char VIN. Our vin field uses ISO 3779 syntax (WMI + VDS + VIS).
- **[schema.org/Vehicle](https://schema.org/Vehicle)** — Our year ≈ vehicleModelDate; model = model; fuelType = fuelType; bodyType = bodyType; drivetrain = driveWheelConfiguration.
- **[NHTSA vPIC VIN Decoder API](https://vpic.nhtsa.dot.gov/api/)** — Practical decoder for year/model/trim/bodyType/fuelType from VIN. Our fields align with vPIC's decoded result.
