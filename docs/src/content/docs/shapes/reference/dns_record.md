---
title: dns_record
description: "A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.)."
sidebar:
  label: dns_record
---

A DNS record for a domain. One domain has many records (A, CNAME, MX, TXT, etc.).

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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[RFC 1035 (DNS)](https://datatracker.ietf.org/doc/html/rfc1035)** — Foundational spec. Our domain/recordName/recordType/ttl/values map directly to NAME/TYPE/CLASS/TTL/RDATA.
- **[RFC 7208 (SPF), RFC 6376 (DKIM), RFC 7489 (DMARC)](https://datatracker.ietf.org/doc/html/rfc7208)** — TXT-record vocabularies that frequently populate our values[] for SPF, DKIM, and DMARC policy records.

## Skills that produce this shape

- [gandi](/skills/reference/hosting/gandi/) — `list_dns_records`, `get_dns_record`
- [porkbun](/skills/reference/hosting/porkbun/) — `list_dns_records`
