---
title: app
description: "A graphical app (TS/React) that runs on top of the engine — browser,"
sidebar:
  label: app
---

A graphical app (TS/React) that runs on top of the engine — browser,
mail, wallet, agent inbox, etc. Distinct from `skill` (Python adapters
with no UI) and `software` (third-party apps we connect to).

The engine reads app manifests from configured sources at boot and
upserts an `app` node for each. Apps declare the shapes they render
via `entity_types` and either take over the shell (`standalone`) or
nest inside another app (`standalone: false`).

| Metadata | Value |
|---|---|
| **Plural** | `apps` |
| **Subtitle field** | `description` |
| **Identity** | `id` |

## Fields

| Field | Type |
|---|---|
| `id` | `string` |
| `app_id` | `string` |
| `standalone` | `boolean` |
| `description` | `string` |
| `entity_types` | `json` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[Desktop Entry Specification (freedesktop.org)](https://specifications.freedesktop.org/desktop-entry-spec/latest/)** — Apps mirror .desktop entries — a user-facing name, a description, and metadata about what categories/file-types the app handles. Our entity_types plays the role of MimeType.
