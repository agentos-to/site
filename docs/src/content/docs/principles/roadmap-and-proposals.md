---
title: Roadmap & proposals
description: The design pipeline — pain, proposal, review, closeout. How architectural decisions get made in AgentOS.
---

Design thinking for AgentOS lives in a **design-thinking pipeline**, not in scattered GitHub issues. Every non-trivial change flows through the same four artifacts.

## The pipeline

Each project is a folder with files in pipeline order:

```
pain.md         What's broken and why it matters
proposal.md     The plan (required: prior art / web research)
review.md       Adversarial review (one or more rounds: v1, v2, …)
closeout.md     What actually shipped vs. what was proposed
```

No numeric prefixes — files sort alphabetically, and that matches the pipeline order well enough.

## Priorities

```
_roadmap/
  p1/             Priority 1 — active
  p2/             Priority 2 — queued
  p3/             Priority 3 — backlog
  _archive/       Completed projects (historical record)
  _drafts/        Rejected proposals (kept for rationale)
  _research/      Background research informing proposals
```

The priority is the parent folder — moving a project between `p2/` and `p1/` is how prioritization is recorded. Completed projects graduate to `_archive/`. Rejected proposals go to `_drafts/` (the *rationale* is often more useful than the proposal itself).

## Why it's separate from the engine

Engine repos (`core`, `skills`, `site`, `apps`) stay focused on code and the ontology. Roadmap material is design thinking — *reasoning about architecture*, not the architecture itself. Mixing them pollutes git history with churn that has no bearing on the engine and leaks half-formed ideas into the public surface.

`_roadmap/` is private. Nothing there is API.

## The role of adversarial review

Proposals get **adversarial reviews** — an agent (or Joe) reads the proposal and tries to break it. Typical review output:

- Is the pain real and clearly articulated?
- Does the proposal actually solve it, or just the symptoms?
- What prior art was missed?
- What's the weakest link? What assumption, if wrong, collapses the plan?
- Where are the escape hatches? If this is wrong, can we roll back, or does it lock us in?

A single critical blocker means **revise**. All critical pass means **implement**. See [Agent empathy → Scoring](/docs/principles/agent-empathy/) for why we use pass/fail/partial labels instead of numeric scores.

## Closeout

After a project ships, a `closeout.md` captures what actually happened vs. what was proposed. This is how the pipeline learns. Closeouts feed into future proposals as prior-art references.

## See also

- [How we build](/docs/principles/how-we-build/) — the posture behind the pipeline.
- [Architectural laws](/docs/principles/architectural-laws/) — the rules a proposal is evaluated against.
