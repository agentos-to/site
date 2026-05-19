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
