# AgentOS App SDK — Python

The Python SDK for writing AgentOS apps. Installed package name:
`agentos` (so apps `from agentos import http, llm, shell, sql`). CLI
entry point: `agent-sdk`.

[agentos.to](https://agentos.to) · [agentos.to/apps/overview](https://agentos.to/apps/overview/)

## What's here

```
agentos/
  __init__.py       Package surface — from agentos import http, llm, …
  _bridge.py        IPC shim into the Rust engine
  _generated.py     AUTO-GENERATED TypedDicts for every shape (from ontology/shapes/*.yaml)
  http.py           HTTP client with browser-header injection + cookie auth
  llm.py            llm() — the brokered LLM service binding (provider-agnostic)
  services.py       Service name constants + broker stubs (generated)
  shell.py          shell.run — subprocess wrapper
  sql.py            sql.query — SQLite read access
  macos/            macOS-specific helpers (keychain, plist, …)
  validate.py       agent-sdk validate — the static app linter
  cli.py            agent-sdk CLI entry point
  decorators.py     @tool, @returns, @provides
  shapes.py         Shape registry
  …
```

## Install

```bash
pipx install -e .     # from this directory (platform/sdk/python)
```

Apps live in the `apps/` workspace sibling (`~/dev/agentos/apps`
alongside `~/dev/agentos/platform`).

## CLI

```bash
agent-sdk validate                  # audit every app under cwd
agent-sdk validate <app-dir>        # single app
agent-sdk validate --all            # walk the apps/ tree
agent-sdk validate --sandbox        # only banned-import sandbox check
agent-sdk new-app my-app            # scaffold a new app
agent-sdk shapes                    # list available shapes
agent-sdk guide                     # print the app development guide
```

## Generated code

`agentos/_generated.py` and `agentos/services.py` are emitted from
`../../ontology/` by `../../codegen/generate.py`. Do not edit —
regenerate. Drift is checked on every commit via the pre-commit hook.

## Sibling repos

| Repo                                                                   | Lang                  | What |
| ---------------------------------------------------------------------- | --------------------- | ---- |
| [`core`](https://github.com/agentos-to/core)                           | Rust                  | The engine, CLI, MCP server + the desktop shell |
| [`site`](https://github.com/agentos-to/site) (this repo, `platform/`)  | YAML + Python + Astro | The contract — ontology, codegen, both SDKs, docs site |
| [`apps`](https://github.com/agentos-to/apps)                           | Python                | Apps — adapters for third-party platforms |
| `commons` (local)                                                      | TS + assets           | Themes, wallpapers, pre-installed apps |

## License

MIT — see [LICENSE](LICENSE).
