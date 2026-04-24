---
title: book
description: "A book. Books are also products, so they inherit price/brand fields."
sidebar:
  label: book
---

A book. Books are also products, so they inherit price/brand fields.
User-specific state (rating, shelf, dates) and platform metrics are modeled as edge values.

| Metadata | Value |
|---|---|
| **Plural** | `books` |
| **Subtitle field** | `author` |
| **Identity (any)** | `isbn13`, `isbn` |
| **Also** | [`product`](/shapes/reference/product/) |

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
| `writtenBy` | [`person`](/shapes/reference/person/) |
| `contributors` | [`person[]`](/shapes/reference/person/) |
| `publisher` | [`organization`](/shapes/reference/organization/) |

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
| `brand` | [`brand`](/shapes/reference/brand/) |
| `manufacturer` | [`organization`](/shapes/reference/organization/) |
| `tagged` | [`tag[]`](/shapes/reference/tag/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Book](https://schema.org/Book)** — Our isbn maps to isbn; writtenBy = author; publisher matches; pages = numberOfPages; language = inLanguage; format ≈ bookFormat (Hardcover/Paperback/EBook).
- **[ONIX for Books 3.0](https://www.editeur.org/83/Overview/)** — Publishing-industry canonical. Our isbn/isbn13/pages/format/language/series/originalTitle align with ONIX Product Identifier, Extent, ProductForm, Language, Collection, and OriginalLanguageTitle composites.
- **[Open Library Books API](https://openlibrary.org/developers/api)** — Practical lookup by ISBN. Our genres/characters/places/awardsWon map to subjects/subject_people/subject_places/subject_times (awards less standardized).

## Skills that produce this shape

- [goodreads](/skills/reference/media/goodreads/) — `get_book`, `list_similar_books`, `list_series_books`, `search_books`, `list_author_books`, `list_books`, `list_shelf_books`
