---
title: Schema.org Relationship Modeling Research
description: How Schema.org and Google Structured Data express relationships between entities.
---

## Why This Matters

Understanding Schema.org's relationship model is critical because:

1. **Schema.org is the web standard** — Used on 45+ million domains, co-created by Google, Microsoft, Yahoo, Yandex
2. **Google interprets these relationships** — Affects Knowledge Graph, search understanding, AI reasoning
3. **JSON-LD is the preferred format** — 83% adoption; Google's recommended approach
4. **Pragmatic design over academic purity** — Tradeoffs made for real-world adoption

This document focuses specifically on **RELATIONSHIPS**, not entity types.

---

## Core Relationship Types

### Person-to-Person Relationships

| Property | Description | Directionality | Notes |
|----------|-------------|----------------|-------|
| `knows` | Most generic bi-directional social/work relation | Symmetric | Deliberately generic; equivalent to FOAF's `foaf:knows` |
| `spouse` | Person's spouse | Symmetric | Expects Person |
| `colleague` | A colleague of the person | Symmetric | Accepts Person or URL |
| `relatedTo` | Most generic familial relation | Symmetric | For family connections |
| `parent` | A parent of this person | Directional | Inverse: `children` |
| `children` | A child of the person | Directional | Inverse: `parent` |
| `sibling` | A sibling of the person | Symmetric | No explicit inverse needed |
| `follows` | Most generic uni-directional social relation | Directional | Social media-style following |

**Key Insight**: Schema.org deliberately uses generic terms (`knows`, `relatedTo`) rather than granular relationship types. This is a conscious design choice favoring broad adoption over precise semantics.

### Person-to-Organization Relationships

| Property | Description | Direction | Notes |
|----------|-------------|-----------|-------|
| `worksFor` | Organizations that person works for | Person → Org | Current employment |
| `affiliation` | Organization person is affiliated with | Person → Org | Broader than employment (schools, clubs, teams) |
| `memberOf` | Organization/ProgramMembership person belongs to | Person → Org | Has inverse: `member` |
| `alumniOf` | Organization person is alumni of | Person → Org | Has inverse: `alumni` |
| `sponsor` | Person/org that supports something | Either direction | Financial/support relationship |
| `funder` | Person/org providing financial contribution | Either direction | More specific than sponsor |

### Organization Relationships

| Property | Description | Direction | Inverse |
|----------|-------------|-----------|---------|
| `member` | Member of an Organization | Org → Person/Org | `memberOf` |
| `employee` | Someone working for the organization | Org → Person | — |
| `founder` | Person/org who founded this organization | Org → Person/Org | — |
| `alumni` | Alumni of the organization | Org → Person | `alumniOf` |
| `parentOrganization` | Parent organization | Org → Org | `subOrganization` |
| `subOrganization` | Subsidiary/child organization | Org → Org | `parentOrganization` |

### Part-Whole Relationships

| Property | Description | Domain | Inverse |
|----------|-------------|--------|---------|
| `hasPart` | Indicates something contains parts | CreativeWork, Place | `isPartOf` |
| `isPartOf` | Indicates something is part of a larger whole | CreativeWork, Place | `hasPart` |
| `containedInPlace` | Geographic containment | Place | `containsPlace` |
| `containsPlace` | Place contains another place | Place | `containedInPlace` |

### Content Relationships

| Property | Description | Direction | Notes |
|----------|-------------|-----------|-------|
| `author` | Who created it | CreativeWork → Person/Org | |
| `creator` | Broader than author | CreativeWork → Person/Org | For non-textual works |
| `publisher` | Who published it | CreativeWork → Person/Org | |
| `contributor` | Secondary contributor | CreativeWork → Person/Org | |
| `about` | Subject matter | CreativeWork → Thing | What the work is about |
| `mentions` | References another thing | CreativeWork → Thing | Weaker than `about` |

---

## Relationship Directionality & Inverse Properties

### The `inverseOf` Meta-Property

Schema.org explicitly declares inverse relationships using the `inverseOf` property at the schema level:

```
alumni → inverseOf → alumniOf
member → inverseOf → memberOf
hasPart → inverseOf → isPartOf
parentOrganization → inverseOf → subOrganization
owns → inverseOf → owner
makesOffer → inverseOf → offeredBy
mainEntity → inverseOf → mainEntityOfPage
```

