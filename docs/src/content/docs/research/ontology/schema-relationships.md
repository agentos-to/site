---
title: Relationship Schema
description: Source of truth for relationship types, patterns, and design principles.
---

This file defines how entities connect. It's a companion to `schema-entities.md` (which defines entities).

---

## Core Philosophy: Event-Sourced, Computed State

We follow an **event-sourcing** paradigm for relationships:

1. **Store events, not state** — Record "married on date X" and "divorced on date Y", not "married: true"
2. **Compute current state** — Current relationship status is derived from event history
3. **Derive complex relationships** — Siblings, grandparents, cousins are computed from primitives
4. **Timestamps on everything** — Every relationship has temporal data

### Why Event-Sourcing?

| Approach | Problems |
|----------|----------|
| **Stored state** | No history, data conflicts, "when did this change?", manual sync |
| **Events** | Full audit trail, temporal queries natural, no conflicts (events are facts) |

**Influenced by:**
- **FamilySearch GEDCOM** — Marriage is an event with date/place, not a boolean
- **Facebook TAO** — All associations have timestamps, ordered by time
- **GEDCOM X** — Relationships are first-class entities with facts, sources, confidence

### The Paradigm Shift

**Wrong (stored state):**
```json
{
  "person": "joe",
  "employer": "acme",
  "employed": true
}
```

**Right (events):**
```json
{
  "type": "employment.started",
  "person": "joe",
  "organization": "acme",
  "date": "2020-01-15"
}
```

To know if Joe works at Acme today: find most recent employment event for that pair.

---

## GEDCOM 7 Compatibility

**Goal:** First-class import/export with GEDCOM 7.0 files.

### GEDCOM 7 Core Structures

| GEDCOM Structure | Our Mapping | Notes |
|------------------|-------------|-------|
| `FAM` record | Couple relationship | Links two partners + children |
| `INDI.FAMC` | Child-of relationship | With PEDI qualifier |
| `INDI.FAMS` | Partner-in relationship | Bidirectional with FAM |
| `MARR`, `DIV`, `ANUL` | Events on couple | Date, place, type |
| `PEDI` | Lineage type | BIRTH, ADOPTED, FOSTER, SEALING |
| `ASSO` + `ROLE` | Association | Generic relationships |

### GEDCOM Parent-Child Types (PEDI)

| GEDCOM Value | Our Value | Meaning |
|--------------|-----------|---------|
| `BIRTH` | `biological` | Birth parents |
| `ADOPTED` | `adoptive` | Legal adoption |
| `FOSTER` | `foster` | Foster care |
| `SEALING` | `sealed` | LDS temple sealing |

### GEDCOM Family Events

| GEDCOM Tag | Event Type | Description |
|------------|------------|-------------|
| `MARR` | `marriage` | Legal/customary marriage |
| `DIV` | `divorce` | Legal dissolution |
| `DIVF` | `divorce_filed` | Filing for divorce |
| `ANUL` | `annulment` | Marriage declared void |
| `ENGA` | `engagement` | Agreement to marry |
| `MARB` | `marriage_bann` | Public notice of intent |
| `MARC` | `marriage_contract` | Prenuptial agreement |
| `MARL` | `marriage_license` | Legal license obtained |
| `MARS` | `marriage_settlement` | Property agreement |

### Import/Export Principles

1. **Preserve GEDCOM IDs** — Store original `@F1@`, `@I1@` in `data.gedcom_id`
2. **Round-trip fidelity** — What we import, we can export back
3. **Map events, not state** — Convert MARR to marriage event, not married flag
4. **Handle NO structure** — GEDCOM's `NO MARR` = "no marriage occurred" assertion

---

## Two Primitive Relationships

Following FamilySearch's elegant model, we use **only two base relationship types**:

### 1. `couple`

A relationship between two people (spouses, partners, etc.).

```json
{
  "id": "rel_abc123",
  "type": "couple",
  "person1": "person_joe",
  "person2": "person_jane",
  "events": [
    {
      "type": "marriage",
      "date": "2015-06-20",
      "place": "San Francisco, CA"
    }
  ]
}
```

**Why not `spouse_of`?** Because:
- Couples aren't always spouses (cohabitation, engagement)
- "Spouse" implies current state; we track events
- GEDCOM 7 uses `FAM` which is couple-centric, not marriage-centric

### 2. `parent_child`

A relationship between a parent and child.

```json
{
  "id": "rel_def456",
  "type": "parent_child",
  "parent": "person_joe",
  "child": "person_joey",
  "lineage": "biological",
  "events": [
    {
      "type": "birth",
      "date": "2018-03-15"
    }
  ]
}
```

**Lineage types:**
- `biological` — Birth parent
- `adoptive` — Legal adoption
- `foster` — Foster care
- `step` — Parent's partner, not biological
- `guardian` — Legal guardian

---

## Computed Relationships

