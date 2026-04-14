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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/WebSite](https://schema.org/WebSite)** — Our url-as-identity matches; ownedBy ≈ publisher; domain relation ≈ url host.
- **[WHOIS (RFC 3912)](https://datatracker.ietf.org/doc/html/rfc3912)** — Our expiresAt/domain source from WHOIS records; claimToken has no direct WHOIS peer (HERE.NOW-specific).
- **[RFC 7033 WebFinger (host-meta)](https://datatracker.ietf.org/doc/html/rfc7033)** — Website metadata discovery. Our claimUrl parallels /.well-known/host-meta patterns.

## Skills that produce this shape

- [here-now](/docs/skills/reference/hosting/here-now/) — `list_websites`
- [here-now](/docs/skills/reference/hosting/here-now/) — `op_create_website`, `op_update_website`
