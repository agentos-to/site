---
title: "The Outcome Entity: A Universal Systems Primitive"
description: Everything is an outcome. An outcome is an input to something else — a universal primitive for modeling roadmaps, OKRs, log frames, biology, chemistry, and system dynamics.
---

## The Insight

Everything is an outcome. An outcome is an input to something else.

The same data structure models:
- Software roadmaps
- Business OKRs  
- International development (log frames, theory of change)
- Biological systems
- Chemical reactions
- Supply chains
- System dynamics

---

## The `outcome` Entity

```yaml
id: outcome
plural: outcomes
name: Outcome
description: A state or result that can enable other outcomes

properties:
  id:
    type: string
    required: true
    
  name:
    type: string
    required: true
    description: What is this outcome?
    
  description:
    type: string
    description: Detailed explanation
    
  # Current state (changes over time)
  value:
    type: number
    description: Current measurement (for numeric outcomes)
    
  unit:
    type: string
    description: Unit of measurement (see Units section below)
    
  # Target (fixed when outcome is created)
  target:
    type: object
    properties:
      value:
        type: number
        description: The goal number to hit
      date:
        type: date
        description: Deadline to hit it by
        
  # Achievement (date, not boolean!)
  achieved:
    type: date
    nullable: true
    description: |
      Date the outcome was achieved. Null = not yet achieved.
      Allows computing: on_time, days_late, etc.
      
  # What this outcome produces (for enabling others)
  output:
    type: object
    description: What this outcome outputs for downstream dependencies
    properties:
      metric:
        type: string
        description: What is being output (voltage, throughput, revenue...)
      value:
        type: number
        description: Current output level
      unit:
        type: string
        
  # How to measure this outcome
  indicators:
    type: array
    items:
      type: string
      
  # Domain-specific extensions
  data:
    type: object
    description: Additional properties per domain
```

### Computed Properties (from graph structure)

| Property | How Computed |
|----------|--------------|
| `is_achieved` | `achieved != null` |
| `on_time` | `achieved <= target.date` |
| `days_late` | `achieved - target.date` (if late) |
| `progress` | `value / target.value` |
| `exceeded` | `value > target.value` |
| `blocked` | Has unmet enables relationships |
| `ready` | All enables relationships met |
| `controllability` | Leaf nodes = direct control |

---

## The `enables` Relationship

The magic is in the relationship. This is what makes true system dynamics modeling possible.

```yaml
relationship: enables
description: One outcome enables another when requirements are met

properties:
  from:
    type: entity_id
    description: The enabling outcome
    
  to:
    type: entity_id
    description: The enabled outcome
    
  # Semantic role
  role:
    type: string
    enum: [causal, assumption]
    description: |
      causal: Direct cause-effect relationship (A causes B)
      assumption: External condition that must hold (context required)
    
  # What's required for enablement? (supports ranges!)
  requires:
    type: object
    properties:
      metric:
        type: string
        description: What metric must be met
      min:
        type: number
        description: Minimum value required (optional)
      max:
        type: number
        description: Maximum value required (optional)
      unit:
        type: string
        
  # Why does this enable that?
  rationale:
    type: string
    description: Explanation of the causal link
    
  # Strength of the relationship
  strength:
    type: string
    enum: [necessary, sufficient, contributory]
    description: |
      necessary: Required but not enough alone
      sufficient: This alone could enable it
      contributory: Helps but not required
```

### Enablement Computation

```python
def is_enabled(enables_rel, from_outcome):
    req = enables_rel.requires
    val = from_outcome.output.value
    
    # Check min threshold
    if req.min is not None and val < req.min:
        return False
    
    # Check max threshold  
    if req.max is not None and val > req.max:
        return False
    
    # For boolean outcomes (no numeric value)
    if val is None:
        return from_outcome.achieved is not None
    
    return True
```

---

## Assumptions ARE Outcomes

**Critical insight:** Assumptions are not strings. They are linked outcomes.

❌ **Old way (just notes, not checkable):**
```yaml
assumptions: ["Schema is stable", "Team has capacity"]
```

✅ **New way (linked outcomes, fully checkable):**
```yaml
# The assumption IS an outcome
- id: schema-stability
  name: "Schema Stability"
  output:
    metric: "changes_per_week"
    value: 1
    unit: "changes"

# The enables relationship with role: assumption
- type: enables
  role: assumption
  from: schema-stability
  to: activity-backfill
  requires:
    metric: "changes_per_week"
    max: 2  # stable = less than 2 changes/week
  rationale: "Schema must be stable before backfilling"
```

