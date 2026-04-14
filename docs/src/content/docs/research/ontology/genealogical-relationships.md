---
title: Genealogical Relationships Research
description: FamilySearch and GEDCOM represent the gold standard for modeling family relationships. What can we learn from their approach to relationships, evidence, and complex family structures?
---

## Why This Matters

Genealogical systems have decades of experience modeling:
- **Billions** of person records (FamilySearch has 1.5+ billion)
- **Complex relationships**: biological, adoptive, step, foster, guardianship
- **Temporal relationships**: marriages, divorces, remarriages
- **Evidence and certainty**: confidence levels, source citations, proof standards
- **Non-traditional families**: same-sex couples, blended families

They've solved hard problems in relationship modeling that apply to any entity graph.

---

## Key Standards

| Standard | Era | Status | Purpose |
|----------|-----|--------|---------|
| GEDCOM 5.5 | 1995 | Legacy (widely used) | Text-based file format for family tree exchange |
| GEDCOM 5.5.1 | 1999 | Industry standard | Minor update, still dominant |
| GEDCOM X | 2012 | Active | Modern data model for evidence-based genealogy |
| FamilySearch GEDCOM 7.0 | 2021 | Current | Updated file format building on GEDCOM X concepts |

---

## Core Relationship Model

### FamilySearch's Two Relationship Types

FamilySearch's Family Tree API supports exactly **two** relationship types:

| Relationship Type | Description | Structure |
|-------------------|-------------|-----------|
| **Couple Relationship** | A relationship between two people (spouses/partners) | Links two `Person` records |
| **Child-and-Parents Relationship** | A relationship between a child and their parents | Links child to up to two parents |

This is remarkably simple. All family structures emerge from just these two primitives.

### GEDCOM's Family-Centric Model

Traditional GEDCOM uses a **FAM (Family) record** as the linking structure:

```
0 @F1@ FAM
1 HUSB @I1@        (husband/partner 1)
1 WIFE @I2@        (wife/partner 2)
1 CHIL @I3@        (child)
1 CHIL @I4@        (another child)
1 MARR
2 DATE 15 JUN 1985
2 PLAC Chicago, Illinois
```

The FAM record is the **only** source of links between individuals. This is similar to a join table in relational databases.

### Key Insight: Sibling Relationships Are Implied

Neither GEDCOM nor FamilySearch explicitly models sibling relationships. Instead:
- Siblings are **inferred** from shared parents
- Half-siblings share exactly one parent
- Step-siblings share no biological parents but have parents in a couple relationship

This avoids redundancy and keeps the model simple.

---

## Parent-Child Relationship Types

### FamilySearch Parent-Child Facts

| Type URI | Description |
|----------|-------------|
| `http://gedcomx.org/BiologicalParent` | Birth parent |
| `http://gedcomx.org/AdoptiveParent` | Legally adopted the child |
| `http://gedcomx.org/StepParent` | Married to biological parent |
| `http://gedcomx.org/FosterParent` | Temporary guardian |
| `http://gedcomx.org/GuardianParent` | Legal guardian |

### GEDCOM PEDI (Pedigree) Tag

GEDCOM 5.5.1 uses the `PEDI` tag to specify parent-child relationship type:

```
0 @I1@ INDI
1 NAME Child /Name/
1 FAMC @F1@
2 PEDI birth          (biological)
1 FAMC @F2@
2 PEDI adopted        (adoptive parents)
```

**PEDI values:**
- `birth` — biological relationship
- `adopted` — legal adoption
- `foster` — foster care
- `sealing` — LDS temple sealing (FamilySearch-specific)

### Multiple Parents

A person can have **multiple sets of parents**:
- Biological parents
- Adoptive parents  
- Step-parents
- Foster parents

Each is a separate `Child-and-Parents` relationship with its own type qualifier.

---

## Couple Relationship Facts

### Supported Couple Events

