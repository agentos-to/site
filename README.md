# platform — the AgentOS contract

The contract agents work against: the data **shapes**, the auth-flow
**contracts**, and — over one generator — the language surfaces those
project into. One ontology, one generator, one repo.

GitHub remote: `agentos-to/site`. Sits at `~/dev/agentos/platform/`
alongside `core/`, `apps/`, `commons/`.

Narrative docs live on the engine's **system volume**
(`core/system-docs/`), not here — agentos.to returns as a
static-exported read-only AgentOS instance (change-static-export).

## Layout

```
platform/
├── ontology/              the contract — authored as YAML
│   ├── shapes/*.yaml          entity schemas (nouns only — no edge typing)
│   ├── ops/*.yaml             engine primitives (shell.run, http.request, …)
│   ├── services/*.yaml        brokered service definitions (web_search, llm, …)
│   ├── migrations/*.yaml      schema migration chain
│   └── auth-contracts/*.yaml  OAuth + cookie provider return shapes
├── codegen/               one generator: YAML → IR → typed code
│   ├── generate.py            orchestrator
│   ├── ir.py                  YAML → one normalized Ontology tree
│   ├── emit/                  one dumb projection per target
│   ├── sdk_client.py          engine-client emitter
│   └── tool_surface.py        tool-surface docs emitter
└── sdk/
    ├── python/            the `agentos` package — Python App SDK
    └── rust/              generated Rust shape tree
```

## Ontology modeling — the rules

**Read this before authoring or changing any shape, relation, or link.**
These are not style preferences — they are the contract. Anyone building
anything that touches the ontology follows them. Prior art is unanimous:
CIDOC-CRM, Wikidata, ActivityStreams 2.0, Neo4j, schema.org and Palantir
Foundry all converge on what's below.

### 1. An event is a relationship — time and place ride on it

A book wasn't "published in 2019" — it was published *by a publisher*,
in 2019. The year is a val on the `published_by` **link**, never a
`datePublished` field on the book node. A node never carries a date,
place, or detail for something that happened *to it via another party* —
that is the denormalization bug. Links carry typed vals (`link_vals`);
that is what they are for.

Vals on an link are not only *when* and *where*. Any **quantity that is a
property of the relationship** rides there too — `joe —owns→ adavia
{share: 1.0, units: 10000000}`. The `link_vals` table types a number or
integer exactly as `node_vals` would; an ownership percentage belongs to
the owning, not to either party.

**Time intervals on links — canonical convention.** When an link
represents a *period* (a residence, a job, a membership, a marriage),
use `{from: date, to: date?}` as the link_vals. `to: null` (or absent)
means the interval is still open — the current/active period. The
`current_*` derived bindings on shapes (e.g. `person.current_residence`,
`person.current_role`) read this convention via the resolver's
`where_link: {to: null}` filter:

```
joe —lived_at→ austin    {from: 2018-06, to: 2020-09}   # closed
joe —lived_at→ portland  {from: 2020-09, to: null}       # current
joe —worked_at→ corp     {from: 2019-01, to: 2024-12, title: "engineer"}
```

This pairs naturally with rule 3 (node vs link): a residence trips no
triggers → stays a dated link with `{from, to}`. If a residence ever
*does* trip a trigger (needs reason, source-of-truth attribution,
witnesses, paperwork — e.g. a visa-application proof-of-address), it
promotes to its own `event(residence)` node and the `lived_at` link
becomes `lived_at_for` (a participation link into the event node).

### 2. Links are verb phrases — one naming axis, no exceptions

Every link label is a **lowercase snake_case verb phrase**, read
`subject —label→ object`:

```
joe —lived_at→ austin          book —published_by→ publisher
joe —born_to→ parent           person —attended→ concert
```

Banned, because each breaks the reading:

- **bare prepositions** as a whole label — `at`, `in`, `of`
- **bare nouns** — `organization`, `member`, `location`, `author`
- **mixing conventions** — once `published_by` exists, never also `publisher`

The preposition is part of the verb, chosen so the link reads as
English: `_at` / `_in` → a place · `_by` → the agent of the action ·
`_to` / `_for` → other relational verbs · none → the verb stands alone
(`founded`, `owns`, `wrote`). Direction lives in the label — store one
direction, the reverse reading is derived (`inverse_name`), never a
second link.

