# wger_agent/mcp_server.py
"""Backward compatibility wrapper redirecting to wger_agent/mcp/ package."""

from scion_sdk.connector_identity import connector_version

__version__ = connector_version("wger_agent")

from wger_agent.mcp.mcp_server import (
    get_mcp_instance,
    mcp_server,
)
from wger_agent.mcp.tools import (
    register_body_tools,
    register_exercise_tools,
    register_ingest_tools,
    register_nutrition_tools,
    register_routine_tools,
    register_routineconfig_tools,
    register_user_tools,
    register_workout_tools,
)

__all__ = [
    "get_mcp_instance",
    "mcp_server",
    "register_routine_tools",
    "register_routineconfig_tools",
    "register_exercise_tools",
    "register_workout_tools",
    "register_nutrition_tools",
    "register_body_tools",
    "register_user_tools",
    "register_ingest_tools",
]

if __name__ == "__main__":
    mcp_server()