| Type URI | Description | Date | Place | Multiple |
|----------|-------------|------|-------|----------|
| `http://gedcomx.org/Marriage` | Legal marriage | Yes | Yes | Yes |
| `http://gedcomx.org/Divorce` | Legal divorce | Yes | Yes | Yes |
| `http://gedcomx.org/Annulment` | Marriage annulment | Yes | Yes | Yes |
| `http://gedcomx.org/CommonLawMarriage` | Common law union | Yes | Yes | Yes |
| `http://familysearch.org/v1/LivedTogether` | Cohabitation | No | No | No |
| `http://familysearch.org/v1/CoupleNeverHadChildren` | Flag for childless couple | No | No | No |

### Temporal Relationship Handling

**Marriage as an Event:**
Marriage in GEDCOM is an **event** with date and place, not a boolean status. The `MARR` record documents when/where the marriage occurred.

**Multiple Marriages:**
When couples marry, divorce, and remarry (even to the same person), best practice is:
- Create a **new FAM record** for each marriage
- Don't combine multiple MARR/DIV events in one record
- This maintains chronological clarity and allows other relationships in between

**Divorce Without Marriage Record:**
GEDCOM allows a `DIV` (divorce) record without a corresponding `MARR` if the marriage date is unknown but divorce is documented.

---

## Evidence and Confidence

### GEDCOM X Conclusion Model

GEDCOM X models genealogical data as **conclusions** that can have:

| Property | Type | Purpose |
|----------|------|---------|
| `confidence` | ConfidenceLevel | How certain is this data? |
| `source` | SourceReference[] | What sources support this? |
| `attribution` | Attribution | Who contributed this? When? |
| `analysis` | Document reference | Written reasoning/proof |
| `note` | Note[] | Additional context |

Every fact, relationship, and person in GEDCOM X is a "conclusion" that can carry this metadata.

### Genealogical Proof Standard (GPS)

The GPS is the established framework for genealogical certainty:

1. **Reasonably exhaustive research** in reliable sources
2. **Complete and accurate source citations** for all facts
3. **Analysis and correlation** of collected information
4. **Resolution of conflicting evidence**
5. **Soundly reasoned, coherently written conclusion**

Meeting GPS doesn't mean "beyond doubt" — it's closer to legal "clear and convincing" standard. Conclusions can be revisited when new evidence emerges.

### Evidence Types

| Type | Definition | Example |
|------|------------|---------|
| **Direct Evidence** | Directly answers the question | Birth certificate listing parents |
| **Indirect Evidence** | Requires interpretation/correlation | Census showing household composition |
| **Negative Evidence** | Absence suggests something | Person not in death records = likely alive |

### Source Classification

| Source Type | Definition | Reliability |
|-------------|------------|-------------|
| **Original** | Created at/near time of event by firsthand observer | Higher |
| **Derivative** | Copied, transcribed, or abstracted from original | Lower |
| **Authored** | Created after the fact (family histories, biographies) | Varies |

---

## GEDCOM X vs GEDCOM 5.5

### Fundamental Philosophy Shift

| Aspect | GEDCOM 5.5 | GEDCOM X |
|--------|------------|----------|
| **Focus** | Conclusions only (the family tree) | Evidence + conclusions (the research process) |
| **Sources** | Optional attachments | First-class citizens |
| **Confidence** | Not supported | Built into conclusion model |
| **Format** | Text-based, single format | JSON/XML, multiple serializations |
| **License** | Proprietary (LDS) | Open source (Apache 2.0) |
| **Media** | External links only | Bundled in file format |

### What GEDCOM X Added

1. **Source Descriptions** — Rich metadata about sources
2. **Source References** — Link conclusions to supporting sources
3. **Evidence References** — Explicitly model evidence chains
4. **Contributor Attribution** — Track who added what and when
5. **Analysis Documents** — Written reasoning and proof arguments
6. **Confidence Levels** — Express certainty about conclusions

### Evolution Timeline

```
1984: GEDCOM created by LDS Church
1995: GEDCOM 5.5 released
1999: GEDCOM 5.5.1 (minor update)
2012: GEDCOM X introduced (evidence-based model)
2021: FamilySearch GEDCOM 7.0 (modernized file format)
```

---

## Complex Family Situations

