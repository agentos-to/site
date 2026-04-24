---
title: credential
description: "A credential held by AgentOS — the graph descriptor that mirrors one"
sidebar:
  label: credential
---

A credential held by AgentOS — the graph descriptor that mirrors one
encrypted row in the vault (~/.agentos/data/agentos.db, credentials table).

Every vault row also exists as a node of this shape. The *value* stays
encrypted in the credentials table, addressed by `storeRowId`. This
node carries only metadata — domain, identifier, itemType, timestamps,
provenance edges — and nothing secret. Descriptor reads are cheap
(graph traversal), decryption is on demand (SDK's `auth_store.read`
by identifier, after the vault system skill returns the descriptor).

Identity is `(domain, identifier, itemType)` — one node per
distinct credential, matching the unique-row constraint on the
credentials SQLite table (minus `source`, which is provenance, not
identity: two providers writing the same domain/identifier/itemType
pair describe the same credential; whichever writes last wins).

| Metadata | Value |
|---|---|
| **Plural** | `credentials` |
| **Subtitle field** | `source` |
| **Identity** | `domain`, `identifier`, `itemType` |

## Fields

| Field | Type |
|---|---|
| `domain` | `string` |
| `identifier` | `string` |
| `itemType` | `string` |
| `source` | `string` |
| `obtainedAt` | `datetime` |
| `lastVerified` | `datetime` |
| `expiresAt` | `datetime` |
| `refreshable` | `boolean` |
| `storeRowId` | `integer` |

## Relations

| Relation | Target |
|---|---|
| `at` | [`organization`](/shapes/reference/organization/) |
| `account` | [`account`](/shapes/reference/account/) |
| `writtenBy` | [`skill`](/shapes/reference/skill/) |

## Prior art

External standards this shape draws from or aligns with. See [Shape design principles](/shapes/shape-design-principles/) for how prior art informs shape design.

- **[OAuth 2.0 Token Introspection (RFC 7662)](https://datatracker.ietf.org/doc/html/rfc7662)** — RFC 7662 describes token metadata as a separate addressable resource from the token itself (active, exp, iss, sub, scope). Same split here: descriptor is queryable graph metadata, encrypted value is retrieved by a separate call (`auth_store.read` by identifier). Our obtainedAt/expiresAt/lastVerified mirror iat/exp/auth_time.
- **[FIDO Metadata Service (MDS3)](https://fidoalliance.org/metadata/)** — FIDO separates authenticator metadata from the authenticator itself — metadata is queryable, the cryptographic material is not. Mirrors our descriptor/vault split.
- **[macOS Keychain SecItem attributes](https://developer.apple.com/documentation/security/keychain_services/keychain_items/item_attribute_keys_and_values)** — Keychain separates `kSecAttr*` (metadata — server, account, creation/modification dates) from `kSecValueData` (the secret). Attributes are queryable without decrypting the value. Our fields map: kSecAttrServer → domain, kSecAttrAccount → identifier, kSecAttrCreationDate → obtainedAt, kSecAttrModificationDate → lastVerified.
- **[schema.org/DigitalDocument (WebAuthn credentials stored as)](https://schema.org/DigitalDocument)** — Weak alignment — schema.org has no native credential type. Cited only to note that existing web ontologies deliberately stop short of secret material; descriptor-only is the established pattern.

## Skills that produce this shape

- [onepassword](/skills/reference/secrets/onepassword/) — `get_credentials`
- [macos-keychain](/skills/reference/macos/macos-keychain/) — `get_credentials`