Everything else is **derived from the primitives**:

| To Find | Query Pattern |
|---------|---------------|
| **Siblings** | People who share ≥1 parent |
| **Full siblings** | Share both parents |
| **Half-siblings** | Share exactly one parent |
| **Step-siblings** | Parents are coupled but no shared parents |
| **Grandparents** | Parents of parents |
| **Grandchildren** | Children of children |
| **Aunts/Uncles** | Siblings of parents |
| **Cousins** | Children of aunts/uncles |
| **In-laws** | Spouses of siblings, siblings of spouse |

### Why Compute Instead of Store?

1. **No redundancy** — Adding a parent automatically updates all derived relationships
2. **No conflicts** — Can't have inconsistent sibling/parent data
3. **Less maintenance** — Two relationship types vs dozens
4. **Natural queries** — "Find all descendants" is a graph traversal

### Implementation

```typescript
function getSiblings(person: Entity): Entity[] {
  const parents = getParents(person);
  const siblings = new Set<Entity>();
  
  for (const parent of parents) {
    for (const child of getChildren(parent)) {
      if (child.id !== person.id) {
        siblings.add(child);
      }
    }
  }
  
  return Array.from(siblings);
}

function getGrandparents(person: Entity): Entity[] {
  return getParents(person).flatMap(p => getParents(p));
}
```

---

## Events on Relationships

Relationships don't have boolean state — they have **events**.

### Couple Events

| Event Type | Meaning | Computes To |
|------------|---------|-------------|
| `engagement` | Agreement to marry | engaged |
| `marriage` | Legal/customary union | married |
| `separation` | Living apart | separated |
| `divorce_filed` | Legal filing | divorce pending |
| `divorce` | Legal dissolution | divorced |
| `annulment` | Marriage voided | annulled |
| `reconciliation` | Back together after separation | married |
| `death` | One partner died | widowed |

**Current status** is computed from the most recent event.

### Parent-Child Events

| Event Type | Meaning |
|------------|---------|
| `birth` | Child born to parent |
| `adoption` | Legal adoption finalized |
| `foster_start` | Foster placement began |
| `foster_end` | Foster placement ended |
| `guardianship_start` | Legal guardianship began |
| `guardianship_end` | Guardianship ended |
| `emancipation` | Child legally independent |

### Event Structure

```json
{
  "type": "marriage",
  "date": "2015-06-20",
  "place": "San Francisco, CA",
  "data": {
    "ceremony_type": "civil",
    "officiant": "Judge Smith"
  }
}
```

---

## Non-Family Relationships

Beyond family, we need other relationship types.

### Association Relationships

Following GEDCOM's `ASSO` pattern for non-family connections:

| Relationship | Description | Computed From |
|--------------|-------------|---------------|
| `colleague` | Work together | Overlapping employment at same org |
| `classmate` | School together | Overlapping education at same school |
| `roommate` | Live together | Overlapping residence at same address |
| `collaborator` | Project together | Shared project membership |
| `mentor_of` | Mentorship | Explicit relationship |
| `friend_of` | Friendship | Explicit relationship |

**Hypothesis:** Many association relationships can be **computed** from overlapping events:
- Colleagues = both employed at same org during overlapping time
- Classmates = both educated at same institution during overlapping time

**What must be explicit:**
- Friendship (no events imply it)
- Mentorship (asymmetric, intentional)
- Godparent (ceremonial role)

### Content Relationships

| Relationship | From | To | Description |
|--------------|------|-----|-------------|
| `authored_by` | work | person | Creator relationship |
| `published_by` | work | organization | Publisher |
| `performed_by` | performance | person | Performer |
| `directed_by` | work | person | Director |
| `produced_by` | work | person/org | Producer |

These may also be event-based:
- "Joe authored the article" = authorship event with date
- "Jane left the band" = membership_ended event

### Containment Relationships

| Relationship | Description | Examples |
|--------------|-------------|----------|
| `part_of` | Containment | Track part of album, chapter part of book |
| `member_of` | Membership | Person member of organization |
| `located_in` | Geographic | City located in country |

---

## Relationship Metadata

Every relationship can have metadata beyond type and participants.

### Common Properties

| Property | Type | Description |
|----------|------|-------------|
| `created_at` | datetime | When relationship was created in our system |
| `confidence` | 0.0-1.0 | For AI-extracted relationships |
| `source` | string | Where we learned about this |
| `notes` | string | Additional context |

### Type-Specific Properties

**Couple relationships:**
- `events[]` — Marriage, divorce, etc.

**Parent-child relationships:**
- `lineage` — biological, adoptive, foster, step, guardian
- `events[]` — Birth, adoption, etc.

**Employment (computed or explicit):**
- `title` — Job title
- `department` — Department
- `started_at` / `ended_at` — Dates

---

## Bidirectionality

### Symmetric Relationships

