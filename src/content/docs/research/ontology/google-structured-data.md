---
title: Google Structured Data & Knowledge Graph Research
description: Google's entity-based approach to search, from the Knowledge Graph to modern structured data.
---

## Why This Matters

Google is moving from keyword-based search to **entity-based understanding**. They said "things, not strings" back in 2012. This has massive implications:

1. **Knowledge Graph** — Google's database of 500+ billion facts about entities
2. **Schema.org** — Google co-created the vocabulary standard
3. **Structured Data** — JSON-LD, microdata that websites use to describe entities
4. **Entity-first SEO** — The future of search is entity recognition

If Google is betting on entities, we should understand how they model them.

---

## Research Tasks

### Knowledge Graph
- [x] When did Google launch Knowledge Graph? (May 16, 2012)
- [x] How many entities does it contain? (5 billion entities, 500 billion facts as of 2020)
- [x] What entity types exist in Knowledge Graph?
- [x] How do they resolve entity identity? (Machine IDs / MIDs)
- [x] How do they handle relationships? (Graph structure with edges as relationships)
- [x] Who built it? Key engineers/researchers?

### Schema.org
- [x] Google's role in creating Schema.org (co-founded with Microsoft, Yahoo, Yandex in 2011)
- [x] What types does Schema.org define? (827 Types, 1,528 Properties)
- [x] How does the type hierarchy work? (Multiple inheritance from Thing)
- [x] Most important types for search (Person, Organization, Product, etc.)
- [x] How has it evolved? (Community-driven via W3C Community Group)

### Structured Data
- [x] JSON-LD format deep dive
- [x] Required vs recommended properties
- [x] How Google uses structured data for rich results
- [x] Common patterns: Article, LocalBusiness, Product, Event, FAQ
- [x] Validation: Rich Results Test

### Entity-Based Search (2024-2025)
- [x] Recent announcements about entity-first search
- [x] How AI/LLMs are changing entity recognition (Gemini integration)
- [x] Implications for SEO
- [x] What new entity types are emerging?

### Wikidata Integration
- [x] How does Google use Wikidata?
- [x] Knowledge Graph vs Wikidata relationship
- [x] Entity reconciliation across sources

### People
- [x] Who led Knowledge Graph development?
- [x] Key researchers at Google on entity recognition
- [x] Schema.org founders/maintainers

---

## Key People

| Person | Role | Organization | Era |
|--------|------|--------------|-----|
| **Amit Singhal** | SVP Engineering, Search | Google | 2000-2016 |
| **John Giannandrea** | Director of Engineering (KG), later SVP Search | Google → Apple | 2010-2018 |
| **R.V. Guha** | Google Fellow, Schema.org founder/chair | Google → OpenAI → Microsoft | 2005-present |
| **Dan Brickley** | Schema.org daily operations, W3C Community Group chair | Google | 2011-present |
| **Steve Macbeth** | Microsoft Schema.org co-founder | Microsoft | 2009-2020 |
| **Peter Mika** | Yahoo Schema.org lead, semantic search | Yahoo | 2011-2016 |
| **Danny Hillis** | Metaweb/Freebase co-founder | Metaweb | 2005-2010 |
| **Robert Cook** | Metaweb/Freebase co-founder | Metaweb | 2005-2010 |
| **Jack Menzel** | Product Management, Google Search | Google | 2010s |
| **Johanna Wright** | Product Manager, Google Search | Google | 2010s |

### R.V. Guha — The Semantic Web Pioneer

**Full career arc:**
- **1987-1994**: Co-leader of Cyc Project at MCC. Designed CycL (representation language), upper ontological layers, NLU components
- **1995-1997**: Apple Computer's Advanced Technology Group. Created Meta Content Framework (MCF), FlyThru visualization
- **1997-1999**: Principal Engineer at Netscape. Created RSS and RDF (with W3C/Tim Bray), helped establish Open Directory Project
- **1999-2000**: Co-founded Epinions (Web of Trust concept)
- **2000-2002**: Founded Alpiri, created TAP (semantic web application)
- **2002-2005**: IBM Almaden Theory group
- **2005-2024**: Google Fellow. Started Google Custom Search, **Schema.org**, and Data Commons
- **Aug 2024**: Moved to OpenAI as Technical Advisor to CEO
- **May 2025**: Joined Microsoft as Technical Fellow working on NLWeb

