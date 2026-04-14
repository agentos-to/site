---
title: software
description: "A software application — web app, desktop app, mobile app, CLI tool."
sidebar:
  label: software
---

A software application — web app, desktop app, mobile app, CLI tool.
Software is also a product, but with additional fields for platforms,
versions, and runtime requirements.

Examples: Gmail, Cursor, Slack, yt-dlp, agentOS itself

| | |
|---|---|
| **Plural** | `software` |
| **Subtitle field** | `text` |
| **Identity** | `url` |
| **Also** | [`product`](/docs/reference/shapes/product/) |

## Fields

| Field | Type |
|---|---|
| `version` | `string` |
| `license` | `string` |
| `platform` | `string[]` |
| `openSource` | `boolean` |
| `repositoryUrl` | `url` |

## Relations

| Relation | Target |
|---|---|
| `developer` | [`organization`](/docs/reference/shapes/organization/) |
| `repository` | [`repository`](/docs/reference/shapes/repository/) |

## Inherited

From [`product`](/docs/reference/shapes/product/):

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
| `brand` | [`brand`](/docs/reference/shapes/brand/) |
| `manufacturer` | [`organization`](/docs/reference/shapes/organization/) |
| `tagged` | [`tag[]`](/docs/reference/shapes/tag/) |

## Used as a base by

- [`platform`](/docs/reference/shapes/platform/)
