---
title: book
description: "A book. Books are BOTH creative works (the intellectual work — its"
sidebar:
  label: book
---

A book. Books are BOTH creative works (the intellectual work — its
author, publisher, license, datePublished come from creative_work)
AND products (commercial books are sold; they inherit price / brand
/ lifecycle dates from product).
User-specific state (rating, shelf, dates) and platform metrics are modeled as link values.

| Metadata | Value |
|---|---|
| **Plural** | `books` |
| **Subtitle field** | `written_by` |
| **Identity (any)** | `isbn13`, `isbn` |
| **Also** | [`creative_work`](/shapes/reference/creative_work/) · [`product`](/shapes/reference/product/) |

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
| `contributed_by` | [`person[]`](/shapes/reference/person/) |

## Inherited

From [`creative_work`](/shapes/reference/creative_work/) · [`product`](/shapes/reference/product/):

| Field | Type |
|---|---|
| `aisle` | `string` |
| `availability` | `string` |
| `barcode` | `string` |
| `calories` | `number` |
| `categories` | `string[]` |
| `category` | `string` |
| `copyrightYear` | `integer` |
| `coverage` | `string` |
| `currency` | `string` |
| `customizationGroups` | `json` |
| `dateCreated` | `date` |
| `department` | `string` |
| `description` | `string` |
| `images` | `json` |
| `license` | `string` |
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
| `tags` | `string[]` |
| `weight` | `string` |
| `weightUnit` | `string` |
| `weightValue` | `number` |

| Relation | Target |
|---|---|
| `branded_as` | [`brand`](/shapes/reference/brand/) |
| `created_by` | [`actor[]`](/shapes/reference/actor/) |
| `held_by` | [`person`](/shapes/reference/person/) |
| `inspired_by` | [`product[]`](/shapes/reference/product/) |
| `manufactured_by` | [`organization`](/shapes/reference/organization/) |
| `published_by` | [`actor`](/shapes/reference/actor/) |
| `tagged_with` | [`tag[]`](/shapes/reference/tag/) |
| `written_by` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Book](https://schema.org/Book)** — Our isbn maps to isbn; writtenBy = author; publisher matches; pages = numberOfPages; language = inLanguage; format ≈ bookFormat (Hardcover/Paperback/EBook).
- **[ONIX for Books 3.0](https://www.editeur.org/83/Overview/)** — Publishing-industry canonical. Our isbn/isbn13/pages/format/language/series/originalTitle align with ONIX Product Identifier, Extent, ProductForm, Language, Collection, and OriginalLanguageTitle composites.
- **[Open Library Books API](https://openlibrary.org/developers/api)** — Practical lookup by ISBN. Our genres/characters/places/awardsWon map to subjects/subject_people/subject_places/subject_times (awards less standardized).

## Apps that produce this shape

- [goodreads](/apps/reference/media/goodreads/) — `get_book`, `list_similar_books`, `list_series_books`, `search_books`, `list_author_books`, `list_books`, `list_shelf_books`
