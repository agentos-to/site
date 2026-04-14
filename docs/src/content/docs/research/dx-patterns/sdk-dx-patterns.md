---
title: SDK & Plugin Platform DX Patterns — Research
description: What makes great developer SDKs and extension platforms successful. Concrete patterns extracted from 8 platforms.
---

## 1. Stripe SDK

**The gold standard for API DX.** Stripe's advantage isn't any single feature — it's that every layer reinforces the same mental model.

### Bootstrap
- No scaffolding needed — the SDK _is_ the starting point. `pip install stripe` / `npm install stripe` and you're writing real code in <5 lines.
- `stripe samples` — clone working end-to-end examples (not "hello world" but real checkout flows).
- Stripe Shell in the dashboard — try API calls before writing code.

### Type Safety
- **OpenAPI spec is the source of truth.** A Ruby DSL defines the API shape → exports to OpenAPI → custom codegen generates SDKs in all languages.
- Custom codegen (not off-the-shelf openapi-generator). They spent a year trying generic tools, concluded none met their quality bar. The codegen produces discriminated union types, proper nullability, and resource-specific types.
- TypeScript: first-class `.d.ts` definitions with every SDK resource fully typed. Autocompletion works everywhere.
- Every SDK version is generated from the same spec → consistent behavior across languages.

### Local Testing
- **`stripe listen --forward-to localhost:3000/webhook`** — tunnels webhook events to your local server. No ngrok needed.
- **`stripe trigger payment_intent.succeeded`** — fire specific webhook events on demand.
- **`stripe-mock`** — stateless mock HTTP server that validates request shapes against the real API schema. Fast CI testing without hitting Stripe's servers.
- **Test Clocks** — the killer feature. Deterministic time control: freeze time, advance by days/months, watch subscription lifecycle events fire. Test a full annual billing cycle in 5 minutes instead of 365 days.
- **Test mode** built into the API itself — every API key has a test counterpart. No separate environment to configure.

### Validation
- The OpenAPI spec validates request shapes at the mock level.
- Rich error messages with specific field-level feedback (not just "400 Bad Request").
- Dashboard shows real-time API request logs with expandable request/response bodies.

### Documentation
- Interactive API reference where you can make real API calls from the docs page.
- Every API endpoint has curl, Python, Ruby, Node, Go, etc. examples side-by-side.
- Workbench — a dashboard tool for exploring webhooks, inspecting event payloads, testing integrations visually.

### Magic
- **Error messages that teach.** Stripe errors include the specific parameter that failed, why, and often a link to the relevant docs section.
- **Idempotency keys** — built into the API design, not bolted on. Retry safety by default.
- **Expandable resources** — `?expand[]=customer` in any API call. One mental model for data fetching.

---

## 2. Shopify App Development

**CLI-driven development with built-in tunneling and hot reload.**

### Bootstrap
- `shopify app init` — interactive scaffold. Asks for app type, language (Remix recommended), template.
- Templates include auth flows, Polaris UI components, billing, webhooks — not just empty shells.
- Generates `shopify.app.toml` config that the CLI validates against schemas.

### Type Safety
- GraphQL Admin API with full schema introspection. Codegen tools generate typed queries.
- `shopify.app.toml` has a known schema — CLI validates every field.
- Polaris (UI kit) is fully typed React components.

### Local Testing
- **`shopify app dev`** — one command starts: your app server, Cloudflare tunnel (automatic, no config), reverse proxy routing, hot module reloading. The app is immediately installable on a dev store.
- `--use-localhost` mode with self-signed certs for offline work.
- Dev stores are free, unlimited, pre-configured for testing.

### Validation
- CLI validates `shopify.app.toml` and all extension configs against their schemas before any deploy.
- `shopify app function build` compiles and validates Shopify Functions (WASM) locally.
- CI-friendly: all validation commands exit with proper codes.

### Documentation
- Dev Assistant (AI) trained on Shopify docs — generates complete Function files with correct boilerplate from natural language.
- GraphiQL explorer built into the admin dashboard.

### Magic
- **One command to go from zero to installed app:** `shopify app init && shopify app dev` — you have a running app on a real store in <2 minutes.
- **Automatic tunnel management** — developers never think about networking.

---

## 3. Slack Bolt SDK

**Listener-based framework with separation of concerns.**

### Bootstrap
- Slack CLI: `slack create my-app` — scaffolds from templates.
- Templates include manifest.yaml, event subscriptions, sample listeners.
- Socket Mode for development — no public URL needed, events come over WebSocket.

