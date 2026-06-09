---
title: persona
description: "An archetype of an audience segment — a named, hypothetical user that"
sidebar:
  label: persona
---

An archetype of an audience segment — a named, hypothetical user that
stands in for a real cohort. Invented in UX by Alan Cooper. NOT a real
human (that is `person`); a persona specializes an audience. Used in
product/UX design, marketing segmentation, service design.

| Metadata | Value |
|---|---|
| **Plural** | `personas` |
| **Subtitle field** | `headline` |

## Fields

| Field | Type |
|---|---|
| `headline` | `string` |
| `who` | `text` |
| `goals` | `string[]` |
| `painPoints` | `string[]` |
| `reachesFor` | `text` |
| `quote` | `text` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Alan Cooper, "The Inmates Are Running the Asylum" (1999)](https://www.nngroup.com/articles/persona/)** — Origin of the persona method — "a precise definition of our user and what he wishes to accomplish"; a hypothetical archetype, not a real person. Maps to role + who + goals + quote.
- **[schema.org/PeopleAudience](https://schema.org/PeopleAudience)** — A persona is a narrative archetype OF an audience; it specializes Audience (audienceType) but adds goals/quote that schema.org lacks — and is firmly distinct from `person` (a real human).
- **[Nielsen Norman Group — personas](https://www.nngroup.com/articles/persona/)** — Canonical UX template — role + goals + pain points + quote, grounded in field research.
