"""Model brokering — `chat` (one completion) and `agent` (a tool-loop).

    from agentos import chat, agent

    msg = await chat(prompt="Summarize this.", model="haiku")
    out = await agent(prompt="Review this code.", model="opus", tools=["exa.search"])

The two functions are named by what they *return*, not by an input
modality: `chat` hands back a message, `agent` hands back the trace of a
tool-loop. There is no `llm` synonym at any layer — the SDK function, the
broker verb, and the `@provides` name are the same word.

All functions are async. Apps must use `await` on every call. For parallel
agents, use `asyncio.gather()`:

    results = await asyncio.gather(
        agent(prompt="Research A", tools=["exa.search"]),
        agent(prompt="Research B", tools=["exa.search"]),
    )

Both functions are thin: the engine does the routing. `chat()` ranks
`@provides("chat")` providers here (cred + model-match) and dispatches;
`agent()` just brokers `services.call("agent")` and lets matchmaking pick the
provider. Adding a new provider app needs zero Rust — it's picked up from the
ontology and routed like any other.

Routing:
  - `chat(model)`  → brokers `@provides("chat")` — one completion, no loop.
  - `agent(model, tools)` → brokers `@provides("agent")`. Matchmaking prefers a
    native provider that declares the model (claude_code's `claude -p`, which
    executes tools itself) and falls back to the engine's wildcard `agent-loop`
    capability (the model-agnostic loop over `chat` providers) for any other
    model. The loop lives in the engine, not here — `agent()`, the MCP
    `services.agent` op, and the eval runner all travel the same path.
"""

import asyncio
import json

from agentos import services
from agentos._bridge import dispatch


class AgentError(Exception):
    """Raised when an agent loop fails.

    Attributes:
        phase: Which phase failed (e.g. "tool_call", "llm_chat", "timeout")
        iteration: Which iteration the error occurred on
        cause: The underlying error message
    """

    def __init__(self, message, *, phase="unknown", iteration=0, cause=None):
        super().__init__(message)
        self.phase = phase
        self.iteration = iteration
        self.cause = cause


# ---------------------------------------------------------------------------
# Provider selection — the matchmaking loop that used to live in
# `ops-llm-router/` (Rust). Moved to Python for the same reason every other
# bespoke matchmaker went: the engine doesn't need to know "chat" or "agent"
# as categories. They're just another @provides(X).
# ---------------------------------------------------------------------------


_CRED_PRIORITY = {"not_required": 0, "present": 1, "missing": 2}


def _rank(p: dict) -> tuple:
    """Rank a provider: a declared-model (`exact`) match beats a wildcard
    provider, then prefer credentialed providers. This is principle 3 — route
    by the model the provider declares, not by cred-rank luck (an ollama with
    no `models=` must not shadow a Claude provider that declares `sonnet`).
    """
    exact = 0 if p.get("model_match") == "exact" else 1
    cred = _CRED_PRIORITY.get(p.get("cred_state", "missing"), 2)
    return (exact, cred)


def _is_auth_error(err: str) -> bool:
    low = (err or "").lower()
    return any(
        k in low
        for k in (
            "401",
            "403",
            "unauthorized",
            "forbidden",
            "invalid api key",
            "invalid_api_key",
            "authentication failed",
        )
    )


async def _call_chat(params: dict) -> dict:
    """Run one chat completion via matchmaking + fallback.

    Ranks every `@provides("chat")` provider by cred_state, calls the best
    one, and falls back on auth errors to the next credentialed provider.
    """
    model = params.get("model") or "sonnet"
    listing = await services.list_providers("chat", model=model)
    providers = sorted(listing.get("providers") or [], key=_rank)

    if not providers:
        raise RuntimeError(f"No chat provider found for model: {model}")

    last_error: str | None = None
    tried: list[str] = []

    for provider in providers:
        app_id = provider["app_id"]
        verb = provider.get("via") or "chat"
        try:
            result = await services.call(
                "chat", verb=verb, app=app_id, params=params,
            )
        except Exception as e:
            err = str(e)
            tried.append(f"{app_id}:{verb} (invoke: {err})")
            last_error = err
            if _is_auth_error(err):
                continue
            # Non-auth failure — don't keep trying providers. Surface
            # the error to the caller with enough context to diagnose.
            raise RuntimeError(
                f"chat provider {app_id}.{verb} failed: {err} "
                f"(tried: {', '.join(tried)})"
            ) from e

        # Some providers return a app_error envelope instead of
        # raising. Treat a `_error` field as a retry signal.
        err_msg = None
        if isinstance(result, dict):
            err_msg = result.get("_error") or result.get("__error__")
        if err_msg:
            tried.append(f"{app_id}:{verb} ({err_msg})")
            last_error = err_msg
            if _is_auth_error(err_msg):
                continue
            raise RuntimeError(
                f"chat provider {app_id}.{verb} returned error: {err_msg} "
                f"(tried: {', '.join(tried)})"
            )

        return result

    raise RuntimeError(
        f"All chat providers failed: {last_error} (tried: {', '.join(tried)})"
    )


