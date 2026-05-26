import os
import sys
import json
import pytest
import importlib
import runpy
from unittest.mock import MagicMock, patch
from typing import Any

from agent_utilities.core.exceptions import AuthError, UnauthorizedError
from wger_agent.api_client import WgerApi
from wger_agent.api.api_client_base import BaseApiClient
from wger_agent import __getattr__, __dir__
import wger_agent
from wger_agent.auth import get_client
import wger_agent.auth as auth_mod
from wger_agent.mcp_server import (
    get_mcp_instance,
    register_routine_tools,
    register_routineconfig_tools,
    register_exercise_tools,
    register_workout_tools,
    register_nutrition_tools,
    register_body_tools,
    register_user_tools,
)
import wger_agent.mcp_server as mcp_server_mod
from wger_agent.agent_server import agent_server
import wger_agent.agent_server as agent_server_mod


def test_init_getattr_and_dir():
    # Test availability flags in __init__.py
    assert wger_agent._MCP_AVAILABLE is True
    assert wger_agent._AGENT_AVAILABLE is True

    # Test availability flags missing branch
    with patch.dict(wger_agent.OPTIONAL_MODULES, {}, clear=True):
        assert wger_agent._MCP_AVAILABLE is False
        assert wger_agent._AGENT_AVAILABLE is False

    # Test attribute error
    with pytest.raises(AttributeError):
        _ = wger_agent.non_existent_attribute_name

    # Check that dir includes CORE_MODULES
    assert "CORE_MODULES" in dir(wger_agent)


def test_import_module_safely_error():
    from wger_agent import _import_module_safely

    # Test importing an invalid module name raises ImportError, returning None
    assert _import_module_safely("invalid_module_foo_bar") is None


def test_auth_client_singleton_and_errors(mock_requests_session):
    # Reset auth singleton
    auth_mod._client = None

    # Successful retrieval
    client = get_client()
    assert client is not None

    # Singleton check
    client2 = get_client()
    assert client2 is client

    # Mock AuthError
    auth_mod._client = None
    mock_response = MagicMock()
    mock_response.status_code = 401
    mock_requests_session.get.return_value = mock_response
    with pytest.raises(RuntimeError) as excinfo:
        get_client()
    assert "AUTHENTICATION ERROR" in str(excinfo.value)

    # Mock UnauthorizedError
    auth_mod._client = None
    mock_response = MagicMock()
    mock_response.status_code = 403
    mock_requests_session.get.return_value = mock_response
    with pytest.raises(RuntimeError) as excinfo:
        get_client()
    assert "AUTHENTICATION ERROR" in str(excinfo.value)


def test_api_client_base_and_methods(mock_requests_session):
    client = WgerApi(token="test_token")

    # Test generic HTTP methods
    mock_requests_session.get.return_value.json.return_value = {"key": "val"}
    assert client._get("endpoint") == {"key": "val"}

    mock_requests_session.post.return_value.json.return_value = {"key": "val_post"}
    assert client._post("endpoint", data={"d": 1}) == {"key": "val_post"}

    mock_requests_session.put.return_value.json.return_value = {"key": "val_put"}
    assert client._put("endpoint", data={"d": 1}) == {"key": "val_put"}

    mock_requests_session.patch.return_value.json.return_value = {"key": "val_patch"}
    assert client._patch("endpoint", data={"d": 1}) == {"key": "val_patch"}

    mock_requests_session.delete.return_value.status_code = 204
    assert client._delete("endpoint") is True

    # Test list parameters
    client._list("endpoint", limit=10, offset=5, ordering="-id", filter1="a")
    mock_requests_session.get.assert_called_with(
        "https://wger.de/api/v2/endpoint/",
        params={"limit": 10, "offset": 5, "ordering": "-id", "filter1": "a"},
    )

    # Test _config_crud variants
    # 1. config_id only, no kwargs -> GET
    client._config_crud("test-config", config_id=123)
    mock_requests_session.get.assert_called_with(
        "https://wger.de/api/v2/test-config/123/", params=None
    )

    # 2. config_id and _delete kwargs -> DELETE
    client._config_crud("test-config", config_id=123, _delete=True)
    mock_requests_session.delete.assert_called_with(
        "https://wger.de/api/v2/test-config/123/"
    )

    # 3. config_id and kwargs -> PATCH
    client._config_crud("test-config", config_id=123, custom_val=456)
    mock_requests_session.patch.assert_called_with(
        "https://wger.de/api/v2/test-config/123/", json={"custom_val": 456}
    )

    # 4. no config_id, kwargs -> POST
    client._config_crud("test-config", custom_val=456)
    mock_requests_session.post.assert_called_with(
        "https://wger.de/api/v2/test-config/", json={"custom_val": 456}
    )

    # 5. no config_id, no kwargs -> LIST
    client._config_crud("test-config", limit=10, offset=0)

    # Cover line 40 of api_client_base.py (generic request exception pass block in __init__)
    mock_response = MagicMock()
    mock_response.status_code = 500
    mock_response.raise_for_status.side_effect = Exception("Generic error")
    mock_requests_session.get.return_value = mock_response
    # Instantiating the client will trigger the exception block and hit line 40!
    WgerApi(token="test_token")


