---
title: Should "Event" Be a Subtype of "Work"? An Ontological Analysis
description: Research conducted 2026-02-13. Covers BFO, DOLCE, SUMO, UFO, CIDOC-CRM, Schema.org, Dublin Core, FRBR/IFLA-LRM, Wikidata, and philosophical literature.
---

## Recommendation: Keep Event as a Separate Primitive

Every major formal ontology, knowledge graph, and metadata standard maintains events and works as categorially distinct. The distinction (endurant/perdurant, continuant/occurrent) is considered foundational. No major ontology makes events a subtype of works.

## Key Findings

### 1. Major Ontologies — Unanimous Separation

| Ontology | Events | Works/Objects | Relationship |
|----------|--------|---------------|-------------|
| BFO | Occurrent | Continuant | Disjoint — separate mereological relations |
| DOLCE | Perdurant | Endurant | Disjoint categories |
| SUMO | Process | Object | Sibling categories under Physical |
| UFO | Perdurant (UFO-B) | Endurant (UFO-A) | Required UFO-AB to relate them |
| CIDOC-CRM | E5 Event (Temporal Entity) | E71 Human-Made Thing (Persistent Item) | Separate branches of hierarchy |
| Schema.org | Event (under Thing) | CreativeWork (under Thing) | Sibling types |
| Dublin Core | "Non-persistent, time-based occurrence" | Persistent resources | Distinct categories |
| Wikidata | subclass of "occurrence" | subclass of "intellectual work" | Separate hierarchies |
| IFLA-LRM | Not modeled | Work → Expression → Manifestation → Item | Events outside FRBR scope |

### 2. CIDOC-CRM: The Key Insight

Creation (E65) is an EVENT that PRODUCES a Thing (E71). The creation event and the created thing are distinct:
- The symphony premiere (event) ≠ the symphony (work)
- The premiere happened once. The symphony persists.
- Events have causal coherence. Works have attributive coherence.

### 3. Greek Etymology — Ergon

ἔργον covers both deed (activity) and product (creation). Aristotle distinguished these senses. This supports having BOTH primitives, not collapsing them.

### 4. What Events Have That Works Don't

- **Participants** (co-present during unfolding) vs. creators/audiences
- **Non-persistence** (happened, now over) vs. persistence
- **Temporal parts** (beginning, middle, end that unfold) vs. structural parts that coexist
- **Causal coherence** vs. attributive coherence
- **Occurrence semantics** ("it happened") vs. expression semantics ("it was published")
- FRBR chain (express_as, adapt, translate, cover) makes no sense for events

### 5. The Philosophical Dissolution Tradition

Whitehead, Quine, Goodman, Lewis dissolve the distinction — but by making EVERYTHING events/processes, not by making events a subtype of objects. This isn't useful for a knowledge graph.

### 6. Industry Perspective

Event management uses "production" language, but also recognizes events are ephemeral experiences, not persistent artifacts. The Experience Economy positions events alongside goods and services — distinct categories.

## Sources

- Stanford Encyclopedia of Philosophy, "Events" (2025 revision)
- CIDOC-CRM v7.1.3 (2024)
- BFO 2.0 / ISO 21838-2
- DOLCE (Laboratory for Applied Ontology)
- SUMO (Ontology Portal)
- UFO (Guizzardi et al.)
- Schema.org type hierarchy
- Dublin Core DCMI Type Vocabulary
- IFLA-LRM (2017)
- Wikidata Q1656682, Q17537576
- Stout, "The Category of Occurrent Continuants"
- Baratella, "Are There Occurrent Continuants? A Reply"
- Guarino, Baratella & Guizzardi, "Events, their names, and their synchronic structure"
