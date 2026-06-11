---
title: module
description: "A self-contained unit of a larger whole — a software module, a course"
sidebar:
  label: module
---

A self-contained unit of a larger whole — a software module, a course
module, a hardware component, a curriculum unit. Defined by what it
encapsulates and what it depends on. The universal part-of-a-system shape.

| Metadata | Value |
|---|---|
| **Plural** | `modules` |
| **Subtitle field** | `role` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `role` | `text` |
| `path` | `string` |
| `version` | `string` |
| `status` | `string` |
| `planned` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `part_of` | `node` |
| `has_part` | [`module[]`](/shapes/reference/module/) |
| `depends_on` | [`module[]`](/shapes/reference/module/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org hasPart / isPartOf (Course modules)](https://schema.org/hasPart)** — Course.hasPart models course modules; hasPart/isPartOf are the inverse composition edges, reusable for any whole/part.
- **[UML 2.5 Component (OMG)](https://www.uml-diagrams.org/component.html)** — A component is a "modular part with encapsulated content, replaceable within its environment" → role + depends_on.
- **[SPDX Package](https://spdx.dev/)** — A package is a versioned, named unit with declared dependencies → version + depends_on, across software and hardware domains.
