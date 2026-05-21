---
title: creative_work
description: "A creative work — the abstract level of FRBR's Work tier. Anything"
sidebar:
  label: creative_work
---

A creative work — the abstract level of FRBR's Work tier. Anything
with an author and a license belongs here (or extends here via `also`).
Books, photographs, fonts, music compositions, sculptures — all
creative works.

AgentOS uses this shape to attribute every asset a theme bundles, so
contributors (designers, photographers, composers) survive the asset's
journey into the graph. A theme bundles fonts; the fonts are
creative_works; their designers are persons; the chain of attribution
is queryable.

Work-level only for v1 — FRBR's Expression / Manifestation / Item tiers
(the "Bold Italic" cut, the .woff2 file, the specific copy on disk) are
represented today as array fields on subtype shapes (font.weights,
font.formats) rather than separate nodes. Re-evaluate when font family
pickers or per-file provenance ship.

| Metadata | Value |
|---|---|
| **Plural** | `creative_works` |
| **Subtitle field** | `written_by` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `description` | `string` |
| `license` | `string` |
| `copyrightYear` | `integer` |
| `datePublished` | `date` |
| `dateCreated` | `date` |
| `url` | `string` |
| `language` | `string` |
| `coverage` | `string` |
| `tags` | `string[]` |

## Used as a base by

- [`book`](/shapes/reference/book/)
- [`font`](/shapes/reference/font/)
- [`icon`](/shapes/reference/icon/)
- [`image`](/shapes/reference/image/)
- [`sound`](/shapes/reference/sound/)
- [`video`](/shapes/reference/video/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/CreativeWork](https://schema.org/CreativeWork)** — Our name=name; written_by≈author; published_by≈publisher; datePublished=datePublished; license=license; copyrightHolder= copyrightHolder; copyrightYear=copyrightYear; description= description; url=url; language=inLanguage; tags=keywords.
- **[Dublin Core Metadata Element Set (ISO 15836)](https://www.dublincore.org/specifications/dublin-core/dces/)** — Maps cleanly to all 15 DC elements except `type` (carried by the shape discriminator), `format` (subtype-specific), `identifier` (universal node id), `relation` (graph links), `subject` (tags).
- **[FRBR (IFLA, 1998)](https://www.ifla.org/files/assets/cataloguing/frbr/frbr.pdf)** — creative_work corresponds to FRBR's Work tier (the abstract intellectual creation). Expression / Manifestation / Item not modeled in v1; subtype shapes carry equivalents as array fields (font.weights, font.formats).
