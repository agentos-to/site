---
title: subscription
description: "A standing subscription — a durable intent to stream live entities, re-armed on every engine boot."
sidebar:
  label: subscription
---

A standing subscription — a durable intent to stream live entities, re-armed on every engine boot.
The node stores WHICH app op arms the stream, never the artifact it
produces (hook JS regenerates fresh on every re-arm, so it can't go
stale on the graph). Engine boot reads these nodes and re-dispatches
each as a normal apps.run call.

One node per (app, op): subscribe upserts, close deletes, boot
reads-and-dispatches. The node row's own updated_at IS the armed-at
timestamp — no field duplicates it.

| Metadata | Value |
|---|---|
| **Plural** | `subscriptions` |
| **Subtitle field** | `target` |
| **Identity** | `app`, `op` |

## Fields

| Field | Type |
|---|---|
| `app` | `string` |
| `op` | `string` |
| `target` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[W3C WebSub subscriptions](https://www.w3.org/TR/websub/)** — A subscription is a stored intent (topic + callback) the hub re-delivers against — content never lives on the subscription. Our app/op ≈ topic/callback.
- **[MQTT persistent sessions](https://docs.oasis-open.org/mqtt/mqtt/v5.0/mqtt-v5.0.html)** — Subscriptions survive connection loss and re-attach on reconnect. Our engine-boot re-arm parallels session resumption.
- **[systemd unit enablement (systemctl enable)](https://www.freedesktop.org/software/systemd/man/systemctl.html)** — Enablement is a durable on-disk fact distinct from the running process; boot re-creates the runtime state from it. Our node ≈ the wants/ symlink, the live CDP hook ≈ the running unit.