**Key Properties with Declared Inverses:**

| Property | Inverse Property |
|----------|------------------|
| `alumniOf` | `alumni` |
| `memberOf` | `member` |
| `isPartOf` | `hasPart` |
| `parentOrganization` | `subOrganization` |
| `owns` | `owner` |
| `makesOffer` | `offeredBy` |
| `mainEntityOfPage` | `mainEntity` |
| `about` | `subjectOf` |
| `funding` | `fundedItem` |

### Properties WITHOUT Explicit Inverses

Many Schema.org relationships lack declared inverses:

- `worksFor` — No inverse like `employs` (use `employee` on Organization instead)
- `knows` — Bi-directional by definition, no formal inverse
- `spouse` — Symmetric, no inverse needed
- `author` — No formal inverse (though `creator` property exists)
- `parent`/`children` — These ARE inverses of each other but not formally declared

**Practical Implication**: When an inverse doesn't exist, you must:
1. Express the relationship from both directions explicitly
2. Use JSON-LD's `@reverse` keyword
3. Let consuming applications infer the inverse

### JSON-LD `@reverse` for Missing Inverses

When Schema.org lacks a property for the inverse direction, JSON-LD provides `@reverse`:

```json
{
  "@context": "https://schema.org",
  "@type": "WebPage",
  "@reverse": {
    "mentions": [
      {
        "@type": "WebPage",
        "url": "https://example.com/page-that-links-to-me"
      }
    ]
  }
}
```

This expresses "this other page mentions me" when you can only say "I mention them" with the standard property.

**Important**: Google's Rich Results Test validates `@reverse` syntax, but it's unclear how much Google uses reverse relationships for knowledge extraction.

---

## Temporal Relationships

### The Role Pattern

Schema.org handles time-bound relationships through the **Role** type:

```json
{
  "@context": "https://schema.org",
  "@type": "SportsTeam",
  "name": "San Francisco 49ers",
  "member": {
    "@type": "OrganizationRole",
    "member": {
      "@type": "Person",
      "name": "Joe Montana"
    },
    "startDate": "1979",
    "endDate": "1992",
    "roleName": "Quarterback"
  }
}
```

**Role Properties:**
- `startDate` — When the role began (ISO 8601 format)
- `endDate` — When the role ended (ISO 8601 format)
- `roleName` — Specific name of the role (e.g., "Quarterback", "CEO")

**Role Subtypes:**
- `Role` — Generic role wrapper
- `OrganizationRole` — For organizational membership with `numberedPosition`
- `EmployeeRole` — Adds `baseSalary`, `salaryCurrency` for employment
- `PerformanceRole` — For performers (characterName)
- `LinkRole` — For qualifying hyperlinks

### Temporal Properties on Entities

Direct temporal properties (without Role wrapper):

| Property | Used On | Purpose |
|----------|---------|---------|
| `startDate` | Event, Role, Schedule, CreativeWorkSeason | When something begins |
| `endDate` | Event, Role, Schedule, CreativeWorkSeason | When something ends |
| `validFrom` | Offer, PriceSpecification, Permit | When something becomes valid |
| `validThrough` | Offer, JobPosting, Demand | When validity expires |
| `birthDate` | Person | Date of birth |
| `deathDate` | Person | Date of death |
| `foundingDate` | Organization | When org was founded |
| `dissolutionDate` | Organization | When org was dissolved |
| `datePublished` | CreativeWork | Publication date |
| `dateCreated` | CreativeWork | Creation date |
| `dateModified` | CreativeWork | Last modification |

**Key Distinction:**
- `startDate`/`endDate` — For events and time-bound activities
- `validFrom`/`validThrough` — For validity periods (offers, pricing, permits)

### Example: Time-Qualified Employment

```json
{
  "@context": "https://schema.org/",
  "@type": "Person",
  "name": "Albert Einstein",
  "hasOccupation": [
    {
      "@type": "Role",
      "hasOccupation": {
        "@type": "Occupation",
        "name": "Patent examiner",
        "occupationalCategory": "23-2099.00"
      },
      "startDate": "1901",
      "endDate": "1906"
    },
    {
      "@type": "Occupation",
      "name": "Professor of Physics",
      "educationRequirements": "PhD in Physics"
    }
  ]
}
```

