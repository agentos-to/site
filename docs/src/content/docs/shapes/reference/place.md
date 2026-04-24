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

| Metadata | Value |
|---|---|
| **Plural** | `places` |
| **Subtitle field** | `fullAddress` |
| **Identity (any)** | `googlePlaceId`, `mapboxId` |

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
| `eta` | `string` |
| `isOrderable` | `boolean` |
| `closedMessage` | `string` |
| `productCount` | `integer` |
| `mapboxId` | `string` |
| `wikidataId` | `string` |
| `googlePlaceId` | `string` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `brand` | [`organization`](/shapes/reference/organization/) |
| `offers` | [`product[]`](/shapes/reference/product/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Place + PostalAddress](https://schema.org/Place)** — Our latitude/longitude = geo.latitude/longitude; street/city/region/postalCode/countryCode map to PostalAddress streetAddress/addressLocality/addressRegion/postalCode/addressCountry; hours ≈ openingHoursSpecification; rating/reviewCount ≈ aggregateRating.
- **[Google Places API (Place resource)](https://developers.google.com/maps/documentation/places/web-service/reference/rest/v1/places)** — Practical POI schema. Our googlePlaceId = id; featureType/categories ≈ types/primaryType; businessStatus, priceLevel, rating match directly.
- **[GeoJSON (RFC 7946) + ISO 3166-1](https://datatracker.ietf.org/doc/html/rfc7946)** — Our latitude/longitude are a GeoJSON Point [lon, lat]; countryCode follows ISO 3166-1 alpha-2.

## Skills that produce this shape

- [uber](/skills/reference/logistics/uber/) — `get_store`, `search_address`, `list_addresses`, `search_stores`, `list_nearby_stores`
- [austin-boulder-project](/skills/reference/fitness/austin-boulder-project/) — `get_locations`
