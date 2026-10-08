# wger_agent/mcp/tools.py
import json
from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from wger_agent.auth import get_client

# CONCEPT:WG-OS.config.register-routine-configuration-tools: Wger Resource API Adapters


def _parse_action_kwargs(params_json: str) -> dict[str, Any] | None:
    """Parse an action's JSON parameter payload into kwargs, dropping None values.

    Returns None if params_json is not valid JSON.
    """
    try:
        raw_kwargs = json.loads(params_json)
    except Exception:
        return None
    return {k: v for k, v in raw_kwargs.items() if v is not None}


def _call_client_action(
    client: Any, action: str, allowed_actions: frozenset[str], kwargs: dict[str, Any]
) -> Any:
    """Invoke the wger client method named by action, if action is allowed.

    Every action in this adapter maps to a same-named method on the wger API
    client; allowed_actions is the explicit allow-list so an unrecognised (or
    otherwise-named) action can never reach an arbitrary client method.
    """
    if action not in allowed_actions:
        raise ValueError(f"Unknown action: {action}")
    return getattr(client, action)(**kwargs)


async def _run_client_action(
    ctx: Context | None,
    action: str,
    params_json: str,
    client: Any,
    allowed_actions: frozenset[str],
) -> dict:
    """Shared body for a wger_* dispatch tool: log, parse params, then dispatch."""
    if ctx:
        await ctx.info("Executing tool...")

    kwargs = _parse_action_kwargs(params_json)
    if kwargs is None:
        return {"error": "Operation failed"}

    return _call_client_action(client, action, allowed_actions, kwargs)


_ROUTINE_ACTIONS = frozenset(
    {
        "get_routines",
        "get_routine",
        "create_routine",
        "delete_routine",
        "get_days",
        "create_day",
        "delete_day",
        "get_slots",
        "create_slot",
        "create_slot_entry",
        "get_templates",
        "get_public_templates",
    }
)


