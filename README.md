# platform — the AgentOS contract

The contract agents work against: the data **shapes**, the auth-flow
**contracts**, and — over one generator — the language surfaces those
project into. One ontology, one generator, one repo.

GitHub remote: `agentos-to/site`. Sits at `~/dev/agentos/platform/`
alongside `core/`, `skills/`, `apps/`.

## Layout

```
platform/
├── ontology/              the contract — authored as YAML
│   ├── shapes/*.yaml          entity schemas
│   ├── ops/*.yaml             engine primitives (shell.run, http.request, …)
│   └── auth-contracts/*.yaml  OAuth + cookie provider return shapes
├── codegen/               one generator: YAML → IR → typed code
│   ├── generate.py            orchestrator
│   ├── ir.py                  YAML → one normalized Ontology tree
│   ├── emit/                  one dumb projection per target
│   ├── sdk_client.py          engine-client emitter
│   └── tool_surface.py        tool-surface docs emitter
├── sdk/
│   ├── python/            the `agentos` package — Python Skills SDK
│   └── typescript/        `@agentos/sdk` — TypeScript Apps SDK
└── docs/                  Astro site → agentos.to
```

## Ontology modeling — the rules

**Read this before authoring or changing any shape, relation, or edge.**
These are not style preferences — they are the contract. Anyone building
anything that touches the ontology follows them. Prior art is unanimous:
CIDOC-CRM, Wikidata, ActivityStreams 2.0, Neo4j, schema.org and Palantir
Foundry all converge on what's below.

### 1. An event is a relationship — time and place ride on it

A book wasn't "published in 2019" — it was published *by a publisher*,
in 2019. The year is a val on the `published_by` **edge**, never a
`datePublished` field on the book node. A node never carries a date,
place, or detail for something that happened *to it via another party* —
that is the denormalization bug. Edges carry typed vals (`edge_vals`);
that is what they are for.

### 2. Edges are verb phrases — one naming axis, no exceptions

Every edge label is a **lowercase snake_case verb phrase**, read
`subject —label→ object`:

```
joe —lived_at→ austin          book —published_by→ publisher
joe —born_to→ parent           person —attended→ concert
```

Banned, because each breaks the reading:

- **bare prepositions** as a whole label — `at`, `in`, `of`
- **bare nouns** — `organization`, `member`, `location`, `author`
- **mixing conventions** — once `published_by` exists, never also `publisher`

The preposition is part of the verb, chosen so the edge reads as
English: `_at` / `_in` → a place · `_by` → the agent of the action ·
`_to` / `_for` → other relational verbs · none → the verb stands alone
(`founded`, `owns`, `wrote`). Direction lives in the label — store one
direction, the reverse reading is derived (`inverse_name`), never a
second edge.

### 3. Node vs edge — a three-trigger test

A relationship is an **edge** by default. Promote it to a **node** at
the first trigger that fires:

1. **Arity** — more than two participants. An edge joins exactly two.
2. **Shared identity** — many parties must point at the *same* occurrence.
3. **Independent reference** — the occurrence is itself named, queried,
   or carries its own relations.

A residence (person + place + dates) trips none → a dated `lived_at`
edge. A job (person + org + dates) trips none → a `worked_at` edge. A
concert (attendee + venue + performer + promoter) trips all three → an
`event` node. When a relationship *is* a node, time and place are vals
**on that node**; the participation edges into it stay clean verb
phrases (`performed_at`, `attended`).

### 4. Edge types are not owned by node shapes

`lived_at` is one edge type, defined once, reused by many shapes. A
shape's `relations:` block lists the relations it *expects* — as
documentation and a validation hint — it does **not** own them, and an
edge to an unexpected node stays possible. A shape gains no relation for
every edge that can touch it: `person` declares no `lived_at` /
`born_at` / `born_to` — those are generic life-edges, not person-fields.

### 5. Shapes are nouns; a shape earns its existence by unique fields

A shape describes what something *is*, intrinsically — not what it did,
not where it came from. A "Goodreads book" is just a `book`. If a shape
adds no fields beyond a shape it `also:`-extends, it is a tag or an
edge, not a shape. (Full list: `docs/.../shapes/shape-design-principles.md`.)

### 6. Two clocks — valid-time vs transaction-time

An edge's `date` / `start` / `end` vals are **valid-time** — when the
fact was true in the world. A separate `recorded_at` is
**transaction-time** — when AgentOS learned it. Never conflate them: a
correction must not erase the prior belief.

> When practice teaches a new rule, add it here. This README is read
> every session, on purpose — that is why the rules live here and not in
> a docs page nobody opens.

## Codegen flow

`codegen/generate.py` is the single generator. `ir.py` parses
`ontology/{shapes,ops,auth-contracts}/*.yaml` into one normalized
`Ontology` tree; the emitters under `emit/` are dumb projections off it.

| Target | Path |
|---|---|
| Python SDK — shapes | `sdk/python/agentos/_generated.py` |
| Python SDK — op stubs | `sdk/python/agentos/{capability,crypto,plist,secrets,shell,sql}.py` |
| TypeScript SDK — shapes | `sdk/typescript/src/shapes.ts` |
| TypeScript SDK — ops | `sdk/typescript/src/ops.ts` |
| Rust — shapes (cross-repo) | `core/crates/contract-generated/src/shapes.rs` |
| Rust — op contract (cross-repo) | `core/crates/contract-generated/src/ops.rs` |
| Reference docs | `docs/src/content/docs/` |

```bash
cd codegen && python3 generate.py            # all SDKs + the op contract
cd codegen && python3 generate.py --docs     # MDX reference pages
cd codegen && python3 generate.py --check    # drift check, exits 1 on stale
```

Drift is caught by `core/dev.sh` on every engine build — it runs
`generate.py --check` and fails on any mismatch. Generated files are
checked in; never hand-edit them.

## The docs site

`docs/` is a standard Astro/Starlight site. Develop and build from
inside it:

```bash
cd docs && pnpm install && pnpm dev
cd docs && pnpm exec astro build
```

It deploys to [agentos.to](https://agentos.to) via
`.github/workflows/deploy.yml` on every push to `main`.

## License

MIT — see `sdk/python/LICENSE`.
