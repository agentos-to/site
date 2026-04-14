---
title: highlight
description: "A personal extraction from a source — a passage you highlighted, annotated,"
sidebar:
  label: highlight
---

A personal extraction from a source — a passage you highlighted, annotated,
or saved. Different from a quote: a highlight is YOUR selection from a work.
A quote is a canonical attribution to a speaker.

Example sources: Goodreads (highlights), future Kindle/Readwise/Hypothesis integration

| | |
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
| `extractedFrom` | [`book`](/docs/reference/shapes/book/) |
| `createdBy` | [`person`](/docs/reference/shapes/person/) |
