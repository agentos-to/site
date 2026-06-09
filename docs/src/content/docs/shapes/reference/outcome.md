---
title: outcome
description: "A tracked target-state — the change being sought, with a status and"
sidebar:
  label: outcome
---

A tracked target-state — the change being sought, with a status and
(optionally) a metric that says when it's met. The universal unit of
"what we're trying to achieve": OKR objectives, learning outcomes,
clinical outcome measures, a roadmap end-state. NOT schema.org/result
("what an action emitted") — an outcome is a target you track over time.

| Metadata | Value |
|---|---|
| **Plural** | `outcomes` |
| **Subtitle field** | `status` |

## Fields

| Field | Type |
|---|---|
| `statement` | `text` |
| `status` | `string` |
| `archived` | `boolean` |
| `metric` | `string` |
| `baseline` | `string` |
| `current` | `string` |
| `target` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[John Doerr, "Measure What Matters" (OKR)](https://www.whatmatters.com/faqs/okr-meaning-definition-example)** — Objective → statement; Key Result → the metric/baseline/current/target quad ("I will X as measured by Y").
- **[W.K. Kellogg Foundation Logic Model Development Guide](https://www.nj.gov/state/assets/pdf/ofbi/kellogg-foundation-logic-model-development-guide.pdf)** — Outcomes as short/intermediate/long-term changes in a causal chain → the depends_on / advances edges.
- **[schema.org/AchieveAction + result](https://schema.org/AchieveAction)** — Closest schema.org neighbor, but `result` models what an action produced, not a tracked target-state — so outcome is its own type.
