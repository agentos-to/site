---
title: change
description: "A delta on something — a file born/modified/removed, a document revision,"
sidebar:
  label: change
---

A delta on something — a file born/modified/removed, a document revision,
a changelog entry, a release note. The universal "what changed" record.
`kind` is the FATE of the target (so a drift audit can assert existence);
`path` (when the target is a file) lets a checker stat it.

| Metadata | Value |
|---|---|
| **Plural** | `changes` |
| **Subtitle field** | `kind` |

## Fields

| Field | Type |
|---|---|
| `kind` | `string` |
| `summary` | `text` |
| `status` | `string` |
| `path` | `string` |
| `phase` | `string` |
| `version` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[PROV-O (W3C)](https://www.w3.org/TR/prov-o/)** — wasRevisionOf / wasGeneratedBy / wasInvalidatedBy model born/modified/removed → kind + the derived_from edge.
- **[Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)** — The six categories (Added/Changed/Deprecated/Removed/Fixed/Security) are the canonical `kind` enum.
- **[Conventional Commits 1.0.0 + SemVer 2.0.0](https://www.conventionalcommits.org/)** — Commit type → impact tier (feat=minor, fix=patch, BREAKING=major); supplies the `version` semantics.
