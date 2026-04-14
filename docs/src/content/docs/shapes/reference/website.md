---
title: website
description: "A published website (not a single page — see webpage for that)."
sidebar:
  label: website
---

A published website (not a single page — see webpage for that).
Websites are created/managed by the here.now publishing skill.

Example sources: here.now

| Metadata | Value |
|---|---|
| **Plural** | `websites` |
| **Subtitle field** | `url` |
| **Identity** | `url` |

## Fields

| Field | Type |
|---|---|
| `status` | `string` |
| `versionId` | `string` |
| `expiresAt` | `datetime` |
| `anonymous` | `boolean` |
| `claimToken` | `string` |
| `claimUrl` | `url` |

## Relations

| Relation | Target |
|---|---|
| `domain` | [`domain`](/docs/shapes/reference/domain/) |
| `ownedBy` | [`organization`](/docs/shapes/reference/organization/) |

## Skills that produce this shape

- [here-now](/docs/skills/reference/hosting/here-now/) — `list_websites`
- [here-now](/docs/skills/reference/hosting/here-now/) — `op_create_website`, `op_update_website`
