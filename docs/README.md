# AgentOS Docs

The documentation site and shape ontology for AgentOS. Deploys to
[agentos.to](https://agentos.to) on every push to `main`.

```
CNAME               agentos.to (pins the custom domain each deploy)
src/content/docs/   Prose — principles, shapes, skills, connections, …
shapes/             *.yaml — the shape ontology (source of truth)
generate.py         Codegen — reads shapes/, emits typed code into sibling SDKs
astro.config.mjs    Starlight config
```

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

`generate.py` reads `shapes/*.yaml` and emits typed code into each
consumer SDK and into the Rust engine:

- `../sdk-skills/agentos/_generated.py` (Python TypedDicts)
- `../sdk-apps/src/shapes.ts` (TypeScript interfaces)
- `../core/crates/shapes/src/generated.rs` (Rust `pub const` names)

Run `python3 generate.py --check` to confirm every downstream artifact
is in sync with the current YAML.

## Sibling repos

| Repo                                                       | Lang         | What |
| ---------------------------------------------------------- | ------------ | ---- |
| [`core`](https://github.com/agentos-to/core)               | Rust + TS    | The engine, CLI, MCP server |
| **`docs`** (this repo)                                     | Astro + YAML | Docs + shape ontology — deploys to [agentos.to](https://agentos.to) |
| [`skills`](https://github.com/agentos-to/skills)           | Python       | Python skills |
| [`sdk-skills`](https://github.com/agentos-to/sdk-skills)   | Python       | Skills SDK (pip-installable) |
| [`apps`](https://github.com/agentos-to/apps)               | TypeScript   | Apps |
| [`sdk-apps`](https://github.com/agentos-to/sdk-apps)       | TypeScript   | Apps SDK + React components |

## Contributing

[Open an issue](https://github.com/agentos-to/docs/issues) or a PR.

## License

MIT — see [LICENSE](LICENSE).
