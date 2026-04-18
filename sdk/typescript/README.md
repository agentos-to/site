# AgentOS Apps SDK — TypeScript

The TypeScript SDK for building AgentOS apps. Package name: `@agentos/sdk`.
Exposes typed shape interfaces (`Book`, `Person`, `Event`, …) generated
from the shared shape ontology in [`docs/shapes/`](../docs/shapes).

[agentos.to](https://agentos.to) · [agentos.to/docs/apps](https://agentos.to/docs/apps/)

## Usage

```ts
import { Book, Person, Event } from '@agentos/sdk'
```

## What's here

```
src/
  index.ts        Package entry — re-exports shapes
  shapes.ts       AUTO-GENERATED TypeScript interfaces for every shape
```

## Generated code

`src/shapes.ts` is emitted from `../docs/shapes/*.yaml` by
`../docs/generate.py --lang typescript`. Do not edit — regenerate.
Drift is checked on every commit via the pre-commit hook.

```bash
npm run generate      # → cd ../docs && python3 generate.py --lang typescript
```

## Build

```bash
npm install
npm run build
```

## Sibling repos

| Repo                                                     | Lang         | What |
| -------------------------------------------------------- | ------------ | ---- |
| [`core`](https://github.com/agentos-to/core)             | Rust         | The engine, CLI, MCP server |
| [`docs`](https://github.com/agentos-to/docs)             | Astro + YAML | Docs + shapes (ontology) — [agentos.to](https://agentos.to) |
| [`skills`](https://github.com/agentos-to/skills)         | Python       | Skills — adapters for third-party services |
| [`sdk-skills`](https://github.com/agentos-to/sdk-skills) | Python       | Skills SDK — the `agentos` package |
| [`apps`](https://github.com/agentos-to/apps)             | TypeScript   | Apps + React components |
| **`sdk-apps`** (this repo)                               | TypeScript   | Apps SDK — `@agentos/sdk` |

## License

MIT — see [LICENSE](LICENSE).
