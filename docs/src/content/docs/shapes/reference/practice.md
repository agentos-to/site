---
title: practice
description: "A field of practice or study — a discipline a person practices, or the"
sidebar:
  label: practice
---

A field of practice or study — a discipline a person practices, or the
body of knowledge a qualification is in. Deliberately broad: it spans
professional disciplines (Orthopaedic Surgery, Civil Engineering,
Intellectual Property Law), academic fields of study (Diagnostic
Radiology), and personal practices (yoga, authentic relating,
meditation). If a person *does* it as a practiced thing, it is one.

One shape, on purpose. The standards keep separate code registries —
NUCC for medical specialties, SOC for occupations, ISCED-F for fields
of study — but those are authority registries, not concepts.
"Diagnostic Radiology" is one thing: a person practices it and a
degree is in it. One node; the optional `code` / `codeSystem` record
which registry classifies it, when one does (yoga has no NUCC code).

Hierarchical via a self-referential `parent` link — "Foot & Ankle" is
a sub-practice of "Orthopaedic Surgery", "Hatha Yoga" of "Yoga". Depth
is emergent; there is no level field.

`name` (inherited) is the display label — "Orthopaedic Surgery".

| Metadata | Value |
|---|---|
| **Plural** | `practices` |
| **Subtitle field** | `parent` |

## Fields

| Field | Type |
|---|---|
| `description` | `text` |
| `code` | `string` |
| `codeSystem` | `string` |
| `aliases` | `string[]` |

## Relations

| Relation | Target |
|---|---|
| `specialization_of` | [`practice`](/shapes/reference/practice/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[NUCC Health Care Provider Taxonomy](https://www.nucc.org/index.php/code-sets-mainmenu-41/provider-taxonomy-mainmenu-40)** — US medical-specialty code set — 3 levels (Grouping / Classification / Specialization), 10-char alphanumeric codes. The source for codeSystem=NUCC and for the parent-link hierarchy.
- **[Standard Occupational Classification (SOC) / O*NET-SOC](https://www.bls.gov/soc/)** — US occupational taxonomy spanning every profession — 4 levels (Major / Minor / Broad / Detailed). codeSystem=SOC.
- **[ISCED Fields of Education and Training 2013 (ISCED-F)](https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/international-standard-classification-education-fields-education-and)** — UNESCO field-of-study taxonomy — 3 levels (Broad / Narrow / Detailed). The field-of-study side, for a qualification's `field`.
- **[schema.org CategoryCode / occupationalCategory](https://schema.org/occupationalCategory)** — schema.org has no dedicated discipline type — only the pluggable CategoryCode (codeValue + inCodeSet). Confirms code + codeSystem as a loose optional pair, not a hard taxonomy dependency.
