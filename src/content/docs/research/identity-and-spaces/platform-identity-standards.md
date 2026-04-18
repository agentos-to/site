---
title: Platform Identity and Normalization Standards
description: Research into how the problem of platform/service identity has been solved across standards and real-world systems.
---

Research into how the problem of platform/service identity has been solved across standards and real-world systems. Core question: when accounts exist across many platforms that come, go, rename, and merge — how do you canonically identify which platform an account belongs to?

Finding: **Every standard that hardcoded platform identifiers broke. The correct approach is platforms-as-entities with open strings for names, Wikidata Q-IDs as the universal external reference, and domain entities for temporal name resolution.**

---

## 1. FOAF (Friend of a Friend) — The Cautionary Tale

FOAF initially hardcoded platform-specific properties:

```
foaf:aimChatID    — AOL Instant Messenger
foaf:icqChatID    — ICQ
foaf:msnChatID    — MSN Messenger
foaf:yahooChatID  — Yahoo Messenger
```

**What happened:** Every platform died or rebranded. These properties became dead weight in the ontology.

**FOAF's retreat:** Generic `foaf:OnlineAccount` with `foaf:accountServiceHomepage` (a URL pointing to the platform). This was better but fragile — URLs change (twitter.com → x.com).

**Key insight:** Hardcoding platform identifiers in the schema is the wrong abstraction level. Platforms are data, not schema.

---

## 2. Schema.org — sameAs and Service-Centric

Schema.org uses `sameAs` to link to external profiles:

```json
{
  "@type": "Person",
  "sameAs": [
    "https://twitter.com/johndoe",
    "https://github.com/johndoe"
  ]
}
```

Platforms are identified by **URL domain**. No platform registry. No entity modeling of the platform itself.

**Problem:** When Twitter becomes X, every `sameAs` URL breaks. The platform identity is embedded in the URL, not in a stable identifier.

---

## 3. Wikidata — The De Facto Platform Registry

Wikidata models platforms as full entities with stable Q-identifiers:

| Platform | Wikidata ID | Survives rename? |
|----------|------------|-----------------|
| Twitter/X | Q918 | Yes — Q918 whether called Twitter or X |
| YouTube | Q866 | Yes |
| WhatsApp | Q18001 | Yes |
| Facebook | Q355 | Yes |
| AIM (defunct) | Q379265 | Yes — still resolvable |
| ICQ (defunct) | Q144644 | Yes |

**Key properties on Wikidata platform entities:**
- `instance of` (P31): social media service, messaging app, etc.
- `operator` (P137): the company running it (Google → YouTube)
- `inception` (P571): when it launched
- `dissolution` (P576): when it died
- `official website` (P856): current URL (changes tracked)
- `country of origin` (P495): useful for regional platforms (VK, WeChat, QQ)

**Key insight:** Wikidata is the closest thing to a universal platform registry. Q-IDs survive rebranding, acquisition, and death. They can serve as the canonical external reference for platform entities.

---

## 4. GEDCOM X — Historical Platform Handling

GEDCOM X (genealogical data standard) faces the same problem at historical scale — people communicated through postal systems, telegraphs, phone networks, and then digital platforms. All of these are "platforms" in the broad sense.

GEDCOM X uses a resource identifier scheme where platforms are identified by authority URIs. The authority can change independently of the data.

**Key insight:** The genealogical world solved this by making the platform a first-class entity that carries its own history. The same person might have been reachable by telegraph in 1880, phone in 1920, and email in 1995 — the platform is a temporal entity, not a static label.

---

## 5. Keybase / Keyoxide — Identity Verification Across Platforms

These systems verify that the same person controls accounts on multiple platforms:

- **Keybase:** Centralized service (now Zoom-owned) that cryptographically proves account ownership across platforms. Maintained an internal platform registry.
- **Keyoxide:** Decentralized alternative using OpenPGP. Platforms identified by "claim" URIs that encode both the platform and the verification method.

**Key insight:** Cross-platform identity verification needs platforms to be identifiable entities, not just strings. The platform's verification mechanism IS a property of the platform entity.

---

## 6. ActivityPub / Fediverse — Instance-Level Identity

The fediverse introduced a new wrinkle: the same platform *type* (Mastodon) has many independent *instances* (mastodon.social, fosstodon.org, hachyderm.io). Each instance:
- Has its own domain
- Has its own rules and culture
- Can defederate from other instances
- Is independently administered

**Two-level identity:** Platform type (Mastodon) + Instance (mastodon.social). An account handle includes the instance: `@user@instance.tld`.

**Key insight:** The platform/instance distinction maps to product/deployment in software terms. We might model this as: Mastodon (product entity) → mastodon.social (place entity, an instance of the product).

---

## 7. IndieWeb — URL-Centric, No Platform Registry

IndieWeb philosophy: your identity IS your domain. You own yourname.com and syndicate to platforms (POSSE — Publish Own Site, Syndicate Elsewhere).

Platform identity is implicit in syndication targets. No formal registry.

**Key insight:** The IndieWeb approach is philosophically aligned with AgentOS (own your data), but its URL-centric identity breaks when domains change hands.

---

## Synthesis: What Breaks and What Works

| Approach | Example | Status |
|----------|---------|--------|
| Hardcoded platform properties | FOAF `aimChatID` | **Broken** — platforms die |
| URL-based identification | Schema.org `sameAs` | **Fragile** — URLs change |
| String-based with aliases | Many apps today | **Messy** — no canonical form |
| Stable external ID | Wikidata Q-ID | **Works** — survives everything |
| Platform as entity | AgentOS approach | **Best** — full modeling |

## Recommendation for AgentOS

1. **Platforms are product entities**, not hardcoded strings. YouTube, Twitter/X, phone network, email — all are product entities in the graph.

2. **The `platform` field on accounts references a product entity** (or resolves to one). The string "youtube" maps to the YouTube product entity.

3. **Domains handle rebranding temporally.** twitter.com (domain entity, 2006-2023) and x.com (domain entity, 2023-present) both link to the same product entity via `owned_by` relationships with temporal bounds.

4. **Wikidata Q-IDs are the universal external reference.** Every product/organization/person entity should have an optional `wikidata_id` property for cross-referencing.

5. **Adapters seed their own platform entities.** Each adapter declares its platform as seed data:
   ```yaml
   seed_entities:
     - id: youtube
       types: [product]
       name: YouTube
       wikidata_id: Q866
       relationships:
         - type: made_by
           to: google  # organization entity
   ```

6. **No hardcoded platform registries.** The graph IS the registry. Platform normalization is entity resolution, not string matching.

This approach means that when a platform rebrands (Twitter → X), you update ONE entity. All accounts that reference it automatically resolve to the new name. Historical data preserves the old name through domain entity relationships. The graph handles what no string registry can.
