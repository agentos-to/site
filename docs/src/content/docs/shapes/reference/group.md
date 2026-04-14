---
title: group
description: "A group or community — online group, reading group, etc."
sidebar:
  label: group
---

A group or community — online group, reading group, etc.

| Metadata | Value |
|---|---|
| **Plural** | `groups` |
| **Subtitle field** | `category` |
| **Identity** | `platform`, `id` |

## Fields

| Field | Type |
|---|---|
| `memberCount` | `integer` |
| `category` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/Group (via Organization/memberOf)](https://schema.org/Organization)** — schema.org models groups as Organization. Our memberCount ≈ numberOfEmployees loosely; category ≈ naics/knowsAbout.
- **[FOAF Group](http://xmlns.com/foaf/spec/#term_Group)** — Foundational social-graph vocabulary. foaf:member populates membership; category has no direct FOAF peer.

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `list_groups`
