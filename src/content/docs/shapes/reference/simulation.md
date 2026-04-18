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
| `primaryMemex` | [`memex`](/shapes/reference/memex/) |
| `mountedMemex` | [`memex[]`](/shapes/reference/memex/) |
| `agent` | [`agent`](/shapes/reference/agent/) |
| `tether` | [`hardware`](/shapes/reference/hardware/) |
| `forkedFrom` | [`simulation`](/shapes/reference/simulation/) |
| `startedBy` | [`person`](/shapes/reference/person/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OpenTelemetry Traces (root span + attributes)](https://opentelemetry.io/docs/concepts/signals/traces/)** — Span-shaped observation of an agent run. Our startedAt/endedAt/ actionCount/writeCount ≈ span attributes; status ≈ span status.
- **[QEMU / VM snapshots](https://qemu-project.gitlab.io/qemu/system/images.html)** — "Disk image vs. VM" metaphor is direct. Our primaryMemex ≈ writable disk; mountedMemex[] ≈ read-only overlays; forkedFrom ≈ snapshot-based fork.
- **[Kubernetes Pod + Volume mounts](https://kubernetes.io/docs/concepts/workloads/pods/)** — Our tether (hardware kill-switch) ≈ Pod security context; mountedMemex[] ≈ ConfigMap/PVC read-only mounts.
