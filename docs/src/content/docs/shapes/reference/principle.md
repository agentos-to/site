---
title: principle
description: "A guiding bright-line — a value or rule used to judge edge cases. Universal:"
sidebar:
  label: principle
---

A guiding bright-line — a value or rule used to judge edge cases. Universal:
design principles, engineering laws, organizational values, ethical
principles, architectural decision drivers. Anyone can hold principles.
The `rationale` is what lets a future reader apply it to a case it never
named — the reasoning, not just the rule.

| Metadata | Value |
|---|---|
| **Plural** | `principles` |
| **Subtitle field** | `domain` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `statement` | `text` |
| `rationale` | `text` |
| `domain` | `string` |
| `status` | `string` |

## Relations

| Relation | Target |
|---|---|
| `held_by` | [`actor`](/shapes/reference/actor/) |
| `supersedes` | [`principle`](/shapes/reference/principle/) |
| `conflicts_with` | [`principle[]`](/shapes/reference/principle/) |
| `governs` | `node` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[principles.design](https://principles.design/)** — 1600+ principles modeled as name + statement + elaboration, grouped into named collections → name / statement / rationale.
- **[MADR (Markdown ADR) — decision drivers](https://adr.github.io/madr/)** — Decision drivers are principles applied to a choice; the status enum (proposed/accepted/deprecated/superseded) → status + supersedes.
- **[GOV.UK Design Principles](https://www.gov.uk/guidance/government-design-principles)** — Canonical 10-principle collection — each principle is an imperative statement + worked examples.
