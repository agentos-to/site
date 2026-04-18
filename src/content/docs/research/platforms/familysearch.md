---
title: FamilySearch Genealogical Data Model
description: Research document for informing family relationship modeling in our knowledge graph.
---

**Research Date:** 2026-01-24

---

## Executive Summary

FamilySearch, operated by The Church of Jesus Christ of Latter-day Saints, has the most mature and battle-tested genealogical data model in existence. Their system uses **GEDCOM X** as the underlying data format and maintains **GEDCOM 7** (FamilySearch GEDCOM) as the interchange standard. The key insight is that FamilySearch uses only **two relationship types** (Couple and Parent-Child) with **fact qualifiers** to express the full complexity of family relationships.

---

## 1. FamilySearch Data Model Overview

### 1.1 Core Philosophy

FamilySearch's data model is centered on **persons** linked together by **relationships**. All other data objects (sources, places, discussions, memories) provide supporting information.

```
Person ←→ Relationships ←→ Person
   ↓           ↓            ↓
 Facts      Facts        Facts
   ↓           ↓            ↓
Sources    Sources      Sources
```

### 1.2 The Two Relationship Types

**FamilySearch has only two relationship types:**

| Relationship Type | Description | API Resource |
|-------------------|-------------|--------------|
| **Couple Relationship** | Between two people (spouses, partners) | `/platform/tree/couple-relationships/{crid}` |
| **Child-and-Parents Relationship** | Between a child and up to two parents | `/platform/tree/child-and-parents-relationships/{caprid}` |

This is a critical design choice. Rather than having dozens of relationship types, they use a minimal set with **facts/qualifiers** to express nuance.

### 1.3 Person Entity Structure

A Person in FamilySearch includes:

| Component | Description |
|-----------|-------------|
| **ID** | Unique identifier (e.g., `KWQV-BGF`) |
| **Names** | Multiple names with types (birth, married, AKA) |
| **Gender** | Male, Female, Unknown |
| **Facts** | Birth, death, and other life events |
| **Relationships** | Links to couple and parent-child relationships |
| **Sources** | Evidence supporting conclusions |
| **Discussions** | Community research notes |
| **Memories** | Photos, documents, audio |
| **Change History** | Audit trail of modifications |

---

## 2. Relationship Types in Detail

### 2.1 Couple Relationship

The Couple Relationship connects two persons as partners/spouses.

**Structure:**
```json
{
  "id": "relationship-id",
  "person1": { "resourceId": "PERSON-1-ID" },
  "person2": { "resourceId": "PERSON-2-ID" },
  "facts": [
    {
      "type": "http://gedcomx.org/Marriage",
      "date": { "original": "12 June 1950" },
      "place": { "original": "Salt Lake City, Utah" }
    }
  ]
}
```

**Supported Facts on Couple Relationships:**

| Fact Type URI | Description |
|---------------|-------------|
| `http://gedcomx.org/Marriage` | Legal or ceremonial marriage |
| `http://gedcomx.org/CommonLawMarriage` | Common law marriage |
| `http://gedcomx.org/Divorce` | Legal divorce |
| `http://gedcomx.org/Annulment` | Marriage annulment |
| `http://familysearch.org/v1/LivedTogether` | Cohabitation without marriage |
| `http://familysearch.org/v1/CoupleNeverHadChildren` | Childless couple marker |

**Note on Gender:** FamilySearch now supports same-sex couples. The API uses generic `person1`/`person2` (not husband/wife) to accommodate all relationships.

### 2.2 Child-and-Parents Relationship

The Child-and-Parents Relationship connects a child to their parents.

**Structure:**
```json
{
  "id": "relationship-id",
  "child": { "resourceId": "CHILD-ID" },
  "parent1": { "resourceId": "PARENT-1-ID" },
  "parent2": { "resourceId": "PARENT-2-ID" },
  "parent1Facts": [
    { "type": "http://gedcomx.org/BiologicalParent" }
  ],
  "parent2Facts": [
    { "type": "http://gedcomx.org/BiologicalParent" }
  ]
}
```

**Lineage Types (Parent-Child Fact Types):**

| Fact Type URI | Description |
|---------------|-------------|
| `http://gedcomx.org/BiologicalParent` | Genetic/birth parent |
| `http://gedcomx.org/AdoptiveParent` | Legally adopted |
| `http://gedcomx.org/FosterParent` | Foster care relationship |
| `http://gedcomx.org/GuardianParent` | Legal guardianship |
| `http://gedcomx.org/StepParent` | Step-parent through marriage |

