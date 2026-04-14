---
title: simulation
description: "A simulation — an isolated runtime where an agent runs. The 'VM'"
sidebar:
  label: simulation
---

A simulation — an isolated runtime where an agent runs. The "VM"
to a memex's "disk image." Loads a memex, applies governor rules,
and runs an agent in a controlled environment.

Simulations provide isolation: writes go to a fork overlay, not the
original memex. The user reviews changes and merges selectively —
like a pull request for your knowledge graph.

Examples: research-agent (forked joe.db + astronomy.db read-only),
legal-review (forked joe.db + law.db read-only)

| Metadata | Value |
|---|---|
| **Plural** | `simulations` |
| **Subtitle field** | `status` |

## Fields

| Field | Type |
|---|---|
| `status` | `string` |
| `profile` | `string` |
| `task` | `text` |
| `graphMode` | `string` |
| `startedAt` | `datetime` |
| `endedAt` | `datetime` |
| `actionCount` | `integer` |
| `writeCount` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `primaryMemex` | [`memex`](/docs/reference/shapes/memex/) |
| `mountedMemex` | [`memex[]`](/docs/reference/shapes/memex/) |
| `agent` | [`agent`](/docs/reference/shapes/agent/) |
| `tether` | [`hardware`](/docs/reference/shapes/hardware/) |
| `forkedFrom` | [`simulation`](/docs/reference/shapes/simulation/) |
| `startedBy` | [`person`](/docs/reference/shapes/person/) |
