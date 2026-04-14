---
title: "LLM & Agent Workflows"
description: "The llm module provides LLM inference: one-shot calls, multi-turn agent loops with tool calling, and structured output."
---

The `llm` module provides LLM inference: one-shot calls, multi-turn agent loops with tool calling, and structured output.

```python
from agentos import llm
```

The engine resolves the best provider based on the requested model and required features. You don't pick a provider — you describe what you need, and the engine matches. Switching providers = changing credentials, not code.

## llm.oneshot() — single LLM call

```python
result = await llm.oneshot(prompt="Summarize this text.", model="sonnet")
print(result["content"])  # "Here is the summary..."
```

No tools, no agent loop.

**Parameters:**
- `prompt` — the user message
- `model` — `"opus"`, `"sonnet"`, `"haiku"`, or provider-specific (default `"sonnet"`)
- `system` — system prompt (optional)
- `temperature` — 0-1 (default 0)

## llm.agent() — multi-turn agent with tools

```python
result = await llm.agent(
    prompt="Research Python async frameworks and summarize findings.",
    system="You are a technical researcher.",
    model="sonnet",
    tools=["exa.search"],
    output_schema={
        "type": "object",
        "properties": {
            "summary": {"type": "string"},
            "frameworks": {
                "type": "array",
                "items": {"type": "object", "properties": {
                    "name": {"type": "string"},
                    "pros": {"type": "array", "items": {"type": "string"}},
                }}
            }
        },
        "required": ["summary", "frameworks"]
    },
    timeout=300,
)

print(result["content"])       # agent's final text response
print(result["data"])          # structured output (parsed JSON matching schema)
print(result["iterations"])    # how many LLM calls were made
print(result["tool_calls"])    # every tool call with name, input, output
```

The agent loop runs in Python. It calls the LLM, dispatches tool calls through the engine, appends results to the conversation, and repeats until the LLM stops calling tools. Everything is `await` — the event loop is never blocked.

**Parameters:**
- `prompt` — the task for the agent
- `system` — system prompt for persona/role (default `""`)
- `model` — `"opus"`, `"sonnet"`, `"haiku"`, or provider-specific (default `"sonnet"`)
- `tools` — tool refs in `"skill.tool"` format (e.g., `["exa.search"]`)
- `max_iterations` — max LLM call iterations (default 20)
- `temperature` — 0-1 (default 0)
- `output_schema` — JSON Schema dict for structured output (optional)
- `timeout` — max wall-clock seconds (default 600)

**Returns:**
```python
{
    "content": str,           # agent's final text response
    "data": dict | None,      # structured output if output_schema set
    "usage": dict,            # {"input_tokens": int, "output_tokens": int}
    "iterations": int,        # how many LLM calls were made
    "tool_calls": list,       # [{name, input, output, error, iteration}]
    "error": str | None,      # error message if agent failed
}
```

**Raises:**
- `AgentError` — if the agent loop fails (tool error, LLM error, max iterations)
- `asyncio.TimeoutError` — if timeout exceeded
- `ValueError` — if any tool ref is invalid

## Tool refs

Tool refs identify tools available to agents. Format: `"skill.tool"` (e.g., `"exa.search"`, `"hackernews.search_posts"`).

Discover available tool refs at runtime:

```python
available = await llm.tools(["exa.search", "hackernews.search_posts"])
# Returns Anthropic-format tool definitions:
# [{"name": "exa.search", "description": "...", "input_schema": {...}}]
```

Tool refs are validated when `llm.agent()` is called. Invalid refs raise `ValueError` immediately — fail fast, not mid-loop.

## Structured output — output_schema

Pass a JSON Schema dict to get structured data back:

```python
result = await llm.agent(
    prompt="Identify 3 personas for this project.",
    output_schema={
        "type": "object",
        "properties": {
            "personas": {
                "type": "array",
                "items": {"type": "object", "properties": {
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                    "painPoints": {"type": "array", "items": {"type": "string"}},
                }}
            }
        },
        "required": ["personas"]
    },
)
personas = result["data"]["personas"]  # typed, no regex
```

