# AgentOS Site

The landing page + documentation site for AgentOS. Deploys to
[agentos.to](https://agentos.to) on every push to `main`.

```
index.html          Plain-HTML landing page (no build needed)
CNAME               agentos.to (pins the custom domain each deploy)
docs/               Astro/Starlight project — builds to /docs/ on the site
  src/content/docs/ Prose — principles, shapes, skills, connections, …
  shapes/           *.yaml — the shape ontology
  generate.py       Codegen — reads shapes/, emits typed SDK stubs
  astro.config.mjs  Starlight config (base: /docs)
```

## Working on it

Landing page: just edit `index.html`. No build, no framework.

Docs:

```bash
cd docs
pnpm install
pnpm dev            # http://localhost:4321/docs/
pnpm build          # build + post-process for file:// browsing
```

The `pnpm build` script runs `scripts/fix-paths.mjs` after `astro
build` so the `dist/` output is browseable directly off disk. CI
deploys run plain `astro build` at `docs/`, then assemble the
deploy artifact: `index.html` + `CNAME` + `docs/dist/` → `_site/`.

## Codegen

`docs/generate.py` reads `docs/shapes/*.yaml` and emits typed code
into each consumer SDK:

- `../../skills/_sdk/agentos/` (Python)
- `../../apps/_sdk/src/` (TypeScript)

Run it whenever a shape changes.

## Sibling repos

| Repo                                                       | Lang         | What |
| ---------------------------------------------------------- | ------------ | ---- |
| [`core`](https://github.com/agentos-to/core)               | Rust + TS    | The engine, CLI, MCP server |
| **`site`** (this repo)                                     | Astro + YAML | Landing + docs + shapes — deploys to [agentos.to](https://agentos.to) |
| [`skills`](https://github.com/agentos-to/skills)           | Python       | Skills + Python SDK |
| [`apps`](https://github.com/agentos-to/apps)               | TypeScript   | Apps + React components + TS SDK |

## Contributing

[Open an issue](https://github.com/agentos-to/site/issues) or a PR.

## License

MIT — see [LICENSE](LICENSE).
