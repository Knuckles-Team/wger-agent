# tests/test_bug_cx_046_ctx_await.py
"""Regression test for BUG-CX-046.

`ctx.info(...)` is an async coroutine method on fastmcp's `Context`. Calling
it without `await` creates a coroutine object that is discarded, the log
line never emits, and Python raises `RuntimeWarning: coroutine
'Context.info' was never awaited`. This test proves the ingestion tools
actually await `ctx.info(...)`.
"""

from typing import Any
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from wger_agent.mcp.tools import register_ingest_tools


@pytest.mark.asyncio
async def test_wger_ingest_tools_await_ctx_info(mock_requests_session):
    tools_dict = {}

    class MockMCP:
        def tool(self, *args, **kwargs):
            def decorator(func):
                tools_dict[func.__name__] = func
                return func

            return decorator

    mock_mcp: Any = MockMCP()
    register_ingest_tools(mock_mcp)  # type: ignore

    assert set(tools_dict) == {
        "wger_ingest_exercises",
        "wger_ingest_routines",
        "wger_ingest_workout_sessions",
        "wger_ingest_nutrition_plans",
    }
    for name, tool in tools_dict.items():
        mock_client = MagicMock()
        mock_client.get_exercises.return_value = {"results": []}
        mock_client.get_routines.return_value = {"results": []}
        mock_client.get_workout_sessions.return_value = {"results": []}
        mock_client.get_nutrition_plans.return_value = {"results": []}
        mock_ctx = MagicMock()
        mock_ctx.info = AsyncMock()
        with patch(
            f"wger_agent.kg_ingest.ingest_{name.removeprefix('wger_ingest_')}",
            AsyncMock(return_value=0),
        ):
            result = await tool(client=mock_client, ctx=mock_ctx, limit=5)
        mock_ctx.info.assert_awaited_once()
        assert result["listed"] == 0, name