The engine uses provider-native structured output when available (e.g., Anthropic's JSON mode), with a fallback extraction for providers that don't support it natively.

## Parallel agents — asyncio.gather()

Multiple agents run concurrently via standard Python async:

```python
import asyncio
from agentos import llm

results = await asyncio.gather(
    llm.agent(prompt="Research topic A", tools=["exa.search"]),
    llm.agent(prompt="Research topic B", tools=["exa.search"]),
    llm.agent(prompt="Research topic C", tools=["exa.search"]),
)

for r in results:
    print(r["data"])
```

While Agent A waits for an LLM response, Agent B dispatches a tool, and Agent C processes results. The Python event loop multiplexes all of them on a single thread. No custom parallel primitives — just `asyncio`.

Use `asyncio.as_completed()` to process results as they arrive:

```python
tasks = [
    llm.agent(prompt=f"Evaluate section: {s}", output_schema=EVAL_SCHEMA)
    for s in sections
]
for coro in asyncio.as_completed(tasks):
    result = await coro
    scores.append(result["data"]["score"])
```

## Agent nesting

An agent can spawn sub-agents — just call `llm.agent()` inside a tool dispatch or inline. Recursive async calls work naturally:

```python
async def write_proposal(topic, **params):
    # Top-level agent identifies personas
    personas = await llm.agent(prompt=f"Identify personas for: {topic}", ...)

    # Each persona runs its own agent loop with tools
    sections = await asyncio.gather(*[
        llm.agent(
            prompt=f"Research {p['name']} perspective on: {topic}",
            system=persona_prompt,
            tools=["exa.search"],
            output_schema=SECTION_SCHEMA,
        )
        for p in personas["data"]["personas"]
    ])
```

No depth limit, no special nesting API.

## AgentError

```python
from agentos.llm import AgentError

try:
    result = await llm.agent(prompt="...", tools=["exa.search"])
except AgentError as e:
    print(e.phase)      # "tool_call", "llm_chat", "timeout", "max_iterations"
    print(e.iteration)  # which iteration failed
    print(e.cause)      # underlying error message
```

## Async skills

All `llm` functions are async. Skills that use them must be `async def`:

```python
from agentos import llm, returns

@returns("document")
async def write_report(topic: str, output: str, **params):
    """Generate a research report using parallel agents."""
    result = await llm.agent(prompt=f"Research: {topic}", tools=["exa.search"])
    return {"id": topic, "name": f"Report: {topic}", "content": result["content"]}
```

The engine detects async functions and runs them on an asyncio event loop. Sync functions continue to work as before — no migration required for skills that don't need agent workflows.

## Checkpoint — resume multi-phase workflows

Long-running skills (multi-agent proposal writing, research pipelines) can save state after each completed phase and resume on restart.

```python
from agentos import checkpoint
```

### save / load / clear

```python
async def write_proposal(topic, output, **params):
    # Check for existing checkpoint
    state = checkpoint.load(output)
    if state and state.get("phase", 0) >= 2:
        # Resume from Phase 3 — skip completed work
        sections = state["sections"]
        personas = state["personas"]
    else:
        # Phase 1-2: Generate RFP
        personas = await _identify_personas(topic)
        sections = await asyncio.gather(*[...])

        # Save after each completed unit of work
        checkpoint.save(output, {
            "phase": 2,
            "personas": personas,
            "sections": sections,
        })

    # Phase 3-4: Proposal + evaluation
    ...

    # Clear checkpoint on success
    checkpoint.clear(output)
```

**Functions:**
- `checkpoint.save(output_dir, state)` — atomic write (temp file + rename). `state` must be JSON-serializable.
- `checkpoint.load(output_dir)` → `dict | None` — returns saved state, or `None` if no checkpoint.
- `checkpoint.clear(output_dir)` — removes checkpoint file after successful completion.

Checkpoint is opt-in. Skills that don't call `save()` have no checkpoint file. The file is `.checkpoint.json` in the skill's output directory.

## Provider architecture

LLM providers (claude, anthropic-api, openrouter, ollama) are skills that declare `@provides(llm)` with feature capabilities:

```python
from agentos import provides
from agentos.tools import llm

@provides(llm,
    models=["opus", "sonnet", "haiku"],
    features=["tool_calling", "structured_output", "streaming"],
)
async def chat(model, messages, tools=None, output_schema=None, **params):
    ...
```

When you call `llm.agent()` or `llm.oneshot()`, the engine resolves the best provider based on the requested model and required features.

**Feature vocabulary:**

| Feature | Meaning |
|---------|---------|
| `tool_calling` | Function/tool calling in requests |
| `structured_output` | JSON Schema-constrained responses |
| `structured_output_with_tools` | Both in same request |
| `streaming` | Token-level streaming |
| `thinking` | Extended thinking / reasoning traces |
| `vision` | Image inputs |
