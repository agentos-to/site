---
title: highlight
description: "A personal extraction from a source — a passage you highlighted, annotated,"
sidebar:
  label: highlight
---

A personal extraction from a source — a passage you highlighted, annotated,
or saved. Different from a quote: a highlight is YOUR selection from a work.
A quote is a canonical attribution to a speaker.

| Metadata | Value |
|---|---|
| **Plural** | `highlights` |

## Fields

| Field | Type |
|---|---|
| `position` | `string` |
| `color` | `string` |

## Relations

| Relation | Target |
|---|---|
| `extractedFrom` | [`book`](/shapes/reference/book/) |
| `createdBy` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/)** — Our extractedFrom = target; createdBy = creator; position ≈ TextPositionSelector/TextQuoteSelector; color ≈ rendering preference.
- **[Hypothes.is annotation schema](https://h.readthedocs.io/en/latest/api-reference/)** — Practical W3C-compatible implementation. Our highlight is shaped like a Hypothes.is annotation minus the body text.
- **[Readwise Reader API](https://readwise.io/reader_api)** — Practical source. Our color/position come directly from Readwise's highlight export.