### Type Safety
- **App Manifest (YAML/JSON)** — declarative app configuration with schema validation.
- `apps.manifest.validate` API endpoint — validate your manifest programmatically before deploying.
- Bolt frameworks (JS/Python/Java) provide typed handler signatures: `app.command("/hello", handler)`, `app.event("app_mention", handler)`.
- TypeScript types for all Slack API payloads.

### Local Testing
- **Socket Mode** — the key DX win. Instead of needing a public URL for webhooks, your app connects outbound via WebSocket. Events arrive locally with zero networking config.
- Sandboxes — Slack CLI creates isolated environments for testing.
- `slack run` — starts your app locally with automatic manifest sync.

### Validation
- Manifest validation inline in the editor with typeahead.
- `apps.manifest.validate` API returns structured errors with `pointer` (JSON path to the problem) and `message`.
- Third-party `slack-manifest` CLI tool for CI/CD validation.

### Documentation
- Full sample apps (not snippets) — e.g., the Tasks app showing a complete joined-up codebase.
- Block Kit Builder — visual tool for composing message layouts, exports to JSON.

### Magic
- **Receiver pattern** — separates your app's server from Bolt framework. Swap HTTP frameworks without changing app logic.
- **Listener middleware** — composable middleware chain per handler, not global.

---

## 4. Home Assistant Custom Integrations

**Scaffold generates files, hassfest validates everything, voluptuous handles schema.**

### Bootstrap
- `python3 -m script.scaffold config_flow_discovery` — generates: `config_flow.py`, `manifest.json`, `const.py`, `api.py`, test files.
- Scaffold command is part of core, not a third-party tool.
- Integration blueprints (community) — GitHub template repos with modern patterns, CI, pre-commit hooks.

### Type Safety
- **Voluptuous** — Python schema validation library. All config schemas are voluptuous schemas:
  ```python
  vol.Schema({
      vol.Required("host"): str,
      vol.Optional("port", default=8080): int,
  })
  ```
- Config flows use voluptuous schemas that auto-generate UI forms.
- `manifest.json` — typed metadata (domain, version, dependencies, iot_class).

### Local Testing
- Run HA Core from checkout with your integration loaded.
- Config flow testing via `hass` test helpers — simulate user input through config flow steps.
- Integration tests use pytest with HA fixtures.

### Validation
- **hassfest** — Home Assistant's integration validation tool. Checks: manifest.json, config_schema, dependencies, requirements, services, translations.
- Runs in CI for all PRs to core.
- `cv.make_entity_service_schema` — enforced schema for entity services (as of 2025.10, custom schemas must meet this).

### Documentation
- Developer docs site with per-component guides.
- Example custom integration repos maintained by HA team.

### Magic
- **Schema → UI generation.** Write a voluptuous schema, get a config UI form for free. The developer never writes UI code for configuration.
- **hassfest catches errors that would only surface at runtime** — it's a static analysis pass over integration metadata.

---

## 5. FastAPI

**Types are the single source of truth for everything: validation, docs, serialization.**

### Bootstrap
- No scaffold needed. One file, one decorator, running API:
  ```python
  @app.get("/items/{id}")
  def read_item(id: int) -> Item:
      ...
  ```
- No project generator because the framework _is_ the boilerplate reduction.

### Type Safety
- **Pydantic models = the schema.** One class defines: validation rules, serialization, documentation, OpenAPI schema, database shape (in many cases).
  ```python
  class Item(BaseModel):
      name: str
      price: float = Field(gt=0)
      tags: list[str] = []
  ```
- Python type hints drive everything — IDE autocompletion everywhere.
- Request body, query params, path params, headers all validated via type hints.

### Local Testing
- `uvicorn main:app --reload` — hot reload on file changes.
- TestClient (based on httpx) for in-process testing without starting a server.
- Dependency injection overrides for testing — swap real services for fakes.

### Validation
- **Validation is automatic.** Define a type → requests are validated. No separate validation layer.
- Pydantic v2: `model_validator`, `field_validator` for custom rules.
- Validation errors return structured JSON with field path + error message.

### Documentation
- **`/docs` (Swagger UI) and `/redoc` generated automatically** from your code. No config. No annotation files. No YAML.
- Docs update live as you change code.
- Try-it-out directly from the docs page.
- Dependency injection graph visible in docs — each endpoint shows its full dependency chain.

### Magic
- **Zero-cost documentation.** You write Python types, you get interactive API docs for free. This is the single most referenced DX feature.
- **Dependency injection that documents itself.** Dependencies appear in the OpenAPI schema, so consumers see what each endpoint requires.
- **Editor completion drives API design.** The framework was designed around "what makes autocomplete work best."

