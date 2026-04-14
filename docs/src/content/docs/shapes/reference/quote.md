---
title: quote
description: "A notable quote. Attribution is a graph relationship, not a field —"
sidebar:
  label: quote
---

A notable quote. Attribution is a graph relationship, not a field —
a document --contains--> the quote, a person --authored--> the document.
The provenance chain IS the attribution. No spokenBy needed.

Freeform edges handle everything:
document/book/article --contains--> quote
person --attributed--> quote (when we know who said it)
quote --inspired--> anything

Example sources: Goodreads, RFCs, papers, talks, podcasts, interviews

| Metadata | Value |
|---|---|
| **Plural** | `quotes` |

## Fields

| Field | Type |
|---|---|
| `context` | `string` |
| `year` | `integer` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Quotation](https://schema.org/Quotation)** — Our context ≈ about; year ≈ datePublished. schema.org models spokenByCharacter/creator — we model attribution via graph edges instead.
- **[Wikiquote data model](https://en.wikiquote.org/wiki/Help:Sources)** — Practical canonical quote source. Our provenance-via-edges (document --contains--> quote --attributedTo--> person) matches Wikiquote's source-citation discipline.

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `list_quotes`