### Adoption Modeling

**GEDCOM approach:**
```
0 @I1@ INDI
1 NAME Adopted /Child/
1 FAMC @F1@           (biological family)
2 PEDI birth
1 FAMC @F2@           (adoptive family)
2 PEDI adopted
1 ADOP                (adoption event)
2 DATE 11 JAN 1990
2 FAMC @F2@           (which family adopted)
3 ADOP BOTH           (both parents adopted)
```

**FamilySearch approach:**
- Create `Child-and-Parents` relationship to biological parents with `BiologicalParent` fact
- Create separate `Child-and-Parents` relationship to adoptive parents with `AdoptiveParent` fact
- Both relationships coexist

### Step-Parent Families

When a biological parent remarries:
1. Child has `BiologicalParent` relationship to birth parents
2. Child can have `StepParent` relationship to parent's new spouse
3. No need to modify biological relationships

### Blended Families ("Patchwork Families")

Multiple FAMC (family child) links handle complex blended families:
- Each child links to their biological parents
- Additional links for step/adoptive relationships
- Couple relationships tie adults together

### Same-Sex Relationships

**FamilySearch (as of recent update):**
- Allows documenting same-sex marriages and adoptions
- Spouse selection no longer restricted by sex
- Photos, stories, documents accepted for same-sex relationships
- Required significant technical redesign of tree search systems

**Limitations:**
- FamilySearch is operated by LDS Church
- Same-sex couples cannot be sealed in temple
- Children cannot be sealed to same-sex parents
- This is genealogical documentation, not religious endorsement

**GEDCOM 7.0:**
- Updated to allow same-sex partnerships
- HUSB/WIFE terminology being reconsidered for neutrality

---

## Limitations and Criticisms

### GEDCOM 5.5 Problems

| Issue | Description |
|-------|-------------|
| **Nuclear family assumption** | Original design assumed husband/wife/children model |
| **No embedded media** | Only links to external files |
| **Inconsistent implementations** | Software interprets spec differently |
| **Proprietary extensions** | Vendors add non-standard tags |
| **Slow evolution** | 26 years between 5.5.1 and 7.0 |
| **Contradictions in spec** | Some requirements are internally inconsistent |

### The Compliance Paradox

Developers face a dilemma:
- **Comply strictly** with GEDCOM spec → incompatible with common software
- **Match common practice** → deviate from official standard

Many genealogy programs don't fully implement the standard, creating an ecosystem of partial compatibility.

### Family-Centric Model Limitations

The FAM record assumes:
- Exactly 0-2 adults (HUSB/WIFE)
- Any number of children
- Adults are in a "couple" relationship

This struggles with:
- Polyamorous relationships
- Communal child-rearing
- Cultures with different family structures
- Situations where "family" has different meaning

### Evidence Model Adoption

While GEDCOM X has excellent evidence modeling, many users:
- Don't use confidence levels
- Skip source citations
- Treat it like GEDCOM 5.5 (conclusions only)

The tools support sophisticated research; user behavior lags.

---

## Data Structures Reference

### GEDCOM 5.5.1 Individual Record

```
0 @I1@ INDI
1 NAME John /Smith/
1 SEX M
1 BIRT
2 DATE 1 JAN 1900
2 PLAC New York, New York
1 DEAT
2 DATE 15 MAR 1975
2 PLAC Los Angeles, California
1 FAMC @F1@           (family as child)
2 PEDI birth
1 FAMS @F2@           (family as spouse)
```

### GEDCOM 5.5.1 Family Record

```
0 @F1@ FAM
1 HUSB @I2@
1 WIFE @I3@
1 CHIL @I1@
1 MARR
2 DATE 15 JUN 1985
2 PLAC Chicago, Illinois
1 DIV
2 DATE 3 MAR 1995
```

### GEDCOM X Relationship (JSON)

```json
{
  "id": "R1",
  "type": "http://gedcomx.org/Couple",
  "person1": { "resource": "#P1" },
  "person2": { "resource": "#P2" },
  "facts": [
    {
      "type": "http://gedcomx.org/Marriage",
      "date": { "original": "15 June 1985" },
      "place": { "original": "Chicago, Illinois" },
      "confidence": "http://gedcomx.org/High"
    }
  ],
  "sources": [
    { "description": "#S1" }
  ]
}
```

