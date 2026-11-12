# wger_agent/mcp_server.py
"""Server entry points of the wger connector.

The SDK derives one typed tool per client operation; this module binds the connector's
own ingestion tools for the SDK's tool discovery.
"""

from scion_sdk.connector_identity import connector_version

__version__ = connector_version("wger_agent")

from wger_agent.mcp.mcp_server import (
    get_mcp_instance,
    mcp_server,
)
from wger_agent.mcp.tools import register_ingest_tools

__all__ = [
    "get_mcp_instance",
    "mcp_server",
    "register_ingest_tools",
]

if __name__ == "__main__":
    mcp_server()
