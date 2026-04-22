"""OAuth token exchange through the engine.

Sugar over ``client.post()`` with standard OAuth2 form body.

    from agentos import oauth

    token = oauth.exchange(
        token_url="https://oauth2.googleapis.com/token",
        refresh_token="...",
        client_id="...",
    )
    # token["access_token"] — the Bearer token
    # token["scope"] — space-separated granted scopes (if returned by provider)
"""

from agentos import client


async def exchange(token_url, refresh_token, client_id, client_secret=None, scope=None):
    """Exchange a refresh token for an access token.

    Args:
        token_url: OAuth2 token endpoint URL.
        refresh_token: The refresh token.
        client_id: OAuth2 client ID.
        client_secret: Optional client secret.
        scope: Optional scope string.

    Returns:
        Dict with access_token, expires_in, token_type, scope, etc.
        The "scope" field (space-separated string) tells you what permissions
        the token actually has — persist this for introspection.
    """
    data = {
        "grant_type": "refresh_token",
        "refresh_token": refresh_token,
        "client_id": client_id,
    }
    if client_secret:
        data["client_secret"] = client_secret
    if scope:
        data["scope"] = scope

    # client.post serializes `data=` as application/x-www-form-urlencoded
    # and reads `.json` off the engine response for us.
    result = await client.post(token_url, data=data)

    parsed = result.get("json") if isinstance(result, dict) else None
    if isinstance(parsed, dict):
        # Check for OAuth error responses (e.g. invalid_grant, unsupported_grant_type).
        if "error" in parsed:
            raise RuntimeError(
                f"OAuth token exchange failed: {parsed.get('error')} "
                f"— {parsed.get('error_description', 'no description')}"
            )
        return parsed
    return result
