"""Operation decorators — read by the engine via AST, no-ops at runtime.

The Rust engine parses Python files at boot time to discover operations.
These decorators exist so apps can import and use them without runtime errors.
The engine reads their arguments from the AST — it never executes Python.

Usage:
    from agentos import returns, provides, connection, timeout

    @returns("event[]")
    @provides(web_search, urls=["example.com/*"])
    @connection("api")
    @timeout(60)
    def list_events(query: str = None, **params) -> list[dict]:
        ...

Module-level connection declaration (replaces YAML `connections:` block):

    from agentos import connection, cookies, account_ops

    connection("portal",
        client="http",
        base_url="https://api.approach.app/v1",
        needs=[cookies(
            domain=".approach.app",
            account=account_ops(check="check_session",
                                login="login",
                                logout="logout"))])
"""


def returns(shape):
    """Declare the return shape of an operation.

    Args:
        shape: Entity shape reference ("event[]", "post"), a union of shape
               references ("account | auth_challenge") when the op's result
               shape depends on the call — the worker discriminates per
               call from the returned dict — or an inline schema dict
               ({"ok": "boolean", "id": "string"}).
    """
    def decorator(func):
        func._agentos_returns = shape
        return func
    return decorator


def provides(tool, **kwargs):
    """Declare that this function provides a brokered service.

    The service is named by its bare string — `@provides("web_search")`.
    There is no constant to import and no registry to register in: a
    service exists because some app provides it, the same way an edge
    verb exists because some `create` mints it. The engine self-registers
    a `shape:service` node from the union of `@provides` across all apps.

    Args:
        tool: Service name string, e.g. `"web_search"`, `"web_fetch"`,
            `"llm"`, `"login_credentials"`.
        urls: Optional URL patterns this tool handles.
        domains: Optional domains (for cookie_auth providers).
        creation_timestamps: Whether provider returns cookie creation timestamps.
    """
    def decorator(func):
        func._agentos_provides = {"tool": tool, **kwargs}
        return func
    return decorator


def connection(name, **kwargs):
    """Declare a connection at module level, or bind a tool to one.

    Two call shapes:

    - **Module-level declaration** — ``connection("portal", client="http",
      base_url=..., needs=[...])``. Replaces the YAML ``connections:`` block.
      The engine reads the full signature from the Python AST; runtime is
      a pure no-op so the import succeeds.
    - **Tool decorator** — ``@connection("portal")``. Binds the decorated
      function to a previously-declared connection. Identical behavior to
      before this SDK addition.

    Args:
        name: Connection name (``"api"``, ``"web"``) or list of names
            (``["api", "cache"]``) for caller-choosable tools.
        client: ``"http"`` or ``"local"`` — SDK auto-wiring
            (module-level form only).
        base_url: Base URL for ``client="http"`` connections
            (module-level form only).
        needs: Conjunctive list of credential/service constructors
            (module-level form only).
        label: Display label for ``agentos call accounts``
            (module-level form only).
        help_url: Sign-in URL for auth-required errors
            (module-level form only).
    """
    # Module-level declaration — call with kwargs, not used as a decorator.
    if kwargs:
        _ = (name, kwargs)
        return None

    # Decorator form — `@connection("portal")`.
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
    """Declare that an operation is exercised by the app test sweep.

    Engine/validator/runner read `_agentos_test` off the decorated function
    via AST (Rust) or the `ast` module (Python). Runtime is a pure no-op —
    this class exists so app code can import the name without the sandbox
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


class _Account:
    """Declare an app's account ops — read by the engine via AST, no-ops at runtime.

    `@account.check` / `@account.login` / `@account.logout` /
    `@account.profile` mark which ops answer "who am I?", "sign me in",
    "sign me out", and "enrich my account node". The engine resolves
    auto-relogin, identity checks, and GUI sign-in through this metadata —
    never through literal tool names. One declaration point: the op itself
    (replaces the `ConnectionAuth.login` key and the frontmatter account
    block).

    `login` returns `account` when a session is already (or now) live, or
    `auth_challenge` when a human must act — declare the union:

        @account.check
        @returns("account")
        async def check_session(**params): ...

        @account.login
        @returns("account | auth_challenge")
        async def login(**params): ...

        @account.logout
        @returns({"ok": "boolean"})
        async def logout(**params): ...

    Every app that can log in must be able to log out — the validator
    enforces the pair (`check_account_trio`).
    """

    @staticmethod
    def check(fn):
        fn._agentos_account = "check"
        return fn

    @staticmethod
    def login(fn):
        fn._agentos_account = "login"
        return fn

    @staticmethod
    def logout(fn):
        fn._agentos_account = "logout"
        return fn

    @staticmethod
    def profile(fn):
        fn._agentos_account = "profile"
        return fn


account = _Account()


def claims(who):
    """Declare that this operation's emitted nodes are claimed by `who`.

    The engine attaches a `Person --claims--> node` link from the named
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
            # Every financial_account this emits gets a `claims` link from
            # the machine owner's person node, so the graph can answer
            # "where do I have accounts?"
            ...
    """
    def decorator(func):
        func._agentos_claims = who
        return func
    return decorator
