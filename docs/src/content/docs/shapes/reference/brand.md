---
title: brand
description: "A consumer brand. Extracted from product listings."
sidebar:
  label: brand
---

A consumer brand. Extracted from product listings.

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

## Relations

| Relation | Target |
|---|---|
| `ownedBy` | [`organization`](/docs/shapes/reference/organization/) |
| `website` | [`website`](/docs/shapes/reference/website/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Brand](https://schema.org/Brand)** — Our tagline ≈ slogan; founded = foundingDate; ownedBy ≈ parentOrganization (on the owning Organization).
- **[Wikidata (Brand, Q431289)](https://www.wikidata.org/wiki/Q431289)** — Cross-reference identity for dedupe. country maps to P17 (country); founded to P571 (inception); ownedBy to P127 (owned by).
