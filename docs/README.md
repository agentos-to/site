# AgentOS Docs

The documentation site for AgentOS — the `docs/` directory of the
`platform` repo (GitHub remote: `agentos-to/site`). Deploys to
[agentos.to](https://agentos.to) on every push to `main`.

```
CNAME               agentos.to (pins the custom domain each deploy)
src/content/docs/   Prose — principles, shapes, apps, connections, …
scripts/            audit.py (stale-content gate), fix-paths.mjs, …
astro.config.mjs    Starlight config
```

The shape ontology itself lives at `../ontology/` (one YAML per shape);
the generator at `../codegen/generate.py`. This directory is prose +
generated reference pages only.

## Working on it

```bash
pnpm install
pnpm dev            # http://localhost:4321/
pnpm build          # build + post-process for file:// browsing
```

The `pnpm build` script runs `scripts/fix-paths.mjs` after `astro build`
so the `dist/` output is browseable directly off disk. CI deploys run
plain `astro build`, then assemble `CNAME + dist/ → _site/`.

## Codegen

`../codegen/generate.py` reads `../ontology/` and emits typed code into
each consumer surface:

- `../sdk/python/agentos/_generated.py` (Python TypedDicts)
- `../sdk/rust/src/shapes/` (Rust shape tree)
- `../../core/web/src/contract-generated/shapes.ts` (the desktop shell's typed contract)
- `../../core/crates/contract-generated/src/` (Rust — the engine's contract crate)
- `src/content/docs/{apps,shapes,ops}/reference/` + `src/content/docs/tool-surface/` (generated reference pages — never hand-edit)

Run `python3 ../codegen/generate.py --check` to confirm every downstream
artifact is in sync with the current YAML.

## Sibling repos

| Repo                                                       | Lang          | What |
| ---------------------------------------------------------- | ------------- | ---- |
| [`core`](https://github.com/agentos-to/core)               | Rust + TS     | The engine, CLI, MCP server, desktop shell |
| **`site`** (this repo)                                     | YAML + Python + Astro | Ontology + codegen + Python SDK + docs — deploys to [agentos.to](https://agentos.to) |
| [`apps`](https://github.com/agentos-to/apps)               | Python        | Apps (platform connectors) |
| [`commons`](https://github.com/agentos-to/commons)         | Mixed         | Themes, wallpapers, pre-installed apps |

## Contributing

[Open an issue](https://github.com/agentos-to/site/issues) or a PR.

## License

MIT — see `../sdk/python/LICENSE`.
