#!/usr/bin/python


import os

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from agent_utilities.exceptions import AuthError, UnauthorizedError

from wger_agent.api_client import WgerApi

_client = None


def get_client() -> WgerApi:
    """Get or create a singleton WgerApi client instance."""
    global _client
    if _client is None:
        base_url = os.getenv("WGER_INSTANCE", "https://wger.de")
        token = os.getenv("WGER_ACCESS_TOKEN", "")
        verify = os.getenv("WGER_VERIFY", "True").lower() in ("true", "1", "yes")

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