**Why this matters:**
- Assumptions are **checkable** in real-time
- Query: "What assumptions are currently failing?"
- Query: "What outcomes are blocked by unmet assumptions?"
- The whole system is **one unified graph**
- Each assumption outcome defines exactly what it means (e.g., "what is capacity?")

---

## Domain Examples

### 1. Software Roadmap

```yaml
# Outcome: Entity Graph (milestone)
- id: entity-graph
  name: "Entity Graph Schema"
  achieved: null  # not done yet
  target:
    date: 2026-02-15
  output:
    metric: "completion"
    value: 0.7
    unit: "percent"

# Outcome: Activity Backfill (depends on entity-graph)
- id: activity-backfill
  name: "Backfill Activity Data"
  achieved: null
  target:
    date: 2026-02-28

# Causal relationship
- type: enables
  role: causal
  from: entity-graph
  to: activity-backfill
  requires:
    metric: "completion"
    min: 1.0  # needs 100% complete
  rationale: "Need entities table before backfilling"

# Assumption: Schema stability
- id: schema-stable
  name: "Schema is Stable"
  output:
    metric: "breaking_changes"
    value: 0
    unit: "per_week"

- type: enables
  role: assumption
  from: schema-stable
  to: activity-backfill
  requires:
    metric: "breaking_changes"
    max: 0
  rationale: "Can't backfill if schema keeps changing"
```

### 2. Biological System (Body Temperature → Enzyme Function)

```yaml
# Outcome: Body Temperature
- id: body-temp
  name: "Core Body Temperature"
  value: 37.0
  unit: "°C"
  output:
    metric: "temperature"
    value: 37.0
    unit: "°C"

# Outcome: Enzyme Function
- id: enzyme-function
  name: "Metabolic Enzyme Activity"
  value: 0.95
  unit: "relative"

# Enables with RANGE (not too hot, not too cold)
- type: enables
  role: causal
  from: body-temp
  to: enzyme-function
  requires:
    metric: "temperature"
    min: 36.5   # hypothermia threshold
    max: 38.5   # fever threshold
    unit: "°C"
  rationale: "Enzymes denature outside optimal temperature range"
```

### 3. Business OKR

```yaml
# Outcome: Sales Pipeline
- id: sales-pipeline
  name: "Build Sales Pipeline"
  value: 2500000
  unit: "USD"
  achieved: 2026-03-15  # hit target on this date
  target:
    value: 2000000
    date: 2026-03-31
  output:
    metric: "pipeline_value"
    value: 2500000
    unit: "USD"

# Outcome: Revenue Target
- id: q1-revenue
  name: "Q1 Revenue Target"
  value: 800000
  unit: "USD"
  achieved: null  # not yet
  target:
    value: 1000000
    date: 2026-03-31

# Relationship
- type: enables
  role: causal
  from: sales-pipeline
  to: q1-revenue
  requires:
    metric: "pipeline_value"
    min: 3000000  # need 3x coverage
  strength: necessary
  rationale: "3x pipeline coverage historically needed"
```

### 4. Chemical Reaction (Activation Energy)

```yaml
# Outcome: Heat Energy
- id: heat-source
  name: "Heat Applied"
  output:
    metric: "energy"
    value: 50
    unit: "kJ"

# Outcome: Reaction Proceeds
- id: reaction-b
  name: "Reaction B Proceeds"
  achieved: null
  target:
    date: 2026-02-05

# Relationship
- type: enables
  role: causal
  from: heat-source
  to: reaction-b
  requires:
    metric: "energy"
    min: 40  # activation energy threshold
    unit: "kJ"
  rationale: "Activation energy barrier must be overcome"
```

---

## Units: Future Work

> **TODO:** Ask Joe to show biomarker/health work for unit patterns

**Open questions:**
1. Do we need a **unit store/registry**?
2. Should units be **pre-seeded per domain**?
   - Health: mg/dL, mcg/dL, mmol/L, etc.
   - Temperature: °C, °F, K
   - Business: USD, EUR, %, basis points
   - Computing: req/s, ms, MB, etc.
3. Could each **entity/skill pre-seed its units**?
   - Health skill seeds health units
   - Finance skill seeds currency units
   - Community-driven unit definitions
4. Unit **conversion** - can we convert between compatible units?

**Examples from blood work:**
- Glucose: mg/dL or mmol/L
- Vitamin D: ng/mL or nmol/L
- Zinc: mcg/dL
- Hemoglobin: g/dL

