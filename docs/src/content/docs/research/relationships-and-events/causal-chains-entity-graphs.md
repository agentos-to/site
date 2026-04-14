---
title: "Blog Ideas: Causal Chains, Development Frameworks, and Entity Graphs"
description: Research from 2026-02-05 session. Fascinating connections between international development frameworks, OKRs, and entity modeling.
---

## Idea 1: "Log Frames, Theory of Change, and the Entity Graph"

**Audience:** International development sector, M&E practitioners

**Hook:** The development sector has been modeling causal relationships for decades. What can software learn from log frames?

### Key Concepts to Cover

**The Log Frame (Logical Framework)**
- 4x4 matrix: Impact → Outcome → Output → Activity
- Each level has: Narrative, Indicators, Means of Verification, Assumptions
- Strict linear chain (ladder)

**Theory of Change**
- More flexible: Directed Acyclic Graph (DAG)
- Allows branching and convergence
- Multiple pathways to same goal
- Assumptions attached to edges, not just levels

**Results Framework (USAID/World Bank)**
- Hierarchical tree with Intermediate Results (IRs)
- Explicit causal hypotheses with rationales

**The Universal Pattern**

```
Input → Activity → Output → Outcome → Impact
  ↑        ↑          ↑         ↑         ↑
CONTROL  CONTROL   CONTROL  INFLUENCE  ATTRIBUTE
```

**Entity-First Lens:**
- Each level is an `outcome` entity
- Relationships are `enables` / `contributes_to` / `precondition`
- Assumptions are first-class entities that gate relationships
- This is a graph, not a hierarchy

**Insight:** "depends_on" in a software roadmap is the same relationship as "precondition" in a theory of change.

---

## Idea 2: "KPI Trees, OKRs, and Driver Metrics"

**Audience:** Product managers, startup operators, business analysts

**Hook:** Your OKRs are a special case of a more general pattern. Understanding the underlying model makes goal-setting more rigorous.

### Key Concepts

**The Input-Output Model**

```
[Controllable Inputs]  →  [Intermediate Drivers]  →  [Observable Outputs]
   Leading indicators         Metrics                  Lagging indicators
   (actionable)              (measurable)              (confirmatory)
```

**KPI Trees / Driver Trees**
- Recursive decomposition: every outcome breaks into drivers
- Mathematical relationships: additive or multiplicative
- `Net New ARR = New ARR + Expansion ARR − Churn`
- `New ARR = Opportunities Won × Average Contract Value`

**OKRs (Objectives and Key Results)**
- Objectives = qualitative aspiration
- Key Results = quantitative measures
- Cascade: Company KR → Department Objective → Team KR
- Quarterly cycles with grading

**The Universal Entity**

| Property | Description |
|----------|-------------|
| **level** | input / activity / output / outcome / impact |
| **controllability** | direct / indirect / observable |
| **indicators[]** | How do we measure? |
| **status** | planned / in_progress / achieved |
| **timeframe** | When? |

**Entity Relationships**
- `decomposes_into` (parent → children, with add/multiply)
- `drives` / `influences` (cause → effect)
- `cascades_to` (org level → team level)

**Insight:** Leading vs lagging indicators map to controllability. You can act on leading indicators; you can only observe lagging ones.

---

## Idea 3: "The Outcome Entity - A Universal Model"

**Audience:** Knowledge management nerds, PKM community, entity-graph enthusiasts

**Hook:** New Year's resolutions, software roadmaps, OKRs, and USAID log frames are all the same data structure.

### The Unified Model

All these things are **outcomes in a causal chain**:

| Domain | Name | Example |
|--------|------|---------|
| Development | Intermediate Result | "Increased access to clean water" |
| Business | Key Result | "Reduce churn to <5%" |
| Personal | Resolution | "Exercise 3x per week" |
| Software | Roadmap Item | "Implement entity graph" |
| Science | Hypothesis | "Compound X reduces inflammation" |

### The `outcome` Base Entity

```yaml
id: outcome
properties:
  name: string
  description: string
  level: [input, activity, output, outcome, impact]
  status: [planned, in_progress, achieved, abandoned]
  controllability: [direct, indirect, observable]
  indicators: string[]
  timeframe: string
```

### Specific Types Extend It

| Type | Adds |
|------|------|
| `roadmap_item` | timing (now/soon/later), file_path, category |
| `okr` | quarter, key_results[], grade |
| `resolution` | year, domain (health, career) |
| `hypothesis` | experiment, evidence[] |

### The `enables` Relationship

```yaml
relationship:
  type: enables
  from: "entity-graph"
  to: "activity-backfill"
  rationale: "Need entities table first"
  assumptions: ["Schema is stable"]
```

This is `depends_on` by another name. Same pattern in Linear's "blocked_by".

---

## Research Sources

- USAID Results Framework guidance
- Theory of Change methodologies (Taplin, Clark)
- Google's OKR framework (Measure What Matters)
- KPI tree / driver tree literature
- FamilySearch GEDCOM patterns (evidence quality, provenance)

---

## Possible Formats

1. **Development sector blog post** - Focus on log frames, ToC, Results Framework. Show the entity-first lens.
2. **Product/startup blog post** - Focus on OKRs, KPI trees. Show how they're the same pattern.
3. **Technical deep-dive** - The `outcome` entity spec with examples from all domains.
4. **Entity map visualization** - Actually build the graph showing how these concepts relate.

---

---

## Session 2 Refinements (same day)

**Key breakthroughs:**

1. **`achieved` is a date, not boolean** - captures "we hit it but late"
   - `achieved: null` = not done
   - `achieved: 2026-02-10` = done on this date
   - Compute: `on_time = achieved <= target.date`

2. **Target is separate from status**
   - `value` = current (changes)
   - `target.value` + `target.date` = goal (fixed)
   - No "timeframe" string needed - target.date IS the temporal component

3. **Enables supports ranges (min/max)**
   - Not just "need at least X"
   - Also "must be within X-Y" (Goldilocks)
   - Body temp must be 36.5-38.5°C for enzyme function

4. **Assumptions ARE outcomes**
   - Not strings like "schema is stable"
   - Linked outcomes with their own thresholds
   - `role: assumption` vs `role: causal`
   - Makes assumptions **checkable**, not just notes

5. **Units need a store**
   - Health has tons: mg/dL, mcg/dL, nmol/L
   - Each skill could pre-seed its units
   - Ask Joe about biomarker work for patterns

**The unified model:**
- Everything is an `outcome`
- Everything connects via `enables`
- The graph structure computes controllability, blocked status, etc.
- Same primitive for software, biology, chemistry, business

*Captured from research session with Joe, 2026-02-05*
