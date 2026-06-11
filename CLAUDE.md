@README.md

# Platform — Agent Instructions

> **Read this every session.** The README imported above carries the
> **Ontology modeling rules** — six rules that govern every shape,
> relation, and link in `ontology/`. They are the contract. Not optional.

Platform is the AgentOS contract: the ontology (`ontology/`), the one
codegen (`codegen/`), the generated SDKs (`sdk/`). Narrative docs live
on the engine's system volume (`core/system-docs/`). The README has the
layout, the codegen flow, and the modeling rules.

## Working here

- **Touching the ontology** — shapes, relations, links — obey the
  README's "Ontology modeling — the rules". An event is a relationship;
  time and place ride on the edge; links are verb phrases.
- **Generated files are never hand-edited.** `sdk/**/_generated.*`,
  `sdk/typescript/src/{shapes,ops}.ts`, `core/crates/contract-generated/`
  are codegen output — change the YAML in `ontology/`, run
  `codegen/generate.py`.
- **A modeling rule that's wrong or missing** — fix it in `README.md`.
  That is the single source, read every session. Don't scatter ontology
  principles into docs pages.
- Commit straight to `main` — no feature branches (workspace convention).