### John Giannandrea — From Freebase to Knowledge Graph

- CTO of Netscape (related browsing technology)
- Co-founded Metaweb, helped build Freebase
- Joined Google in 2010 when Google acquired Metaweb
- **Led the creation of Google Knowledge Graph** (launched May 2012)
- Appointed Google search chief in 2016, replacing Amit Singhal
- Left Google in 2018 to join Apple as SVP of Machine Learning and AI Strategy
- Announced retirement December 2025

---

## Findings

### Knowledge Graph Architecture

**Launch & Scale:**
- Launched **May 16, 2012** with 500 million entities, 3.5 billion facts
- By 2020: **5 billion entities**, **500 billion facts**
- Tripled in size within 7 months of launch (570M entities, 18B facts)

**Philosophy:**
> "Things, not strings" — Google's fundamental shift from keyword matching to entity understanding

**Data Sources:**
- Freebase (acquired 2010 from Metaweb)
- Wikipedia
- CIA World Factbook
- Google Books
- Online event listings
- Web crawl data
- Commercial datasets (undisclosed)
- Wikidata (after Freebase sunset)

**Primary Entity Categories:**
- **People** — individuals, historical figures, fictional characters
- **Places** — locations, landmarks, cities, geographical features
- **Things** — products, objects, concepts
- **Organizations** — companies, institutions, groups
- **Events** — occurrences at specific times/locations
- **Creative Works** — books, movies, music, articles

**Entity Identity Resolution:**
- Uses **Machine IDs (MIDs)** — globally unique identifiers
- Format examples: `/m/0dl567` (Taylor Swift in original KG), `c-024dcv3mk` (Cloud KG)
- MID namespaces: `c` (Cloud KG), `r` (reconciliation candidate), `e` (reconciled master)
- Entity Reconciliation API handles deduplication across sources
- Creates master entity with new MID when merging

**Graph Structure:**
- Non-hierarchical graph: nodes (topics/entities) connected by edges (relationships)
- Each entity can have multiple types assigned
- Relationships are typed and can carry attributes

---

### Schema.org Type Hierarchy

**Current Scale (as of 2024):**
- **827 Types** (classes)
- **1,528 Properties**
- **14 Datatypes**
- **94 Enumerations** with 522 enumeration members
- Used on **45+ million web domains**
- Over **450 billion Schema.org objects** marked up

**Founding (2011):**
- Co-created by **Google, Microsoft (Bing), Yahoo, and Yandex**
- Key founders: R.V. Guha (Google), Steve Macbeth (Microsoft), Peter Mika (Yahoo), Alex Shubin (Yandex)
- Based on RDF Schema (derived from CycL)
- Pragmatic design over academic purity

**Hierarchy Design:**
- **Thing** is the root type — all other types inherit from it
- **Multiple inheritance** — types can have multiple parent types
- Properties can have multiple domains and ranges
- Avoids creating artificial types

**Core Type Branches (direct children of Thing):**