**Key Design Decisions:**

1. **Each parent has separate lineage type** — Parent 1 could be biological while Parent 2 is adoptive
2. **A child can have multiple parent sets** — Biological parents AND adoptive parents each get their own relationship
3. **One parent can be unspecified** — Single parent situations are supported
4. **No sibling relationship type** — Siblings are derived from shared parents

---

## 3. GEDCOM Standards

### 3.1 GEDCOM 7 (FamilySearch GEDCOM)

GEDCOM 7 (released 2021, current version 7.0.16) is the file interchange format. It uses a hierarchical line-based structure.

**Family (FAM) Record Structure:**
```gedcom
0 @F1@ FAM
1 HUSB @I1@
1 WIFE @I2@
1 CHIL @I3@
1 CHIL @I4@
1 MARR
2 DATE 15 JUN 1952
2 PLAC Salt Lake City, Utah
1 DIV
2 DATE 1 MAR 1970
```

**Individual (INDI) Record Structure:**
```gedcom
0 @I1@ INDI
1 NAME John /Smith/
2 GIVN John
2 SURN Smith
1 SEX M
1 BIRT
2 DATE 1 JAN 1930
2 PLAC Boston, Massachusetts
1 FAMC @F0@
1 FAMS @F1@
```

**GEDCOM 7 Relationship Links:**

| Tag | Meaning |
|-----|---------|
| `FAMC` | Family as child (links INDI to FAM where they are a child) |
| `FAMS` | Family as spouse (links INDI to FAM where they are a partner) |
| `HUSB` | Husband/Partner 1 in family |
| `WIFE` | Wife/Partner 2 in family |
| `CHIL` | Child in family |

**Pedigree (PEDI) Values in GEDCOM 7:**

| Value | Meaning |
|-------|---------|
| `ADOPTED` | Adoptive parents |
| `BIRTH` | Family structure at time of birth |
| `FOSTER` | Foster or guardian family |
| `SEALING` | LDS temple sealing (not birth parents) |
| `OTHER` | Other relationship type (use PHRASE) |

### 3.2 GEDCOM X

GEDCOM X is a modern JSON/XML data model, separate from GEDCOM 7. It's used by FamilySearch's API.

**Key GEDCOM X Specifications:**

| Specification | Purpose |
|---------------|---------|
| Conceptual Model | Core data types (Person, Relationship, Source) |
| Fact Types | Enumerated facts for persons and relationships |
| Event Types | Birth, death, marriage, etc. |
| Date Format | Flexible date representation |
| JSON Format | JSON serialization |
| XML Format | XML serialization |

**GEDCOM X Relationship Types:**

```
http://gedcomx.org/Couple
http://gedcomx.org/ParentChild
```

That's it. Just two. All complexity comes from facts attached to these relationships.

### 3.3 GEDCOM X vs GEDCOM 7

| Aspect | GEDCOM 7 | GEDCOM X |
|--------|----------|----------|
| Format | Line-based text | JSON/XML |
| Purpose | File interchange | API data model |
| Family Unit | FAM record groups family | No family entity; just relationships |
| Maintenance | FamilySearch | FamilySearch |
| Current Version | 7.0.16 (March 2025) | Stable |

---

## 4. Handling Complex Cases

### 4.1 Multiple Parents (Adoption, Foster, Step)

**Scenario:** A child has biological parents AND adoptive parents.

**Solution:** Create multiple Child-and-Parents relationships, each with its own lineage type facts.

```
Child-and-Parents Relationship 1:
  - Child: John
  - Parent1: BiologicalMother (BiologicalParent fact)
  - Parent2: BiologicalFather (BiologicalParent fact)

Child-and-Parents Relationship 2:
  - Child: John  
  - Parent1: AdoptiveMother (AdoptiveParent fact)
  - Parent2: AdoptiveFather (AdoptiveParent fact)
```

### 4.2 Step-Parents

**Scenario:** Mother remarries; child gains step-father.

**Solution:** 
1. Original Child-and-Parents relationship with biological parents
2. New Child-and-Parents relationship with mother (BiologicalParent) and step-father (StepParent)

### 4.3 Multiple Marriages

**Scenario:** Person has been married three times.

**Solution:** Three separate Couple Relationships, each with their own marriage/divorce facts and dates.

### 4.4 Same-Sex Parents

