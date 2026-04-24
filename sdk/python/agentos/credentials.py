"""Agent-driven credential resolution.

`credentials.retrieve(domain, required)` matchmakes every installed
`@provides(login_credentials)` skill (1Password, Keychain, etc.) and
returns the resolved field values from the first one that answers.
Skills call this from their `login` tools when the caller didn't pass
credentials explicitly.

Shape of the flow:
    1. `capability.list_providers("login_credentials")` enumerates every
       `@provides(login_credentials)` skill. Providers with creds present
       (or no creds required) are tried first.
    2. For each, `capability.call(..., skill=p["skill_id"])` forces the
       picked provider. The provider's `__secrets__` envelope persists
       the decrypted fields into `~/.agentos/data/agentos.db` before the
       call returns. The call result is `{provided, identifier}`.
    3. On a provider match, `auth_store.read(...)` reads the freshly-
       written row back so the caller gets the concrete `value:
       {email, password, ...}` dict without the provider having to
       return plaintext inline.

There is no read-side cache in v1 — every call re-invokes the provider
(which means Touch ID every time for 1Password). User consent on each
access is a feature, not a bug; cache can land later as a config knob.
"""

from __future__ import annotations

from typing import Any

from agentos import capability
from agentos._bridge import dispatch


_CRED_PRIORITY = {"not_required": 0, "present": 1, "missing": 2}

# Vault wins ties. The local encrypted store is ~ms and never prompts —
# asking any other provider first when the answer is sitting in the vault
# is architecturally backwards (vault is the user's durable state, not
# a cache). Everything else sorts by cred_state + insertion order.
_VAULT_SKILL_ID = "vault"


async def retrieve(
    domain: str,
    *,
    account: str | None = None,
    required: list[str] | None = None,
) -> dict[str, Any]:
    """Resolve login credentials for a domain.

    Args:
        domain: Canonical credential-store domain (e.g. `".approach.app"`).
        required: Field names the caller needs (e.g. `["email", "password"]`).
        account: Optional disambiguator when multiple items match.

    Returns:
        A `{found, identifier, value, source}` envelope. On no-match,
        `found` is `False` and the caller should raise `NeedsCredentials`.
    """
    req_fields = required or []

    listing = await capability.list_providers("login_credentials")
    providers = sorted(
        listing.get("providers") or [],
        key=lambda p: (
            _CRED_PRIORITY.get(p.get("cred_state", "missing"), 2),
            0 if p.get("skill_id") == _VAULT_SKILL_ID else 1,
        ),
    )

    for provider in providers:
        provider_result = await capability.call(
            "login_credentials",
            verb=provider.get("via") or "get_credentials",
            skill=provider["skill_id"],
            params={
                "domain": domain,
                "account": account,
                "required": req_fields,
            },
        )
        if not provider_result or not provider_result.get("provided"):
            continue

        identifier = provider_result.get("identifier")
        if not identifier:
            continue

        # Provider's `__secrets__` sidecar just persisted the row — read
        # it back by identifier for the decrypted values.
        row = await dispatch(
            "auth_store.read",
            {
                "domain": domain,
                "item_type": "login_credentials",
                "account": identifier,
            },
        )
        if not row.get("found"):
            continue

        row_value = row.get("value") or {}
        if req_fields and not all(k in row_value for k in req_fields):
            # Provider matched but didn't populate every required field —
            # try the next provider rather than returning a partial.
            continue

        value = {k: row_value[k] for k in req_fields if k in row_value}

        return {
            "found": True,
            "identifier": row.get("identifier") or identifier,
            "value": value,
            "source": row.get("source") or provider["skill_id"],
        }

    return {"found": False}
