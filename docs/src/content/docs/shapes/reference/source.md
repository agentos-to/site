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

| Metadata | Value |
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
| `folder` | [`folder`](/docs/shapes/reference/folder/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[Homebrew Taps](https://docs.brew.sh/Taps)** — Direct precedent. Our sourceId/address match tap name/URL; our platform=agentos parallels tap formulae discovery.
- **[Cydia / Sileo (APT repos for iOS)](https://wiki.theapebox.com/index.php/Package_Management)** — Namespaced third-party source model. Our sourceId prefix is the Cydia repo-namespace pattern.
- **[Debian APT sources.list](https://wiki.debian.org/SourcesList)** — Canonical third-party source mechanism. Our enabled flag parallels APT source enable/disable; lastSynced ≈ apt-get update timestamp.