---

## 6. Terraform Providers

**Schema-first development with acceptance tests that run real infrastructure.**

### Bootstrap
- **Code generation pipeline:** OpenAPI spec → Provider Code Specification (JSON) → Framework Code Generator → Go files.
- `tfplugingen-framework generate` + `tfplugingen-framework scaffold` — generates `_gen.go` files with schema and data models.
- OpenAPI spec generator for REST APIs: feed it your OpenAPI spec, get a Terraform provider skeleton.

### Type Safety
- **Schema is Go code.** Each resource defines its schema in Go structs with typed attributes:
  ```go
  schema.StringAttribute{Required: true, Validators: []validator.String{...}}
  ```
- Provider-defined types — custom types with validation baked in (not just primitives).
- `terraform-plugin-framework-validators` module — reusable validators for common patterns (string length, regex match, integer range).

### Local Testing
- **Acceptance tests run actual Terraform plans.** `resource.Test()` runs plan → apply → refresh → destroy cycle.
- TestCase/TestStep pattern — each step is a Terraform config string + check functions.
- `TF_ACC` env var gates real tests — prevents accidental resource creation.
- Unit tests for schema validation via `ValidateImplementation()`.

### Validation
- Schema validation at multiple points: `ValidateProviderConfig`, `ValidateResourceConfig`, `ValidateDataSourceConfig`.
- Attribute-level validators, resource-level validators, provider-level validators — hierarchical.
- Plan-time validation (before any resources are created).
- `terraform validate` command for syntax + schema checking.

### Documentation
- Registry documentation generated from schema — resource attributes, types, defaults all auto-documented.
- `tfplugindocs` generates markdown docs from schema + examples.

### Magic
- **Plan is a dry run.** Developers see exactly what will happen before anything changes. This is Terraform's core DX insight.
- **Acceptance tests are real.** No mocks, no fakes — tests create actual infrastructure and verify it. This catches real bugs.
- **Schema generates docs.** Write the schema, get the Terraform Registry docs for free.

---

## 7. VS Code Extensions

**Declarative manifest + typed API + in-editor debugging.**

### Bootstrap
- `yo code` (Yeoman generator) — interactive scaffold. Picks: TypeScript/JavaScript, extension type (color theme, language, snippets, full extension).
- Generated project includes: `package.json` (manifest), `src/extension.ts`, `.vscode/launch.json` (debug config), test skeleton.

### Type Safety
- **`@types/vscode`** — complete TypeScript definitions for the entire VS Code API.
- `engines.vscode` in package.json controls which API version you target — types match exactly.
- `package.json` contribution points are the schema — commands, menus, settings, keybindings all declared in JSON with known structure.

### Local Testing
- **F5 debugging** — press F5, a new VS Code window opens with your extension loaded. Set breakpoints, inspect variables, hot reload.
- `@vscode/test-electron` — runs VS Code in a test harness, your extension loads, you assert against the real VS Code API.
- `@vscode/test-cli` — command-line test runner for CI.

### Validation
- `package.json` is validated against the VS Code extension schema (contribution points, activation events).
- `vsce` (VS Code Extension CLI) validates before publishing.
- TypeScript compiler catches API misuse at compile time.

### Documentation
- Full API reference at `code.visualstudio.com/api`.
- Extension samples repo with 50+ examples.
- Contribution points reference — every declarative extension point documented with examples.

### Magic
- **F5 is instant feedback.** Edit code → press F5 → see it running in a real VS Code window. No deploy, no build step (with esbuild watch).
- **Declarative + imperative hybrid.** Simple things (commands, menus, settings) are pure JSON in `package.json`. Complex things are TypeScript. You pick the right tool.
- **Activation events** — your extension only loads when relevant. Declared in JSON, enforced by the runtime.

---

## 8. OpenAI Function Calling / Structured Outputs

**JSON Schema as the contract, with runtime enforcement.**

### Bootstrap
- No scaffolding. Define tools as JSON Schema objects inline:
  ```python
  tools = [{"type": "function", "function": {
      "name": "get_weather",
      "parameters": {"type": "object", "properties": {"location": {"type": "string"}}}
  }}]
  ```
- OpenAI Agents SDK: define tools as Python functions with type hints → schema auto-generated via Pydantic.
- Playground "Generate Anything" — describe a function in natural language, get a valid schema.

