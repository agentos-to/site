---
title: protocol
description: "A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc."
sidebar:
  label: protocol
---

A protocol or technical spec — git, bitcoin, ssh, smtp, oauth, etc.
Used as an `at` target by accounts that exist within a protocol's namespace
(a git author identity, a bitcoin wallet) rather than within an organization
or product. The `protocol` relation on `account` also targets this shape.

| Metadata | Value |
|---|---|
| **Plural** | `protocols` |
| **Subtitle field** | `name` |
| **Identity** | `name` |

## Fields

| Field | Type |
|---|---|
| `name` | `string` |
| `homepage` | `url` |
| `rfc` | `string` |
| `wikidataId` | `string` |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[schema.org/CreativeWork](https://schema.org/CreativeWork)** — Closest match in schema.org — protocols are creative works in the broadest sense. We narrow to protocols and technical specifications used as identity namespaces.
- **[Wikidata (Communication protocol, Q15836568)](https://www.wikidata.org/wiki/Q15836568)** — wikidataId enables cross-reference for dedupe across other knowledge graphs. Most well-known protocols have Q-IDs.
- **[IANA Protocol Registry](https://www.iana.org/protocols)** — Authoritative registry for many protocols. Our `name` aligns with IANA protocol slugs where applicable.
