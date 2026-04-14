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

| Metadata | Value |
|---|---|
| **Plural** | `software` |
| **Subtitle field** | `text` |
| **Identity** | `url` |
| **Also** | [`product`](/docs/shapes/reference/product/) |

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
| `developer` | [`organization`](/docs/shapes/reference/organization/) |
| `repository` | [`repository`](/docs/shapes/reference/repository/) |

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
| `manufacturer` | [`organization`](/docs/shapes/reference/organization/) |
| `tagged` | [`tag[]`](/docs/shapes/reference/tag/) |

## Used as a base by

- [`platform`](/docs/shapes/reference/platform/)
