---
title: '"No Orphans" Constraint: Research Summary'
description: How graph databases and entity systems handle the constraint that every node/entity must have at least one edge/relationship.
---

Research on how graph databases and entity systems handle the constraint that every node/entity must have at least one edge/relationship.

**Core problem:**
- You need to create entities before you can create relationships (foreign keys)
- But you want to ensure no entity exists without at least one relationship
- Batch imports need to be atomic

---

## 1. Neo4j

### Can you enforce that all nodes must have relationships?

**Short answer: No.** Neo4j does not have a built-in constraint to enforce that all nodes must have relationships.

### Available Constraint Types

Neo4j supports these constraint types:

| Constraint Type | What it enforces | Edition |
|----------------|------------------|---------|
| **Property uniqueness** | Property values are unique | All |
| **Property existence** | Specific properties exist on all nodes with a label | Enterprise |
| **Node key** | Properties exist and are unique (composite) | Enterprise |

**None of these enforce relationship requirements.**

### How Batch Imports Work

**Neo4j Admin Import (`neo4j-admin database import`):**
- Designed for high-performance bulk loading of CSV/Parquet data
- **Constraints and indexes are NOT created during import** — must be added afterward
- Assumes clean data where "relationships' start and end nodes exist"
- No built-in validation for orphan nodes

**Transactional Batch Operations:**
- Use `apoc.periodic.iterate` for batching large writes
- Default batch size: 10,000 rows per transaction
- As of Neo4j 5.21: parallel transaction processing via `CALL {...} IN CONCURRENT TRANSACTIONS`
- Still no built-in orphan prevention

### Solutions for Neo4j

**1. Post-import validation:**
```cypher
// Find orphan nodes
MATCH (n)
WHERE NOT (n)--()
RETURN n
```

**2. APOC periodic cleanup:**
Use `apoc.periodic.repeat` to periodically query and delete orphan nodes.

**3. SHACL validation (Neosemantics module):**
- Use W3C SHACL (Shapes Constraint Language) for validation
- Can define constraints like "a Task node must be connected to at least one TaskOwner node through an OWNED_BY relationship"
- Validation can run in batch mode, on selected node sets, or transactionally with rollback capability
- Example: `sh:minCount` on relationship paths

**Key insight:** Neo4j defers constraint validation to post-import or external validation frameworks. The import tool prioritizes performance over constraint checking.

---

## 2. FamilySearch GEDCOM

### Do they require every person to be connected?

**Short answer: No.** FamilySearch GEDCOM does not require every person to be connected through relationships.

### How GEDCOM Handles Orphans

**What the spec allows:**
- Individuals without family connections can exist in a GEDCOM file
- They may appear as isolated entries rather than part of a connected family tree structure

**What FamilySearch recommends:**
- When preparing a GEDCOM file for upload, FamilySearch recommends checking for "unattached individuals"
- This suggests that while unconnected people are permitted, they should be reviewed as part of file preparation

### Relationship Types in GEDCOM

When relationships are included, FamilySearch GEDCOM recognizes:
- **Couple relationships** (between two people)
- **Child-and-parents relationships** (between a child and two parents)

**Key insight:** GEDCOM prioritizes data preservation over structural constraints. Orphan individuals are allowed because genealogical research often starts with incomplete information.

---

## 3. Wikidata

### Can items exist without any statements/relationships?

**Short answer: Yes.** Wikidata items without statements and relationships can exist as "orphans."

### The Orphan Problem in Wikidata

**Items without statements:**
- Wikidata contains numerous items that lack any statements (claims)
- These are tracked in database reports: "Popular items without claims"
- Examples include entities with significant incoming links but no actual data:
  - Shikinaisha Former Site (111 links, no statements)
  - Various FIDE chess rankings (100 links each, no statements)
- Reports show thousands of items across different Wikipedia language editions have zero statements