```
Thing
├── Action (performed by agent on object)
│   ├── AchieveAction, AssessAction, ConsumeAction
│   ├── CreateAction, InteractAction, MoveAction
│   ├── OrganizeAction, PlayAction, SearchAction
│   ├── TradeAction, TransferAction, UpdateAction
│   └── ... (100+ action subtypes)
├── BioChemEntity
│   └── Gene, Protein, MolecularEntity, ChemicalSubstance
├── CreativeWork
│   ├── Article → NewsArticle, BlogPosting, ScholarlyArticle
│   ├── Book → Audiobook
│   ├── Dataset, SoftwareApplication, WebPage
│   ├── Movie, MusicRecording, Photograph
│   └── ... (100+ subtypes)
├── Event
│   ├── BusinessEvent, MusicEvent, SportsEvent
│   ├── ConferenceEvent, Festival, Hackathon
│   └── ... (30+ event types)
├── Intangible (utility class)
│   ├── Brand, Language, Occupation, Service
│   ├── Offer, Order, Invoice, Reservation
│   ├── Rating, Role, Schedule
│   └── ... (200+ intangible types)
├── MedicalEntity
│   └── AnatomicalStructure, Drug, MedicalCondition...
├── Organization
│   ├── Corporation, EducationalOrganization
│   ├── GovernmentOrganization, LocalBusiness
│   ├── MedicalOrganization, PerformingGroup
│   └── ... (150+ org subtypes)
├── Person (alive, dead, undead, or fictional)
├── Place
│   ├── Accommodation, AdministrativeArea, CivicStructure
│   ├── Landform, LocalBusiness (also under Organization)
│   └── ... (100+ place types)
├── Product
│   ├── IndividualProduct, ProductGroup, Vehicle
│   └── Drug, DietarySupplement
└── Taxon (biological taxonomy)
```

**Key Property Categories:**

| Type | Key Properties |
|------|----------------|
| **Person** | name, birthDate, birthPlace, affiliation, jobTitle, email, alumniOf, colleague, children |
| **Organization** | name, address, contactPoint, founder, employee, numberOfEmployees, areaServed |
| **CreativeWork** | name, author, datePublished, about, publisher, copyrightHolder |
| **Event** | name, startDate, endDate, location, organizer, performer, offers |
| **Place** | name, address, geo (coordinates), containedInPlace, openingHours |
| **Product** | name, brand, offers, sku, gtin, manufacturer, productID |

**Multi-Typed Entities (MTEs):**
- Single entity can be marked as multiple types simultaneously
- Example: A Book that is also a Product (when it has an Offer)
- Extends multiple inheritance at the instance level

**Extensions:**
- **health-lifesci.schema.org** — Medical/healthcare vocabulary (moved from core in 2016)
- **pending section** — 825 work-in-progress terms
- **auto extension** — Vehicle-specific types

---

### JSON-LD Patterns

**What is JSON-LD?**
- JavaScript Object Notation for Linked Data
- **Google's recommended format** (used in 83.2% of implementations)
- Placed in `<script type="application/ld+json">` tags
- Can appear anywhere in HTML document

**Basic Structure:**
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "John Doe",
  "jobTitle": "Software Engineer",
  "email": "john@example.com"
}
```

**Common Patterns:**

**Article/BlogPosting:**
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Article Title",
  "author": {
    "@type": "Person",
    "name": "Author Name"
  },
  "datePublished": "2024-01-15",
  "publisher": {
    "@type": "Organization",
    "name": "Publisher Name",
    "logo": {
      "@type": "ImageObject",
      "url": "https://example.com/logo.png"
    }
  }
}
```

**LocalBusiness:**
```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Restaurant Name",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "123 Main St",
    "addressLocality": "City",
    "addressRegion": "State"
  },
  "openingHours": "Mo-Sa 11:00-22:00",
  "priceRange": "$$"
}
```

**Product with Offer:**
```json
{
  "@context": "https://schema.org",
  "@type": "Product",
  "name": "Product Name",
  "offers": {
    "@type": "Offer",
    "price": "99.99",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  }
}
```

