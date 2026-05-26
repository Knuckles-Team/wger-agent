# wger_agent/mcp/tools.py
import json

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from wger_agent.auth import get_client

# CONCEPT:WGER-04: Wger Resource API Adapters


def register_routine_tools(mcp: FastMCP):
    """CONCEPT:WGER-04: Register routine tools with FastMCP."""

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
        if ctx:
            ctx.info("Executing tool...")

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_routines":
            return client.get_routines(**kwargs)
        if action == "get_routine":
            return client.get_routine(**kwargs)
        if action == "create_routine":
            return client.create_routine(**kwargs)
        if action == "delete_routine":
            return client.delete_routine(**kwargs)
        if action == "get_days":
            return client.get_days(**kwargs)
        if action == "create_day":
            return client.create_day(**kwargs)
        if action == "delete_day":
            return client.delete_day(**kwargs)
        if action == "get_slots":
            return client.get_slots(**kwargs)
        if action == "create_slot":
            return client.create_slot(**kwargs)
        if action == "create_slot_entry":
            return client.create_slot_entry(**kwargs)
        if action == "get_templates":
            return client.get_templates(**kwargs)
        if action == "get_public_templates":
            return client.get_public_templates(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_routineconfig_tools(mcp: FastMCP):
    """CONCEPT:WGER-04: Register routine configuration tools with FastMCP."""

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
        if ctx:
            ctx.info("Executing tool...")

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "create_weight_config":
            return client.create_weight_config(**kwargs)
        if action == "get_weight_configs":
            return client.get_weight_configs(**kwargs)
        if action == "create_repetitions_config":
            return client.create_repetitions_config(**kwargs)
        if action == "get_repetitions_configs":
            return client.get_repetitions_configs(**kwargs)
        if action == "create_sets_config":
            return client.create_sets_config(**kwargs)
        if action == "create_rest_config":
            return client.create_rest_config(**kwargs)
        if action == "create_rir_config":
            return client.create_rir_config(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_exercise_tools(mcp: FastMCP):
    """CONCEPT:WGER-04: Register exercise tools with FastMCP."""

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
        if ctx:
            ctx.info("Executing tool...")

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_exercises":
            return client.get_exercises(**kwargs)
        if action == "get_exercise_info":
            return client.get_exercise_info(**kwargs)
        if action == "search_exercises":
            return client.search_exercises(**kwargs)
        if action == "get_exercise_categories":
            return client.get_exercise_categories(**kwargs)
        if action == "get_equipment":
            return client.get_equipment(**kwargs)
        if action == "get_muscles":
            return client.get_muscles(**kwargs)
        if action == "get_exercise_images":
            return client.get_exercise_images(**kwargs)
        if action == "get_variations":
            return client.get_variations(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_workout_tools(mcp: FastMCP):
    """CONCEPT:WGER-04: Register workout tools with FastMCP."""

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
        if ctx:
            ctx.info("Executing tool...")

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_workout_sessions":
            return client.get_workout_sessions(**kwargs)
        if action == "get_workout_session":
            return client.get_workout_session(**kwargs)
        if action == "create_workout_session":
            return client.create_workout_session(**kwargs)
        if action == "delete_workout_session":
            return client.delete_workout_session(**kwargs)
        if action == "get_workout_logs":
            return client.get_workout_logs(**kwargs)
        if action == "create_workout_log":
            return client.create_workout_log(**kwargs)
        if action == "delete_workout_log":
            return client.delete_workout_log(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_nutrition_tools(mcp: FastMCP):
    """CONCEPT:WGER-04: Register nutrition tools with FastMCP."""

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
        if ctx:
            ctx.info("Executing tool...")

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_nutrition_plans":
            return client.get_nutrition_plans(**kwargs)
        if action == "get_nutrition_plan_info":
            return client.get_nutrition_plan_info(**kwargs)
        if action == "create_nutrition_plan":
            return client.create_nutrition_plan(**kwargs)
        if action == "delete_nutrition_plan":
            return client.delete_nutrition_plan(**kwargs)
        if action == "create_meal":
            return client.create_meal(**kwargs)
        if action == "create_meal_item":
            return client.create_meal_item(**kwargs)
        if action == "get_ingredients":
            return client.get_ingredients(**kwargs)
        if action == "get_ingredient_info":
            return client.get_ingredient_info(**kwargs)
        if action == "get_nutrition_diary":
            return client.get_nutrition_diary(**kwargs)
        if action == "log_nutrition":
            return client.log_nutrition(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_body_tools(mcp: FastMCP):
    """CONCEPT:WGER-04: Register body measurement tools with FastMCP."""

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
        if ctx:
            ctx.info("Executing tool...")

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_weight_entries":
            return client.get_weight_entries(**kwargs)
        if action == "log_body_weight":
            return client.log_body_weight(**kwargs)
        if action == "delete_weight_entry":
            return client.delete_weight_entry(**kwargs)
        if action == "get_measurements":
            return client.get_measurements(**kwargs)
        if action == "log_measurement":
            return client.log_measurement(**kwargs)
        if action == "get_measurement_categories":
            return client.get_measurement_categories(**kwargs)
        if action == "create_measurement_category":
            return client.create_measurement_category(**kwargs)
        if action == "get_gallery":
            return client.get_gallery(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_user_tools(mcp: FastMCP):
    """CONCEPT:WGER-04: Register user configuration tools with FastMCP."""

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
        if ctx:
            ctx.info("Executing tool...")

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_user_profile":
            return client.get_user_profile(**kwargs)
        if action == "get_user_statistics":
            return client.get_user_statistics(**kwargs)
        if action == "get_user_trophies":
            return client.get_user_trophies(**kwargs)
        if action == "get_languages":
            return client.get_languages(**kwargs)
        if action == "get_repetition_units":
            return client.get_repetition_units(**kwargs)
        if action == "get_weight_unit_settings":
            return client.get_weight_unit_settings(**kwargs)
        raise ValueError(f"Unknown action: {action}")