**Orphan entities (different concept):**
- Wikidata "orphans" are entities without corresponding Wikipedia articles
- Research found that only ~10% of Wikidata's sitelinks map to English Wikipedia
- The vast majority of Wikidata entities lack dedicated article coverage
- These orphan entities often "suffer from incompleteness and lack of maintenance"

### How Wikidata Handles This

**Maintenance tracking:**
- Wikidata maintains tracking systems to identify sparse items with minimal statements
- Recognizes this as an ongoing maintenance concern for the knowledge base
- Community-driven cleanup efforts

**Key insight:** Wikidata follows an **open world assumption** — absence of data doesn't mean negation. Items can exist without statements because:
1. They might be placeholders for future data
2. They have incoming links from other items (even if no outgoing statements)
3. The system prioritizes data preservation over structural constraints

---

## 4. General Patterns

### Common Solutions for "No Orphans" Constraint

#### Pattern 1: Deferred Constraint Checking

**How it works:**
- Constraints are checked at transaction commit, not immediately
- Allows multi-step operations without temporarily violating constraints
- Entities can be created first, relationships added later, constraint checked at commit

**Database support:**
- **Oracle & PostgreSQL:** Support `DEFERRABLE INITIALLY DEFERRED` constraints
- Defer validation until transaction commit rather than checking immediately
- Prevents orphan violations during intermediate transaction states

**Example use case:**
When deleting a parent record and reassigning dependent records, deferred constraints prevent orphan violations during intermediate transaction states.

**Key insight:** This is the standard SQL database solution. Graph databases typically don't support deferred constraints natively.

#### Pattern 2: Two-Phase Import

**Phase 1: Create all entities**
- Disable foreign key checks temporarily
- Import all entities without relationships
- Re-enable foreign key checks

**Phase 2: Create all relationships**
- Import all relationships
- Validate that all referenced entities exist

**Database support:**
- **MySQL:** `SET foreign_key_checks=0;` ... `SET foreign_key_checks=1;`
- **PostgreSQL:** Similar pattern with constraint disabling
- **Neo4j:** Import tool assumes clean data; no built-in two-phase support

**Trade-offs:**
- Can save significant disk I/O for large tables
- Must ensure data is valid, as this approach can lead to inconsistencies if not carefully managed
- Requires careful ordering of operations

#### Pattern 3: Transactional Batch Operations

**How it works:**
- Group entity creation and relationship creation into a single atomic transaction
- All operations succeed or all fail together
- Prevents partial writes

**Implementation examples:**

**Azure Cosmos DB:**
- Uses `TransactionalBatch` class
- Groups multiple entity operations (create, update, delete) within the same container and partition key
- Guarantees atomicity

**Prisma ORM:**
- Supports batch operations through `$transaction()` API
- Sequential operations and `createMany`/`updateMany`/`deleteMany` for bulk writes
- Options for both independent and dependent writes including relationship creation

**Neo4j (neomodel):**
- Provides `create()` and `create_or_update()` batch methods
- Execute multiple node operations in a single transaction

**Key insight:** This works well for small-to-medium batches but may not scale to millions of entities. Requires all operations to be in a single partition/container.

#### Pattern 4: Post-Import Validation

**How it works:**
1. Complete batch import first (entities + relationships)
2. Create constraints after import
3. Run validation queries to identify orphans
4. Handle violations (delete, connect, or flag for review)

**When to use:**
- Large-scale imports where transactional batches aren't feasible
- When you can tolerate temporary constraint violations
- When cleanup/validation can happen asynchronously

**Example validation query (Neo4j):**
```cypher
// Find all orphan nodes
MATCH (n)
WHERE NOT (n)--()
RETURN n
```

**Key insight:** This is the most common pattern for graph databases. Constraints are enforced after import, not during.

#### Pattern 5: External Validation Frameworks

**SHACL (Shapes Constraint Language):**
- W3C standard for validating RDF graphs
- Can define constraints like "every Person must have at least one relationship"
- Validation can run transactionally with rollback capability
- Used by Neo4j Neosemantics module

