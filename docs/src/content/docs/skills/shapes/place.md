---
title: place
description: "A physical location — address, building, city, or point of interest."
sidebar:
  label: place
---

A physical location — address, building, city, or point of interest.
Used for meeting locations, shipping addresses, store/restaurant locations,
headquarters, airports, etc.

Follows the Google Places / Mapbox model: a place IS the thing. A Costco
location is a place with feature_type "poi", hours, rating, and delivery.
The company (Costco Inc.) is an organization. The location is a place.

Example sources: Apple Calendar, Amazon (shipping), Mapbox (geocoding)

| Metadata | Value |
|---|---|
| **Plural** | `places` |
| **Subtitle field** | `fullAddress` |
| **Identity** | `googlePlaceId`, `mapboxId` |

## Fields

| Field | Type |
|---|---|
| `fullAddress` | `string` |
| `placeFormatted` | `string` |
| `streetNumber` | `string` |
| `street` | `string` |
| `neighborhood` | `string` |
| `locality` | `string` |
| `city` | `string` |
| `district` | `string` |
| `region` | `string` |
| `postalCode` | `string` |
| `country` | `string` |
| `countryCode` | `string` |
| `latitude` | `number` |
| `longitude` | `number` |
| `accuracy` | `string` |
| `featureType` | `string` |
| `categories` | `string[]` |
| `phone` | `string` |
| `website` | `url` |
| `hours` | `json` |
| `businessStatus` | `string` |
| `rating` | `number` |
| `reviewCount` | `integer` |
| `priceLevel` | `string` |
| `timezone` | `string` |
| `mapboxId` | `string` |
| `wikidataId` | `string` |
| `googlePlaceId` | `string` |

## Relations

| Relation | Target |
|---|---|
| `brand` | [`organization`](/docs/reference/shapes/organization/) |
| `offers` | [`product[]`](/docs/reference/shapes/product/) |

## Skills that produce this shape

- [uber](/docs/reference/skills/logistics/uber/) — `get_store`
- [uber](/docs/reference/skills/logistics/uber/) — `search_address`, `list_addresses`, `search_stores`, `list_nearby_stores`