**Scenario:** Child has two mothers.

**Solution:** FamilySearch's "Generic Relationships" update (2019) removed gender constraints. Use person1/person2 for couple relationships; both can have any gender.

### 4.5 Uncertain/Disputed Relationships

FamilySearch handles this through:

1. **Confidence indicators** on the relationship itself
2. **Multiple competing assertions** from different contributors
3. **Discussion threads** attached to relationships
4. **Source references** with quality assessments

In GEDCOM 7, the `FAMC.STAT` (status) enumeration handles this:

| Value | Meaning |
|-------|---------|
| `CHALLENGED` | Linkage is suspect but not proven/disproven |
| `DISPROVEN` | Linkage has been disproven |
| `PROVEN` | Linkage has been proven |

---

## 5. Relationship Metadata

### 5.1 Dates

Relationships support date ranges:

```json
{
  "type": "http://gedcomx.org/Marriage",
  "date": {
    "original": "about 1952",
    "formal": "+1952"
  }
}
```

**Date modifiers in GEDCOM 7:**
- `ABT` - About (approximate)
- `CAL` - Calculated from other data
- `EST` - Estimated
- `BEF` - Before
- `AFT` - After
- `BET...AND` - Between dates
- `FROM...TO` - Date period

### 5.2 Source Citations

Every fact and relationship should have sources:

```json
{
  "sources": [
    {
      "description": "https://familysearch.org/ark:/...",
      "attribution": {
        "contributor": { "resourceId": "contributor-id" },
        "modified": "2023-01-15T10:30:00Z"
      }
    }
  ]
}
```

### 5.3 Confidence/Quality

GEDCOM 7 includes a `QUAY` (Quality of data) tag with enumerated values:

| Value | Meaning |
|-------|---------|
| `0` | Unreliable evidence or estimated data |
| `1` | Questionable reliability (interviews, census, oral) |
| `2` | Secondary evidence, recorded after event |
| `3` | Direct and primary evidence |

FamilySearch's collaborative model uses voting/consensus rather than individual confidence scores.

---

## 6. FamilySearch API Summary

### 6.1 Authentication

- OAuth 2.0 authentication required
- Requires API key from developer program
- Free for non-commercial genealogy use

### 6.2 Key Endpoints

| Endpoint | Purpose |
|----------|---------|
| `/platform/tree/persons/{pid}` | Read/write person |
| `/platform/tree/couple-relationships/{crid}` | Read/write couple relationship |
| `/platform/tree/child-and-parents-relationships/{caprid}` | Read/write parent-child relationship |
| `/platform/tree/ancestry` | Get pedigree/ancestry |
| `/platform/tree/descendancy` | Get descendants |

### 6.3 Response Formats

- `application/json` (standard JSON)
- `application/x-gedcomx-v1+json` (GEDCOM X JSON)
- `application/x-fs-v1+json` (FamilySearch extensions)

---

## 7. Comparison with Other Platforms

### 7.1 Ancestry.com

- Uses GEDCOM for export but proprietary internal model
- No public API for tree data (only DNA)
- Likely similar two-relationship model internally

### 7.2 MyHeritage

- Family Graph API (REST, JSON)
- Similar graph-based approach
- "Theory of Family Relativity" for automatic relationship detection
- Read-only API initially; limited write access

### 7.3 Graph Databases for Genealogy

Neo4j is popular for genealogy because:
- Relationships are first-class citizens
- Avoids complex joins
- Natural query patterns: "Find all descendants of X"

Common approaches:
1. **Simple model:** `married`, `child_of` relationships
2. **Bipartite model:** Person nodes + Family nodes
3. **All-person model:** Direct person-to-person relationships

---

## 8. Recommendations for Our Schema

Based on this research, here are recommendations for our knowledge graph:

### 8.1 Core Family Relationship Types

**Recommended approach: Two base types with qualifiers**

```yaml
# Couple/Partner relationship
spouse_of:
  from: person
  to: person
  properties:
    - type: enum [marriage, civil_union, domestic_partnership, cohabitation]
    - started: date
    - ended: date
    - end_reason: enum [divorce, annulment, death, separation]
    
# Parent-Child relationship  
parent_of:
  from: person
  to: person
  properties:
    - type: enum [biological, adoptive, foster, step, guardian]
    - started: date  # adoption date, etc.
    - ended: date    # guardianship ended, etc.
```

### 8.2 Derived Relationships (Computed, Not Stored)