---

## Relationship Strength & Weight

### What Schema.org DOESN'T Have

**Schema.org has no built-in mechanism for:**
- Relationship strength/intensity (1-10 scale)
- Acquaintance vs friend vs close friend
- Confidence levels
- Frequency of interaction
- Emotional closeness

This is a significant limitation for social/personal relationship modeling.

### Alternative: The RELATIONSHIP Vocabulary

The [RELATIONSHIP vocabulary](https://vocab.org/relationship/) extends FOAF with more granular relationship types:

| Relationship | Definition |
|--------------|------------|
| `acquaintanceOf` | More than slight knowledge but short of friendship |
| `friendOf` | Mutual friendship |
| `closeFriendOf` | Close mutual friendship |
| `parentOf` | Parent of this person |
| `childOf` | Child of this person |
| `spouseOf` | Married to |
| `lifePartnerOf` | Domestic partner |
| `enemyOf` | Mutual enmity |
| `collaboratesWith` | Working together on a project |
| `employerOf` | Employs this person |
| `employedBy` | Employed by this person |
| `mentorOf` | Acts as mentor |
| `apprenticeTo` | Apprentice of |

**Note**: This vocabulary is **categorical** (friend vs acquaintance) rather than **quantitative** (strength = 0.7).

### Workaround: Custom Extensions

For relationship strength, you'd need custom properties:

```json
{
  "@context": {
    "@vocab": "https://schema.org/",
    "relationshipStrength": "https://example.org/relationshipStrength"
  },
  "@type": "Person",
  "name": "Alice",
  "knows": {
    "@type": "Person", 
    "name": "Bob",
    "relationshipStrength": 0.8
  }
}
```

However, Google won't interpret custom properties for search features.

---

## Property Hierarchy & Specificity

### subPropertyOf Relationships

Schema.org uses `subPropertyOf` to establish property hierarchies:

- If property `A` is a subproperty of `B`, then `A` implies `B`
- Example: If `author` were subproperty of `creator`, every author would also be a creator

**Example Hierarchies:**
```
affiliation → subPropertyOf → memberOf (affiliation is more specific)
```

### Generic vs Specific Properties

| Generic | Specific Alternatives |
|---------|----------------------|
| `knows` | `colleague`, `spouse`, `sibling` |
| `relatedTo` | `parent`, `children`, `spouse` |
| `creator` | `author`, `illustrator`, `composer` |
| `contributor` | `editor`, `translator` |

**Recommendation**: Use the most specific property that applies. Use generic properties (`knows`, `relatedTo`) only when more specific ones don't fit.

---

## JSON-LD Expression Patterns

### Basic Relationship

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Jane Doe",
  "colleague": [
    "http://www.xyz.edu/students/alicejones.html",
    "http://www.xyz.edu/students/bobsmith.html"
  ]
}
```

Note: Relationships can accept URLs as values (not just embedded objects).

### Nested Entity Relationship

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "George Bush",
  "disambiguatingDescription": "41st President of the United States",
  "children": {
    "@type": "Person",
    "name": "George W. Bush",
    "disambiguatingDescription": "43rd President of the United States"
  }
}
```

### Referenced Entity (Same Document)

```json
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@id": "#person1",
      "@type": "Person",
      "name": "Alice",
      "knows": {"@id": "#person2"}
    },
    {
      "@id": "#person2",
      "@type": "Person",
      "name": "Bob",
      "knows": {"@id": "#person1"}
    }
  ]
}
```

### Cross-Site Identity with `sameAs`

```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Tim Berners-Lee",
  "sameAs": [
    "https://www.wikidata.org/wiki/Q80",
    "https://en.wikipedia.org/wiki/Tim_Berners-Lee",
    "https://twitter.com/timberners_lee"
  ]
}
```

**`sameAs` is critical for entity reconciliation** — it declares "this entity is the same as that entity on another site."

---

## Known Limitations & Controversies

### 1. Symmetric vs Asymmetric Ambiguity