**FAQPage:**
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [{
    "@type": "Question",
    "name": "What is the question?",
    "acceptedAnswer": {
      "@type": "Answer",
      "text": "The answer text."
    }
  }]
}
```

**Validation Tools:**
- **Rich Results Test** — Google's official validator
- **Schema Markup Validator** — General Schema.org validation
- **Google Search Console** — Rich results performance reporting

**Format Comparison:**

| Format | Recommendation | Notes |
|--------|----------------|-------|
| JSON-LD | **Preferred** | Separate from HTML, easy to manage |
| Microdata | Supported | Embedded in HTML elements |
| RDFa | Supported | Part of broader RDF ecosystem |

---

### Entity-Based Search Evolution

**2012: "Things, Not Strings"**
- Knowledge Graph launch marked shift from keyword matching to entity understanding
- Enabled disambiguation (Taj Mahal: monument vs. musician vs. casino)
- Information panels appear alongside search results

**2016: AI Transition**
- Amit Singhal (search traditionalist) replaced by John Giannandrea (AI/ML head)
- Signaled Google's move toward machine learning-driven search

**2024: AI Overviews**
- May 2024: Introduced AI Overviews powered by custom Gemini model
- Multi-step reasoning beyond simple entity retrieval
- Synthesized answers, not just entity cards

**2025: Gemini 3 Integration**
- November 2025: Gemini 3 brought directly into Search
- "State-of-the-art reasoning, deep multimodal understanding, powerful agentic capabilities"
- Enhanced "query fan-out" for discovering relevant content
- Dynamic visual layouts and interactive tools
- AI Mode for sophisticated research capabilities

**Evolution Pattern:**
1. **2012**: Entity recognition (what is this thing?)
2. **2016**: ML-enhanced entity understanding (context, relationships)
3. **2024**: Entity reasoning (synthesize knowledge about entities)
4. **2025**: Agentic entity interaction (take actions, research deeply)

---

### Freebase → Wikidata Migration

**Freebase History:**
- Created by Metaweb Technologies (founded 2005 by Danny Hillis, Robert Cook, John Giannandrea)
- Collaborative knowledge base with 39+ million topics
- Google acquired Metaweb in July 2010
- Used MQL (Metaweb Query Language) via graphd triplestore
- Had 23,000-40,000 types organized into domains

**Shutdown & Migration:**
- December 2014: Google announced Freebase closure
- Data transferred to Wikidata community
- Initial import covered 10%+ of Freebase collection
- Google released Primary Sources Tool for migration
- Final data dump: 1.9 billion RDF triples

**Entity Reconciliation Challenges:**
- Freebase used domains/types structure
- Wikidata uses properties like "instance of" (P31) instead of formal types
- 4.4 million relations mapped
- Conflicts resolved by preferring Wikidata mappings (6,000 cases)

**Wikidata Entity Model:**
- **Q numbers** — Entity identifiers (Q80 = Tim Berners-Lee)
- **P numbers** — Property identifiers (P108 = employer)
- **L numbers** — Lexeme identifiers (linguistics)
- Statements: Subject (Q) — Predicate (P) — Object (Q or value)
- Qualifiers add context to statements
- Example: Tim Berners-Lee (Q80) — employer (P108) — CERN (Q42944)

---

### Schema.org Governance

**Structure:**
- Independent project with its own steering group (chaired by R.V. Guha)
- W3C Schema.org Community Group handles public discussion
- Dan Brickley chairs Community Group and runs daily operations

**Decision Process:**
1. Proposals discussed via GitHub and public mailing list
2. Webmaster maintains staging site reflecting discussions
3. Release candidates submitted to steering group
4. 10 business day review period
5. Official release every few weeks

**Community Scale:**
- Open participation via W3C Community Group
- Public mailing lists and GitHub issues
- "Early Access Fixes" fast-track for simple changes

---

### Academic Research on Entity Disambiguation

**Key Approaches:**

1. **Freebase-based Disambiguation** (Google Research)
   - Used Freebase's 22M entities (more than Wikipedia)
   - Leveraged naturally disambiguated aliases and rich taxonomy
   - Achieved 90% accuracy without labeled training data

2. **GEEK (Graphical Entity Extraction Kit)**
   - Graph-based entity linking
   - Considers entity commonness, relatedness, contextual similarity
   - Integrates Knowledge Graph and Wikipedia APIs

3. **Plato** (Google)
   - Probabilistic model for entity resolution
   - Handles noisy features
   - Scales to 10^7+ entities
   - Combines Wikipedia training with unlabeled text

4. **SMAPH**
   - Entity recognition in search queries
   - Uses SVM classifiers for disambiguation
   - Handles query brevity and noisy language

---

### Adoption Statistics (2024)

- **44% of websites** use schema markup globally
- **10+ million websites** implement Schema.org
- **83.2% use JSON-LD** as format

**Most Popular Schema Types (Top 1M sites):**
| Type | Adoption |
|------|----------|
| Organization | 22.26% (222,550 sites) |
| Person | 14.37% (143,694 sites) |
| Product | 6.97% (69,747 sites) |
| Offer | 6.54% (65,396 sites) |
| PostalAddress | 6.2% (61,966 sites) |
| AggregateRating | 4.28% (42,752 sites) |

**SEO Impact:**
- Rich results appear in **33%+ of Google searches**
- **88% of featured snippets** pull from schema-enhanced pages
- Case studies show **25-82% increases** in click-through rates

---

## Entity Type Implications

### What We Can Learn from Schema.org

**1. "Thing" as Universal Base**
- Every entity inherits from `Thing`
- Thing has universal properties: `name`, `description`, `url`, `image`, `identifier`
- This provides a consistent baseline for all entities

**2. Multiple Inheritance is Practical**
- Schema.org uses multiple inheritance (type can have multiple parents)
- More flexible than strict single-inheritance hierarchies
- Example: `LocalBusiness` appears under both `Organization` and `Place`
- Reflects real-world messiness

**3. Multi-Typed Entities (MTEs)**
- Single instance can have multiple types
- A `Book` can also be a `Product` (when being sold)
- This is instance-level, not class-level
- **Implication**: Our entities should support multiple type assignments

**4. Properties vs Types**
- Schema.org has 1,528 properties vs 827 types
- Properties carry more information than types
- Relationships are expressed as properties, not separate edge types
- **Implication**: Rich properties may matter more than type granularity

**5. Pragmatic Over Pure**
- Properties accept text even when specific types expected
- Multiple domains/ranges on properties
- Avoiding "artificial types" for technical reasons
- **Implication**: Usability > ontological purity

**6. Core Types Are Few**
- Despite 827 types, the core everyday types are limited:
  - Person, Organization, Place, Event, CreativeWork, Product
- Most sites use just Organization, Person, Product
- **Implication**: Start with 6-10 core types, extend later

**7. Action Types Exist**
- Schema.org has 100+ Action subtypes (CreateAction, UpdateAction, BuyAction...)
- Actions are first-class entities, not just events
- **Implication**: Consider modeling actions/activities as entities

**8. Extensions Are Layered**
- Core vocabulary + pending + extensions (health, auto)
- Domain-specific vocabulary separated from core
- **Implication**: Design for extensibility from day one

---

## Relationship Implications

### How Schema.org Models Relationships

**1. Relationships Are Properties**
- No separate "edge" or "relationship" type
- Relationships are properties on entities
- `author`, `creator`, `memberOf`, `worksFor` — all properties

**2. Key Relationship Properties:**

| Property | Domain | Range | Notes |
|----------|--------|-------|-------|
| `author` | CreativeWork | Person, Organization | Who created it |
| `creator` | CreativeWork | Person, Organization | Broader than author |
| `publisher` | CreativeWork | Organization, Person | Who published it |
| `memberOf` | Person, Organization | Organization | Membership |
| `worksFor` | Person | Organization | Employment |
| `affiliation` | Person | Organization | Any affiliation |
| `alumniOf` | Person | EducationalOrganization | Alumni relationship |
| `parent` / `children` | Person | Person | Family relationships |
| `spouse` | Person | Person | Marriage |
| `colleague` | Person | Person | Professional relationship |
| `knows` | Person | Person | Knows another person |
| `isPartOf` | CreativeWork | CreativeWork | Part/whole |
| `hasPart` | CreativeWork | CreativeWork | Contains parts |
| `subOrganization` | Organization | Organization | Org hierarchy |
| `parentOrganization` | Organization | Organization | Parent org |
| `location` | Event, Organization | Place | Where something is |
| `containedInPlace` | Place | Place | Geographic containment |
| `sameAs` | Thing | URL | Identity across sources |

**3. Inverse Properties**
- `hasPart` ↔ `isPartOf`
- `parentOrganization` ↔ `subOrganization`
- Explicitly defined inverses aid traversal

**4. Role-Based Relationships**
- Schema.org has `Role` type for qualified relationships
- `OrganizationRole`, `PerformanceRole`, `EmployeeRole`
- Allows adding metadata to relationships (start date, end date)
- **Implication**: Consider role/reification for relationship metadata

**5. `sameAs` for Identity**
- Links to equivalent entities on other sites
- Key for entity reconciliation
- Points to authoritative sources (Wikipedia, Wikidata)

**6. Relationship Cardinality**
- Properties are multi-value by default
- Can have multiple authors, multiple locations
- **Implication**: Design for multi-valued relationships

---

## Entity Identity Observations

### How Google Resolves "Same Entity"

**1. Machine IDs (MIDs)**
- Globally unique identifiers per entity
- Different namespaces for different sources
- Master entity created when merging

**2. Reconciliation Approach:**
- Fuzzy text matching on names/aliases
- Common relationships as signals
- Entity types and attributes
- Semantic clustering

**3. Cross-Source Linking:**
- `sameAs` property for web identity
- MID mappings between systems
- Prefer established mappings, resolve conflicts

**4. Multi-Source Truth:**
- No single source of truth
- Entities assembled from multiple sources
- Wikipedia, Wikidata, web crawl, commercial data

**Implications for Our Knowledge Graph:**
- Need stable entity identifiers
- Support for aliases and alternative names
- Explicit cross-reference properties
- Ability to merge entities from different sources
- Confidence/source tracking per fact

---

## Sources

### Primary Sources

**Google Official:**
- https://blog.google/products/search/introducing-knowledge-graph-things-not — Original "Things, Not Strings" announcement (May 2012)
- https://developers.google.com/knowledge-graph — Knowledge Graph Search API documentation
- https://developers.google.com/knowledge-graph/reference/rest/v1 — API Reference (entities.search)
- https://cloud.google.com/enterprise-knowledge-graph/docs/overview — Enterprise Knowledge Graph overview
- https://cloud.google.com/enterprise-knowledge-graph/docs/mid — Machine ID (MID) documentation
- https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data — Structured data intro
- https://support.google.com/knowledgepanel/answer/9787176 — How Knowledge Graph works
- https://blog.google/products/search/about-knowledge-graph-and-knowledge-panels — KG and Knowledge Panels reintroduction
- https://developers.google.com/freebase — Freebase data dumps (historical)

**Schema.org:**
- https://schema.org/ — Main Schema.org site
- https://schema.org/docs/full.html — Full type hierarchy
- https://schema.org/docs/datamodel.html — Data model explanation
- https://schema.org/docs/about.html — About Schema.org (founders, governance)
- https://schema.org/docs/howwework.html — How Schema.org works
- https://schema.org/docs/extension.html — Extension mechanism
- https://schema.org/docs/pending.home.html — Pending terms
- https://www.w3.org/community/schemaorg/ — W3C Community Group
- https://www.w3.org/community/schemaorg/how-we-work/ — Community Group process

**Wikidata:**
- https://www.wikidata.org/wiki/Wikidata:WikiProject_Freebase — Freebase migration project
- https://www.wikidata.org/wiki/Help:FAQ/Freebase — Freebase FAQ
- https://www.wikidata.org/wiki/Wikidata:Data_model — Wikidata data model
- https://www.wikidata.org/wiki/Wikidata:Identifiers — Q/P number system

### Research & Analysis

**Academic Papers:**
- https://research.google/pubs/entity-disambiguation-with-freebase/ — Entity Disambiguation with Freebase
- https://research.google/pubs/plato-a-selective-context-model-for-entity-resolution/ — Plato entity resolution
- https://research.google/pubs/from-freebase-to-wikidata-the-great-migration/ — Freebase to Wikidata migration
- https://queue.acm.org/detail.cfm?id=2857276 — "Schema.org: Evolution of Structured Data on the Web" (ACM Queue)

**Technical Deep Dives:**
- https://arstechnica.com/information-technology/2012/06/inside-the-architecture-of-googles-knowledge-graph-and-microsofts-satori/ — KG architecture analysis
- https://www.theverge.com/2012/6/8/3071190/google-knowledge-graph-star-trek-computer-john-giannandrea-interview — Giannandrea interview on KG
- https://www.theguardian.com/technology/2013/jan/19/google-search-knowledge-graph-singhal-interview — Amit Singhal interview

**Industry Analysis:**
- https://techcrunch.com/2012/05/16/google-just-got-a-whole-lot-smarter-launches-its-knowledge-graph/ — KG launch coverage
- https://techcrunch.com/2010/07/16/google-acquires-metaweb-to-make-search-smarter/ — Metaweb acquisition
- https://almanac.httparchive.org/en/2024/structured-data — HTTP Archive structured data analysis
- https://trends.builtwith.com/framework/schema — Schema usage statistics
- https://www.searchenginejournal.com/structured-data-in-2024/532846/ — Structured data patterns study

**People Profiles:**
- https://guha.com/cv.html — R.V. Guha CV
- https://en.wikipedia.org/wiki/Ramanathan_V._Guha — R.V. Guha Wikipedia
- https://en.wikipedia.org/wiki/John_Giannandrea — John Giannandrea Wikipedia
- https://www.w3.org/People/DanBri/ — Dan Brickley at W3C
- https://en.wikipedia.org/wiki/Knowledge_Graph_(Google) — Knowledge Graph Wikipedia

**Videos:**
- https://www.youtube.com/watch?v=yp8AjMBG87g — Google I/O 2013: From Structured Data to Knowledge Graph

### Tools

- https://search.google.com/test/rich-results — Rich Results Test
- https://validator.schema.org — Schema.org Validator
- https://www.jsonld-examples.com/ — JSON-LD examples
- https://jsonld.com/ — JSON-LD code snippets
- https://github.com/google/freebase-wikidata-converter — Freebase to Wikidata converter

---

## Session Log

### 2025-01-24: Initial setup
- Created research doc
- Outlined research tasks
- Next: Subagent deep-dives on Schema.org and Knowledge Graph

### 2025-01-24: Phase 1 Web Research Complete
- Extensive web research completed on all research areas
- **Knowledge Graph**: Launch date, scale (5B entities, 500B facts), architecture, MID system, entity reconciliation
- **Schema.org**: Complete type hierarchy (827 types, 1528 properties), founding story, governance
- **Key People**: Documented 10 key figures including Guha, Giannandrea, Singhal, Brickley, Macbeth, Mika
- **JSON-LD**: Patterns for Article, LocalBusiness, Product, FAQ, etc.
- **Entity Evolution**: 2012 → 2016 (AI transition) → 2024 (Gemini) → 2025 (agentic)
- **Freebase/Wikidata**: Migration history, entity reconciliation approaches
- **Adoption**: 44% of sites, 83% use JSON-LD, Organization most popular type

**Key Insights for Our Project:**
1. Start with ~6 core types (Person, Org, Place, Event, CreativeWork, Product)
2. Use multiple inheritance and multi-typed entities
3. Properties matter more than type granularity
4. Stable identifiers (like MIDs) are critical
5. Support `sameAs` for cross-source identity
6. Design for extensibility from day one

**Next Steps:**
- Phase 2: Synthesize findings into entity model recommendations
- Compare with Wikidata research
- Draft initial type hierarchy for our knowledge graph
