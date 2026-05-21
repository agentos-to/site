---
title: product
description: "A purchasable item OR an identifiable product released into the world."
sidebar:
  label: product
---

A purchasable item OR an identifiable product released into the world.
Base type for book, aircraft, hardware, software.
Cross-skill: Amazon products, Uber Eats grocery items, any retail catalog,
operating systems (Windows XP, Mac OS 9), aircraft types (Boeing 737),
books (any ISBN), cited code libraries (XP.css, 98.css).

Lifecycle fields (released, discontinued) are context-dependent:
- software:        released = first public release; discontinued = end of support
(Windows XP: released 2001-10-25, discontinued 2014-04-08)
- hardware:        released = launch date; discontinued = retirement / EOL
(iPhone 4: released 2010-06-24, discontinued 2013-09-10)
- aircraft:        released = type certification; discontinued = production end
(Boeing 707: released 1958-10-26, discontinued 1979-01-01)
- book:            released = publication date; discontinued = "out of print"
- retail product:  released = first sold; discontinued = stopped selling
A single field family captures all of these. Skills/apps can interpret
discontinued meaning per product-type via the product's `also:` shape membership.

| Metadata | Value |
|---|---|
| **Plural** | `products` |
| **Subtitle field** | `brand` |
| **Identity (any)** | `url` |

## Fields

| Field | Type |
|---|---|
| `category` | `string` |
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
| `customizationGroups` | `json` |

## Used as a base by

- [`aircraft`](/shapes/reference/aircraft/)
- [`book`](/shapes/reference/book/)
- [`software`](/shapes/reference/software/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Product + Offer](https://schema.org/Product)** — Product on schema.org, price/priceAmount/currency/availability on nested Offer. Our sku/barcode map to sku/gtin13/gtin12; brand/manufacturer match directly. schema.org has `releaseDate` on Product (mirrors our `released`) but no formalized end-of-life property.
- **[Wikidata P2669 (discontinued date)](https://www.wikidata.org/wiki/Property:P2669)** — Wikidata's canonical "discontinued date" property — broadly used across Wikidata's product entities (software, hardware, vehicles, consumer goods) with consistent semantics ("date when a product ceased to be manufactured, supported, or available"). Our `discontinued` field aligns directly. Wikidata P577 (publication date) similarly aligns with our `released`.
- **[schema.org/CreativeWork (creator, isBasedOn)](https://schema.org/CreativeWork)** — Our `creator: actor[]` mirrors schema.org/creator (Person|Organization). Our `inspiredBy: product[]` maps to schema.org/isBasedOn (CreativeWork derivation/credit link); we keep the more readable name and broaden the target to any product so non-CreativeWork lineages (one aircraft type inspired by another, one OS inspired by another) work the same way.
- **[GS1 GTIN (UPC/EAN)](https://www.gs1.org/standards/id-keys/gtin)** — Canonical barcode standard. Our barcode field is a GTIN-8/12/13/14; GS1 also underlies schema.org's gtin* properties.
- **[Open Food Facts API](https://openfoodfacts.github.io/openfoodfacts-server/api/)** — Best practical source for food attributes. Our nutritionScore/novaGroup/calories/servingSize mirror nutriscore_grade/nova_group/nutriments.energy-kcal/serving_size.

## Skills that produce this shape

- [uber](/skills/reference/logistics/uber/) — `get_item_customizations`, `search_products`
- [amazon](/skills/reference/logistics/amazon/) — `search_products`, `buy_again`, `get_product`
