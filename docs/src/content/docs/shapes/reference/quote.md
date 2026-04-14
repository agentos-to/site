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

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `list_quotes`
