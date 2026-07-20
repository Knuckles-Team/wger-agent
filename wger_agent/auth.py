#!/usr/bin/python

from agent_utilities.core.config import setting
from agent_utilities.core.exceptions import AuthError, UnauthorizedError

from wger_agent.api_client import WgerApi

_client = None


def get_client() -> WgerApi:
    """Get or create a singleton WgerApi client instance."""
    global _client
    if _client is None:
        base_url: str = setting("WGER_URL", "") or setting(
            "WGER_INSTANCE", "https://wger.de"
        )
        token: str = setting("WGER_TOKEN", "") or setting("WGER_ACCESS_TOKEN", "")
        try:
            _client = WgerApi(
                base_url=base_url,
                token=token,
            )
        except (AuthError, UnauthorizedError) as e:
            raise RuntimeError(
                "AUTHENTICATION ERROR: The configured API token was rejected. "
                f"Please check your WGER_ACCESS_TOKEN and WGER_INSTANCE environment variables. "
                f"Error details: {type(e).__name__}"
            ) from e

    return _client
