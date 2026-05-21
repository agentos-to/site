---
title: font
description: "A typeface — the family-level work. One node per font family"
sidebar:
  label: font
---

A typeface — the family-level work. One node per font family
("Trebuchet MS", "Inter", "MS Sans Serif"); weights, styles, and file
formats are array fields on this node, not separate nodes (FRBR Work
level only for v1).

A font is a creative_work (its designer, publisher, license, dates
come from there) but NOT a file — the family is an abstract typeface
design; individual files (Trebuchet-Bold.woff2) are FRBR
Manifestations that we don't model as separate nodes.

| Metadata | Value |
|---|---|
| **Plural** | `fonts` |
| **Subtitle field** | `author` |
| **Identity (any)** | `family`, `postscriptName` |
| **Also** | [`creative_work`](/shapes/reference/creative_work/) |

## Fields

| Field | Type |
|---|---|
| `family` | `string` |
| `genericFamily` | `string` |
| `postscriptName` | `string` |
| `weights` | `integer[]` |
| `styles` | `string[]` |
| `formats` | `string[]` |
| `scripts` | `string[]` |
| `glyphCount` | `integer` |
| `designerUrl` | `string` |
| `vendorUrl` | `string` |
| `licenseInfoUrl` | `string` |

## Inherited

From [`creative_work`](/shapes/reference/creative_work/):

| Field | Type |
|---|---|
| `copyrightYear` | `integer` |
| `coverage` | `string` |
| `dateCreated` | `date` |
| `description` | `string` |
| `language` | `string` |
| `license` | `string` |
| `tags` | `string[]` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Typeface](https://schema.org/Typeface)** — Schema.org added Typeface in 2024. Sparse compared to OpenType (fontFamily, format only) — we lean on the OpenType `name` table for most fields.
- **[OpenType `name` table (ISO/IEC 14496-22)](https://learn.microsoft.com/en-us/typography/opentype/spec/name)** — nameID 1=family; 6=postscriptName; 8=manufacturer (publisher in our model, via creative_work); 9=designer (author via creative_work); 13=licenseDescription (license via creative_work); 14=licenseInfoUrl; 11=vendorUrl; 12=designerUrl. Our font shape is a graph-native projection of this table; .woff2 metadata can round-trip losslessly.
- **[Google Fonts metadata](https://fonts.google.com/specimen/Roboto)** — Treats fonts as "families" with weights / styles arrays. Same model we adopt. Google Fonts also tracks subsets (Latin / Cyrillic / Greek) — equivalent to our scripts field.
- **[ISO 15924 (script codes)](https://www.unicode.org/iso15924/iso15924-codes.html)** — Our scripts field uses ISO 15924 four-letter codes (Latn / Cyrl / Grek / Arab / Hans / Hant / Jpan / Kore / etc.). Canonical identification of writing systems.
