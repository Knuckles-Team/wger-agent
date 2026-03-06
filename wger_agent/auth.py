#!/usr/bin/python
# coding: utf-8

import os
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

from wger_agent.wger_api import WgerApi

_client = None


def get_client() -> WgerApi:
    """Get or create a singleton WgerApi client instance."""
    global _client
    if _client is None:
        base_url = os.getenv("WGER_INSTANCE", "https://wger.de")
        token = os.getenv("WGER_ACCESS_TOKEN", "")
        verify = os.getenv("WGER_VERIFY", "True").lower() in ("true", "1", "yes")

        _client = WgerApi(
            base_url=base_url,
            token=token,
            verify=verify,
        )

    return _client
