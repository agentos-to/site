---
title: product
description: "A purchasable item. Base type for book and aircraft."
sidebar:
  label: product
---

A purchasable item. Base type for book and aircraft.
Cross-skill: Amazon products, Uber Eats grocery items, any retail catalog.

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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Product + Offer](https://schema.org/Product)** — Product on schema.org, price/priceAmount/currency/availability on nested Offer. Our sku/barcode map to sku/gtin13/gtin12; brand/manufacturer match directly.
- **[GS1 GTIN (UPC/EAN)](https://www.gs1.org/standards/id-keys/gtin)** — Canonical barcode standard. Our barcode field is a GTIN-8/12/13/14; GS1 also underlies schema.org's gtin* properties.
- **[Open Food Facts API](https://openfoodfacts.github.io/openfoodfacts-server/api/)** — Best practical source for food attributes. Our nutritionScore/novaGroup/calories/servingSize mirror nutriscore_grade/nova_group/nutriments.energy-kcal/serving_size.

## Skills that produce this shape

- [uber](/docs/skills/reference/logistics/uber/) — `get_item_customizations`, `search_products`
- [amazon](/docs/skills/reference/logistics/amazon/) — `search_products`, `buy_again`, `get_product`
