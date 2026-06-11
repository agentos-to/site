---
title: step
description: "One ordered act within a flow. A first-class node, not an array slot:"
sidebar:
  label: step
---

One ordered act within a flow. A first-class node, not an array slot:
schema.org warns markup order is insufficient — order rides on `position`
(and an optional `next` edge); the actor is the swim-lane the step sits in.

| Metadata | Value |
|---|---|
| **Plural** | `steps` |
| **Subtitle field** | `status` |

## Fields

| Field | Type |
|---|---|
| `position` | `integer` |
| `detail` | `text` |
| `status` | `string` |

## Relations

| Relation | Target |
|---|---|
| `part_of` | [`flow`](/shapes/reference/flow/) |
| `next` | [`step`](/shapes/reference/step/) |
| `performed_by` | `node` |
| `happens_in` | [`module`](/shapes/reference/module/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/HowToStep](https://schema.org/HowToStep)** — A step is its own type with a `position` Integer + nextItem/previousItem; schema.org states markup order alone is insufficient for ordering.
- **[BPMN 2.0 SequenceFlow](https://www.omg.org/spec/BPMN/2.0/)** — Order is an explicit SequenceFlow edge between activity nodes → the `next` edge; the actor is lane membership.
