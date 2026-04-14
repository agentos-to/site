---
title: Architectural laws
description: The laws of the codebase. Every change is evaluated against these.
---

The laws of the codebase. Every change is evaluated against these.

## 1. Rust is a generic engine

The Rust code knows about *entities*, *relationships*, *schemas*, and *operations*. It never knows about "tasks", "messages", "people", or any specific entity type. **Zero entity-specific or relationship-specific code in Rust.** Hard no.

If you see any of these in Rust, raise it immediately — it's a bug in the architecture:

- Hardcoded field names (`priority`, `done`, `blocks`, `blocked_by`)
- Grouping, sorting, or partitioning logic for specific entity types
- Display/formatting/rendering decisions for specific entity types
- Conditional branches on entity type names
- Bespoke data-fetching functions for specific entity types

**Where specific behavior belongs:**

| Layer | Responsibility | Format |
|-------|---------------|--------|
| Entity schemas | Properties, validation, display hints, sort order, operations | Shape YAMLs (`site/docs/shapes/`) |
| Templates | Rendering, layout, grouping, formatting | MiniJinja markdown |
| Skills | API mappings, field transforms | Python + YAML frontmatter |

## 2. Templates do the work

Rendering is never the Rust code's job. Rust provides small, composable filters — `listing`, `table`, `tree`, `props`. Templates compose them. Layout decisions live in templates, never in Rust.

A filter should do **one thing**. If a filter is making layout decisions (choosing headings, grouping by priority, separating done/not-done), it's too big. Break it up.

## 3. Foundation first

The most foundational work that prevents tech debt, always. If you're choosing between a feature and fixing an abstraction, fix the abstraction.

## 4. The graph is the source of truth

Every entity modeled correctly, every relationship captured. Skills sync data in; the graph is the authority for reads.

## 5. We have infinite time

No customers, no deadlines, no shortcuts. Do it right or don't do it.

## 5b. Blast radius is not a cost — stale architecture is

AgentOS is pre-launch with zero users, no data to protect, no backward compatibility, no migration path. An "audacious" refactor that touches the Rust dispatch pipeline, the SDK bridge, every executor, and every skill in one shot is *not more expensive* than a one-line fix — the constraint is correctness, not disruption.

When you find a bug, ask: is this a leaf symptom, or is there an inconsistency in the abstraction underneath? If two code paths exist where one would do, two wire-format shapes exist where one would do, or a sync wrapper sits on top of an async call, the right fix is to delete the asymmetry at the root — even if it means rewriting the executor, the bridge, and every caller.

**The hardest, most audacious *appropriate* refactor is usually the right answer.** Small safe patches that leave the inconsistency in place are worse than large refactors that remove it. Reject pragmatic band-aids in code review. Reward scope in proposals. When in doubt, tear it up and do it right.

*Caveat: "appropriate." This is not a license to burn down code that is correct just because it looks ugly. The trigger is a root-cause inconsistency you can name. If you can't name the inconsistency, the refactor isn't audacious — it's churn.*

## 6. Co-CTOs

Present the hard design question, decide together. Don't make big architectural choices silently.

## 7. Pain-driven

If you can't articulate the pain, don't build it.

## 7b. Delete dead code on sight

Pre-launch means zero legacy obligations. Code containing any of these signals should be challenged in every review:

- `legacy`, `compat`, `backwards`, `deprecated`, `migration`, `fallback`
- `TODO remove`, `TODO delete`, `temporary`, `one-time`, `workaround`
- Feature flags, capability checks for removed features, commented-out code
- Silent-skip branches (`exit 0` on failure, empty `catch` blocks that swallow errors)
- Fallback chains ("try X, if that fails try Y") where only one path is correct
- URL redirects preserving old paths — move pages, update links, delete the old URL. No redirects.

The question is always: **does this still serve a purpose?** If not, delete it — don't comment it out, don't leave it "for reference," don't rename it with an underscore. Git has the history if we ever need it back.

## The Campsite Rule

Leave every module better than you found it. Before writing code, ask yourself: **Is anything bugging me about these abstractions, naming, or architecture?** If yes — tell the user. Propose the cleanup before moving forward.