**Example SHACL shape:**
```turtle
:PersonShape a sh:NodeShape ;
    sh:targetClass :Person ;
    sh:property [
        sh:path :knows ;
        sh:minCount 1 ;
        sh:class :Person
    ] .
```

**Key insight:** External validation frameworks provide more expressive constraint languages than native database constraints, but require additional tooling and may have performance overhead.

---

## Comparison Table

| System | Native "No Orphans" Constraint? | Batch Import Strategy | Validation Approach |
|--------|-------------------------------|----------------------|---------------------|
| **Neo4j** | ❌ No | Post-import validation or SHACL | External validation or periodic cleanup |
| **PostgreSQL** | ✅ Yes (deferred) | Deferred constraints or two-phase import | Native deferred constraint checking |
| **MySQL** | ⚠️ Partial | Two-phase import (disable checks) | Manual validation after import |
| **Wikidata** | ❌ No | Allows orphans | Community-driven cleanup |
| **FamilySearch GEDCOM** | ❌ No | Allows orphans | Recommends review, doesn't enforce |
| **Azure Cosmos DB** | ⚠️ Partial | Transactional batches | Atomic transactions within partition |

---

## Recommendations for Entity Systems

### For Small-to-Medium Batches (< 100K entities)

**Use transactional batch operations:**
- Create entities and relationships in a single atomic transaction
- All-or-nothing guarantee
- Simplest to reason about

### For Large Batches (> 100K entities)

**Use two-phase import with deferred validation:**
1. **Phase 1:** Create all entities (disable constraint checks if possible)
2. **Phase 2:** Create all relationships
3. **Phase 3:** Validate constraints and handle violations

### For Graph Databases (Neo4j, etc.)

**Use post-import validation:**
- Import entities and relationships together
- Run validation queries to find orphans
- Handle violations (delete, connect, or flag)
- Consider SHACL for complex constraint validation

### For Relational Databases

**Use deferred constraints:**
- Define constraints as `DEFERRABLE INITIALLY DEFERRED`
- Create entities, then relationships, all in one transaction
- Constraints checked at commit time

### General Principle

**The constraint is enforced at commit time, not during intermediate states.**

This allows:
- Entities to exist temporarily without relationships
- Batch operations to proceed atomically
- Validation to happen when the transaction is complete

---

## Open Questions for Your System

Based on your schema and relationship modeling research, here are questions to consider:

1. **Should orphans be allowed temporarily during import?**
   - If yes: Use deferred validation or two-phase import
   - If no: Require transactional batches (limits scalability)

2. **What happens to orphans after import?**
   - Delete them automatically?
   - Flag them for review?
   - Connect them to a "root" entity?

3. **Are there legitimate orphan cases?**
   - Root entities (e.g., a "world" place entity)?
   - Temporary entities during editing?
   - Entities that will be connected later?

4. **How strict should the constraint be?**
   - Hard requirement (transaction fails)?
   - Soft requirement (warning/flag)?
   - Context-dependent (some types require relationships, others don't)?

5. **What's the performance impact?**
   - Can you afford transactional batches?
   - Do you need two-phase import for scale?
   - Is post-import validation acceptable?

---

## References

### Standards & Documentation
- [Neo4j Constraints Documentation](https://neo4j.com/docs/cypher-manual/current/constraints/managing-constraints/)
- [Neo4j Import Best Practices](https://neo4j.com/docs/operations-manual/current/import/)
- [PostgreSQL Deferred Constraints](https://www.postgresql.org/docs/current/sql-set-constraints.html)
- [SHACL Specification](https://www.w3.org/TR/shacl/)

### Research & Examples
- [Wikidata Database Reports: Items Without Claims](https://www.wikidata.org/wiki/Wikidata:Database_reports/Popular_items_without_claims)
- [FamilySearch GEDCOM Specification](https://gedcom.io/specifications/FamilySearchGEDCOMv7.html)
- [Neo4j SHACL Validation](https://neo4j.com/labs/neosemantics/4.2/validation/)

---

*Research compiled January 2026*
