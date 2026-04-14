---
title: book
description: "A book. Books are also products, so they inherit price/brand fields."
sidebar:
  label: book
---

A book. Books are also products, so they inherit price/brand fields.
User-specific state (rating, shelf, dates) and platform metrics are modeled as edge values.

Example sources: Goodreads

| Metadata | Value |
|---|---|
| **Plural** | `books` |
| **Subtitle field** | `author` |
| **Identity** | `isbn13`, `isbn` |
| **Also** | [`product`](/docs/shapes/reference/product/) |

## Fields

| Field | Type |
|---|---|
| `isbn` | `string` |
| `isbn13` | `string` |
| `pages` | `integer` |
| `genres` | `string[]` |
| `series` | `string` |
| `format` | `string` |
| `language` | `string` |
| `originalTitle` | `string` |
| `places` | `string[]` |
| `characters` | `string[]` |
| `awardsWon` | `string[]` |

## Relations

| Relation | Target |
|---|---|
| `writtenBy` | [`person`](/docs/shapes/reference/person/) |
| `contributors` | [`person[]`](/docs/shapes/reference/person/) |
| `publisher` | [`organization`](/docs/shapes/reference/organization/) |

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

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `get_book`
- [goodreads](/docs/skills/reference/media/goodreads/) — `list_similar_books`, `list_series_books`, `search_books`, `list_author_books`, `list_books`, `list_shelf_books`