def test_sub_clients(mock_requests_session):
    client = WgerApi()

    # ExercisesApi
    client.get_exercises(limit=10)
    client.search_exercises(term="bench")
    client.get_exercise(1)
    client.get_exercise_info(1)
    client.get_exercise_infos(limit=10)
    client.get_exercise_translations(limit=10)
    client.get_exercise_categories(limit=10)
    client.get_exercise_category(1)
    client.get_equipment(limit=10)
    client.get_equipment_item(1)
    client.get_muscles(limit=10)
    client.get_muscle(1)
    client.get_exercise_images(limit=10)
    client.get_exercise_image(1)
    client.get_exercise_videos(limit=10)
    client.get_exercise_comments(limit=10)
    client.get_exercise_aliases(limit=10)
    client.get_variations(limit=10)

    # BodyApi
    client.get_weight_entries(limit=10)
    client.get_weight_entry(1)
    client.create_weight_entry(date="2026-05-22", weight=80.5)
    client.update_weight_entry(1, weight="81.0")
    client.delete_weight_entry(1)
    client.get_measurements(limit=10)
    client.get_measurement(1)
    client.create_measurement(category=1, date="2026-05-22", value=35.5)
    client.update_measurement(1, value="36.0")
    client.delete_measurement(1)
    client.get_measurement_categories(limit=10)
    client.get_measurement_category(1)
    client.create_measurement_category(name="Arm", unit="cm")
    client.delete_measurement_category(1)
    client.get_gallery(limit=10)

    # ConfigsApi
    client.get_weight_configs(limit=10)
    client.get_weight_config(1)
    client.create_weight_config(slot_entry=1, iteration=2, value=5.0)
    client.update_weight_config(1, value=6.0)
    client.delete_weight_config(1)
    client.get_max_weight_configs(limit=10)
    client.create_max_weight_config(slot_entry=1, value=100.0)
    client.get_repetitions_configs(limit=10)
    client.create_repetitions_config(slot_entry=1, value=10.0)
    client.update_repetitions_config(1, value=12.0)
    client.delete_repetitions_config(1)
    client.get_max_repetitions_configs(limit=10)
    client.create_max_repetitions_config(slot_entry=1, value=15.0)
    client.get_sets_configs(limit=10)
    client.create_sets_config(slot_entry=1, value=3.0)
    client.update_sets_config(1, value=4.0)
    client.delete_sets_config(1)
    client.get_max_sets_configs(limit=10)
    client.create_max_sets_config(slot_entry=1, value=5.0)
    client.get_rest_configs(limit=10)
    client.create_rest_config(slot_entry=1, value=60.0)
    client.update_rest_config(1, value=90.0)
    client.delete_rest_config(1)
    client.get_max_rest_configs(limit=10)
    client.create_max_rest_config(slot_entry=1, value=120.0)
    client.get_rir_configs(limit=10)
    client.create_rir_config(slot_entry=1, value=2.0)
    client.update_rir_config(1, value=3.0)
    client.delete_rir_config(1)
    client.get_max_rir_configs(limit=10)
    client.create_max_rir_config(slot_entry=1, value=4.0)

    # NutritionApi
    client.get_nutrition_plans(limit=10)
    client.get_nutrition_plan(1)
    client.get_nutrition_plan_info(1)
    client.create_nutrition_plan(
        description="Bulk",
        goal_energy=3000,
        goal_protein=150,
        goal_carbohydrates=300,
        goal_fat=80,
        _goal_fiber=30,
    )
    client.update_nutrition_plan(1, description="Cut")
    client.delete_nutrition_plan(1)
    client.get_meals(limit=10)
    client.get_meal(1)
    client.create_meal(plan=1, name="Lunch", time="12:00", order=2)
    client.update_meal(1, name="Dinner")
    client.delete_meal(1)
    client.get_meal_items(limit=10)
    client.get_meal_item(1)
    client.create_meal_item(meal=1, ingredient=1, amount=100.0, weight_unit=1)
    client.update_meal_item(1, amount=150.0)
    client.delete_meal_item(1)
    client.get_ingredients(limit=10)
    client.get_ingredient(1)
    client.get_ingredient_info(1)
    client.get_ingredient_weight_units(limit=10)
    client.get_weight_units(limit=10)
    client.get_nutrition_diary(limit=10)
    client.create_nutrition_diary_entry(
        plan=1, ingredient=1, amount=200.0, meal=1, weight_unit=1
    )
    client.delete_nutrition_diary_entry(1)
    client.get_ingredient_images(limit=10)

    # RoutineApi
    client.get_routines(limit=10)
    client.get_routine(1)
    client.create_routine(
        name="5x5",
        description="Strength",
        start_date="2026-01-01",
        end_date="2026-06-01",
        fit_in_week=True,
    )
    client.update_routine(1, name="Hypertrophy")
    client.delete_routine(1)
    client.get_templates(limit=10)
    client.get_template(1)
    client.get_public_templates(limit=10)
    client.get_days(limit=10)
    client.get_day(1)
    client.create_day(
        routine=1,
        name="Day A",
        description="Squat day",
        is_rest=False,
        order=1,
        day_type="custom",
        need_logs_to_advance=True,
    )
    client.update_day(1, name="Day A Revised")
    client.delete_day(1)
    client.get_slots(limit=10)
    client.get_slot(1)
    client.create_slot(day=1, order=1, slot_type="normal", duration=120)
    client.update_slot(1, order=2)
    client.delete_slot(1)
    client.get_slot_entries(limit=10)
    client.get_slot_entry(1)
    client.create_slot_entry(slot=1, exercise=1, order=1, reps=5)
    client.update_slot_entry(1, reps=6)
    client.delete_slot_entry(1)

    # UserSystemApi
    mock_requests_session.get.return_value.json.return_value = {"results": [{"id": 42}]}
    client.get_user_profile()
    client.update_user_profile(age=25)

    # Case with empty results list
    mock_requests_session.get.return_value.json.return_value = {"results": []}
    client.get_user_profile()
    client.update_user_profile(age=25)

    # Case with non-dict results
    mock_requests_session.get.return_value.json.return_value = []
    client.get_user_profile()

    client.get_user_statistics()
    client.get_trophies(limit=10)
    client.get_user_trophies(limit=10)
    client.get_languages(limit=10)
    client.get_licenses(limit=10)
    client.get_deletion_log(limit=10)
    client.get_repetition_units(limit=10)
    client.get_weight_unit_settings(limit=10)

    # WorkoutSessionsApi
    client.get_workout_sessions(limit=10)
    client.get_workout_session(1)
    client.create_workout_session(
        routine=1, date="2026-05-22", time_start="10:00", time_end="11:00"
    )
    client.update_workout_session(1, notes="Hard")
    client.delete_workout_session(1)
    client.get_workout_logs(limit=10)
    client.get_workout_log(1)
    client.create_workout_log(
        exercise=1, routine=1, date="2026-05-22", repetitions=10, weight=60.0, rir="2"
    )
    client.update_workout_log(1, reps=12)
    client.delete_workout_log(1)


