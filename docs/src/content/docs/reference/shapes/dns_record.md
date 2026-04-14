---
title: dns_record
description: "A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.)."
sidebar:
  label: dns_record
---

A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.).

Example sources: Gandi, Porkbun

| Metadata | Value |
|---|---|
| **Plural** | `dns_records` |
| **Subtitle field** | `recordType` |
| **Identity** | `domain`, `recordType`, `recordName` |

## Fields

| Field | Type |
|---|---|
| `domain` | `string` |
| `recordName` | `string` |
| `recordType` | `string` |
| `ttl` | `integer` |
| `values` | `string[]` |

## Skills that produce this shape

- [gandi](/docs/reference/skills/hosting/gandi/) — `list_dns_records`
- [gandi](/docs/reference/skills/hosting/gandi/) — `get_dns_record`
- [porkbun](/docs/reference/skills/hosting/porkbun/) — `list_dns_records`
