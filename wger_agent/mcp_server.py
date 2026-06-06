# wger_agent/mcp_server.py
"""Backward compatibility wrapper redirecting to wger_agent/mcp/ package."""

__version__ = "0.28.0"

from wger_agent.mcp.mcp_server import (
    get_mcp_instance,
    mcp_server,
)
from wger_agent.mcp.tools import (
    register_body_tools,
    register_exercise_tools,
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
]

if __name__ == "__main__":
    mcp_server()
