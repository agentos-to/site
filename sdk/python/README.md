# AgentOS Skills SDK — Python

The Python SDK for writing AgentOS skills. Installed package name:
`agentos` (so skills `from agentos import http, llm, shell, sql`). CLI
entry point: `agent-sdk`.

[agentos.to](https://agentos.to) · [agentos.to/docs/skills](https://agentos.to/docs/skills/)

## What's here

```
agentos/
  __init__.py       Package surface — from agentos import http, llm, …
  _bridge.py        IPC shim into the Rust engine
  _generated.py     AUTO-GENERATED TypedDicts for every shape (from docs/shapes/*.yaml)
  http.py           HTTP client with browser-header injection + cookie auth
  llm.py            LLM capability binding (provider-agnostic)
  shell.py          shell.run — subprocess wrapper
  sql.py            sql.query — SQLite read access
  macos/            macOS-specific helpers (keychain, plist, …)
  validate.py       agent-sdk validate — the static skill linter
  cli.py            agent-sdk CLI entry point
  decorators.py     @tool, @returns, @provides
  shapes.py         Shape registry
  …
```

## Install

```bash
pip install -e ../sdk-skills
```

Run from a skills clone that sits next to this repo
(`~/dev/agentos/skills` alongside `~/dev/agentos/sdk-skills`).

## CLI

```bash
agent-sdk validate                  # audit every skill under cwd
agent-sdk validate <skill-dir>      # single skill
agent-sdk validate --all            # walk skills/ tree
agent-sdk validate --sandbox        # only banned-import sandbox check
agent-sdk new-skill my-skill        # scaffold a new skill
agent-sdk shapes                    # list available shapes
```

## Generated code

`agentos/_generated.py` is emitted from `../docs/shapes/*.yaml` by
`../docs/generate.py --lang python`. Do not edit — regenerate. Drift is
checked on every commit via the pre-commit hook.

## Sibling repos

| Repo                                                     | Lang         | What |
| -------------------------------------------------------- | ------------ | ---- |
| [`core`](https://github.com/agentos-to/core)             | Rust         | The engine, CLI, MCP server |
| [`docs`](https://github.com/agentos-to/docs)             | Astro + YAML | Docs + shapes (ontology) — [agentos.to](https://agentos.to) |
| [`skills`](https://github.com/agentos-to/skills)         | Python       | Skills — adapters for third-party services |
| **`sdk-skills`** (this repo)                             | Python       | Skills SDK — the `agentos` package |
| [`apps`](https://github.com/agentos-to/apps)             | TypeScript   | Apps + React components |
| [`sdk-apps`](https://github.com/agentos-to/sdk-apps)     | TypeScript   | Apps SDK — React components + TS shapes |

## License

MIT — see [LICENSE](LICENSE).