These should be computed from the base relationships, not stored:

| Derived Relationship | How to Compute |
|---------------------|----------------|
| `sibling_of` | Share at least one parent |
| `half_sibling_of` | Share exactly one parent |
| `step_sibling_of` | Parents are spouses but children share no parents |
| `grandparent_of` | Parent of parent |
| `grandchild_of` | Child of child |
| `uncle_of` / `aunt_of` | Sibling of parent |
| `cousin_of` | Child of parent's sibling |

### 8.3 Relationship Metadata Pattern

```yaml
relationship:
  id: nanoid
  from_entity: entity_id
  to_entity: entity_id
  type: relationship_type
  data:
    subtype: string           # biological, adoptive, etc.
    started_at: datetime
    ended_at: datetime
    confidence: float         # 0.0 to 1.0
    status: enum              # proven, challenged, disproven
  sources: source_citation[]
```

### 8.4 Multiple Parent Sets

Allow the same child to have multiple `parent_of` relationships with different parent pairs and types:

```
Person: John
  ← parent_of (type: biological) ← BiologicalMother
  ← parent_of (type: biological) ← BiologicalFather
  ← parent_of (type: adoptive) ← AdoptiveMother
  ← parent_of (type: adoptive) ← AdoptiveFather
```

### 8.5 Same-Sex Parents

Use neutral terminology (`person1`/`person2` or just `from`/`to`) rather than gendered terms. The schema already supports this with `spouse_of` and `parent_of`.

### 8.6 Bidirectional vs Unidirectional

**Recommendation: Store as unidirectional, compute inverses**

- Store `parent_of` (parent → child)
- Compute `child_of` (child → parent) as inverse
- Store `spouse_of` once (person1 → person2)
- Treat as bidirectional in queries

---

## 9. Sources Consulted

### Official Documentation

1. **FamilySearch Developer Documentation**
   - https://developers.familysearch.org/main/docs/the-family-tree-data-model
   - https://www.familysearch.org/developers/docs/guides/facts
   - https://www.familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_resource
   - https://www.familysearch.org/developers/docs/api/tree/Couple_Relationship_resource

2. **GEDCOM 7 Specification**
   - https://gedcom.io/specifications/FamilySearchGEDCOMv7.html
   - https://gedcom.io/specs/

3. **GEDCOM X Specifications**
   - https://gedcomx.org/Specifications.html
   - https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md
   - https://github.com/FamilySearch/gedcomx/blob/master/specifications/fact-types-specification.md
   - https://github.com/FamilySearch/gedcomx/blob/master/specifications/relationship-types-specification.md

### Help Articles

4. **FamilySearch Help Center**
   - https://www.familysearch.org/en/help/helpcenter/article/how-do-i-specify-biological-step-adopted-and-foster-relationships-in-family-tree
   - https://www.familysearch.org/en/help/helpcenter/article/how-do-i-add-step-adopted-and-foster-parents-to-a-child-in-family-tree

5. **Same-Sex Relationship Support**
   - https://www.familytree.com/blog/familysearch-to-allow-same-sex-relationships-on-family-trees/
   - https://www.familysearch.org/developers/docs/guides/generic-relationships-update

### Other Platforms

6. **MyHeritage**
   - https://github.com/myheritage/familygraph-php
   - https://www.myheritage.com/wiki/Theory_of_Family_Relativity

7. **Neo4j Genealogy**
   - https://neo4j.com/blog/developer/discover-auradb-free-importing-gedcom-files-and-exploring-genealogy-ancestry-data-as-a-graph

### Academic/Community

8. **Genealogical Proof Standard**
   - https://en.wikipedia.org/wiki/Genealogical_Proof_Standard

---

## 10. Key Takeaways

1. **Simplicity wins:** FamilySearch uses only TWO relationship types (Couple, Parent-Child) with qualifiers, not dozens of specific types.

2. **Facts modify relationships:** The richness comes from facts/qualifiers attached to relationships, not from relationship type proliferation.

3. **Multiple parents are first-class:** A child can have multiple parent-child relationships with different lineage types.

4. **Siblings are derived:** No explicit sibling relationship — compute from shared parents.

5. **Source everything:** Every conclusion needs source citations with quality/confidence indicators.

6. **Status for uncertainty:** Use status fields (proven, challenged, disproven) rather than avoiding uncertain data.

7. **Gender-neutral design:** Modern systems use generic terms to support all family structures.
