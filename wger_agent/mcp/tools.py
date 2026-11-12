# wger_agent/mcp/tools.py
"""Wire-First native knowledge-graph ingestion tools for wger records.

CONCEPT:AU-KG.ingest.enterprise-source-extractor. The API operations are derived by
the SDK, one typed tool per client method. This module holds only the connector's own
ingestion tools: each lists one wger modality through the real client and pushes it
into the medulla knowledge graph as typed OWL nodes. Best-effort: ``ingested`` is
``None`` when no KG engine is reachable.
"""

from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from wger_agent.auth import get_client


def _list_filters(
    limit: int | None, offset: int | None, ordering: str | None
) -> dict[str, Any]:
    values = {"limit": limit, "offset": offset, "ordering": ordering}
    return {key: value for key, value in values.items() if value is not None}


def register_ingest_tools(mcp: FastMCP):
    """CONCEPT:AU-KG.ingest.enterprise-source-extractor: Register the ingestion tools."""

    @mcp.tool(tags={"Ingest"})
    async def wger_ingest_exercises(
        limit: int | None = Field(default=None, description="Maximum records to list."),
        offset: int | None = Field(default=None, description="Records to skip."),
        ordering: str | None = Field(default=None, description="Ordering field."),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """List wger exercises and ingest them into the knowledge graph as :Exercise nodes."""
        if ctx:
            await ctx.info("Ingesting wger exercises into the knowledge graph...")
        from wger_agent import kg_ingest

        resp = client.get_exercises(**_list_filters(limit, offset, ordering))
        result = await kg_ingest.ingest_exercises(resp)
        return {"listed": len(kg_ingest._records(resp)), "ingested": result}

    @mcp.tool(tags={"Ingest"})
    async def wger_ingest_routines(
        limit: int | None = Field(default=None, description="Maximum records to list."),
        offset: int | None = Field(default=None, description="Records to skip."),
        ordering: str | None = Field(default=None, description="Ordering field."),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """List wger routines and ingest them into the knowledge graph as :WorkoutRoutine nodes."""
        if ctx:
            await ctx.info("Ingesting wger routines into the knowledge graph...")
        from wger_agent import kg_ingest

        resp = client.get_routines(**_list_filters(limit, offset, ordering))
        result = await kg_ingest.ingest_routines(resp)
        return {"listed": len(kg_ingest._records(resp)), "ingested": result}

    @mcp.tool(tags={"Ingest"})
    async def wger_ingest_workout_sessions(
        limit: int | None = Field(default=None, description="Maximum records to list."),
        offset: int | None = Field(default=None, description="Records to skip."),
        ordering: str | None = Field(default=None, description="Ordering field."),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """List wger workout sessions and ingest them into the knowledge graph as :WorkoutSession nodes."""
        if ctx:
            await ctx.info(
                "Ingesting wger workout sessions into the knowledge graph..."
            )
        from wger_agent import kg_ingest

        resp = client.get_workout_sessions(**_list_filters(limit, offset, ordering))
        result = await kg_ingest.ingest_workout_sessions(resp)
        return {"listed": len(kg_ingest._records(resp)), "ingested": result}

    @mcp.tool(tags={"Ingest"})
    async def wger_ingest_nutrition_plans(
        limit: int | None = Field(default=None, description="Maximum records to list."),
        offset: int | None = Field(default=None, description="Records to skip."),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """List wger nutrition plans and ingest them into the knowledge graph as :NutritionPlan nodes."""
        if ctx:
            await ctx.info("Ingesting wger nutrition plans into the knowledge graph...")
        from wger_agent import kg_ingest

        resp = client.get_nutrition_plans(**_list_filters(limit, offset, None))
        result = await kg_ingest.ingest_nutrition_plans(resp)
        return {"listed": len(kg_ingest._records(resp)), "ingested": result}
