---
title: account
description: "A user's presence within a namespace — their GitHub handle, Gmail address,"
sidebar:
  label: account
---

A user's presence within a namespace — their GitHub handle, Gmail address,
Mastodon @-handle, Chase bank login, etc.

Identity is graph-native: (at, identifier). `at` is a relation to whichever
entity owns the namespace (an organization, a product, or other software).
`identifier` is the local handle within that namespace. The relation-keyed
identity means rebrands (Twitter → X), bank mergers (First Republic → Chase),
and instance migrations don't fragment accounts on string changes — the node
persists, the edge persists with it.

| Metadata | Value |
|---|---|
| **Plural** | `accounts` |
| **Subtitle field** | `identifier` |
| **Identity** | `at`, `identifier` |

## Fields

| Field | Type |
|---|---|
| `identifier` | `string` |
| `handle` | `string` |
| `displayName` | `string` |
| `display` | `string` |
| `email` | `string` |
| `phone` | `string` |
| `bio` | `text` |
| `accountType` | `string` |
| `color` | `string` |
| `isActive` | `boolean` |
| `joinedDate` | `datetime` |
| `lastActive` | `datetime` |
| `lastProfileFetch` | `datetime` |
| `userId` | `string` |
| `issuer` | `string` |
| `metadata` | `json` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`actor`](/shapes/reference/actor/) |
| `via` | [`product`](/shapes/reference/product/) |
| `operator` | [`actor`](/shapes/reference/actor/) |
| `protocol` | [`protocol`](/shapes/reference/protocol/) |
| `owner` | [`person`](/shapes/reference/person/) |
| `authenticatedVia` | [`account`](/shapes/reference/account/) |
| `previousIdentity` | [`account[]`](/shapes/reference/account/) |
| `follows` | [`account[]`](/shapes/reference/account/) |
| `followers` | [`account[]`](/shapes/reference/account/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[ActivityPub Actor model](https://www.w3.org/TR/activitypub/)** — Account id is a URL; Server/Application/Operator are separate Actor objects. We adopt the same separation but ground each in graph nodes rather than URLs, so node lifecycle (rebrand, merge) propagates to all referencing accounts.
- **[schema.org Offer.seller union](https://schema.org/Offer)** — seller: Person | Organization. The `actor` shape (which `at` and `operator` target) is our existing union of person/org/agent — same pattern.
- **[OpenID Connect Core 1.0 (`iss`/`sub`)](https://openid.net/specs/openid-connect-core-1_0.html)** — OIDC keeps issuer as opaque URL because there's no shared graph across token issuers. We have a graph; we replace the URL with a graph node, gaining mutability and traversal at the cost of requiring a node to exist before an account can reference it. Trade is worth it.
- **[WebFinger (RFC 7033)](https://datatracker.ietf.org/doc/html/rfc7033)** — Resolves issuer+identifier pairs to profile metadata. Our identifier aligns with WebFinger's acct: URI scheme (user@host), but the `host` part becomes a graph node (not a string).
- **[vCard 4.0 (RFC 6350)](https://datatracker.ietf.org/doc/html/rfc6350)** — Defines displayName/email/phone/org in contact cards. We adopt vCard's contact semantics for the human-readable fields.

## Skills that produce this shape

- [goodreads](/skills/reference/media/goodreads/) — `get_profile`, `check_session`
- [moltbook](/skills/reference/media/moltbook/) — `me_account`, `get_account`
- [united](/skills/reference/logistics/united/) — `store_session_cookies`, `check_session`
- [uber](/skills/reference/logistics/uber/) — `check_session`, `check_eats_session`
- [amazon](/skills/reference/logistics/amazon/) — `check_session`
- [austin-boulder-project](/skills/reference/fitness/austin-boulder-project/) — `check_session`
- [linear](/skills/reference/dev/linear/) — `whoami`
- [greptile](/skills/reference/dev/greptile/) — `check_session`, `list_members`
- [claude](/skills/reference/ai/claude/) — `check_session`
- [exa](/skills/reference/web/exa/) — `check_session`
- [posthog](/skills/reference/web/posthog/) — `list_persons`, `search_persons`, `get_person`
