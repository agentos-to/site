---
title: product
description: "A purchasable item. Base type for book and aircraft."
sidebar:
  label: product
---

A purchasable item. Base type for book and aircraft.
Cross-skill: Amazon products, Uber Eats grocery items, any retail catalog.

Example sources: Amazon, Uber Eats (grocery), Open Food Facts (enrichment)

| Metadata | Value |
|---|---|
| **Plural** | `products` |
| **Subtitle field** | `brand` |

## Fields

| Field | Type |
|---|---|
| `price` | `string` |
| `priceAmount` | `number` |
| `originalPrice` | `string` |
| `originalPriceAmount` | `number` |
| `currency` | `string` |
| `categories` | `string[]` |
| `availability` | `string` |
| `images` | `json` |
| `quantity` | `integer` |
| `weight` | `string` |
| `weightValue` | `number` |
| `weightUnit` | `string` |
| `soldByWeight` | `boolean` |
| `department` | `string` |
| `aisle` | `string` |
| `sku` | `string` |
| `barcode` | `string` |
| `nutritionScore` | `string` |
| `novaGroup` | `integer` |
| `calories` | `number` |
| `servingSize` | `string` |

## Relations

| Relation | Target |
|---|---|
| `brand` | [`brand`](/docs/shapes/reference/brand/) |
| `manufacturer` | [`organization`](/docs/shapes/reference/organization/) |
| `tagged` | [`tag[]`](/docs/shapes/reference/tag/) |

## Used as a base by

- [`aircraft`](/docs/shapes/reference/aircraft/)
- [`book`](/docs/shapes/reference/book/)
- [`hardware`](/docs/shapes/reference/hardware/)
- [`software`](/docs/shapes/reference/software/)
- [`vehicle`](/docs/shapes/reference/vehicle/)

## Skills that produce this shape

- [uber](/docs/skills/reference/logistics/uber/) — `get_item_customizations`
- [uber](/docs/skills/reference/logistics/uber/) — `search_products`
- [amazon](/docs/skills/reference/logistics/amazon/) — `search_products`, `buy_again`
- [amazon](/docs/skills/reference/logistics/amazon/) — `get_product`
