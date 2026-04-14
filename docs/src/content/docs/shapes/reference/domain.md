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

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/ontology/shape-design-principles/) for how prior art informs shape design.

- **[RFC 1035 (Domain Names)](https://datatracker.ietf.org/doc/html/rfc1035)** — Canonical domain-name syntax + nameservers + TTL. Our nameservers are NS records for the apex.
- **[RFC 3912 (WHOIS)](https://datatracker.ietf.org/doc/html/rfc3912)** — Our registrar/status/expiresAt/autoRenew come from WHOIS response fields.

## Skills that produce this shape

- [gandi](/docs/skills/reference/hosting/gandi/) — `list_domains`
- [gandi](/docs/skills/reference/hosting/gandi/) — `get_domain`
- [porkbun](/docs/skills/reference/hosting/porkbun/) — `list_domains`
