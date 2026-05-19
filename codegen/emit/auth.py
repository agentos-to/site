"""Auth-contract emitters — auth-contract YAML → Python TypedDicts +
Rust constants.

`ontology/auth-contracts/{oauth,cookie}.yaml` is the single source of
truth for what skills decorated `@provides(oauth_auth, ...)` /
`@provides(cookie_auth, ...)` must return. Both emitters are dumb
projections off the `AuthContract` IR — they never traverse raw YAML.

Why: the mimestream camelCase / engine snake_case bug
(_roadmap/p1/observability/panes.md). Implicit contracts → silent
401s. Explicit contracts → uncommittable bugs.
"""

from __future__ import annotations

from ir import Ontology

_PY_PRIMITIVE = {
    "string": "str",
    "integer": "int",
    "number": "float",
    "boolean": "bool",
    "array": "list[Any]",
    "json": "Any",
}


def _py_field(name: str, type_str: str) -> str:
    return f"    {name}: {_PY_PRIMITIVE.get(type_str, 'Any')}"


def emit_python_auth_contracts(onto: Ontology) -> str:
    """Emit the Python auth contracts module — TypedDicts + AUTH_CONTRACTS dict."""
    lines = [
        '"""DO NOT EDIT — generated from platform/ontology/auth-contracts/{oauth,cookie}.yaml.',
        "",
        "Regen: python3 platform/codegen/generate.py",
        "",
        "Skills decorated `@provides(oauth_auth, ...)` should return a dict",
        "matching `OAuthCredential`. Skills decorated `@provides(cookie_auth, ...)`",
        "return `CookieCredential`. agent-sdk validate enforces this at commit",
        "time using the AUTH_CONTRACTS dict at the bottom of this file.",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "from typing import Any, TypedDict",
        "",
    ]

    oauth = onto.auth("oauth")
    if oauth:
        cred = oauth.group("credential")
        lines += [
            "class OAuthCredential(TypedDict, total=False):",
            f'    """{(oauth.description or "OAuth provider return shape.").strip()}',
            "",
            "    All fields snake_case to match the OAuth 2.0 spec (RFC 6749 §5.1)",
            "    and the engine resolver (crates/auth/src/types.rs). Required:",
            "    `access_token`. Strongly recommended for refresh:",
            "    `refresh_token`, `expires_in`, `client_id`, `token_url`.",
            '    """',
        ]
        for f in (cred.required if cred else []):
            lines.append(_py_field(f.name, f.type))
        for f in (cred.recommended if cred else []):
            lines.append(_py_field(f.name, f.type))
        lines += ["", ""]

    cookie = onto.auth("cookie")
    if cookie:
        elem = cookie.group("element")
        lines += [
            "class Cookie(TypedDict, total=False):",
            '    """A single cookie in a CookieCredential.cookies array."""',
        ]
        for f in (elem.required if elem else []):
            lines.append(_py_field(f.name, f.type))
        for f in (elem.recommended if elem else []):
            lines.append(_py_field(f.name, f.type))
        lines += ["", ""]

        env = cookie.group("envelope")
        lines += [
            "class CookieCredential(TypedDict, total=False):",
            f'    """{(cookie.description or "Cookie provider return shape.").strip()}"""',
        ]
        for f in (env.required if env else []):
            ty = "list[Cookie]" if f.name == "cookies" else _PY_PRIMITIVE.get(f.type, "Any")
            lines.append(f"    {f.name}: {ty}")
        for f in (env.recommended if env else []):
            lines.append(_py_field(f.name, f.type))
        lines += ["", ""]

    # AUTH_CONTRACTS — what agent-sdk validate reads.
    lines += [
        "# Machine-readable contract — what agent-sdk validate enforces.",
        "# Every key here corresponds to a `@provides(<name>_auth, ...)`",
        "# decorator. Format:",
        "#   {'required': [field, ...], 'recommended': [field, ...],",
        "#    'forbidden_camel_case': {camelCase: snake_case_replacement, ...}}",
        "AUTH_CONTRACTS: dict[str, dict] = {",
    ]
    for c in onto.auth_contracts:
        cred = c.group("credential")
        required = [f.name for f in cred.required] if cred else []
        recommended = [f.name for f in cred.recommended] if cred else []
        forbidden = c.forbidden_camel_case
        lines.append(f"    {c.kind!r}: {{")
        lines.append(f"        'required': {required!r},")
        lines.append(f"        'recommended': {recommended!r},")
        lines.append(f"        'forbidden_camel_case': {dict(forbidden)!r},")
        # Cookie has a nested element (cookie_fields) contract too — flatten
        # under a sibling key so the validator can check each Cookie dict.
        elem = c.group("element")
        if elem:
            cf_required = [f.name for f in elem.required]
            cf_recommended = [f.name for f in elem.recommended]
            lines.append(f"        'cookie_fields_required': {cf_required!r},")
            lines.append(f"        'cookie_fields_recommended': {cf_recommended!r},")
        lines.append("    },")
    lines.append("}")
    lines.append("")

    return "\n".join(lines)


