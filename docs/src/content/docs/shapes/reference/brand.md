---
title: brand
description: "A consumer brand — a named, visual, commercial identity. Often (but not"
sidebar:
  label: brand
---

A consumer brand — a named, visual, commercial identity. Often (but not
always) coincident with an organization: United Airlines IS a brand, the
company IS the brand, they share a wordmark. When renderers need to show
a brand on screen (badges, headers on itinerary PDFs, tiles in a trip
list), this is where the visual identity lives.

Brand is a mixin. `airline` says `also: [organization, brand]` so an
airline node carries both operational metadata (iataCode, alliance) and
visual metadata (primaryColor, logo). Hotels, rental agencies, and
restaurants should do the same.

Color fields use the same hex-with-hash format used elsewhere in the
workspace (`#002244`), matching skill-frontmatter color and CSS hex.
Wikidata's P465 "hex color code" uses the same format without the hash,
but we keep the hash for parity with CSS and the skill-frontmatter
convention; renderers can strip it if they need raw hex.

| Metadata | Value |
|---|---|
| **Plural** | `brands` |
| **Subtitle field** | `tagline` |
| **Identity** | `url` |

## Fields

| Field | Type |
|---|---|
| `tagline` | `string` |
| `founded` | `datetime` |
| `country` | `string` |
| `primaryColor` | `string` |
| `textColor` | `string` |

## Relations

| Relation | Target |
|---|---|
| `ownedBy` | [`organization`](/shapes/reference/organization/) |
| `website` | [`website`](/shapes/reference/website/) |
| `logo` | [`image`](/shapes/reference/image/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Brand](https://schema.org/Brand)** — Our tagline ≈ slogan; founded = foundingDate; ownedBy ≈ parentOrganization (on the owning Organization); logo = logo. schema.org doesn't model color on Brand; that's a Wikidata extension.
- **[Wikidata (Brand, Q431289)](https://www.wikidata.org/wiki/Q431289)** — Cross-reference identity for dedupe. country maps to P17 (country); founded to P571 (inception); ownedBy to P127 (owned by); primaryColor ≈ P465 "hex color code" (Wikidata stores without the "#" prefix — we include it to match CSS and our skill-frontmatter convention).
- **[Apple PassKit pkpass](https://developer.apple.com/documentation/walletpasses)** — Wallet passes carry backgroundColor / foregroundColor / labelColor — three-color palette aligned with our primaryColor / textColor. We ship two here (pairing primary with its paired text color) and defer the third until a renderer needs it. An itinerary PDF can derive a "label" color from a lighter tint of textColor at render time if needed, rather than fixing it at the data layer.
- **[Material Design 3 — dynamic color roles](https://m3.material.io/styles/color/roles)** — Material's palette has paired slots (`primary` / `onPrimary`; `secondary` / `onSecondary`; `surface` / `onSurface`). Our primaryColor/textColor follows the primary/onPrimary pairing. Secondary tiers are deferred until renderers actually need them.
