---
title: volume
description: "A storage volume — local disk, external drive, network share, or cloud drive."
sidebar:
  label: volume
---

A storage volume — local disk, external drive, network share, or cloud drive.
Distinct from folder: volumes have capacity, filesystem type, and mount state.

Example sources: macos-control (local volumes), future: Google Drive, Dropbox, iCloud

| Metadata | Value |
|---|---|
| **Plural** | `volumes` |
| **Subtitle field** | `path` |

## Fields

| Field | Type |
|---|---|
| `path` | `string` |
| `totalBytes` | `integer` |
| `freeBytes` | `integer` |
| `usedBytes` | `integer` |
| `filesystem` | `string` |
| `volumeType` | `string` |
| `removable` | `boolean` |
| `readOnly` | `boolean` |

## Relations

| Relation | Target |
|---|---|
| `contains` | [`folder[]`](/docs/shapes/reference/folder/) |