def emit_rust_auth_contracts(onto: Ontology) -> str:
    """Emit Rust constants for the auth resolver."""
    lines = [
        "// DO NOT EDIT — generated from platform/ontology/auth-contracts/{oauth,cookie}.yaml.",
        "// Regen: `python3 platform/codegen/generate.py`.",
        "//",
        "// Single source of truth for OAuth + cookie provider contracts.",
        "// Replaces literal field-name strings (\"access_token\", \"refresh_token\",",
        "// etc.) scattered through crates/auth/src/{types,resolve,source,cache}.rs.",
        "//",
        "// See _roadmap/p1/observability/panes.md for the bug that motivated this.",
        "",
        "#![allow(dead_code)]",
        "",
    ]

    def emit_const(name: str, items: list[str]) -> list[str]:
        body = ", ".join(f'"{i}"' for i in items)
        return [f"pub const {name}: &[&str] = &[{body}];"]

    oauth = onto.auth("oauth")
    if oauth:
        cred = oauth.group("credential")
        required = [f.name for f in cred.required] if cred else []
        recommended = [f.name for f in cred.recommended] if cred else []
        forbidden = oauth.forbidden_camel_case
        lines += [
            "// ── OAuth provider contract ─────────────────────────────────────────",
            "",
        ]
        lines += emit_const("OAUTH_REQUIRED_FIELDS", required)
        lines += emit_const("OAUTH_RECOMMENDED_FIELDS", recommended)
        lines.append("")
        lines.append("/// camelCase variants the engine should warn loudly about when found")
        lines.append("/// in an OAuth provider response. (camel_case_form, snake_case_replacement).")
        lines.append("pub const OAUTH_FORBIDDEN_CAMEL_CASE: &[(&str, &str)] = &[")
        for camel, snake in forbidden.items():
            lines.append(f'    ("{camel}", "{snake}"),')
        lines.append("];")
        lines.append("")

    cookie = onto.auth("cookie")
    if cookie:
        env = cookie.group("envelope")
        elem = cookie.group("element")
        env_required = [f.name for f in env.required] if env else []
        env_recommended = [f.name for f in env.recommended] if env else []
        cf_required = [f.name for f in elem.required] if elem else []
        cf_recommended = [f.name for f in elem.recommended] if elem else []
        forbidden = cookie.forbidden_camel_case
        lines += [
            "// ── Cookie provider contract ────────────────────────────────────────",
            "",
        ]
        lines += emit_const("COOKIE_ENVELOPE_REQUIRED", env_required)
        lines += emit_const("COOKIE_ENVELOPE_RECOMMENDED", env_recommended)
        lines += emit_const("COOKIE_FIELDS_REQUIRED", cf_required)
        lines += emit_const("COOKIE_FIELDS_RECOMMENDED", cf_recommended)
        lines.append("")
        lines.append("/// camelCase variants flagged in cookie provider responses.")
        lines.append("pub const COOKIE_FORBIDDEN_CAMEL_CASE: &[(&str, &str)] = &[")
        for camel, snake in forbidden.items():
            lines.append(f'    ("{camel}", "{snake}"),')
        lines.append("];")
        lines.append("")

    return "\n".join(lines)