### Type Safety
- **`strict: true`** — constrained decoding. The model can _only_ output tokens that match your JSON Schema. Not "tries its best" — mathematically guaranteed.
- Pydantic models → JSON Schema → sent to API. Types flow from Python to API contract.
- Agents SDK: `function_schema` module introspects Python type hints and builds the tool schema automatically.

### Local Testing
- No special tooling — you call the API and verify the output matches your schema.
- Pydantic validation on the response side catches schema mismatches.

### Validation
- API-side: schema validated before the request is processed. Invalid schemas return errors.
- `strict: true` schemas have restrictions (no `default` values, no `format` fields) — API validates these constraints.
- Structured errors when manifest/schema validation fails.

### Documentation
- Cookbook notebooks with end-to-end examples.
- API reference with inline schema examples.
- Playground for interactive testing.

### Magic
- **Constrained decoding is the breakthrough.** With `strict: true`, the model literally cannot produce invalid JSON. This eliminates an entire class of parsing/validation bugs.
- **Python types → tool schema → constrained output** — a single type definition flows through the entire stack.

---

## Cross-Platform Patterns — What Actually Matters

### Tier 1: Non-Negotiable (every great platform has these)

| Pattern | Who does it | Why it matters |
|---------|-------------|----------------|
| **Schema is the source of truth** | Stripe (OpenAPI), FastAPI (Pydantic), Terraform (Go schema), HA (voluptuous), Slack (manifest YAML), OpenAI (JSON Schema) | One definition → validation + docs + types + UI. Eliminates drift. |
| **Types flow from schema to code** | Stripe (codegen), FastAPI (type hints), VS Code (`@types/vscode`), OpenAI (Pydantic → JSON Schema) | Developers get autocomplete + compile-time errors. |
| **Local testing without deployment** | Stripe (`listen`/`trigger`/`mock`), Shopify (`app dev` + tunnel), Slack (Socket Mode), VS Code (F5), FastAPI (`--reload`) | If you can't test locally, you can't iterate fast. |
| **Structured error messages** | Stripe (field-level errors + docs links), FastAPI (field path + message), Slack (pointer + message), Terraform (plan output) | Developers must know _what_ failed and _where_. |

### Tier 2: Major DX Multipliers

| Pattern | Who does it | Why it matters |
|---------|-------------|----------------|
| **Schema → docs generation** | FastAPI (`/docs`), Terraform (Registry docs), Stripe (API reference) | Zero-cost documentation. Docs never drift from implementation. |
| **Schema → UI generation** | Home Assistant (voluptuous → config flow UI), FastAPI (Pydantic → Swagger try-it) | Developer writes data shape, gets UI for free. |
| **One-command bootstrap** | Shopify (`app init`), VS Code (`yo code`), HA (`script.scaffold`), Slack (`slack create`) | Eliminates "where do I start?" friction. |
| **CLI validates before deploy** | Shopify (schema validation), Slack (`manifest.validate`), Terraform (`validate`), HA (hassfest) | Catch errors in dev, not production. |
| **Declarative manifest** | VS Code (`package.json`), Slack (manifest), Shopify (`shopify.app.toml`), HA (`manifest.json`) | Machine-readable config enables tooling, validation, and generation. |

### Tier 3: Delightful Extras

| Pattern | Who does it | Why it matters |
|---------|-------------|----------------|
| **Time manipulation for testing** | Stripe (Test Clocks) | Test time-dependent behavior without waiting. |
| **Constrained output** | OpenAI (`strict: true`) | Eliminate entire error classes by construction. |
| **Dependency injection** | FastAPI (Depends), VS Code (activation events) | Testability + documentation of requirements. |
| **Error messages that teach** | Stripe (docs links in errors) | Turn errors into learning moments. |
| **Plan/dry-run** | Terraform (`plan`), Shopify (validation before deploy) | See effects before committing. |

---

## Key Takeaway for agentOS

The pattern that appears in **every** successful platform:

> **One schema definition generates everything: validation, types, documentation, and (where applicable) UI.**

- Stripe: OpenAPI → SDKs + docs + mock validation
- FastAPI: Pydantic model → validation + Swagger docs + serialization
- Terraform: Go schema → validation + Registry docs + plan output
- Home Assistant: voluptuous schema → validation + config UI
- OpenAI: JSON Schema → constrained decoding + validation
- VS Code: package.json → activation + contribution points + marketplace listing

The second universal pattern:

> **Local testing must be zero-config.** Stripe gives you `listen`/`trigger`. Shopify auto-tunnels. Slack has Socket Mode. FastAPI has `--reload`. VS Code has F5. The developer should never think about infrastructure to test their work.
