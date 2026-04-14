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

Example sources: future PKM integrations (Obsidian, Apple Notes, Google Keep)

| | |
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
| `createdBy` | [`person`](/docs/reference/shapes/person/) |
| `references` | [`note[]`](/docs/reference/shapes/note/) |
| `extractedFrom` | [`webpage`](/docs/reference/shapes/webpage/) |