This is important for enabling cross-system queries and visualizations.

---

## System Dynamics Features

With this model, we can:

### 1. **Find Bottlenecks**
```sql
SELECT o.* FROM outcomes o
JOIN enables e ON e.to_id = o.id
JOIN outcomes enabler ON e.from_id = enabler.id
WHERE (e.requires_min IS NOT NULL AND enabler.output_value < e.requires_min)
   OR (e.requires_max IS NOT NULL AND enabler.output_value > e.requires_max)
```

### 2. **Check Failing Assumptions**
```sql
SELECT o.*, e.rationale 
FROM outcomes o
JOIN enables e ON e.from_id = o.id
WHERE e.role = 'assumption'
  AND ((e.requires_min IS NOT NULL AND o.output_value < e.requires_min)
       OR (e.requires_max IS NOT NULL AND o.output_value > e.requires_max))
```

### 3. **Simulate Changes**
"If we increase temperature to 39°C, what becomes disabled?"
→ Walk enables relationships, recompute enablement

### 4. **Trace Causality**
"Why isn't X happening?" → Walk backwards through unmet enables

### 5. **Identify Leverage Points**
"Which outcomes, if improved, would unblock the most downstream outcomes?"

### 6. **Timeline Views**
Sort by `target.date`, show `achieved` date, compute on-time %

### 7. **Progress Tracking**
`value / target.value` over time → burndown/burnup charts

---

## Summary: What Makes This Powerful

1. **Everything is an outcome** - no artificial levels (input/output/impact)
2. **Achieved is a date** - not boolean, captures timing
3. **Target is fixed** - value + date, no moving goalposts
4. **Enables has thresholds** - numeric, not just boolean
5. **Supports ranges** - min/max for "Goldilocks" requirements
6. **Assumptions are outcomes** - linked, checkable, not just notes
7. **Graph structure computes** - controllability, blocked status, etc.
8. **Works universally** - software, biology, chemistry, business, development

---

## Implementation: SQL Schema

```sql
-- Outcomes table
CREATE TABLE outcomes (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  description TEXT,
  
  -- Current state
  value REAL,
  unit TEXT,
  
  -- Target
  target_value REAL,
  target_date DATE,
  
  -- Achievement (null = not achieved)
  achieved DATE,
  
  -- Output for downstream
  output_metric TEXT,
  output_value REAL,
  output_unit TEXT,
  
  -- Extensible
  data JSON
);

-- Enables relationships
CREATE TABLE enables (
  id TEXT PRIMARY KEY,
  from_id TEXT REFERENCES outcomes(id),
  to_id TEXT REFERENCES outcomes(id),
  
  role TEXT CHECK(role IN ('causal', 'assumption')),
  
  requires_metric TEXT,
  requires_min REAL,
  requires_max REAL,
  requires_unit TEXT,
  
  rationale TEXT,
  strength TEXT CHECK(strength IN ('necessary', 'sufficient', 'contributory'))
);

-- Computed views
CREATE VIEW blocked_outcomes AS
SELECT DISTINCT o.*
FROM outcomes o
JOIN enables e ON e.to_id = o.id
JOIN outcomes enabler ON e.from_id = enabler.id
WHERE (e.requires_min IS NOT NULL AND enabler.output_value < e.requires_min)
   OR (e.requires_max IS NOT NULL AND enabler.output_value > e.requires_max)
   OR (enabler.achieved IS NULL AND e.requires_min IS NULL AND e.requires_max IS NULL);

CREATE VIEW ready_outcomes AS
SELECT o.*
FROM outcomes o
WHERE o.achieved IS NULL  -- not yet achieved
  AND o.id NOT IN (SELECT id FROM blocked_outcomes);
```

---

## Next Steps

1. [ ] Create `outcome` entity in skills/
2. [ ] Create `enables` relationship type  
3. [ ] Build roadmap plugin using this model
4. [ ] **Unit store research** - ask Joe about biomarker work
5. [ ] Prototype system dynamics visualization
6. [ ] Test with biological system model
7. [ ] Explore simulation capabilities

---

## References

- USAID Results Framework
- Theory of Change methodology
- System Dynamics (Forrester, Meadows)
- Stock and Flow models
- Causal Loop Diagrams
- OKR framework (Doerr)
- Log Frames (international development)

---

*This is foundational. The same primitive models software, business, biology, chemistry, and any system with causal dependencies and thresholds.*
