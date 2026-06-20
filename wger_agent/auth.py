#!/usr/bin/python
import urllib3

from wger_agent.api_client import WgerApi

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from agent_utilities.core.config import setting
from agent_utilities.core.exceptions import AuthError, UnauthorizedError

_client = None


def get_client() -> WgerApi:
    """Get or create a singleton WgerApi client instance."""
    global _client
    if _client is None:
        base_url: str = setting("WGER_URL", "") or setting(
            "WGER_INSTANCE", "https://wger.de"
        )
        token: str = setting("WGER_TOKEN", "") or setting("WGER_ACCESS_TOKEN", "")
        ssl_verify = setting("WGER_SSL_VERIFY", None, cast=bool)
        verify: bool = (
            ssl_verify if ssl_verify is not None else setting("WGER_VERIFY", True)
        )

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
