# tests/test_bug_cx_046_ctx_await.py
"""Regression test for BUG-CX-046.

`ctx.info(...)` is an async coroutine method on fastmcp's `Context`. Calling
it without `await` creates a coroutine object that is discarded, the log
line never emits, and Python raises `RuntimeWarning: coroutine
'Context.info' was never awaited`. This test proves the tool under test
actually awaits `ctx.info(...)`.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock

import pytest

from wger_agent.mcp.tools import register_routine_tools


@pytest.mark.asyncio
async def test_wger_routine_awaits_ctx_info(mock_requests_session):
    tools_dict = {}

    class MockMCP:
        def tool(self, *args, **kwargs):
            def decorator(func):
                tools_dict[func.__name__] = func
                return func

            return decorator

    mock_mcp: Any = MockMCP()
    register_routine_tools(mock_mcp)  # type: ignore

    mock_client = MagicMock()
    mock_ctx = MagicMock()
    mock_ctx.info = AsyncMock()

    wger_routine = tools_dict["wger_routine"]
    await wger_routine(
        action="get_routines",
        params_json="{}",
        client=mock_client,
        ctx=mock_ctx,
    )

    mock_ctx.info.assert_awaited_once()