`knows` is defined as "bi-directional" but there's no formal mechanism ensuring symmetry. If Alice `knows` Bob, must Bob `knows` Alice be stated?

**Schema.org's answer**: Both directions should be stated explicitly for clarity. The schema doesn't enforce symmetry.

### 2. No Relationship Reification (Native)

Schema.org doesn't have native relationship reification (making statements about statements). The Role pattern is a workaround, not true reification.

**Example problem**: "Alice worked for Company X from 2010-2015, introduced by Bob"

The Role pattern handles dates but not "introduced by Bob."

### 3. Incomplete Inverse Coverage

Many useful inverses aren't defined:
- `worksFor` has no `employs` inverse
- `author` has no `authorOf` inverse
- `knows` (symmetric) doesn't need inverse, but tooling doesn't always recognize this

### 4. Flat Over Normalized

Schema.org prioritizes "something is better than nothing" over precise semantics:

> "The vocabulary is intentionally 'flat and less normalized' rather than database-oriented"

This means:
- Properties accept `Text` even when specific types are expected
- Relationships can be URLs or embedded objects
- Data quality varies wildly in the wild

### 5. No Cardinality Constraints

All properties are multi-value by default. There's no way to say "a Person can have only one spouse" (legally debatable anyway).

### 6. Limited Provenance

No native properties for:
- Who asserted this relationship
- When was it asserted
- Confidence level
- Source of information

### 7. Datatype Issues

Schema.org creates custom datatypes (like `schema:Text`, `schema:URL`) that duplicate XSD standards, causing interoperability issues with RDF tools.

---

## Recent Evolution (2024-2025)

### Version 29.4 (December 2025)

Recent additions relevant to relationships:

- `lifeEvent` property added to Person (accepts Event type)
- `linkRelationship` property for web link relationships
- Enhanced event types: `ConferenceEvent`, `PerformingArtsEvent`, `InstantaneousEvent`
- OWL equivalences added for external ontology interoperability

### Ongoing Patterns

1. **More event/action types** — Moving beyond static entities to temporal occurrences
2. **Cross-vocabulary alignment** — Better interop with GS1, UN/CEFACT
3. **Pending vocabulary growth** — 825+ terms in pending section
4. **Extension namespaces** — Domain-specific vocabularies (health, auto)

---

## Comparison with Other Vocabularies

### Schema.org vs FOAF

| Aspect | Schema.org | FOAF |
|--------|------------|------|
| Relationship granularity | Generic (`knows`) | Also generic (`knows`) |
| Extensions | Via properties | RELATIONSHIP vocabulary |
| Adoption | 45M+ domains | Academic/semantic web |
| JSON-LD support | Native | Supported |
| Google interpretation | Yes | Limited |

### Schema.org vs Wikidata

| Aspect | Schema.org | Wikidata |
|--------|------------|----------|
| Relationship model | Properties on entities | Statements with qualifiers |
| Temporal support | Role pattern | Qualifiers (start time, end time) |
| Provenance | Not native | References on statements |
| Reification | Limited (Role) | Full qualifier support |
| Scale | 1,528 properties | 12,000+ properties |

---

## Implications for Entity Modeling

### What to Adopt from Schema.org

1. **Relationships as properties** — Simple, widely understood model
2. **Inverse property pairs** — Declare both directions for important relationships
3. **Role pattern for temporal** — Wrap relationships that need dates
4. **`sameAs` for identity** — Critical for cross-source reconciliation
5. **Generic + specific** — Have both `knows` and `colleague`, `spouse`, etc.

### What to Extend Beyond Schema.org

1. **Relationship strength/weight** — Add custom properties if needed
2. **Provenance** — Track who asserted relationships and when
3. **Confidence levels** — Useful for AI-extracted relationships
4. **Richer temporal model** — Consider Wikidata-style qualifiers
5. **Bi-directional enforcement** — If A knows B, create B knows A automatically

### Recommended Core Relationship Properties

For a personal knowledge graph, consider:

**Person-Person:**
- `knows` (generic)
- `relatedTo` (family - generic)
- `spouse`, `parent`, `children`, `sibling` (family - specific)
- `colleague`, `collaboratesWith` (professional)

