---
title: shortcut
description: "A named alias that expands to a location URI at parse time."
sidebar:
  label: shortcut
---

A named alias that expands to a location URI at parse time.
Simple name -> target mappings. No patterns, no regex.
Built-in shortcuts (limbo, search, help, web, files) are seeded at boot.
Skills can register shortcuts (reddit, youtube, etc).
Users can create, modify, or delete any shortcut.

Structural input (URLs, domains, absolute paths) is handled by the normalizer
before shortcut lookup — shortcuts don't need pattern matching.

Example sources: boot seed, skill registration, user creation

| Metadata | Value |
|---|---|
| **Plural** | `shortcuts` |
| **Subtitle field** | `target` |
| **Identity** | `name` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `target` | `string` |
| `filter` | `string` |
| `builtin` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `skill` | [`skill`](/docs/shapes/reference/skill/) |