Some relationships are symmetric — if A relates to B, B relates to A the same way:
- Siblings
- Spouses
- Colleagues
- Friends

For symmetric relationships, we store **one relationship** and query from either direction.

### Asymmetric Relationships

Some relationships have different meanings in each direction:
- Parent → Child (inverse: Child → Parent)
- Mentor → Mentee
- Employer → Employee

For asymmetric relationships, we store **with directionality** and define inverse names:

| Forward | Inverse |
|---------|---------|
| `parent_of` | `child_of` |
| `mentor_of` | `mentee_of` |
| `employs` | `employed_by` |
| `authored` | `authored_by` |

### Implementation

When storing:
```json
{
  "type": "parent_child",
  "parent": "person_joe",
  "child": "person_joey"
}
```

When querying "who are Joey's parents?":
- Find all `parent_child` where `child = joey`
- Return the `parent` values

When querying "who are Joe's children?":
- Find all `parent_child` where `parent = joe`
- Return the `child` values

---

## Hypotheses and Open Questions

### Hypothesis: Most Relationships Are Computed

**Claim:** The majority of interesting relationships can be derived from events:
- Colleague = overlapping employment
- Classmate = overlapping education
- Neighbor = overlapping residence
- Fellow traveler = overlapping trips

**Implication:** We should focus on capturing events accurately, not on creating relationship types for every possible connection.

**Open question:** What's the right balance? Some computed relationships need explicit confirmation.

### Hypothesis: Timestamps Everywhere

**Claim:** Every relationship should have temporal bounds, even if imprecise.

**Reasoning:**
- Enables "what was true on date X?" queries
- Enables change tracking
- Matches how Facebook TAO works
- Matches GEDCOM's event-centric model

**Open question:** What about relationships without known dates? Use `null` or estimate?

### Hypothesis: Relationships Are First-Class Entities

**Claim:** Relationships should have their own IDs, not just be edges.

**Reasoning:**
- Can attach metadata (confidence, source, notes)
- Can have events (marriage → divorce sequence)
- Can be referenced by other structures
- Matches GEDCOM X model

**Open question:** Does this add too much complexity for simple cases?

### Open: Connection Strength

Facebook calculates relationship strength internally from:
- Mutual friends
- Interaction frequency
- Profile overlap

**Question:** Should we expose strength as a property?

**Arguments for:**
- Useful for prioritizing in UI
- Enables "closest friends" queries

**Arguments against:**
- Schema.org doesn't have it
- Subjective, changes over time
- Should be computed, not stored?

**Current decision:** Don't include in schema. Can be computed by applications.

### Open: Open vs Closed World Assumption

**OWA (Open World):** Absence of data = unknown (RDF, OWL)
**CWA (Closed World):** Absence of data = false (Databases, SHACL)

Most applications expect CWA:
- "Show me Joe's children" expects complete list
- "Does Joe have a spouse?" expects yes/no

But OWA is more honest:
- We might not know all of Joe's children
- Joe might have a spouse we don't know about

**Current decision:** Lean toward CWA for application behavior, but support confidence levels and provenance to indicate uncertainty.

---

## Relationship Data Model

### Database Schema (SQLite)

```sql
-- Base relationships table
CREATE TABLE relationships (
  id TEXT PRIMARY KEY,
  type TEXT NOT NULL,  -- 'couple', 'parent_child', 'member_of', etc.
  entity1_id TEXT NOT NULL,
  entity2_id TEXT NOT NULL,
  data JSON,  -- Type-specific properties
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (entity1_id) REFERENCES entities(id),
  FOREIGN KEY (entity2_id) REFERENCES entities(id)
);

-- Events on relationships
CREATE TABLE relationship_events (
  id TEXT PRIMARY KEY,
  relationship_id TEXT NOT NULL,
  type TEXT NOT NULL,  -- 'marriage', 'divorce', 'birth', etc.
  date TEXT,  -- ISO date or partial
  place TEXT,
  data JSON,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (relationship_id) REFERENCES relationships(id)
);
```

### JSON Representation

```json
{
  "id": "rel_abc123",
  "type": "couple",
  "entity1_id": "person_joe",
  "entity2_id": "person_jane",
  "data": {},
  "events": [
    {
      "id": "evt_111",
      "type": "engagement",
      "date": "2014-12-25"
    },
    {
      "id": "evt_222",
      "type": "marriage",
      "date": "2015-06-20",
      "place": "San Francisco, CA",
      "data": {
        "ceremony_type": "civil"
      }
    }
  ],
  "created_at": "2026-01-24T12:00:00Z"
}
```

---

## Research Sources

### Primary Influences

| Source | Key Lesson |
|--------|------------|
| **FamilySearch** | Two primitives (couple + parent-child), compute everything else |
| **GEDCOM 7** | Events not state, marriage is an event with date/place |
| **GEDCOM X** | Relationships as first-class entities with confidence |
| **Facebook TAO** | Timestamps on everything, typed associations |

