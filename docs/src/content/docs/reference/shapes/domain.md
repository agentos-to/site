---
title: domain
description: "A registered domain name. Also auto-created from email sender/recipient addresses."
sidebar:
  label: domain
---

A registered domain name. Also auto-created from email sender/recipient addresses.

Example sources: Gandi, Porkbun (registered domains); Gmail (extracted from addresses)

| | |
|---|---|
| **Plural** | `domains` |
| **Identity** | `name` |

## Fields

| Field | Type |
|---|---|
| `status` | `string` |
| `registrar` | `string` |
| `expiresAt` | `datetime` |
| `autoRenew` | `boolean` |
| `nameservers` | `string[]` |

## Skills that produce this shape

- [gandi](/docs/reference/skills/gandi/) — `list_domains`
- [gandi](/docs/reference/skills/gandi/) — `get_domain`
- [porkbun](/docs/reference/skills/porkbun/) — `list_domains`
