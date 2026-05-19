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
│   └── auth-contracts/*.yaml  OAuth + cookie provider return shapes
├── codegen/               one generator: YAML → typed code
│   ├── generate.py            orchestrator (shapes, auth, docs)
│   ├── sdk_client.py          engine-client emitter
│   ├── tool_surface.py        tool-surface docs emitter
│   └── gen_sdk_stubs.py       op-stub emitter (reads core's ops-manifest.json)
├── sdk/
│   ├── python/            the `agentos` package — Python Skills SDK
│   └── typescript/        `@agentos/sdk` — TypeScript Apps SDK
└── docs/                  Astro site → agentos.to
```

## Codegen flow

`codegen/generate.py` is the single generator. It reads
`ontology/shapes/*.yaml` and emits typed code into every consumer:

| Target | Path |
|---|---|
| Python SDK | `sdk/python/agentos/_generated.py` |
| TypeScript SDK | `sdk/typescript/src/shapes.ts` |
| Rust (cross-repo) | `core/crates/shapes-generated/src/lib.rs` |
| Reference docs | `docs/src/content/docs/` |

```bash
cd codegen && python3 generate.py            # shapes + auth → all SDKs
cd codegen && python3 generate.py --docs     # MDX reference pages
cd codegen && python3 generate.py --check    # drift check, exits 1 on stale
```

Drift is caught by `core/dev.sh` on every engine build — it runs
`gen_sdk_stubs.py` and `generate.py --check` and fails on any
mismatch. Generated files are checked in; never hand-edit them.

> The op contract is still hand-written Rust in `core/crates/ops/`
> with a second codegen path. Folding ops into `ontology/ops/*.yaml`
> under this same generator is the rest of the Platform project —
> see `core/_roadmap/p1/platform/plan.md`.

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