### GEDCOM X Parent-Child Relationship (JSON)

```json
{
  "id": "R2",
  "type": "http://gedcomx.org/ParentChild",
  "person1": { "resource": "#P1" },  // parent
  "person2": { "resource": "#P3" },  // child
  "facts": [
    {
      "type": "http://gedcomx.org/BiologicalParent"
    }
  ]
}
```

---

## Lessons for Entity Graphs

### 1. Two Relationship Types Are Enough

FamilySearch models all family structures with just:
- Couple relationships
- Parent-child relationships

Sibling, grandparent, cousin, etc. are **computed**, not stored.

### 2. Relationships Are Entities, Not Edges

Relationships in GEDCOM X have:
- Their own IDs
- Facts/events attached
- Source citations
- Confidence levels
- Temporal data

They're full entities, not just foreign keys.

### 3. Evidence Matters

Sophisticated systems separate:
- **Information** — raw data from sources
- **Evidence** — information that answers a question
- **Conclusion** — accepted answer with supporting evidence

This three-layer model enables proper reasoning and revision.

### 4. Temporal Relationships Need Events

Don't model "married: true/false". Model:
- Marriage event (date, place)
- Divorce event (date, place)
- Remarriage event (date, place)

The current status is computed from event history.

### 5. Multiple Relationship Instances

A person can have multiple:
- Parent relationships (biological + adoptive + step)
- Spouse relationships (sequential marriages)
- The same two people can have multiple relationships (married, divorced, remarried)

### 6. Types Are Extensible

Both GEDCOM and GEDCOM X support:
- Standard relationship types
- Custom types via data URIs
- Extension mechanisms for domain-specific needs

---

## Key Resources

### Specifications
- [FamilySearch GEDCOM 7.0](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html)
- [GEDCOM X Specifications](https://gedcomx.org/Specifications.html)
- [GEDCOM X Conceptual Model](https://github.com/FamilySearch/gedcomx/blob/master/specifications/conceptual-model-specification.md)

### Developer Documentation
- [FamilySearch Family Tree Data Model](https://developers.familysearch.org/main/docs/the-family-tree-data-model)
- [FamilySearch Facts Guide](https://www.familysearch.org/developers/docs/guides/facts)
- [Child-and-Parents Relationship API](https://www.familysearch.org/developers/docs/api/tree/Child-and-Parents_Relationship_resource)
- [Couple Relationship API](https://www.familysearch.org/developers/docs/api/tree/Couple_Relationship_resource)

### Research Standards
- [Genealogical Proof Standard](https://www.familysearch.org/en/wiki/Genealogical_Proof_Standard)
- *Evidence Explained* by Elizabeth Shown Mills
- *Mastering Genealogical Proof* by Thomas W. Jones
- *Genealogy Standards* from Board for Certification of Genealogists

### Community Resources
- [GEDCOM.io](https://gedcom.io/) — Official GEDCOM specification site
- [GEDCOM X](https://gedcomx.org/) — GEDCOM X documentation
- [Tamura Jones GEDCOM Articles](https://www.tamurajones.net/) — Excellent technical analysis

---

## Open Questions

1. **How do other cultures model family?** — GEDCOM assumes Western nuclear family. What about extended family structures, clan systems, or cultures with different kinship terminology?

2. **What's the right abstraction level?** — FamilySearch's two-relationship model is elegant but requires computation for common queries (siblings, grandparents). Is this the right trade-off?

3. **How should confidence propagate?** — If a parent-child relationship has low confidence, how does that affect inferred relationships (siblings, grandparents)?

4. **Relationship vs. Role?** — Is "biological parent" a relationship type or a role within a parent-child relationship? GEDCOM X uses "facts" on relationships, which is role-like.

5. **Time modeling** — Relationships have beginnings (marriage) and endings (divorce, death). How granular should temporal modeling be?
