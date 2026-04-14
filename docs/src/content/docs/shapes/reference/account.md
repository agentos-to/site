---
title: account
description: "A user's presence on a platform — their GitHub handle, Gmail address, etc."
sidebar:
  label: account
---

A user's presence on a platform — their GitHub handle, Gmail address, etc.
Created by most skills. Links a person to their platform-specific identity.

Identity: [issuer, identifier] — one node per platform+handle combo.
issuer = platform domain (e.g. "github.com", "gmail.com")
identifier = platform-specific handle (e.g. "octocat", "user@example.com")

| Metadata | Value |
|---|---|
| **Plural** | `accounts` |
| **Subtitle field** | `identifier` |
| **Identity** | `issuer`, `identifier` |

## Fields

| Field | Type |
|---|---|
| `issuer` | `string` |
| `identifier` | `string` |
| `handle` | `string` |
| `displayName` | `string` |
| `email` | `string` |
| `phone` | `string` |
| `bio` | `text` |
| `accountType` | `string` |
| `color` | `string` |
| `isActive` | `boolean` |
| `joinedDate` | `datetime` |
| `lastActive` | `datetime` |

## Relations

| Relation | Target |
|---|---|
| `platform` | [`product`](/docs/shapes/reference/product/) |
| `owner` | [`person`](/docs/shapes/reference/person/) |
| `follows` | [`account[]`](/docs/shapes/reference/account/) |
| `followers` | [`account[]`](/docs/shapes/reference/account/) |

## Used as a base by

- [`financial_account`](/docs/shapes/reference/financial_account/)

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/docs/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OpenID Connect (OIDC) Core 1.0](https://openid.net/specs/openid-connect-core-1_0.html)** — Our issuer/identifier maps to OIDC's iss/sub claims. OIDC is the canonical federated-identity model for "account = (issuer, subject)".
- **[WebFinger (RFC 7033)](https://datatracker.ietf.org/doc/html/rfc7033)** — Resolves issuer+identifier pairs to profile metadata. Our identifier aligns with WebFinger's acct: URI scheme (user@host).
- **[vCard 4.0 (RFC 6350)](https://datatracker.ietf.org/doc/html/rfc6350)** — Defines displayName/email/phone/org in contact cards. We adopt vCard's contact semantics for the human-readable fields.

## Skills that produce this shape

- [goodreads](/docs/skills/reference/media/goodreads/) — `get_profile`
- [moltbook](/docs/skills/reference/media/moltbook/) — `me_account`, `get_account`
- [amazon](/docs/skills/reference/logistics/amazon/) — `whoami`
- [chase](/docs/skills/reference/finance/chase/) — `check_session`, `get_accounts`
- [copilot-money](/docs/skills/reference/finance/copilot-money/) — `load_accounts`
- [greptile](/docs/skills/reference/dev/greptile/) — `list_members`
