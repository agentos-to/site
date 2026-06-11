---
title: flow
description: "A process / swim-lane — actors across ordered steps. The universal shape"
sidebar:
  label: flow
---

A process / swim-lane — actors across ordered steps. The universal shape
for any multi-actor procedure: a business process, a user journey, an
onboarding, a recipe, a build pipeline. Steps are their own `step` nodes
(ordering needs an explicit position — schema.org/HowToStep warns markup
order is insufficient; BPMN orders via sequence flow).

| Metadata | Value |
|---|---|
| **Plural** | `flows` |
| **Subtitle field** | `goal` |

## Fields

| Field | Type |
|---|---|
| `goal` | `text` |
| `trigger` | `string` |
| `status` | `string` |

## Relations

| Relation | Target |
|---|---|
| `involves` | `node[]` |
| `has_step` | [`step[]`](/shapes/reference/step/) |
| `serves` | `node[]` |
| `produces` | `node` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[BPMN 2.0 (OMG)](https://www.omg.org/spec/BPMN/2.0/)** — Pools/lanes = actors; SequenceFlow imposes step order; the lane a step sits in assigns its actor.
- **[schema.org/HowTo](https://schema.org/HowTo)** — HowTo = a flow; its steps are HowToStep items; HowTo.result ≈ goal.
- **[UML Activity Diagram (activity partitions)](https://www.uml-diagrams.org/activity-diagrams.html)** — Activity partitions are the formal name for swim-lanes; actions are ordered by control flow.