### Secondary References

- [GEDCOM 7.0 Specification](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html)
- [GEDCOM X Conceptual Model](https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md)
- [TAO: Facebook's Distributed Data Store](https://www.usenix.org/conference/atc13/technical-sessions/presentation/bronson)
- [Schema.org Relationships](https://schema.org/Person) — Reference for property names

### What We Rejected

| System | Why Rejected |
|--------|--------------|
| Schema.org | Too generic, weak abstractions, no temporal model |
| OGP | Unidirectional, fixed vocabulary, limited metadata |
| FOAF | Simple but no temporal support, limited adoption |

---

## Session Log

### 2026-01-24: Initial Research

- Researched Schema.org, Facebook, FamilySearch, OGP, knowledge graphs
- Found consensus on: timestamps everywhere, bidirectionality matters
- Found divergence on: relationships as edges vs entities, explicit vs computed
- Decision: Follow FamilySearch's event-sourcing model
- Decision: First-class GEDCOM 7 compatibility

### 2026-01-24: Schema Draft

- Created this document
- Defined two primitive relationships: `couple`, `parent_child`
- Defined event types for each
- Documented computed relationship patterns
- Listed hypotheses and open questions

---

## Relationship Gap Analysis (2026-01-24)

### Missing Relationships (High Confidence — To Implement)

| Relationship | Research Source | Notes |
|--------------|-----------------|-------|
| `follows` | Facebook, Schema.org | Asymmetric social (A follows B ≠ B follows A) |
| `contributed_to` | Schema.org | Secondary creator role |
| `about` | Schema.org | What the work is about |
| `mentions` | Schema.org | References another entity (weaker than `about`) |
| `from` / `to` | Gmail, Messages | Sender/recipient for messages |
| `reply_to` | Gmail, Reddit | Message/comment threading |
| `comment_on` | YouTube, Facebook | What a comment responds to |
| `extracted_from` | Readwise | Source of a highlight |
| `spoken_by` | Wikiquote | Speaker of a quote |
| `appears_in` | Wikiquote | Where a quote was found |

### Event-Related Relationships

| Relationship | From → To | Notes |
|--------------|-----------|-------|
| `attended_by` | event → person | Event attendance |
| `organized_by` | event → person/org | Event organizer |

### Identity Relationships

| Relationship | Notes |
|--------------|-------|
| `same_as` | Identity link to external entity (Wikidata Q-number, external URL) |

---

## Next Steps

1. **GEDCOM 7 import/export** — Build parser and serializer
2. **Computed relationships** — Implement sibling, grandparent queries
3. **Test with real data** — Import family tree, verify round-trip
4. **Association relationships** — Decide which to compute vs store explicitly

---

## Research Proposals (2026-01-24)

> **Divergent thinking phase.** Everything from Google Takeout and Facebook Graph research. Converge later.

### Complete Relationship Taxonomy

Based on research across Google Takeout (23 products), Facebook Graph API, Instagram, Threads, WhatsApp, and Twitter/X.

#### Social Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `friend_of` | Bidirectional | person ↔ person | created_at | Facebook |
| `follows` | Unidirectional | person → person/org/channel | created_at | FB, IG, Twitter, YouTube |
| `blocked` | Unidirectional | person → person | created_at | Facebook |
| `knows` | Bidirectional | person ↔ person | confidence, context | Schema.org |

**Design note:** Facebook's `friend` is bidirectional (creates edges both ways). `follow` is unidirectional. Consider supporting both patterns.

---

#### Family Relationships (Existing + Extensions)

Already defined: `couple`, `parent_child` (primitives)

**Additional family edges from Facebook (computed from primitives):**

| Computed | Query Pattern |
|----------|---------------|
| `sibling_of` | Share ≥1 parent |
| `grandparent_of` / `grandchild_of` | Parent of parent |
| `aunt_uncle_of` / `niece_nephew_of` | Sibling of parent |
| `cousin_of` | Child of aunt/uncle |
| `in_law` | Spouse of sibling, sibling of spouse |

**Keep as computed, not stored.**

---

#### Professional Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `works_at` | Unidirectional | person → organization | title, department, started_at, ended_at | Google Contacts, LinkedIn |
| `colleague_of` | Bidirectional | person ↔ person | organization, overlap_period | Computed |
| `manages` | Unidirectional | person → person | started_at | Workplace |
| `reports_to` | Unidirectional | person → person | started_at | Workplace (inverse of manages) |
| `founded` | Unidirectional | person → organization | date | — |
| `invested_in` | Unidirectional | person/org → organization | amount, date | — |

**Hypothesis:** `colleague_of` should be computed from overlapping `works_at` relationships, not stored explicitly.

---

#### Content Creation Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `authored_by` | Unidirectional | work → person | role (author, co-author, editor) | OGP, Schema.org |
| `directed_by` | Unidirectional | video.movie → person | — | OGP |
| `performed_by` | Unidirectional | music.song → person | role (artist, featured) | OGP |
| `produced_by` | Unidirectional | work → person/org | — | OGP |
| `published_by` | Unidirectional | work → organization | date | — |
| `contributed_to` | Unidirectional | person → work | role, contribution | Schema.org |

---

#### Content Organization Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `part_of` | Unidirectional | entity → container | position | Universal |
| `contains` | Unidirectional | container → entity | — | Inverse of part_of |
| `episode_of` | Unidirectional | video.episode → video.tv_show | season, episode_number | OGP |
| `track_on` | Unidirectional | music.song → music.album | disc, track_number | OGP |
| `chapter_of` | Unidirectional | section → book | — | — |
| `tagged_with` | Unidirectional | entity → label/tag | — | Keep, Gmail, Blogger |

**Note:** `part_of` is the universal containment relationship. Specific forms like `episode_of`, `track_on` are just typed `part_of` with metadata.

---

#### Messaging Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `from` | Unidirectional | message → person | — | Gmail, FB, WhatsApp |
| `to` | Unidirectional | message → person | — | Gmail, FB, WhatsApp |
| `cc` | Unidirectional | message → person | — | Gmail |
| `bcc` | Unidirectional | message → person | — | Gmail |
| `reply_to` | Unidirectional | message → message | — | Gmail, Reddit, FB |
| `attachment` | Unidirectional | message → file | — | Gmail |
| `participant_in` | Unidirectional | person → conversation | role (admin, member), joined_at | Chat, WhatsApp |

---

#### Engagement Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `liked` | Unidirectional | person → content | created_at | Facebook, IG |
| `reacted_to` | Unidirectional | person → content | reaction_type, created_at | Facebook |
| `commented_on` | Unidirectional | comment → content | — | FB, IG, YouTube |
| `shared` | Unidirectional | post → post (original) | share_time | Facebook |
| `saved` | Unidirectional | person → content | collection, created_at | FB, IG, Google Saved |
| `tagged_in` | Unidirectional | content → person | x, y (for photos), created_at | FB, IG |
| `mentioned` | Unidirectional | content → person | — | FB, IG, Twitter |
| `subscribed_to` | Unidirectional | person → channel/podcast | created_at | YouTube, Podcasts |

**Design decision:** Reactions could be separate relationships per type (`loved`, `wowed`, etc.) or one `reacted_to` with type metadata. Recommend: one relationship with metadata.

---

#### Location Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `located_at` | Unidirectional | entity → place | — | FB, Google |
| `located_in` | Unidirectional | place → place | — | Geographic hierarchy |
| `visited` | Unidirectional | person → place | arrived_at, departed_at, confidence | Google Timeline |
| `taken_at` | Unidirectional | photo/video → place | — | Google Photos, FB |
| `lives_in` | Unidirectional | person → place | since | FB, Contacts |
| `born_in` | Unidirectional | person → place | — | FB |
| `hometown` | Unidirectional | person → place | — | FB |
| `checked_in` | Unidirectional | person → place | timestamp, post | FB (deprecated) |

---

#### Event Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `attending` | Unidirectional | person → event | rsvp_status, rsvp_time | FB, Google Calendar |
| `hosted_by` | Unidirectional | event → person/org | — | FB, Calendar |
| `invited_to` | Unidirectional | person → event | invited_by, invited_at | FB, Calendar |
| `speaker_at` | Unidirectional | person → event | — | — |
| `venue_of` | Unidirectional | event → place | — | FB, Calendar |

**RSVP statuses (from Facebook):** attending, maybe, declined, invited (no response)

---

#### Commerce Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `purchased_by` | Unidirectional | order → person | — | Gmail schema.org |
| `sold_by` | Unidirectional | order → organization | — | Gmail schema.org |
| `contains` | Unidirectional | order → product | quantity, price | Gmail schema.org |
| `delivered_by` | Unidirectional | delivery → organization | — | Gmail schema.org |
| `part_of_order` | Unidirectional | delivery → order | — | Gmail schema.org |
| `reserved_for` | Unidirectional | reservation → person | — | Gmail schema.org |
| `reserved_at` | Unidirectional | reservation → place | — | Gmail schema.org |

---

#### Pass/Credential Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `held_by` | Unidirectional | pass → person | — | Google Wallet |
| `issued_by` | Unidirectional | pass → organization | — | Google Wallet |
| `valid_for` | Unidirectional | pass → event/transit | — | Google Wallet |

---

#### Content Extraction Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `extracted_from` | Unidirectional | highlight → work | position, page | Readwise, Kindle |
| `spoken_by` | Unidirectional | quote → person | context | — |
| `appears_in` | Unidirectional | quote → work | page, chapter | — |
| `review_of` | Unidirectional | review → entity | — | Schema.org, Goodreads |

---

#### Identity Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `same_as` | Bidirectional | entity ↔ external_id | — | Wikidata, Schema.org |
| `linked_account` | Bidirectional | account ↔ account | platform | Meta Accounts Center |
| `alias_of` | Unidirectional | name → person | — | — |

---

#### Media Relationships

| Relationship | Direction | Between | Properties | Source |
|--------------|-----------|---------|------------|--------|
| `appears_in` | Unidirectional | person → photo/video | x, y, confidence | Google Photos, FB |
| `thumbnail_of` | Unidirectional | photo → video | — | — |
| `cover_of` | Unidirectional | photo → album/playlist/book | — | FB, Spotify |
| `transcript_of` | Unidirectional | text → audio/video | — | YouTube, Podcasts |

---

### Relationship Metadata Patterns

From Facebook TAO research, all relationships benefit from metadata:

#### Universal Metadata

| Property | Type | Description |
|----------|------|-------------|
| `created_at` | datetime | When relationship was created |
| `confidence` | 0.0-1.0 | For AI-extracted relationships |
| `source` | string | How we learned about this |

#### Type-Specific Metadata

**Engagement relationships:**
- `reaction_type` — LIKE, LOVE, HAHA, WOW, SAD, ANGRY, CARE

**Tagging relationships:**
- `x`, `y` — Position in photo (0-100 coordinates)

**Membership relationships:**
- `role` — admin, moderator, member
- `joined_at` — When joined

**Event attendance:**
- `rsvp_status` — attending, maybe, declined, invited
- `rsvp_time` — When they responded

**Employment:**
- `title` — Job title
- `department` — Department
- `started_at`, `ended_at` — Tenure

**Content positioning:**
- `position` — Order in container (playlist position, track number)
- `season`, `episode` — For TV episodes

---

### TAO Design Patterns to Adopt

From Facebook's TAO paper:

1. **Single association per type between two objects**
   - Can't like something twice
   - Different types can coexist (like AND comment on same post)

2. **Timestamps required on all associations**
   - Enables "most recent" queries
   - Enables temporal filtering

3. **Bidirectional relationships = two associations**
   - Friend A↔B stored as (A→B) AND (B→A)
   - Query from either direction efficiently

4. **Association lists ordered by time**
   - Most recent first
   - Enables efficient "latest N" queries

5. **Optional data payload**
   - Associations carry key-value metadata
   - Type-specific properties (role, coordinates, etc.)

---

### Computed vs Explicit Relationships

**Should be computed (not stored):**
- `sibling_of` — from shared parents
- `grandparent_of` — parent of parent
- `colleague_of` — overlapping employment
- `classmate_of` — overlapping education
- `neighbor_of` — overlapping residence

**Must be explicit (user declares):**
- `friend_of` — no events imply it
- `mentor_of` — intentional, asymmetric
- `godparent_of` — ceremonial role
- `romantic_partner` — requires confirmation

**Could be either:**
- `knows` — could be computed from interactions OR explicit
- `worked_with` — could be computed from overlapping employment OR explicit for project collaboration

---

### Inverse Relationship Names

For asymmetric relationships, define both directions:

| Forward | Inverse |
|---------|---------|
| `parent_of` | `child_of` |
| `authored` | `authored_by` |
| `employs` | `employed_by` |
| `manages` | `managed_by` / `reports_to` |
| `contains` | `part_of` / `contained_in` |
| `mentor_of` | `mentee_of` |
| `hosts` | `hosted_by` |
| `follows` | `followed_by` |
| `invited` | `invited_to` |
| `tagged` | `tagged_in` |

---

### Relationship Lifecycle

From Facebook research, relationships have lifecycle states:

1. **Pending** — Request sent, awaiting confirmation (friend requests)
2. **Active** — Confirmed, in effect
3. **Ended** — Terminated (unfriend, unfollow, divorce)
4. **Blocked** — Explicitly blocked

For event-sourced relationships, track via events:
- `friendship_requested` → `friendship_confirmed` → `unfriended`
- `engaged` → `married` → `divorced`

---

### Privacy Per-Relationship

From Facebook:
- Entity visibility and relationship visibility are **independent**
- Both parties can have **different privacy settings** for the same relationship
- Some status changes are **silent** (divorce doesn't post to feed)

Consider:
- `visibility` property on relationships
- Different views for self vs others vs public

---

### Cross-Platform Comparison

| Aspect | Facebook | Google | Twitter | Our Model |
|--------|----------|--------|---------|-----------|
| **Relationship storage** | TAO (typed edges) | Separate APIs | Snowflake IDs | Event-sourced |
| **Bidirectional handling** | Two edges | Varies | Two edges | Two edges |
| **Timestamps** | Required | Usually | Required | Required |
| **Metadata on edges** | Optional data | Varies | Limited | Full support |
| **Privacy per-edge** | Yes | Limited | No | TBD |

---

### Proposed Relationship Hierarchy

#### Tier 1: Core Relationships (Must Have)

| Relationship | Priority | Notes |
|--------------|----------|-------|
| `couple` | ✅ | Family primitive |
| `parent_child` | ✅ | Family primitive |
| `authored_by` | High | Content creation |
| `part_of` | High | Universal containment |
| `from` / `to` | High | Messaging |
| `reply_to` | High | Threading |
| `follows` | High | Social |
| `member_of` | High | Groups, organizations |
| `attended_by` | High | Events |
| `located_at` | High | Location |
| `same_as` | High | Identity linking |

#### Tier 2: Important Relationships

| Relationship | Priority | Notes |
|--------------|----------|-------|
| `works_at` | Medium | Professional |
| `comment_on` | Medium | Engagement |
| `tagged_in` | Medium | Media |
| `liked` / `reacted_to` | Medium | Engagement |
| `extracted_from` | Medium | Highlights |
| `spoken_by` / `appears_in` | Medium | Quotes |
| `subscribed_to` | Medium | Follows for channels |
| `review_of` | Medium | Reviews |

#### Tier 3: Extended Relationships

| Relationship | Priority | Notes |
|--------------|----------|-------|
| `purchased_by` / `sold_by` | Lower | Commerce |
| `held_by` / `issued_by` | Lower | Passes |
| `visited` | Lower | Location history |
| `transcript_of` | Lower | Media |
| `thumbnail_of` / `cover_of` | Lower | Media |

---

### Summary: Key Design Decisions Needed

1. **Reaction as relationship or entity?** 
   - Recommendation: Relationship with `reaction_type` metadata

2. **Generic `part_of` vs specific containment types?**
   - Recommendation: Generic `part_of` with metadata (position, role)

3. **How to handle bidirectional relationships?**
   - Recommendation: Store two edges (TAO pattern)

4. **Privacy per-relationship?**
   - Open question: Do we need this complexity?

5. **Computed vs explicit threshold?**
   - Recommendation: Compute social inference, require explicit for meaningful relationships

6. **Relationship lifecycle events?**
   - Recommendation: Full event sourcing for family/romantic, simpler for content relationships

---

## Design Principles from Research (2026-01-24)

> **Synthesis of key learnings across all research sources.** These principles should guide the convergence phase.

### Principle 1: Two Family Relationship Primitives

**Source:** FamilySearch, GEDCOM 7

- `couple` + `parent_child` express all family relationships
- Siblings, grandparents, cousins are **computed**, not stored
- Avoids redundancy and consistency issues
- One person can have multiple parent relationships (biological + adoptive)

### Principle 2: Event-Sourcing Over Stored State

**Source:** FamilySearch, GEDCOM X, Facebook TAO

- Store events, not current state
- "Joe married Jane on 2020-06-15" not "married: true"
- Current status is computed from event history
- Divorce, remarriage are events on the same `couple` relationship

### Principle 3: Timestamps on Everything

**Source:** Facebook TAO, FamilySearch

- Every relationship has temporal data (`created_at`, events with dates)
- Required for "what was true on date X?" queries
- Association lists ordered by time (TAO pattern)
- Events have date/place/confidence qualifiers

### Principle 4: Relationships Are First-Class Entities

**Source:** GEDCOM X, property graphs

- Relationships have their own IDs
- Can attach metadata: confidence, source, notes
- Can have events: marriage → separation → reconciliation → divorce
- Not just foreign keys in a join table

### Principle 5: Compute Don't Store (Derived Relationships)

**Source:** FamilySearch, Facebook

| Computed | Query Pattern |
|----------|---------------|
| Sibling | Share ≥1 parent |
| Grandparent | Parent of parent |
| Colleague | Overlapping employment |
| Classmate | Overlapping education |
| Neighbor | Overlapping residence |

Only store explicit relationships (friendship, mentorship, authorship).

### Principle 6: TAO Association Rules

**Source:** Facebook TAO paper

1. **Single association per type** — Can't "like" something twice
2. **Timestamps required** — Enables time-based ordering
3. **Bidirectional = two edges** — Store both directions for symmetric
4. **Optional data payload** — Relationships carry key-value metadata

### Principle 7: GEDCOM 7 Compatibility

**Source:** FamilySearch research

- First-class import/export with GEDCOM 7.0 files
- Map: `FAM` → couple, `FAMC` → parent_child
- Preserve GEDCOM IDs in `data.gedcom_id`
- Handle PEDI (lineage types): BIRTH, ADOPTED, FOSTER, SEALING

### Principle 8: Inverse Property Names

**Source:** Schema.org, property graph best practices

| Forward | Inverse |
|---------|---------|
| `parent_of` | `child_of` |
| `authored_by` | `author_of` |
| `employs` | `employed_by` |
| `contains` | `part_of` |
| `follows` | `followed_by` |

Store in one direction, compute inverse on query.

### Principle 9: Confidence for AI-Extracted Relationships

**Source:** GEDCOM X, knowledge graph research

- AI-extracted relationships carry `confidence: 0.0-1.0`
- Source tracking: where did we learn this?
- Status enum: `proven`, `challenged`, `disproven` (from GEDCOM)
- Humans can confirm/reject

### Principle 10: Privacy Per-Relationship (Future)

**Source:** Facebook research

- Entity visibility and relationship visibility are independent
- Both parties can have different privacy settings
- Some status changes are silent (divorce doesn't broadcast)
- Open question: Do we need this complexity now?

---

## Relationship Type Summary (Pre-Convergence)

### Tier 1: Core Relationships (Must Have)

| Category | Relationships | Notes |
|----------|---------------|-------|
| **Family Primitives** | `couple`, `parent_child` | Everything else computed |
| **Content Creation** | `authored_by`, `directed_by`, `performed_by` | Creator relationships |
| **Containment** | `part_of`, `member_of` | Universal hierarchy |
| **Messaging** | `from`, `to`, `reply_to` | Threading |
| **Social** | `follows` | Asymmetric follow |
| **Event** | `attended_by`, `organized_by` | Event participation |
| **Location** | `located_at` | Place associations |
| **Identity** | `same_as` | Cross-source linking |

### Tier 2: Important Relationships

| Category | Relationships | Notes |
|----------|---------------|-------|
| **Professional** | `works_at`, `manages` | Employment |
| **Engagement** | `comment_on`, `liked`, `reacted_to` | User interactions |
| **Content** | `extracted_from`, `spoken_by`, `appears_in` | Quotes/highlights |
| **Subscription** | `subscribed_to` | Follows for channels |
| **Review** | `review_of` | Review relationships |

### Tier 3: Extended Relationships

| Category | Relationships | Notes |
|----------|---------------|-------|
| **Commerce** | `purchased_by`, `sold_by`, `delivered_by` | Orders/delivery |
| **Passes** | `held_by`, `issued_by`, `valid_for` | Wallet passes |
| **Location History** | `visited` | Timeline visits |
| **Media** | `transcript_of`, `thumbnail_of`, `cover_of` | Media relationships |

### Computed Relationships (Never Stored)

| Relationship | Computed From |
|--------------|---------------|
| `sibling_of` | Shared parents |
| `grandparent_of` | Parent of parent |
| `aunt_uncle_of` | Sibling of parent |
| `cousin_of` | Child of aunt/uncle |
| `colleague_of` | Overlapping `works_at` |
| `classmate_of` | Overlapping education |

---

## Universal Metadata Patterns (Applied to Relationships)

> **See `schema-entities.md` for full pattern definitions.** This section describes how they apply to relationships specifically.

### How Patterns Apply to Relationships

| Pattern | Application to Relationships |
|---------|------------------------------|
| **Evidence Quality** | How do we know these two are connected? Quality of the source. |
| **Temporal Precision** | When did this relationship start/end? (imprecise dates supported) |
| **Provenance** | Who asserted this connection? From what source? |
| **Aliases** | N/A — relationships don't have names |

### Relationship with Full Attribution

```yaml
relationship:
  type: "couple"
  from: "person_abc"
  to: "person_xyz"
  
  # Temporal (from Pattern 2)
  started_at:
    value: "1920-06-15"
    modifier: "about"
    original: "abt Jun 1920"
  
  # Evidence (from Pattern 1)
  evidence:
    quality: 2              # Secondary source
    confidence: 0.9
    method: "imported"
  
  # Provenance (from Pattern 3)
  provenance:
    source: "Marriage certificate, County Records"
    contributor: "user_joe"
    status: "verified"
  
  # Relationship-specific
  events:
    - type: "marriage"
      date: { value: "1920-06-15", modifier: "about" }
      place: "New York, NY"
```

### Events on Relationships Also Get Attribution

Events that occur on relationships (marriage, divorce, etc.) can also carry evidence and provenance:

```yaml
event:
  type: "marriage"
  date:
    value: "1920-06-15"
    modifier: "exact"
  evidence:
    quality: 3              # Primary source (marriage certificate)
    confidence: 1.0
  provenance:
    source: "entity_id_of_certificate"
    contributor: "user_joe"
```

This allows different facts about the same relationship to have different source quality.

---

## Next Steps (Convergence Phase)

1. **Finalize Tier 1 relationships** — These are the core schema
2. **Define event types per relationship** — What events can attach to `couple`?
3. **Spec the data model** — Relationships table, events table
4. **Apply universal patterns** — Evidence, temporal, provenance on relationships
5. **Build GEDCOM 7 import/export** — First integration test
6. **Define inverse computation** — How to query in both directions
