---
title: software
description: "A software product — operating system, application, library, icon pack,"
sidebar:
  label: software
---

A software product — operating system, application, library, icon pack,
stylesheet kit, anything that's "code (or bundled assets) released into
the world."

Examples: Windows XP, Mac OS 9, XP.css (CSS library), marchmountain
icon pack, Photoshop, VS Code, Slack desktop app.

Software is a product (`also: [product]`), so it inherits lifecycle dates
(released, discontinued), brand, manufacturer, creator, inspiredBy, and the
rest of product's surface. Software-specific fields below.

| Metadata | Value |
|---|---|
| **Plural** | `software` |
| **Subtitle field** | `applicationCategory` |
| **Identity (any)** | `url` |
| **Also** | [`product`](/shapes/reference/product/) |

## Fields

| Field | Type |
|---|---|
| `version` | `string` |
| `applicationCategory` | `string` |
| `runtimePlatform` | `string` |
| `codename` | `string` |

## Relations

| Relation | Target |
|---|---|
| `manufactured_by` | [`organization`](/shapes/reference/organization/) |

## Inherited

From [`product`](/shapes/reference/product/):

| Field | Type |
|---|---|
| `aisle` | `string` |
| `availability` | `string` |
| `barcode` | `string` |
| `calories` | `number` |
| `categories` | `string[]` |
| `category` | `string` |
| `currency` | `string` |
| `customizationGroups` | `json` |
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
| `branded_as` | [`brand`](/shapes/reference/brand/) |
| `created_by` | [`actor[]`](/shapes/reference/actor/) |
| `inspired_by` | [`product[]`](/shapes/reference/product/) |
| `tagged_with` | [`tag[]`](/shapes/reference/tag/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/SoftwareApplication](https://schema.org/SoftwareApplication)** — Our applicationCategory mirrors schema.org applicationCategory (free-form string, common values include "GameApplication", "BusinessApplication", "BrowserApplication"). Our version maps to softwareVersion; runtimePlatform maps to operatingSystem (the closest analog — schema.org uses `operatingSystem` to mean "which platform the software runs on", which matches our intent). Codename has no schema.org equivalent.
- **[schema.org/SoftwareSourceCode](https://schema.org/SoftwareSourceCode)** — For libraries / open-source code (XP.css, 98.css), schema.org has a separate SoftwareSourceCode type with codeRepository / programmingLanguage fields. We keep one `software` shape and let the product's url field carry the repo URL when applicable.
- **[Wikidata Q7397 (software)](https://www.wikidata.org/wiki/Q7397)** — Wikidata software entities use P348 (software version identifier), P178 (developer) ≈ our manufacturer/creator, P306 (operating system) ≈ our runtimePlatform, and P2669 (discontinued date) — inherited from product. Cross-reference identity rather than direct field alignment.