def register_routine_tools(mcp: FastMCP):
    """CONCEPT:WG-OS.config.register-routine-configuration-tools: Register routine tools with FastMCP."""

    @mcp.tool(tags={"Routine"})
    async def wger_routine(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_routines', 'get_routine', 'create_routine', 'delete_routine', 'get_days', 'create_day', 'delete_day', 'get_slots', 'create_slot', 'create_slot_entry', 'get_templates', 'get_public_templates'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage wger routine operations."""
        return await _run_client_action(
            ctx, action, params_json, client, _ROUTINE_ACTIONS
        )


_ROUTINECONFIG_ACTIONS = frozenset(
    {
        "create_weight_config",
        "get_weight_configs",
        "create_repetitions_config",
        "get_repetitions_configs",
        "create_sets_config",
        "create_rest_config",
        "create_rir_config",
    }
)


def register_routineconfig_tools(mcp: FastMCP):
    """CONCEPT:WG-OS.config.register-routine-configuration-tools: Register routine configuration tools with FastMCP."""

    @mcp.tool(tags={"RoutineConfig"})
    async def wger_routineconfig(
        action: str = Field(
            description="Action to perform. Must be one of: 'create_weight_config', 'get_weight_configs', 'create_repetitions_config', 'get_repetitions_configs', 'create_sets_config', 'create_rest_config', 'create_rir_config'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage wger routineconfig operations."""
        return await _run_client_action(
            ctx, action, params_json, client, _ROUTINECONFIG_ACTIONS
        )


_EXERCISE_ACTIONS = frozenset(
    {
        "get_exercises",
        "get_exercise_info",
        "search_exercises",
        "get_exercise_categories",
        "get_equipment",
        "get_muscles",
        "get_exercise_images",
        "get_variations",
    }
)


def register_exercise_tools(mcp: FastMCP):
    """CONCEPT:WG-OS.config.register-routine-configuration-tools: Register exercise tools with FastMCP."""

    @mcp.tool(tags={"Exercise"})
    async def wger_exercise(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_exercises', 'get_exercise_info', 'search_exercises', 'get_exercise_categories', 'get_equipment', 'get_muscles', 'get_exercise_images', 'get_variations'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage wger exercise operations."""
        return await _run_client_action(
            ctx, action, params_json, client, _EXERCISE_ACTIONS
        )


_WORKOUT_ACTIONS = frozenset(
    {
        "get_workout_sessions",
        "get_workout_session",
        "create_workout_session",
        "delete_workout_session",
        "get_workout_logs",
        "create_workout_log",
        "delete_workout_log",
    }
)


def register_workout_tools(mcp: FastMCP):
    """CONCEPT:WG-OS.config.register-routine-configuration-tools: Register workout tools with FastMCP."""

    @mcp.tool(tags={"Workout"})
    async def wger_workout(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_workout_sessions', 'get_workout_session', 'create_workout_session', 'delete_workout_session', 'get_workout_logs', 'create_workout_log', 'delete_workout_log'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage wger workout operations."""
        return await _run_client_action(
            ctx, action, params_json, client, _WORKOUT_ACTIONS
        )


_NUTRITION_ACTIONS = frozenset(
    {
        "get_nutrition_plans",
        "get_nutrition_plan_info",
        "create_nutrition_plan",
        "delete_nutrition_plan",
        "create_meal",
        "create_meal_item",
        "get_ingredients",
        "get_ingredient_info",
        "get_nutrition_diary",
        "log_nutrition",
    }
)


def register_nutrition_tools(mcp: FastMCP):
    """CONCEPT:WG-OS.config.register-routine-configuration-tools: Register nutrition tools with FastMCP."""

    @mcp.tool(tags={"Nutrition"})
    async def wger_nutrition(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_nutrition_plans', 'get_nutrition_plan_info', 'create_nutrition_plan', 'delete_nutrition_plan', 'create_meal', 'create_meal_item', 'get_ingredients', 'get_ingredient_info', 'get_nutrition_diary', 'log_nutrition'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage wger nutrition operations."""
        return await _run_client_action(
            ctx, action, params_json, client, _NUTRITION_ACTIONS
        )


_BODY_ACTIONS = frozenset(
    {
        "get_weight_entries",
        "log_body_weight",
        "delete_weight_entry",
        "get_measurements",
        "log_measurement",
        "get_measurement_categories",
        "create_measurement_category",
        "get_gallery",
    }
)


def register_body_tools(mcp: FastMCP):
    """CONCEPT:WG-OS.config.register-routine-configuration-tools: Register body measurement tools with FastMCP."""

    @mcp.tool(tags={"Body"})
    async def wger_body(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_weight_entries', 'log_body_weight', 'delete_weight_entry', 'get_measurements', 'log_measurement', 'get_measurement_categories', 'create_measurement_category', 'get_gallery'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage wger body operations."""
        return await _run_client_action(ctx, action, params_json, client, _BODY_ACTIONS)


_USER_ACTIONS = frozenset(
    {
        "get_user_profile",
        "get_user_statistics",
        "get_user_trophies",
        "get_languages",
        "get_repetition_units",
        "get_weight_unit_settings",
    }
)


def register_user_tools(mcp: FastMCP):
    """CONCEPT:WG-OS.config.register-routine-configuration-tools: Register user configuration tools with FastMCP."""

    @mcp.tool(tags={"User"})
    async def wger_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_user_profile', 'get_user_statistics', 'get_user_trophies', 'get_languages', 'get_repetition_units', 'get_weight_unit_settings'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage wger user operations."""
        return await _run_client_action(ctx, action, params_json, client, _USER_ACTIONS)


def register_ingest_tools(mcp: FastMCP):
    """CONCEPT:AU-KG.ingest.enterprise-source-extractor: Wire-First native KG ingestion tools.

    Lists wger records via the real client and natively pushes them into the
    epistemic-graph knowledge graph as typed OWL nodes (``:Exercise``,
    ``:WorkoutRoutine``, ``:WorkoutSession``, ``:NutritionPlan``). Best-effort:
    ``ingested`` is ``None`` when no KG engine is reachable.
    """

    @mcp.tool(tags={"Ingest"})
    async def wger_ingest(
        action: str = Field(
            description=(
                "Modality to ingest. Must be one of: 'exercises', 'routines', "
                "'workout_sessions', 'nutrition_plans'"
            )
        ),
        params_json: str = Field(
            default="{}",
            description="JSON string of list filters (e.g. {'limit': 100}).",
        ),
        client=Depends(get_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Natively ingest wger records into epistemic-graph as typed nodes."""
        if ctx:
            await ctx.info("Ingesting wger records into the knowledge graph...")

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}
        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        from wger_agent import kg_ingest

        if action == "exercises":
            resp = client.get_exercises(**kwargs)
            result = kg_ingest.ingest_exercises(resp)
        elif action == "routines":
            resp = client.get_routines(**kwargs)
            result = kg_ingest.ingest_routines(resp)
        elif action == "workout_sessions":
            resp = client.get_workout_sessions(**kwargs)
            result = kg_ingest.ingest_workout_sessions(resp)
        elif action == "nutrition_plans":
            resp = client.get_nutrition_plans(**kwargs)
            result = kg_ingest.ingest_nutrition_plans(resp)
        else:
            raise ValueError(f"Unknown action: {action}")

        listed = len(kg_ingest._records(resp))
        return {"listed": listed, "ingested": result}
