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
| `brand` | [`brand`](/docs/reference/shapes/brand/) |
| `manufacturer` | [`organization`](/docs/reference/shapes/organization/) |
| `tagged` | [`tag[]`](/docs/reference/shapes/tag/) |

## Used as a base by

- [`aircraft`](/docs/reference/shapes/aircraft/)
- [`book`](/docs/reference/shapes/book/)
- [`hardware`](/docs/reference/shapes/hardware/)
- [`software`](/docs/reference/shapes/software/)
- [`vehicle`](/docs/reference/shapes/vehicle/)

## Skills that produce this shape

- [uber](/docs/reference/skills/logistics/uber/) — `get_item_customizations`
- [uber](/docs/reference/skills/logistics/uber/) — `search_products`
- [amazon](/docs/reference/skills/logistics/amazon/) — `search_products`, `buy_again`
- [amazon](/docs/reference/skills/logistics/amazon/) — `get_product`
