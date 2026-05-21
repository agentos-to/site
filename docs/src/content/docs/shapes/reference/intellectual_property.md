---
title: intellectual_property
description: "A registered or pending intellectual-property right — a trademark,"
sidebar:
  label: intellectual_property
---

A registered or pending intellectual-property right — a trademark,
patent, registered design, or registered copyright. The unifying
primitive for "an exclusive, jurisdiction-bound legal right in an
intangible, held by an actor and granted by an IP office."

One shape, not many — `category` discriminates (Wikidata models
trademark / patent / design as siblings under `intellectual property
right`; WIPO ST.96 splits the schema by Trademark / Patent / Design
Components but the *right* is one concept).

NOT a `creative_work`: a creative_work is the authored intangible
itself (the book, the font, the logo-as-artwork). An
intellectual_property node is the *legal right over* an intangible.
A logo can be both — a creative_work node AND the subject of an
intellectual_property node — wired by an link, never by `also`.

NOT a `qualification`: a qualification attests to a person's
competency. An IP right attests to nothing and is held by an org as
readily as a person. Sibling nouns, no `also` between them.

Lifecycle (filed -> examined -> published -> allowed -> registered ->
renewed) is N distinct-verb dated milestone links to the granting
office, NOT fields on the node (events-as-links rule 1). The node
carries only intrinsic, current-state facts. `status` is the current
stage; the milestone links carry the dated history.

`name` (inherited) is the display label — "ADAVIA (trademark)".

| Metadata | Value |
|---|---|
| **Plural** | `intellectual_properties` |
| **Subtitle field** | `category` |
| **Identity (any)** | `identifier` |

## Fields

| Field | Type |
|---|---|
| `category` | `string` |
| `mark` | `string` |
| `identifier` | `string` |
| `register` | `string` |
| `status` | `string` |
| `filingBasis` | `string` |
| `niceClass` | `integer[]` |
| `validIn` | `string` |
| `renewalPeriod` | `string` |
| `verificationUrl` | `url` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Wikidata — trademark (Q167270) / registered trademark (Q111048186)](https://www.wikidata.org/wiki/Q167270)** — Trademark is a subclass of `intellectual property right` and of `mark`; holder via `owned by` (P127). registered-vs-pending is a status of one type, not a separate type — our `status` field.
- **[WIPO Standard ST.96 — Trademark Components](https://www.wipo.int/standards/en/st96/v8-0/release_notes.html)** — Canonical IP-office XML model. Source for mark, identifier, register, niceClass, status. Splits schemas by Trademark / Patent / Design Components — confirms `category` as the discriminator across one `intellectual_property` concept.
- **[WIPO Standard ST.87 — IP event codes](https://www.wipo.int/standards/en/)** — Standard lifecycle-event vocabulary (KeyEventCode). The filed/published/granted/lapsed milestones are dated links to the granting office, not node fields — events-as-links rule 1.
- **[Nice Classification (Nice Agreement 1957; NCL 13-2026)](https://www.wipo.int/en/web/classification-nice)** — 45-class system (1-34 goods, 35-45 services). `niceClass` is an integer[] of class numbers — a standard code. ADAVIA is Class 42.
- **[USPTO — trademark process & intent-to-use basis](https://www.uspto.gov/trademarks/basics/trademark-process)** — Lifecycle and the use-vs-intent-to-use fork. Source for the `status` value set and `filingBasis`.
- **[schema.org/Intangible, schema.org/Brand](https://schema.org/Intangible)** — Weak alignment — schema.org has no Trademark type; `Brand` is the marketing concept, not the legal right. Cited to mark the gap web ontologies leave: the IP right needs its own shape.
