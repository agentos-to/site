---
title: volume
description: "A storage volume — local disk, external drive, network share, or cloud drive."
sidebar:
  label: volume
---

A storage volume — local disk, external drive, network share, or cloud drive.
Distinct from folder: volumes have capacity, filesystem type, and mount state.

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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[POSIX / Single Unix Specification (mount)](https://pubs.opengroup.org/onlinepubs/9699919799/functions/mount.html)** — Our path = mount point; filesystem ≈ fs type; readOnly ≈ ro mount option.
- **[macOS DiskArbitration + diskutil](https://ss64.com/osx/diskutil.html)** — Practical source. Our totalBytes/freeBytes/usedBytes/removable/ volumeType match diskutil info output.
- **[Linux /proc/mounts + statvfs](https://man7.org/linux/man-pages/man5/proc.5.html)** — POSIX-family source. Our filesystem values (apfs, hfs+, ext4, ntfs) are standard /proc/mounts fs-types.
