---
title: hardware
description: "A physical hardware product — computer, phone, appliance, component."
sidebar:
  label: hardware
---

A physical hardware product — computer, phone, appliance, component.

Examples: MacBook Pro, iPhone, Arduino, server rack

| Metadata | Value |
|---|---|
| **Plural** | `hardware` |
| **Subtitle field** | `author` |
| **Identity** | `serialNumber` |
| **Also** | [`product`](/shapes/reference/product/) |

## Fields

| Field | Type |
|---|---|
| `modelNumber` | `string` |
| `serialNumber` | `string` |
| `specs` | `json` |

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

- **[schema.org/Product (IndividualProduct subtype)](https://schema.org/IndividualProduct)** — Our serialNumber = serialNumber; modelNumber ≈ model; specs ≈ additionalProperty (PropertyValue list).
- **[GS1 Global Trade Item Number (GTIN)](https://www.gs1.org/standards/id-keys/gtin)** — Hardware bar-codes are GTIN-12/13/14 — we reuse the product shape's barcode alignment.
