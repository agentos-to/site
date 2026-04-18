---
title: job
description: "A running or completed unit of work the engine is responsible for —"
sidebar:
  label: job
---

A running or completed unit of work the engine is responsible for —
an agent turn, a background sync, a scheduled task. The engine creates
one job per dispatched request and owns its full lifecycle: status,
kind, config, and boot epoch (for crash recovery across engine restarts).

Jobs are NOT tool invocations (see `tool_call`). A single job can issue
many tool calls; a tool call belongs to exactly one job via its parent
message.

| Metadata | Value |
|---|---|
| **Plural** | `jobs` |
| **Subtitle field** | `name` |
| **Identity** | `name`, `boot_epoch` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `status` | `string` |
| `kind` | `string` |
| `config` | `json` |
| `boot_epoch` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `produced` | [`conversation`](/shapes/reference/conversation/) |
| `requested_by` | [`account`](/shapes/reference/account/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[systemd unit — Active/Sub state machine](https://www.freedesktop.org/software/systemd/man/systemd.html#Concepts)** — Status mirrors systemd's active/sub state pairing — our "running" ≈ active+running, "completed" ≈ inactive+dead, "failed" ≈ failed+failed. boot_epoch plays the role of systemd's boot_id.
- **[Kubernetes Job (batch/v1)](https://kubernetes.io/docs/concepts/workloads/controllers/job/)** — Kubernetes Jobs model the same "run-once, report status, possibly resume" lifecycle. Our kind ≈ spec.template.spec.containers[].image; config ≈ spec.template.spec.
