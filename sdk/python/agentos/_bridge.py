"""Engine dispatch bridge — invisible to skill authors.

The engine's Python worker injects `_dispatch_to_engine` into `_dispatch`
at boot. SDK modules call `await dispatch(op, params)` which forwards
through the engine for policy gating, logging, and real execution.

Wire protocol (§8.1 / §8.3 of the runtime-core proposal):

  Python → Engine (request)
      {"__type__": "dispatch",
       "__id__": "<request_id>",
       "__dispatch_id__": "d-N",
       "__caps__": [...skill capabilities...],
       "__dispatch__": {"op": "<dotted.op>", "params": {...}}}

  Engine → Python (success)
      {"__type__": "dispatch_result",
       "__dispatch_id__": "d-N",
       "payload": <handler return value>}

  Engine → Python (failure)
      {"__type__": "dispatch_result",
       "__dispatch_id__": "d-N",
       "__error__": "<reason>"}

`dispatch()` unwraps the envelope so SDK wrappers see only the handler's
payload. On failure it raises `RuntimeError(f"engine dispatch {op} failed:
{msg}")`. Skill authors never import this module — they use
`from agentos import http, sql, secrets, crypto, …`.

All SDK modules are async. Skills must be `async def` and `await` every
SDK call. The worker runs an asyncio event loop so multiple skill
operations run concurrently; each sideband dispatch yields the loop
while the engine does the real work.
"""

import inspect

_dispatch = None  # Injected by the engine's Python worker at boot.


async def dispatch(op: str, params: dict):
    """Send one dispatch to the engine and return its payload.

    The engine always replies with the §8.1 uniform envelope:

        {"__type__": "dispatch_result",
         "__dispatch_id__": "...",
         "payload": <handler-returned value>}

    On failure the envelope carries `__error__` instead of `payload`:

        {"__type__": "dispatch_result",
         "__dispatch_id__": "...",
         "__error__": "<reason>"}

    Args:
        op: Dotted op name (e.g. ``"secrets.read"``, ``"http.request"``).
        params: Parameter dict matching the op's `RequestShape`.

    Returns:
        The handler's payload (dict, scalar, bytes — whatever the op
        returns). Envelope metadata is stripped.

    Raises:
        RuntimeError: The SDK was called outside an engine-managed
            Python worker.
        RuntimeError: The engine reported a dispatch failure.
    """
    if _dispatch is None:
        raise RuntimeError(
            "agentos SDK called outside of engine context. "
            "SDK modules can only be used inside skill functions "
            "executed by the engine."
        )

    # Two injection sites: python_worker.rs binds an async coroutine
    # (`_dispatch_to_engine`), while python.rs (the legacy per-op sidecar
    # used by command/swift executors) binds a sync `_call`. Handle both.
    result = _dispatch(op, params)
    if inspect.isawaitable(result):
        result = await result

    if "__error__" in result:
        raise RuntimeError(
            f"engine dispatch {op!s} failed: {result['__error__']}"
        )

    return result["payload"]
