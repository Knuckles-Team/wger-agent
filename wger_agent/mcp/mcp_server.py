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
import sys
from typing import Any

from agent_utilities.mcp_utilities import (
    create_mcp_server,
    load_config,
    register_tool_surface,
)
from starlette.requests import Request
from starlette.responses import JSONResponse

from wger_agent.api_client import WgerApi
from wger_agent.auth import get_client
from wger_agent.mcp import tools

__version__ = "0.14.0"

logger = get_logger(name="wger-agent")
logger.setLevel(logging.INFO)


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance.

    Bootstraps FastMCP instance, custom routes, and conditionally registers tools.
    """
    load_config()
    args, mcp, middlewares = create_mcp_server(
        name="wger-agent MCP",
        version=__version__,
        instructions="wger-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request | None = None) -> JSONResponse:
        """Standard Starlette endpoint for health status checking."""
        return JSONResponse({"status": "OK"})

    register_tool_surface(
        mcp,
        client_cls=WgerApi,
        get_client=get_client,
        service="wger-agent",
        tools_module=tools,
    )

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
