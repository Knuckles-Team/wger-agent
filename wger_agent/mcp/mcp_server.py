# wger_agent/mcp/mcp_server.py
import warnings

from fastmcp.utilities.logging import get_logger

# FastMCP Server & Command-Line Interfaces

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from starlette.requests import Request
from starlette.responses import JSONResponse

from wger_agent.mcp import tools

__version__ = "0.14.0"

logger = get_logger(name="wger-agent")
logger.setLevel(logging.INFO)


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance.

    Bootstraps FastMCP instance, custom routes, and conditionally registers tools.
    """
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="wger-agent MCP",
        version=__version__,
        instructions="wger-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request | None = None) -> JSONResponse:
        """Standard Starlette endpoint for health status checking."""
        return JSONResponse({"status": "OK"})

    # Map environment variable toggles to registration functions
    tool_registrations = [
        ("ROUTINETOOL", tools.register_routine_tools),
        ("ROUTINECONFIGTOOL", tools.register_routineconfig_tools),
        ("EXERCISETOOL", tools.register_exercise_tools),
        ("WORKOUTTOOL", tools.register_workout_tools),
        ("NUTRITIONTOOL", tools.register_nutrition_tools),
        ("BODYTOOL", tools.register_body_tools),
        ("USERTOOL", tools.register_user_tools),
    ]

    # Modular iteration to register active tools with FastMCP (CC=2)
    for env_var, register_func in tool_registrations:
        if to_boolean(os.getenv(env_var, "True")):
            register_func(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    """Run the MCP server application.

    Configures transport mechanisms and executes the FastMCP runner.
    """
    mcp, args, middlewares = get_mcp_instance()
    print(f"wger-agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        raise SystemExit(1)


if __name__ == "__main__":
    mcp_server()
