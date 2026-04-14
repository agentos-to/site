---
title: platform
description: "A service that users interact with — Amazon, Gmail, Reddit, WhatsApp."
sidebar:
  label: platform
---

A service that users interact with — Amazon, Gmail, Reddit, WhatsApp.
Extends software (which extends product). A platform has accounts,
produces data, and is the context for entity identity.

Not all skills connect to platforms — some connect to plain software
or products. The "platform" tag is for services that host user data.

Example sources: seeded by skills at load time

| Metadata | Value |
|---|---|
| **Plural** | `platforms` |
| **Subtitle field** | `website` |
| **Identity** | `website` |
| **Also** | [`software`](/docs/shapes/reference/software/) |

## Fields

| Field | Type |
|---|---|
| `website` | `url` |
| `platformType` | `string` |

## Inherited

From [`software`](/docs/shapes/reference/software/):

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
| `license` | `string` |
| `novaGroup` | `integer` |
| `nutritionScore` | `string` |
| `openSource` | `boolean` |
| `originalPrice` | `string` |
| `originalPriceAmount` | `number` |
| `platform` | `string[]` |
| `price` | `string` |
| `priceAmount` | `number` |
| `quantity` | `integer` |
| `repositoryUrl` | `url` |
| `servingSize` | `string` |
| `sku` | `string` |
| `soldByWeight` | `boolean` |
| `version` | `string` |
| `weight` | `string` |
| `weightUnit` | `string` |
| `weightValue` | `number` |

| Relation | Target |
|---|---|
| `brand` | [`brand`](/docs/shapes/reference/brand/) |
| `developer` | [`organization`](/docs/shapes/reference/organization/) |
| `manufacturer` | [`organization`](/docs/shapes/reference/organization/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |
| `tagged` | [`tag[]`](/docs/shapes/reference/tag/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/SoftwareApplication](https://schema.org/SoftwareApplication)** — Our website ≈ url; platformType ≈ applicationCategory.
- **[schema.org/WebSite](https://schema.org/WebSite)** — A platform often IS a website. Our website field is canonical identity — matches schema.org's url/sameAs.