The suffix follows English **idiom**, not the object's type: you
`worked_at` an *organization*, `born_at` a *place*, `lived_at` an
*address* — `_at` tracks how the verb is spoken, not what it points to.
And a **stative** relation English has no verb for — citizenship,
holding a credential — takes a role-noun phrase: `citizen_of`,
`held_by`. That is *not* the banned bare noun: it keeps a preposition,
reads as English, carries direction. The ban is on a noun standing
*alone* as the whole label (`member`, `author`).

### 3. Node vs link — a three-trigger test

A relationship is an **link** by default. Promote it to a **node** at
the first trigger that fires:

1. **Arity** — more than two participants. An link joins exactly two.
2. **Shared identity** — many parties must point at the *same* occurrence.
3. **Independent reference** — the occurrence is itself named, queried,
   or carries its own relations.

A residence (person + place + dates) trips none → a dated `lived_at`
link. A job (person + org + dates) trips none → a `worked_at` link. A
concert (attendee + venue + performer + promoter) trips all three → an
`event` node. When a relationship *is* a node, time and place are vals
**on that node**; the participation links into it stay clean verb
phrases (`performed_at`, `attended`).

**Recurrence forces a node.** The graph stores at most one link per
`(from, label, to)` — `create_link` is `ON CONFLICT … DO UPDATE`, so a
second `create` of the same triple overwrites the first's vals. When the
*same* verb recurs between the *same* two parties — two filings with one
office, two investments in one company — it cannot be N links. Promote
each occurrence to a node. This is trigger 3 made physical: a recurrence
is almost always itself referenceable — a `document`, a `transaction` —
and the storage layer makes the under-modeled version impossible to
write. (A *thin* recurrence with no referenceable occurrence — living at
one address across two stints — has no natural node; that case is a
known limit, not yet resolved.)

### 4. Edges are untyped and self-registering — shapes own no relations

There is no edge schema anywhere: no `links/*.yaml`, no link codegen, no
`relations:` block on a shape. **Nouns are typed, verbs are not** — the
entity-space is finite and knowable, the relationship-space is open and
emergent (the RDF/OWL over-typing mistake property graphs already
corrected). A skill or the agent mints an edge inline with
`create({from, label, inverse, to})`; the engine learns the verb the first
time it sees it and records the pair in the lazy `link_defs` registry, so
no edge is ever one-directional. The `inverse` rides each edge and is never
rejected when it differs — the same verb reads back differently in
different contexts, and that drift is fine.

A shape therefore declares only its own data (fields, identity, display,
`also`). It gains no relation for every link that can touch it: `person`
declares no `lived_at` / `born_at` / `born_to` — those are generic
life-links, not person-fields. **An app names the child's noun, not the
edge's type:** a nested relation child in a return carries its own
`shape:` (`operated_by: {shape: "airline", …}`); the engine links any
shaped child under any verb. Pick the child's shape at the **widest noun
it can be** — `account` for a platform handle, `person` for a human,
`organization` for an org — a child typed narrower than reality lies.

### 5. Shapes are nouns; a shape earns its existence by unique fields

A shape describes what something *is*, intrinsically — not what it did,
not where it came from. A "Goodreads book" is just a `book`. If a shape
adds no fields beyond a shape it `also:`-extends, it is a tag or an
link, not a shape. (Full list: `docs/.../shapes/shape-design-principles.md`.)

### 6. Two clocks — valid-time vs transaction-time

An link's `date` / `start` / `end` vals are **valid-time** — when the
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
| Python SDK — op stubs | `sdk/python/agentos/{crypto,plist,secrets,shell,sql}.py` |
| Python SDK — services | `sdk/python/agentos/services.py` |
| Rust SDK — shape tree | `sdk/rust/src/shapes/` |
| Shell contract (cross-repo) | `core/web/src/contract-generated/shapes.ts` |
| Rust — shapes (cross-repo) | `core/crates/contract-generated/src/shapes.rs` |
| Rust — op contract (cross-repo) | `core/crates/contract-generated/src/ops.rs` |
| Symbol nodes (cross-repo) | `core/crates/core/generated/yaml-symbols.json` — shapes + SDK ops projected onto the engine's system volume |

```bash
cd codegen && python3 generate.py            # all SDKs + the op contract
cd codegen && python3 generate.py --check    # drift check, exits 1 on stale
```

Drift is caught by `core/dev.sh` on every engine build — it runs
`generate.py --check` and fails on any mismatch. Generated files are
checked in; never hand-edit them.

## License

MIT — see `sdk/python/LICENSE`.