**Person-Organization:**
- `memberOf` / `member`
- `worksFor` / `employee` (or custom `employs`)
- `alumniOf` / `alumni`
- `affiliation`
- `founded` / `founder`

**Content:**
- `author` / `creator`
- `about` / `mentions`
- `isPartOf` / `hasPart`

**Identity:**
- `sameAs` — Always include for cross-referencing

---

## Sources

### Primary Sources

**Schema.org Official:**
- https://schema.org/Person — Person type with all relationship properties
- https://schema.org/knows — "knows" property definition
- https://schema.org/spouse — Spouse property
- https://schema.org/colleague — Colleague property
- https://schema.org/memberOf — MemberOf property
- https://schema.org/Role — Role type for temporal qualification
- https://schema.org/inverseOf — Inverse property meta-definition
- https://schema.org/hasPart — Part-whole relationship
- https://schema.org/isPartOf — Inverse of hasPart
- https://schema.org/startDate — Temporal property
- https://schema.org/validFrom — Validity property

**JSON-LD:**
- https://w3c.github.io/json-ld-bp/ — JSON-LD Best Practices (W3C)
- https://json-ld.github.io/json-ld.org/spec/latest/json-ld-api-best-practices/ — API best practices
- https://www.w3.org/ns/json-ld — JSON-LD vocabulary (includes @reverse)

**Alternative Vocabularies:**
- https://vocab.org/relationship/ — RELATIONSHIP vocabulary for FOAF
- https://gmpg.org/xfn/and/foaf — XFN and FOAF comparison
- https://www.w3.org/2001/sw/Europe/events/foaf-galway/papers/fp/ontological_consideration_on_human_relationship_vocabulary/ — FOAF relationship ontology research

### Technical References

**Inverse Properties:**
- https://schema.org/inverseOf — Meta-property definition
- https://www.w3.org/wiki/WebSchemas/InverseProperties — W3C WebSchemas discussion

**Temporal Modeling:**
- https://schema.org/EmployeeRole — Employee role with salary
- https://schema.org/OrganizationRole — Organization role with position
- https://www.w3.org/wiki/images/2/22/RolesinSchema.orgMar26.pdf — Roles in Schema.org (W3C)

**Limitations & Criticism:**
- https://github.com/schemaorg/schemaorg/issues/1781 — Datatype duplication issues
- https://github.com/schemaorg/schemaorg/issues/1896 — subPropertyOf inference questions
- https://queue.acm.org/detail.cfm?id=2857276 — "Schema.org: Evolution" (ACM) — discusses pragmatic constraints
- https://stackoverflow.com/questions/27149247/use-schema-org-as-database-schema-a-rational-approuch — Database schema concerns

**JSON-LD @reverse:**
- https://www.richeyweb.com/blog/seo/self-reporting-backlinks-with-json-ld-reverse — Practical @reverse examples
- https://json-ld.org/spec/latest/json-ld-connect/ — JSON-LD Connect spec

### Schema.org Releases

- https://www.schema.org/docs/releases.html — Full release history
- https://schema.org/version/latest — Current version (29.4 as of Dec 2025)

---

## Session Log

### 2025-01-24: Initial Research

- Created focused research document on Schema.org relationships
- Web searches covering:
  - Core relationship properties (knows, spouse, colleague, memberOf)
  - JSON-LD relationship patterns
  - Inverse properties and directionality
  - Temporal relationships (Role pattern, startDate/endDate)
  - Relationship strength limitations
  - Recent Schema.org evolution (v29.4)
  - Known limitations and criticisms
- Fetched and analyzed complete Schema.org Person type definition
- Compared with FOAF, RELATIONSHIP vocabulary, Wikidata approaches

**Key Findings:**
1. Schema.org uses **generic relationship types** (`knows`) by design
2. **Role pattern** is the standard for time-bound relationships
3. **No native support** for relationship strength/weight
4. `@reverse` in JSON-LD enables inverse relationships not in schema
5. ~40% of relationship properties have explicit inverses
6. Pragmatic design prioritizes adoption over semantic precision

**Implications for Our Project:**
- Use Schema.org property names for interoperability
- Extend with custom properties for strength/confidence if needed
- Implement Role pattern for temporal relationships
- Always create both directions of important relationships
- Include `sameAs` for entity reconciliation
