"""Agent-driven credential resolution.

`credentials.retrieve(domain, required)` matchmakes every installed
`@provides(login_credentials)` app and returns the resolved field
values from the first one that answers. **Never hardcode a provider
id in a login cascade** — vault first, then the user's
`pref:system.defaultCredentialProvider` pick, then everyone else.

Apps call this from their `login` tools when the caller didn't pass
credentials explicitly.

Shape of the flow:
    1. `services.list_providers("login_credentials")` enumerates every
       `@provides(login_credentials)` app. Providers with creds present
       (or no creds required) are tried first.
    2. For each, `services.call(..., app=p["app_id"])` forces the
       picked provider. The provider's `__secrets__` envelope persists
       the decrypted fields into `~/.agentos/data/agentos.db` before the
       call returns. The call result is `{provided, identifier}`.
    3. On a provider match, `auth_store.read(...)` reads the freshly-
       written row back so the caller gets the concrete `value:
       {email, password, ...}` dict without the provider having to
       return plaintext inline.
    4. If a provider needs an interactive unlock (e.g. 1Password Master
       Password via AgentOS Security), retrieve stops and returns
       `{found: false, unlock_required: true, challengeId, ...}` so the
       caller can surface the challenge instead of fake NeedsCredentials.
"""

from __future__ import annotations

from typing import Any

from agentos import services
from agentos._bridge import dispatch


_CRED_PRIORITY = {"not_required": 0, "present": 1, "missing": 2}

# Vault wins ties. The local encrypted store is ~ms and never prompts —
# asking any other provider first when the answer is sitting in the vault
# is architecturally backwards (vault is the user's durable state, not
# a cache). Everything else sorts by defaultCredentialProvider, then
# cred_state + insertion order.
_VAULT_APP_ID = "vault"


async def _default_credential_provider() -> str | None:
    """`pref:system.defaultCredentialProvider` — optional preferred app id
    after vault (e.g. ``onepassword``, ``macos-keychain``). Never required.
    """
    try:
        settings = await dispatch(
            "data.read",
            {"id": "settings", "fields": ["pref:system"]},
        )
        if not isinstance(settings, dict):
            return None
        blob = settings.get("pref:system")
        if isinstance(blob, str):
            import json

            blob = json.loads(blob)
        if not isinstance(blob, dict):
            return None
        pick = (blob.get("defaultCredentialProvider") or "").strip()
        return pick or None
    except Exception:
        return None

_UNLOCK_CODES = frozenset(
    {
        "OnePasswordUnlockRequired",
        "UnlockRequired",
        "SecretChallengePending",
    }
)


def _unlock_pending(result: Any) -> bool:
    """True when a credential provider opened (or needs) AgentOS Security."""
    if not isinstance(result, dict):
        return False
    code = str(result.get("code") or "")
    if code in _UNLOCK_CODES:
        return True
    if result.get("prompt") == "secret_challenge":
        return True
    if result.get("challengeId") and not result.get("provided"):
        return True
    return False


def _unlock_envelope(result: dict[str, Any], *, source: str) -> dict[str, Any]:
    return {
        "found": False,
        "unlock_required": True,
        "challengeId": result.get("challengeId"),
        "prompt": result.get("prompt") or "secret_challenge",
        "forApp": result.get("forApp"),
        "code": result.get("code") or "OnePasswordUnlockRequired",
        "error": result.get("error") or result.get("message"),
        "hint": result.get("hint"),
        "source": source,
    }


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
        On success: `{found: true, identifier, value, source}`.
        On unlock needed: `{found: false, unlock_required: true, challengeId, …}`.
        On no-match: `{found: false}` — caller should raise `NeedsCredentials`.
    """
    req_fields = required or []

    preferred = await _default_credential_provider()
    listing = await services.list_providers("login_credentials")
    # Order: vault → user default (if set) → everyone else by cred_state.
    # Never name a provider in cascade code — only this pref + vault.
    providers = sorted(
        listing.get("providers") or [],
        key=lambda p: (
            0 if p.get("app_id") == _VAULT_APP_ID else 1,
            0 if preferred and p.get("app_id") == preferred else 1,
            _CRED_PRIORITY.get(p.get("cred_state", "missing"), 2),
        ),
    )

    for provider in providers:
        try:
            provider_result = await services.call(
                "login_credentials",
                verb=provider.get("via") or "get_credentials",
                app=provider["app_id"],
                params={
                    "domain": domain,
                    "account": account,
                    "required": req_fields,
                },
            )
        except RuntimeError as e:
            # Some paths surface unlock as a dispatch failure string.
            msg = str(e)
            if "OnePasswordUnlockRequired" in msg or "UnlockRequired" in msg:
                return _unlock_envelope(
                    {"code": "OnePasswordUnlockRequired", "error": msg},
                    source=provider["app_id"],
                )
            continue

        if _unlock_pending(provider_result):
            return _unlock_envelope(
                provider_result if isinstance(provider_result, dict) else {},
                source=provider["app_id"],
            )

        # Ambiguous match — surface it; don't silently fall through.
        if isinstance(provider_result, dict) and provider_result.get("code") == "MultipleMatches":
            return {
                "found": False,
                "error": provider_result.get("error"),
                "code": "MultipleMatches",
                "domain": domain,
                "candidates": provider_result.get("candidates"),
                "source": provider["app_id"],
            }

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
            "source": row.get("source") or provider["app_id"],
        }

    return {"found": False}
