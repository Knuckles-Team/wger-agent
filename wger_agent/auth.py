#!/usr/bin/python
import os

import urllib3

from wger_agent.api_client import WgerApi

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from agent_utilities.core.exceptions import AuthError, UnauthorizedError

_client = None


def get_client() -> WgerApi:
    """Get or create a singleton WgerApi client instance."""
    global _client
    if _client is None:
        base_url: str = os.getenv("WGER_URL", "") or os.getenv(
            "WGER_INSTANCE", "https://wger.de"
        )
        token: str = os.getenv("WGER_TOKEN", "") or os.getenv("WGER_ACCESS_TOKEN", "")
        ssl_verify_env: str = os.getenv("WGER_SSL_VERIFY", "") or os.getenv(
            "WGER_VERIFY", "True"
        )
        verify: bool = ssl_verify_env.lower() in ("true", "1", "yes")

        try:
            _client = WgerApi(
                base_url=base_url,
                token=token,
                verify=verify,
            )
        except (AuthError, UnauthorizedError) as e:
            raise RuntimeError(
                f"AUTHENTICATION ERROR: The Wger API token provided is not valid for '{base_url}'. "
                f"Please check your WGER_ACCESS_TOKEN and WGER_INSTANCE environment variables. "
                f"Error details: {str(e)}"
            ) from e

    return _client
