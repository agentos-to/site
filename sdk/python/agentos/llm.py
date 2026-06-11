"""LLM inference — oneshot calls and agent loops.

    from agentos import llm

    result = await llm.oneshot(prompt="Summarize this.", model="haiku")
    result = await llm.agent(prompt="Review this code.", model="opus", tools=["exa.search"])

All functions are async. Apps must use `await` on every call.
For parallel agents, use `asyncio.gather()`:

    results = await asyncio.gather(
        llm.agent(prompt="Research A", tools=["exa.search"]),
        llm.agent(prompt="Research B", tools=["exa.search"]),
    )

Provider selection and fallback happen here, not in Rust. The engine
only ships the generic `services.call` + `services.list_providers`
primitives; this module stacks ranking + retry on top. Adding a new
`@provides(llm)` app needs zero Rust — list_providers picks it up
from the ontology and oneshot/agent route to it like any other
provider.
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
# `ops-llm-router/` (Rust). Moved to Python for the same reason every
# other bespoke matchmaker went: the engine doesn't need to know about
# "LLM" as a category. It's just another @provides(X).
# ---------------------------------------------------------------------------


_CRED_PRIORITY = {"not_required": 0, "present": 1, "missing": 2}


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


async def _call_llm(params: dict) -> dict:
    """Run one chat completion via matchmaking + fallback.

    Replaces the old `dispatch("llm.chat", ...)` sideband — the Rust
    router is gone. Ranks every `@provides(llm)` provider by
    cred_state, calls the best one, and falls back on auth errors to
    the next credentialed provider.
    """
    model = params.get("model") or "sonnet"
    listing = await services.list_providers("llm", model=model)
    providers = sorted(
        listing.get("providers") or [],
        key=lambda p: _CRED_PRIORITY.get(p.get("cred_state", "missing"), 2),
    )

    if not providers:
        raise RuntimeError(f"No LLM provider found for model: {model}")

    last_error: str | None = None
    tried: list[str] = []

    for provider in providers:
        app_id = provider["app_id"]
        verb = provider.get("via") or "chat"
        try:
            result = await services.call(
                "llm", verb=verb, app=app_id, params=params,
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
                f"LLM provider {app_id}.{verb} failed: {err} "
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
                f"LLM provider {app_id}.{verb} returned error: {err_msg} "
                f"(tried: {', '.join(tried)})"
            )

        return result

    raise RuntimeError(
        f"All LLM providers failed: {last_error} (tried: {', '.join(tried)})"
    )


async def oneshot(*, prompt, model="sonnet", system=None,
                  temperature=0) -> dict:
    """Single LLM call. No tools, no agent loop.

    The SDK picks the best `@provides(llm)` provider for the model,
    calls its chat operation, and returns the response.
    """
    messages = [{"role": "user", "content": prompt}]
    return await _call_llm({
        "model": model,
        "messages": messages,
        "system": system or "",
        "temperature": temperature,
    })


async def tools(refs: list[str]) -> list[dict]:
    """Resolve tool refs to LLM tool definitions.

    Args:
        refs: Tool refs in "app.operation" format (e.g., ["exa.search"])

    Returns:
        List of Anthropic-format tool definitions:
        [{"name": "exa.search", "description": "...", "input_schema": {...}}]

    Raises:
        ValueError: If any tool ref is invalid or not found
    """
    result = await dispatch("llm.resolve_tools", {"tools": refs})
    return result.get("tools", [])


async def agent(*, prompt, system="", model="sonnet", tools=None,
                files=None, max_iterations=20, temperature=0,
                output_schema=None, timeout=600) -> dict:
    """Multi-turn agent loop with tool dispatch.

    Runs an LLM agent that can call tools and iterate until it produces
    a final answer. Multiple agent() calls can run concurrently via
    asyncio.gather() — each runs as an independent async task.

    Args:
        prompt: The task for the agent.
        system: System prompt for persona/role.
        model: Model name — "opus", "sonnet", "haiku", or provider-specific.
        tools: Tool refs in "app.operation" format (e.g., ["exa.search"]).
        files: Reserved for future use (file sandbox boundary).
        max_iterations: Max LLM call iterations (default 20).
        temperature: LLM temperature (default 0).
        output_schema: JSON Schema dict for structured output. When set,
            the agent is instructed to respond with JSON matching this schema.
        timeout: Max wall-clock seconds (default 600).

    Returns:
        {
            "content": str,           # agent's final text response
            "data": dict | None,      # structured output if output_schema set
            "usage": dict,            # aggregate token counts
            "iterations": int,        # how many LLM calls were made
            "tool_calls": list,       # every tool call with name, input, output
            "error": str | None,      # error message if agent failed
        }

    Raises:
        AgentError: If the agent loop fails (tool error, LLM error, etc.)
        asyncio.TimeoutError: If timeout exceeded.
        ValueError: If any tool ref is invalid.
    """
    # Resolve tool definitions
    tool_defs = []
    tool_refs = tools or []
    if tool_refs:
        tool_defs = await _resolve_tools(tool_refs)

    # Build system prompt with output_schema instructions
    full_system = system or ""
    if output_schema:
        schema_instruction = (
            "\n\nYou MUST respond with valid JSON matching this schema:\n"
            f"```json\n{json.dumps(output_schema, indent=2)}\n```\n"
            "Output ONLY the JSON object, no other text."
        )
        full_system = (full_system + schema_instruction).strip()

    # Initialize conversation
    messages = [{"role": "user", "content": prompt}]
    all_tool_calls = []
    total_usage = {"input_tokens": 0, "output_tokens": 0}

    try:
        result = await asyncio.wait_for(
            _agent_loop(
                model=model,
                system=full_system,
                messages=messages,
                tool_defs=tool_defs,
                tool_refs=tool_refs,
                max_iterations=max_iterations,
                temperature=temperature,
                all_tool_calls=all_tool_calls,
                total_usage=total_usage,
            ),
            timeout=timeout,
        )
    except asyncio.TimeoutError:
        raise AgentError(
            f"Agent timed out after {timeout}s",
            phase="timeout",
            iteration=len(all_tool_calls),
        )

    content = result.get("content", "")

    # Extract structured data if output_schema was set
    data = None
    if output_schema and content:
        data = _extract_json(content)

    return {
        "content": content,
        "data": data,
        "usage": total_usage,
        "iterations": result.get("iterations", 0),
        "tool_calls": all_tool_calls,
        "error": None,
    }


async def _resolve_tools(refs: list[str]) -> list[dict]:
    """Resolve tool refs. `dispatch` raises RuntimeError on engine failure."""
    result = await dispatch("llm.resolve_tools", {"tools": refs})
    return result.get("tools", [])


async def _agent_loop(*, model, system, messages, tool_defs, tool_refs,
                      max_iterations, temperature, all_tool_calls,
                      total_usage) -> dict:
    """Core agent loop — iterate LLM calls and tool dispatches."""
    iterations = 0

    for iteration in range(max_iterations):
        iterations += 1

        # Call LLM
        chat_params = {
            "model": model,
            "messages": messages,
            "system": system,
            "temperature": temperature,
        }
        if tool_defs:
            chat_params["tools"] = tool_defs

        try:
            response = await _call_llm(chat_params)
        except Exception as e:
            raise AgentError(
                f"LLM call failed on iteration {iterations}: {e}",
                phase="llm_chat",
                iteration=iterations,
                cause=str(e),
            )

        # Accumulate usage
        usage = response.get("usage") or {}
        total_usage["input_tokens"] += usage.get("input_tokens", 0)
        total_usage["output_tokens"] += usage.get("output_tokens", 0)

        content = response.get("content") or ""
        tool_calls = response.get("tool_calls") or []
        stop_reason = response.get("stop_reason", "end_turn")

        # If no tool calls, we're done
        if not tool_calls or stop_reason != "tool_use":
            return {"content": content, "iterations": iterations}

        # Add assistant message with tool calls
        messages.append({
            "role": "assistant",
            "content": content,
            "tool_calls": tool_calls,
        })

        # Execute tool calls (concurrently if multiple)
        tool_results = await _execute_tool_calls(
            tool_calls, tool_refs, all_tool_calls, iterations
        )

        # Add tool results to conversation
        for result in tool_results:
            messages.append(result)

    # Hit max iterations
    raise AgentError(
        f"Agent hit max iterations ({max_iterations}) without completing",
        phase="max_iterations",
        iteration=iterations,
    )


async def _execute_tool_calls(tool_calls, tool_refs, all_tool_calls,
                              iteration) -> list[dict]:
    """Execute tool calls and return message dicts for the conversation."""

    async def execute_one(tc):
        name = tc["name"]
        inp = tc.get("input", {})
        tc_id = tc.get("id", "")

        try:
            result = await dispatch(name, inp)
            output = json.dumps(result) if isinstance(result, (dict, list)) else str(result)
            is_error = False
        except Exception as e:
            output = f"Tool error: {e}"
            is_error = True

        all_tool_calls.append({
            "name": name,
            "input": inp,
            "output": output,
            "error": is_error,
            "iteration": iteration,
        })

        return {
            "role": "tool",
            "tool_call_id": tc_id,
            "content": output,
        }

    # Run all tool calls concurrently
    results = await asyncio.gather(
        *(execute_one(tc) for tc in tool_calls),
        return_exceptions=True,
    )

    # Convert exceptions to error messages
    processed = []
    for i, r in enumerate(results):
        if isinstance(r, Exception):
            tc = tool_calls[i]
            processed.append({
                "role": "tool",
                "tool_call_id": tc.get("id", ""),
                "content": f"Tool execution error: {r}",
            })
        else:
            processed.append(r)

    return processed


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