@pytest.mark.asyncio
async def test_mcp_tools_and_server(mock_requests_session):
    tools_dict = {}

    class MockMCP:
        def tool(self, *args, **kwargs):
            def decorator(func):
                tools_dict[func.__name__] = func
                return func

            return decorator

        def custom_route(self, *args, **kwargs):
            def decorator(func):
                tools_dict[func.__name__] = func
                return func

            return decorator

        def add_middleware(self, *args, **kwargs):
            pass

    mock_mcp: Any = MockMCP()

    # Register everything onto our mock MCP
    register_routine_tools(mock_mcp)  # type: ignore
    register_routineconfig_tools(mock_mcp)  # type: ignore
    register_exercise_tools(mock_mcp)  # type: ignore
    register_workout_tools(mock_mcp)  # type: ignore
    register_nutrition_tools(mock_mcp)  # type: ignore
    register_body_tools(mock_mcp)  # type: ignore
    register_user_tools(mock_mcp)  # type: ignore

    # Mock client and context
    mock_client = MagicMock()
    mock_ctx = MagicMock()

    # Test wger_routine actions
    wger_routine = tools_dict["wger_routine"]
    await wger_routine(
        action="get_routines",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    mock_client.get_routines.assert_called_with(limit=10)

    await wger_routine(
        action="get_routine",
        params_json='{"routine_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="create_routine",
        params_json='{"name": "test"}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="delete_routine",
        params_json='{"routine_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="get_days", params_json='{"limit": 10}', client=mock_client, ctx=mock_ctx
    )
    await wger_routine(
        action="create_day",
        params_json='{"routine": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="delete_day",
        params_json='{"day_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="get_slots",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="create_slot", params_json='{"day": 1}', client=mock_client, ctx=mock_ctx
    )
    await wger_routine(
        action="create_slot_entry",
        params_json='{"slot": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="get_templates",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routine(
        action="get_public_templates",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    with pytest.raises(ValueError):
        await wger_routine(
            action="unknown", params_json="{}", client=mock_client, ctx=mock_ctx
        )

    # Test wger_routineconfig actions
    wger_routineconfig = tools_dict["wger_routineconfig"]
    await wger_routineconfig(
        action="create_weight_config",
        params_json='{"slot_entry": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routineconfig(
        action="get_weight_configs",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routineconfig(
        action="create_repetitions_config",
        params_json='{"slot_entry": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routineconfig(
        action="get_repetitions_configs",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routineconfig(
        action="create_sets_config",
        params_json='{"slot_entry": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routineconfig(
        action="create_rest_config",
        params_json='{"slot_entry": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_routineconfig(
        action="create_rir_config",
        params_json='{"slot_entry": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    with pytest.raises(ValueError):
        await wger_routineconfig(
            action="unknown", params_json="{}", client=mock_client, ctx=mock_ctx
        )

    # Test wger_exercise actions
    wger_exercise = tools_dict["wger_exercise"]
    await wger_exercise(
        action="get_exercises",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_exercise(
        action="get_exercise_info",
        params_json='{"exercise_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_exercise(
        action="search_exercises",
        params_json='{"term": "bench"}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_exercise(
        action="get_exercise_categories",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_exercise(
        action="get_equipment",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_exercise(
        action="get_muscles",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_exercise(
        action="get_exercise_images",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_exercise(
        action="get_variations",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    with pytest.raises(ValueError):
        await wger_exercise(
            action="unknown", params_json="{}", client=mock_client, ctx=mock_ctx
        )

    # Test wger_workout actions
    wger_workout = tools_dict["wger_workout"]
    await wger_workout(
        action="get_workout_sessions",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_workout(
        action="get_workout_session",
        params_json='{"session_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_workout(
        action="create_workout_session",
        params_json='{"routine": 1, "date": "2026"}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_workout(
        action="delete_workout_session",
        params_json='{"session_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_workout(
        action="get_workout_logs",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_workout(
        action="create_workout_log",
        params_json='{"exercise": 1, "routine": 1, "date": "2026"}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_workout(
        action="delete_workout_log",
        params_json='{"log_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    with pytest.raises(ValueError):
        await wger_workout(
            action="unknown", params_json="{}", client=mock_client, ctx=mock_ctx
        )

    # Test wger_nutrition actions
    wger_nutrition = tools_dict["wger_nutrition"]
    await wger_nutrition(
        action="get_nutrition_plans",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="get_nutrition_plan_info",
        params_json='{"plan_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="create_nutrition_plan",
        params_json='{"description": "Bulk"}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="delete_nutrition_plan",
        params_json='{"plan_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="create_meal",
        params_json='{"plan": 1, "name": "Lunch"}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="create_meal_item",
        params_json='{"meal": 1, "ingredient": 1, "amount": 100.0}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="get_ingredients",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="get_ingredient_info",
        params_json='{"ingredient_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="get_nutrition_diary",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_nutrition(
        action="log_nutrition",
        params_json='{"plan": 1, "ingredient": 1, "amount": 100.0}',
        client=mock_client,
        ctx=mock_ctx,
    )
    with pytest.raises(ValueError):
        await wger_nutrition(
            action="unknown", params_json="{}", client=mock_client, ctx=mock_ctx
        )

    # Test wger_body actions
    wger_body = tools_dict["wger_body"]
    await wger_body(
        action="get_weight_entries",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_body(
        action="log_body_weight",
        params_json='{"date": "2026", "weight": 80.0}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_body(
        action="delete_weight_entry",
        params_json='{"entry_id": 1}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_body(
        action="get_measurements",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_body(
        action="log_measurement",
        params_json='{"category": 1, "date": "2026", "value": 35.0}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_body(
        action="get_measurement_categories",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_body(
        action="create_measurement_category",
        params_json='{"name": "Arm"}',
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_body(
        action="get_gallery",
        params_json='{"limit": 10}',
        client=mock_client,
        ctx=mock_ctx,
    )
    with pytest.raises(ValueError):
        await wger_body(
            action="unknown", params_json="{}", client=mock_client, ctx=mock_ctx
        )

    # Test wger_user actions
    wger_user = tools_dict["wger_user"]
    await wger_user(
        action="get_user_profile", params_json="{}", client=mock_client, ctx=mock_ctx
    )
    await wger_user(
        action="get_user_statistics", params_json="{}", client=mock_client, ctx=mock_ctx
    )
    await wger_user(
        action="get_user_trophies", params_json="{}", client=mock_client, ctx=mock_ctx
    )
    await wger_user(
        action="get_languages", params_json="{}", client=mock_client, ctx=mock_ctx
    )
    await wger_user(
        action="get_repetition_units",
        params_json="{}",
        client=mock_client,
        ctx=mock_ctx,
    )
    await wger_user(
        action="get_weight_unit_settings",
        params_json="{}",
        client=mock_client,
        ctx=mock_ctx,
    )
    with pytest.raises(ValueError):
        await wger_user(
            action="unknown", params_json="{}", client=mock_client, ctx=mock_ctx
        )

    # Test invalid json error branches for ALL action tools
    for tool_name in [
        "wger_routine",
        "wger_routineconfig",
        "wger_exercise",
        "wger_workout",
        "wger_nutrition",
        "wger_body",
        "wger_user",
    ]:
        res = await tools_dict[tool_name](
            action="dummy", params_json="invalid_json", client=mock_client, ctx=mock_ctx
        )
        assert "error" in res


def test_mcp_server_run_and_startup(mock_requests_session):
    """CONCEPT:WGER-03: Verifies that the FastMCP server can startup and run under stdio, SSE, and HTTP transport modes."""
    # Test get_mcp_instance
    with patch.dict(
        os.environ, {"ROUTINETOOL": "True", "BODYTOOL": "True", "USERTOOL": "True"}
    ):
        mcp, args, middlewares = get_mcp_instance()
        assert mcp is not None

    # Test mcp_server running logic
    # Mock mcp instance run and args
    mock_mcp = MagicMock()

    # We want to cover transport branches in mcp_server()
    # Mock get_mcp_instance to return mock_mcp, and mock args
    mock_args = MagicMock()
    mock_args.transport = "stdio"
    mock_args.auth_type = "none"

    with patch(
        "wger_agent.mcp.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args, []),
    ):
        mcp_server_mod.mcp_server()
        mock_mcp.run.assert_called_with(transport="stdio")

        # Test streamable-http
        mock_args.transport = "streamable-http"
        mock_args.host = "localhost"
        mock_args.port = 8000
        mcp_server_mod.mcp_server()
        mock_mcp.run.assert_called_with(
            transport="streamable-http", host="localhost", port=8000
        )

        # Test sse
        mock_args.transport = "sse"
        mcp_server_mod.mcp_server()
        mock_mcp.run.assert_called_with(transport="sse", host="localhost", port=8000)

        # Test invalid transport
        mock_args.transport = "invalid"
        with pytest.raises(SystemExit):
            mcp_server_mod.mcp_server()


@pytest.mark.asyncio
async def test_health_check_endpoint():
    """CONCEPT:WGER-03: Verifies that the custom /health endpoint returns a successful HTTP 200 response."""
    # Retrieve mcp instance and test custom health route
    mcp, _, _ = get_mcp_instance()
    health_route = next(r for r in mcp._additional_http_routes if r.path == "/health")
    response = await health_route.endpoint()
    assert response.status_code == 200


def test_mcp_server_exceptions_reload():
    # Cover lines 15-16 of mcp_server.py and mcp/mcp_server.py (except ImportError logic)
    mcp_module = sys.modules["wger_agent.mcp.mcp_server"]
    with patch.dict("sys.modules", {"requests.exceptions": None}):
        importlib.reload(mcp_server_mod)
        importlib.reload(mcp_module)


def test_agent_server(mock_requests_session):
    # Test agent_server in agent_server.py
    mock_agent_utils = MagicMock()
    mock_meta = MagicMock()
    mock_meta.get.side_effect = lambda key, default=None: {
        "name": "TestWger",
        "description": "TestDesc",
        "content": "TestContent",
    }.get(key, default)
    mock_agent_utils.load_identity.return_value = mock_meta

    mock_parser = MagicMock()
    mock_parser.parse_args.return_value = MagicMock(
        debug=True,
        mcp_url="http://localhost:8000",
        mcp_config="mcp_config.json",
        host="localhost",
        port=8080,
        provider="openai",
        model_id="gpt-4",
        base_url="http://base",
        api_key="key",
        custom_skills_directory=None,
        web=True,
        otel=True,
        otel_endpoint="otel",
        otel_headers={},
        otel_public_key="pub",
        otel_secret_key="sec",
        otel_protocol="grpc",
    )
    mock_agent_utils.create_agent_parser.return_value = mock_parser

    with patch.dict("sys.modules", {"agent_utilities": mock_agent_utils}):
        agent_server()

    mock_agent_utils.initialize_workspace.assert_called_once()
    mock_agent_utils.load_identity.assert_called_once()
    mock_agent_utils.create_agent_server.assert_called_once()


def test_main_execution(mock_requests_session):
    # Cover wger_agent.__main__ logic (using runpy)
    with (
        patch("wger_agent.agent_server.agent_server") as mock_agent_server,
        patch("sys.argv", ["main"]),
    ):
        runpy.run_module("wger_agent.__main__", run_name="__main__")
        mock_agent_server.assert_called_once()


def test_agent_server_main():
    # Cover wger_agent.agent_server __main__ logic
    mock_agent_utils = MagicMock()
    mock_meta = MagicMock()
    mock_meta.get.side_effect = lambda key, default=None: {
        "name": "TestWger",
        "description": "TestDesc",
        "content": "TestContent",
    }.get(key, default)
    mock_agent_utils.load_identity.return_value = mock_meta

    mock_parser = MagicMock()
    mock_parser.parse_args.return_value = MagicMock(
        debug=True,
        mcp_url="http://localhost:8000",
        mcp_config="mcp_config.json",
        host="localhost",
        port=8080,
        provider="openai",
        model_id="gpt-4",
        base_url="http://base",
        api_key="key",
        custom_skills_directory=None,
        web=True,
        otel=True,
        otel_endpoint="otel",
        otel_headers={},
        otel_public_key="pub",
        otel_secret_key="sec",
        otel_protocol="grpc",
    )
    mock_agent_utils.create_agent_parser.return_value = mock_parser

    with (
        patch.dict("sys.modules", {"agent_utilities": mock_agent_utils}),
        patch("sys.argv", ["agent-server"]),
    ):
        runpy.run_module("wger_agent.agent_server", run_name="__main__")

    mock_agent_utils.initialize_workspace.assert_called_once()


def test_mcp_server_main():
    # Cover wger_agent.mcp_server __main__ logic
    with patch("fastmcp.FastMCP.run") as mock_run, patch("sys.argv", ["mcp-server"]):
        runpy.run_module("wger_agent.mcp_server", run_name="__main__")
        mock_run.assert_called_once()