async def chat(*, prompt, model="sonnet", system=None, temperature=0) -> dict:
    """One model completion. No tools, no agent loop.

    Brokers `@provides("chat")`: picks the best provider for the model,
    calls its chat operation, returns the response. A single call with no
    loop *is* `chat` — there is no separate "oneshot".
    """
    messages = [{"role": "user", "content": prompt}]
    return await _call_chat({
        "model": model,
        "messages": messages,
        "system": system or "",
        "temperature": temperature,
    })


async def tools(refs: list[str]) -> list[dict]:
    """Resolve tool refs to provider-native tool definitions.

    Args:
        refs: Tool refs in "app.operation" format (e.g., ["exa.search"])

    Returns:
        List of Anthropic-format tool definitions:
        [{"name": "exa.search", "description": "...", "input_schema": {...}}]

    Raises:
        ValueError: If any tool ref is invalid or not found
    """
    result = await dispatch("agent.resolve_tools", {"tools": refs})
    return result.get("tools", [])


async def agent(*, prompt, system="", model="sonnet", tools=None,
                files=None, max_iterations=20, temperature=0,
                output_schema=None, timeout=600) -> dict:
    """Spawn a sub-agent: a tool-loop that iterates to a final answer.

    A thin shim over the brokered `agent` capability — it builds the request
    and hands it to `services.call("agent")`, then normalizes the return. The
    *broker* does the routing: matchmaking prefers a native `@provides("agent")`
    provider that declares the model (claude_code's `claude -p`, which executes
    tools itself), and falls back to the wildcard `agent-loop` provider (the SDK
    loop over `chat` providers) for any other model. There is no native-vs-loop
    branch here — `agent()`, the MCP `services.agent` op, and the eval runner all
    travel the same path.

    Multiple agent() calls can run concurrently via asyncio.gather().

    Args:
        prompt: The task for the agent.
        system: System prompt for persona/role.
        model: Model name — "opus", "sonnet", "haiku", or provider-specific.
        tools: Tool refs in "app.operation" format (e.g., ["exa.search"]).
        files: Reserved for future use (file sandbox boundary).
        max_iterations: Max model call iterations (default 20).
        temperature: Sampling temperature (default 0).
        output_schema: JSON Schema dict for structured output. When set,
            the agent is instructed to respond with JSON matching this schema.
        timeout: Max wall-clock seconds (default 600).

    Returns:
        {
            "content": str,           # agent's final text response
            "data": dict | None,      # structured output if output_schema set
            "usage": dict,            # aggregate token counts
            "iterations": int,        # how many model calls were made
            "tool_calls": list,       # every tool call with name, input, output
            "error": str | None,      # error message if agent failed
        }

    Raises:
        AgentError: If the agent loop fails (tool error, model error, etc.)
        asyncio.TimeoutError: If timeout exceeded.
        ValueError: If any tool ref is invalid.
    """
    params = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}],
        "system": system or "",
        "tools": tools or [],
        "temperature": temperature,
        "max_iterations": max_iterations,
    }
    if output_schema:
        params["output_schema"] = output_schema

    result = await asyncio.wait_for(
        services.call("agent", params=params),
        timeout=timeout,
    )

    # A failed/capped run comes back as a first-class conversation with
    # status "error"/"timeout" (so the run is still recorded on the graph),
    # not as a raised dispatch error. Re-raise it here so a Python caller
    # keeps its fail-loud contract — the run's transcript is on the graph.
    status = result.get("status")
    if status in ("error", "timeout"):
        raise AgentError(
            result.get("error") or f"agent run ended: {status}",
            phase="timeout" if status == "timeout" else "run",
            iteration=result.get("iterations") or 0,
            cause=result.get("error"),
        )

    content = result.get("content") or ""
    data = result.get("structured_output")
    if data is None and output_schema and content:
        data = _extract_json(content)

    return {
        "content": content,
        "data": data,
        "usage": result.get("usage") or {},
        "iterations": result.get("iterations") or result.get("num_turns", 0),
        "tool_calls": result.get("tool_calls") or [],
        "error": None,
    }


# `agent.tools(...)` — resolve tool refs off the agent surface.
agent.tools = tools


def _extract_json(text: str) -> dict | None:
    """Try to extract JSON from text. Handles markdown code blocks."""
    text = text.strip()

    # Try direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Try extracting from ```json ... ``` blocks
    if "```" in text:
        import re
        match = re.search(r'```(?:json)?\s*\n?(.*?)\n?\s*```', text, re.DOTALL)
        if match:
            try:
                return json.loads(match.group(1).strip())
            except json.JSONDecodeError:
                pass

    return None
