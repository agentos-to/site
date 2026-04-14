---
title: domain
description: "A registered domain name. Also auto-created from email sender/recipient addresses."
sidebar:
  label: domain
---

A registered domain name. Also auto-created from email sender/recipient addresses.

Example sources: Gandi, Porkbun (registered domains); Gmail (extracted from addresses)

| Metadata | Value |
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

- [gandi](/docs/skills/reference/hosting/gandi/) — `list_domains`
- [gandi](/docs/skills/reference/hosting/gandi/) — `get_domain`
- [porkbun](/docs/skills/reference/hosting/porkbun/) — `list_domains`
