---
title: note
description: "Private text content, primarily for the author. Journal entries, PKM notes,"
sidebar:
  label: note
---

Private text content, primarily for the author. Journal entries, PKM notes,
fleeting ideas, drafts. Notes have no engagement metrics, no platform, no
audience — they're yours.

A note can reference other notes (Zettelkasten-style linking) and can be
extracted from sources (literature notes from books, articles, videos).

| Metadata | Value |
|---|---|
| **Plural** | `notes` |

## Fields

| Field | Type |
|---|---|
| `noteType` | `string` |
| `isPinned` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `createdBy` | [`person`](/docs/shapes/reference/person/) |
| `references` | [`note[]`](/docs/shapes/reference/note/) |
| `extractedFrom` | [`webpage`](/docs/shapes/reference/webpage/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Zettelkasten / Luhmann slip-box](https://zettelkasten.de/overview/)** — Our noteType (fleeting/literature/permanent) is the canonical Zettelkasten triad; references[] ≈ Luhmann's permanent links.
- **[W3C Web Annotation Data Model](https://www.w3.org/TR/annotation-model/)** — Our extractedFrom = target; createdBy = creator. Notes are annotations without a structured position selector.
- **[Obsidian / Roam / Logseq PKM conventions](https://obsidian.md/)** — Practical PKM lineage. isPinned/noteType mirror the "pinned/daily/permanent" UX of modern note apps.
