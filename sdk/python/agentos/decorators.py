"""Operation decorators — read by the engine via AST, no-ops at runtime.

The Rust engine parses Python files at boot time to discover operations.
These decorators exist so skills can import and use them without runtime errors.
The engine reads their arguments from the AST — it never executes Python.

Usage:
    from agentos import returns, provides, connection, timeout

    @returns("event[]")
    @provides(web_search, urls=["example.com/*"])
    @connection("api")
    @timeout(60)
    def list_events(query: str = None, **params) -> list[dict]:
        ...
"""


def returns(shape):
    """Declare the return shape of an operation.

    Args:
        shape: Entity shape reference ("event[]", "post") or inline schema dict
               ({"ok": "boolean", "id": "string"}).
    """
    def decorator(func):
        func._agentos_returns = shape
        return func
    return decorator


def provides(tool, **kwargs):
    """Declare that this function provides a standard tool capability.

    Args:
        tool: Tool constant (e.g., web_search, web_read, email_lookup).
        urls: Optional URL patterns this tool handles.
        domains: Optional domains (for cookie_auth providers).
        creation_timestamps: Whether provider returns cookie creation timestamps.
    """
    def decorator(func):
        func._agentos_provides = {"tool": tool, **kwargs}
        return func
    return decorator


def connection(name):
    """Bind this operation to a specific connection for auth resolution.

    Args:
        name: Connection name (e.g., "api", "web") or list of names
              (e.g., ["api", "cache"]) for caller-choosable connections.
    """
    def decorator(func):
        func._agentos_connection = name
        return func
    return decorator


def timeout(seconds):
    """Override the default 30-second timeout for this operation.

    Args:
        seconds: Timeout in seconds.
    """
    def decorator(func):
        func._agentos_timeout = seconds
        return func
    return decorator


class _Test:
    """Declare that an operation is exercised by the skill test sweep.

    Engine/validator/runner read `_agentos_test` off the decorated function
    via AST (Rust) or the `ast` module (Python). Runtime is a pure no-op —
    this class exists so skill code can import the name without the sandbox
    (banned-imports) rejecting anything.

    Three forms, all attach the same shape:

        @test                              # bare — one case with no params
        @test(params={...}, account="...")  # single case, explicit args
        @test.cases({...}, {...})           # multiple cases (each a dict)
        @test.skip(reason="...")            # explicit skip, surfaced by runner

    Stored shape on `fn._agentos_test`:

        {
          "cases": [{"params": {...}, "account": "..."}, ...],
          "skip": bool,
          "skip_reason": Optional[str],
        }

    Rename-safe by construction: the function name *is* the identifier the
    runner dispatches against; renaming moves the decorator with it.
    """

    def __call__(self, fn=None, *, params=None, account=None):
        # Bare form: `@test` passes the function directly.
        if callable(fn):
            _attach_test(fn, [{}])
            return fn
        # Call form: `@test(params=..., account=...)` returns a decorator.
        case = {}
        if params is not None:
            case["params"] = params
        if account is not None:
            case["account"] = account

        def deco(fn):
            _attach_test(fn, [case])
            return fn

        return deco

    def cases(self, *cases):
        """Multiple test runs. Each case is a dict of the same kwargs (`params`, `account`)."""
        normalised = [dict(c) for c in cases]

        def deco(fn):
            _attach_test(fn, normalised)
            return fn

        return deco

    def skip(self, *, reason=None):
        """Skip this op in the sweep. `reason` is surfaced by the runner."""
        def deco(fn):
            _attach_test(fn, [], skip=True, skip_reason=reason)
            return fn

        return deco


def _attach_test(fn, cases, *, skip=False, skip_reason=None):
    fn._agentos_test = {
        "cases": list(cases),
        "skip": skip,
        "skip_reason": skip_reason,
    }


test = _Test()


def claims(who):
    """Declare that this operation's emitted nodes are claimed by `who`.

    The engine attaches a `Person --claims--> node` edge from the named
    claimant to every top-level node this operation upserts — automatic
    actor-ownership for first-party self-identity ops.

    Args:
        who: Claimant spec. Currently supports "primary_user" — the machine
             owner (resolved via the singleton Person with primary_user=true).
             Extensible in later phases to named people, org accounts, etc.

    Example:
        @claims("primary_user")
        @returns("financial_account[]")
        async def load_accounts(**params) -> list:
            # Every financial_account this emits gets a `claims` edge from
            # the machine owner's person node, so the graph can answer
            # "where do I have accounts?"
            ...
    """
    def decorator(func):
        func._agentos_claims = who
        return func
    return decorator
