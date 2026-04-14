---
title: source
description: "A content source — where skills, themes, shapes, and wallpapers live."
sidebar:
  label: source
---

A content source — where skills, themes, shapes, and wallpapers live.
Sources are like Cydia repos, Homebrew taps, or APT sources.

Identity: address — the canonical location (filesystem path, git URL, or HTTP URL).
Two entries pointing to the same address are the same source.

Platform tells the engine which scanner to use:
- "agentos" scans for skills/, themes/, apps/, shapes/, wallpapers/ subdirs
- Future: homebrew, apt, synology, etc.

| | |
|---|---|
| **Plural** | `sources` |
| **Subtitle field** | `sourceId` |
| **Identity** | `address` |

## Fields

| Field | Type |
|---|---|
| `sourceId` | `string` |
| `address` | `string` |
| `platform` | `string` |
| `enabled` | `boolean` |
| `description` | `text` |
| `lastSynced` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `folder` | [`folder`](/docs/reference/shapes/folder/) |
