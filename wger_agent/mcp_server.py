#!/usr/bin/python
import warnings

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
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field
from starlette.responses import JSONResponse

from wger_agent.auth import get_client

__version__ = "0.10.0"

logger = get_logger(name="wger-agent")
logger.setLevel(logging.INFO)


def register_routine_tools(mcp: FastMCP):
    @mcp.tool(tags={"Routine"})
    async def wger_routine(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_routines', 'get_routine', 'create_routine', 'delete_routine', 'get_days', 'create_day', 'delete_day', 'get_slots', 'create_slot', 'create_slot_entry', 'get_templates', 'get_public_templates'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        ordering: str | None = Field(default=None, description="ordering"),
        routine_id: int | None = Field(default=None, description="routine id"),
        name: str | None = Field(default=None, description="name"),
        description: str | None = Field(default=None, description="description"),
        start_date: str | None = Field(default=None, description="start date"),
        end_date: str | None = Field(default=None, description="end date"),
        fit_in_week: bool | None = Field(default=None, description="fit in week"),
        routine: int | None = Field(default=None, description="routine"),
        is_rest: bool | None = Field(default=None, description="is rest"),
        order: int | None = Field(default=None, description="order"),
        day_type: str | None = Field(default=None, description="day type"),
        need_logs_to_advance: bool | None = Field(
            default=None, description="need logs to advance"
        ),
        day_id: int | None = Field(default=None, description="day id"),
        day: int | None = Field(default=None, description="day"),
        slot_type: str | None = Field(default=None, description="slot type"),
        slot: int | None = Field(default=None, description="slot"),
        exercise: int | None = Field(default=None, description="exercise"),
        client=Depends(get_client),
    ) -> Any:
        """Manage routine operations.

        Actions:
          - 'get_routines': List all routines.
          - 'get_routine': Get a specific routine by ID.
          - 'create_routine': Create a new routine.
          - 'delete_routine': Delete a routine.
          - 'get_days': List all workout days.
          - 'create_day': Create a workout day in a routine.
          - 'delete_day': Delete a day.
          - 'get_slots': List all slots (sets).
          - 'create_slot': Create a slot (set) in a day.
          - 'create_slot_entry': Create a slot entry (add exercise to slot).
          - 'get_templates': List user's workout templates.
          - 'get_public_templates': List public workout templates.
        """
        kwargs: dict[str, Any]
        if action == "get_routines":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_routines(**kwargs)
        if action == "get_routine":
            kwargs = {"routine_id": routine_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_routine(**kwargs)
        if action == "create_routine":
            kwargs = {
                "name": name,
                "description": description,
                "start_date": start_date,
                "end_date": end_date,
                "fit_in_week": fit_in_week,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_routine(**kwargs)
        if action == "delete_routine":
            kwargs = {"routine_id": routine_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_routine(**kwargs)
        if action == "get_days":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_days(**kwargs)
        if action == "create_day":
            kwargs = {
                "routine": routine,
                "name": name,
                "description": description,
                "is_rest": is_rest,
                "order": order,
                "day_type": day_type,
                "need_logs_to_advance": need_logs_to_advance,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_day(**kwargs)
        if action == "delete_day":
            kwargs = {"day_id": day_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_day(**kwargs)
        if action == "get_slots":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_slots(**kwargs)
        if action == "create_slot":
            kwargs = {
                "day": day,
                "order": order,
                "slot_type": slot_type,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_slot(**kwargs)
        if action == "create_slot_entry":
            kwargs = {
                "slot": slot,
                "exercise": exercise,
                "order": order,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_slot_entry(**kwargs)
        if action == "get_templates":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_templates(**kwargs)
        if action == "get_public_templates":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_public_templates(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_routines', 'get_routine', 'create_routine', 'delete_routine', 'get_days', 'create_day', 'delete_day', 'get_slots', 'create_slot', 'create_slot_entry', 'get_templates', 'get_public_templates"
        )


def register_routineconfig_tools(mcp: FastMCP):
    @mcp.tool(tags={"RoutineConfig"})
    async def wger_routineconfig(
        action: str = Field(
            description="Action to perform. Must be one of: 'create_weight_config', 'get_weight_configs', 'create_repetitions_config', 'get_repetitions_configs', 'create_sets_config', 'create_rest_config', 'create_rir_config'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        slot_entry: int | None = Field(default=None, description="slot entry"),
        iteration: int | None = Field(default=None, description="iteration"),
        value: float | None = Field(default=None, description="value"),
        operation: str | None = Field(default=None, description="operation"),
        step: str | None = Field(default=None, description="step"),
        repeat: bool | None = Field(default=None, description="repeat"),
        client=Depends(get_client),
    ) -> dict:
        """Manage routineconfig operations.

        Actions:
          - 'create_weight_config': Create a weight progression config.
          - 'get_weight_configs': List weight progression configs.
          - 'create_repetitions_config': Create a repetitions config.
          - 'get_repetitions_configs': List repetitions configs.
          - 'create_sets_config': Create a sets config.
          - 'create_rest_config': Create a rest time config.
          - 'create_rir_config': Create a RiR config.
        """
        kwargs: dict[str, Any]
        if action == "create_weight_config":
            kwargs = {
                "slot_entry": slot_entry,
                "iteration": iteration,
                "value": value,
                "operation": operation,
                "step": step,
                "repeat": repeat,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_weight_config(**kwargs)
        if action == "get_weight_configs":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_weight_configs(**kwargs)
        if action == "create_repetitions_config":
            kwargs = {
                "slot_entry": slot_entry,
                "iteration": iteration,
                "value": value,
                "operation": operation,
                "step": step,
                "repeat": repeat,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_repetitions_config(**kwargs)
        if action == "get_repetitions_configs":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_repetitions_configs(**kwargs)
        if action == "create_sets_config":
            kwargs = {
                "slot_entry": slot_entry,
                "iteration": iteration,
                "value": value,
                "operation": operation,
                "step": step,
                "repeat": repeat,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_sets_config(**kwargs)
        if action == "create_rest_config":
            kwargs = {
                "slot_entry": slot_entry,
                "iteration": iteration,
                "value": value,
                "operation": operation,
                "step": step,
                "repeat": repeat,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_rest_config(**kwargs)
        if action == "create_rir_config":
            kwargs = {
                "slot_entry": slot_entry,
                "iteration": iteration,
                "value": value,
                "operation": operation,
                "step": step,
                "repeat": repeat,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_rir_config(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: create_weight_config', 'get_weight_configs', 'create_repetitions_config', 'get_repetitions_configs', 'create_sets_config', 'create_rest_config', 'create_rir_config"
        )


def register_exercise_tools(mcp: FastMCP):
    @mcp.tool(tags={"Exercise"})
    async def wger_exercise(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_exercises', 'get_exercise_info', 'search_exercises', 'get_exercise_categories', 'get_equipment', 'get_muscles', 'get_exercise_images', 'get_variations'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        ordering: str | None = Field(default=None, description="ordering"),
        exercise_id: int | None = Field(default=None, description="exercise id"),
        term: str | None = Field(default=None, description="search term"),
        client=Depends(get_client),
    ) -> Any:
        """Manage exercise operations.

        Actions:
          - 'get_exercises': List exercises. Supports filters: language, category, muscles, equipment, etc.
          - 'get_exercise_info': Get detailed exercise info (includes translations, images, muscles, etc.).
          - 'search_exercises': Call search_exercises
          - 'get_exercise_categories': List exercise categories (e.g., Arms, Legs, etc.).
          - 'get_equipment': List equipment (e.g., Barbell, Dumbbell, etc.).
          - 'get_muscles': List muscles.
          - 'get_exercise_images': List exercise images.
          - 'get_variations': List exercise variations.
        """
        kwargs: dict[str, Any]
        if action == "get_exercises":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_exercises(**kwargs)
        if action == "get_exercise_info":
            kwargs = {"exercise_id": exercise_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_exercise_info(**kwargs)
        if action == "search_exercises":
            kwargs = {"term": term}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.search_exercises(**kwargs)
        if action == "get_exercise_categories":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_exercise_categories(**kwargs)
        if action == "get_equipment":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_equipment(**kwargs)
        if action == "get_muscles":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_muscles(**kwargs)
        if action == "get_exercise_images":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_exercise_images(**kwargs)
        if action == "get_variations":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_variations(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_exercises', 'get_exercise_info', 'search_exercises', 'get_exercise_categories', 'get_equipment', 'get_muscles', 'get_exercise_images', 'get_variations"
        )


def register_workout_tools(mcp: FastMCP):
    @mcp.tool(tags={"Workout"})
    async def wger_workout(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_workout_sessions', 'get_workout_session', 'create_workout_session', 'delete_workout_session', 'get_workout_logs', 'create_workout_log', 'delete_workout_log'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        ordering: str | None = Field(default=None, description="ordering"),
        session_id: int | None = Field(default=None, description="session id"),
        routine: int | None = Field(default=None, description="routine"),
        date: str | None = Field(default=None, description="date"),
        impression: str | None = Field(default=None, description="impression"),
        notes: str | None = Field(default=None, description="notes"),
        time_start: str | None = Field(default=None, description="time start"),
        time_end: str | None = Field(default=None, description="time end"),
        exercise: int | None = Field(default=None, description="exercise"),
        repetitions: int | None = Field(default=None, description="repetitions"),
        weight: float | None = Field(default=None, description="weight"),
        rir: str | None = Field(default=None, description="rir"),
        log_id: int | None = Field(default=None, description="log id"),
        client=Depends(get_client),
    ) -> Any:
        """Manage workout operations.

        Actions:
          - 'get_workout_sessions': List workout sessions.
          - 'get_workout_session': Get a specific workout session.
          - 'create_workout_session': Create a workout session. Impression: 1=General discomfort, 2=Could be better, 3=Neutral, 4=Good, 5=Perfect.
          - 'delete_workout_session': Delete a workout session.
          - 'get_workout_logs': List workout logs.
          - 'create_workout_log': Create a workout log entry.
          - 'delete_workout_log': Delete a workout log.
        """
        kwargs: dict[str, Any]
        if action == "get_workout_sessions":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_workout_sessions(**kwargs)
        if action == "get_workout_session":
            kwargs = {"session_id": session_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_workout_session(**kwargs)
        if action == "create_workout_session":
            kwargs = {
                "routine": routine,
                "date": date,
                "impression": impression,
                "notes": notes,
                "time_start": time_start,
                "time_end": time_end,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_workout_session(**kwargs)
        if action == "delete_workout_session":
            kwargs = {"session_id": session_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_workout_session(**kwargs)
        if action == "get_workout_logs":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_workout_logs(**kwargs)
        if action == "create_workout_log":
            kwargs = {
                "exercise": exercise,
                "routine": routine,
                "date": date,
                "repetitions": repetitions,
                "weight": weight,  # type: ignore
                "rir": rir,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_workout_log(**kwargs)
        if action == "delete_workout_log":
            kwargs = {"log_id": log_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_workout_log(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_workout_sessions', 'get_workout_session', 'create_workout_session', 'delete_workout_session', 'get_workout_logs', 'create_workout_log', 'delete_workout_log"
        )


def register_nutrition_tools(mcp: FastMCP):
    @mcp.tool(tags={"Nutrition"})
    async def wger_nutrition(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_nutrition_plans', 'get_nutrition_plan_info', 'create_nutrition_plan', 'delete_nutrition_plan', 'create_meal', 'create_meal_item', 'get_ingredients', 'get_ingredient_info', 'get_nutrition_diary', 'log_nutrition'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        plan_id: int | None = Field(default=None, description="plan id"),
        description: str | None = Field(default=None, description="description"),
        only_logging: bool | None = Field(default=None, description="only logging"),
        goal_energy: float | None = Field(default=None, description="goal energy"),
        goal_protein: float | None = Field(default=None, description="goal protein"),
        goal_carbohydrates: float | None = Field(
            default=None, description="goal carbohydrates"
        ),
        goal_fat: float | None = Field(default=None, description="goal fat"),
        _goal_fiber: float | None = Field(default=None, description=" goal fiber"),
        plan: int | None = Field(default=None, description="plan"),
        name: str | None = Field(default=None, description="name"),
        time: str | None = Field(default=None, description="time"),
        order: int | None = Field(default=None, description="order"),
        meal: int | None = Field(default=None, description="meal"),
        ingredient: int | None = Field(default=None, description="ingredient"),
        amount: float | None = Field(default=None, description="amount"),
        weight_unit: int | None = Field(default=None, description="weight unit"),
        ordering: str | None = Field(default=None, description="ordering"),
        ingredient_id: int | None = Field(default=None, description="ingredient id"),
        client=Depends(get_client),
    ) -> Any:
        """Manage nutrition operations.

        Actions:
          - 'get_nutrition_plans': List nutrition plans.
          - 'get_nutrition_plan_info': Get detailed nutrition plan info (includes meals, items, nutritional values).
          - 'create_nutrition_plan': Create a nutrition plan.
          - 'delete_nutrition_plan': Delete a nutrition plan.
          - 'create_meal': Create a meal in a nutrition plan.
          - 'create_meal_item': Add an ingredient to a meal.
          - 'get_ingredients': List ingredients. Supports filters: language, name, etc.
          - 'get_ingredient_info': Get detailed ingredient info (includes weight units).
          - 'get_nutrition_diary': List nutrition diary entries.
          - 'log_nutrition': Call log_nutrition
        """
        kwargs: dict[str, Any]
        if action == "get_nutrition_plans":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_nutrition_plans(**kwargs)
        if action == "get_nutrition_plan_info":
            kwargs = {"plan_id": plan_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_nutrition_plan_info(**kwargs)
        if action == "create_nutrition_plan":
            kwargs = {
                "description": description,  # type: ignore
                "only_logging": only_logging,
                "goal_energy": goal_energy,  # type: ignore
                "goal_protein": goal_protein,  # type: ignore
                "goal_carbohydrates": goal_carbohydrates,  # type: ignore
                "goal_fat": goal_fat,  # type: ignore
                "_goal_fiber": _goal_fiber,  # type: ignore
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_nutrition_plan(**kwargs)
        if action == "delete_nutrition_plan":
            kwargs = {"plan_id": plan_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_nutrition_plan(**kwargs)
        if action == "create_meal":
            kwargs = {
                "plan": plan,
                "name": name,
                "time": time,
                "order": order,
            }  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_meal(**kwargs)
        if action == "create_meal_item":
            kwargs = {
                "meal": meal,
                "ingredient": ingredient,
                "amount": amount,  # type: ignore
                "weight_unit": weight_unit,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_meal_item(**kwargs)
        if action == "get_ingredients":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_ingredients(**kwargs)
        if action == "get_ingredient_info":
            kwargs = {"ingredient_id": ingredient_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_ingredient_info(**kwargs)
        if action == "get_nutrition_diary":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }  # type: ignore
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_nutrition_diary(**kwargs)
        if action == "log_nutrition":
            kwargs = {
                "plan": plan,
                "ingredient": ingredient,
                "amount": amount,
                "meal": meal,
                "weight_unit": weight_unit,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_nutrition_diary_entry(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_nutrition_plans', 'get_nutrition_plan_info', 'create_nutrition_plan', 'delete_nutrition_plan', 'create_meal', 'create_meal_item', 'get_ingredients', 'get_ingredient_info', 'get_nutrition_diary', 'log_nutrition"
        )


def register_body_tools(mcp: FastMCP):
    @mcp.tool(tags={"Body"})
    async def wger_body(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_weight_entries', 'log_body_weight', 'delete_weight_entry', 'get_measurements', 'log_measurement', 'get_measurement_categories', 'create_measurement_category', 'get_gallery'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        ordering: str | None = Field(default=None, description="ordering"),
        entry_id: int | None = Field(default=None, description="entry id"),
        name: str | None = Field(default=None, description="name"),
        unit: str | None = Field(default=None, description="unit"),
        date: str | None = Field(default=None, description="date"),
        weight: float | None = Field(default=None, description="weight"),
        category: int | None = Field(default=None, description="category"),
        value: float | None = Field(default=None, description="value"),
        client=Depends(get_client),
    ) -> Any:
        """Manage body operations.

        Actions:
          - 'get_weight_entries': List body weight entries.
          - 'log_body_weight': Call log_body_weight
          - 'delete_weight_entry': Delete a weight entry.
          - 'get_measurements': List body measurements.
          - 'log_measurement': Call log_measurement
          - 'get_measurement_categories': List measurement categories (e.g., Biceps, Chest, etc.).
          - 'create_measurement_category': Create a measurement category.
          - 'get_gallery': List progress gallery images.
        """
        kwargs: dict[str, Any]
        if action == "get_weight_entries":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_weight_entries(**kwargs)
        if action == "log_body_weight":
            kwargs = {"date": date, "weight": weight}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_weight_entry(**kwargs)
        if action == "delete_weight_entry":
            kwargs = {"entry_id": entry_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_weight_entry(**kwargs)
        if action == "get_measurements":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_measurements(**kwargs)
        if action == "log_measurement":
            kwargs = {"category": category, "date": date, "value": value}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_measurement(**kwargs)
        if action == "get_measurement_categories":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_measurement_categories(**kwargs)
        if action == "create_measurement_category":
            kwargs = {"name": name, "unit": unit}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_measurement_category(**kwargs)
        if action == "get_gallery":
            kwargs = {
                "limit": limit,
                "offset": offset,
                "ordering": ordering,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_gallery(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_weight_entries', 'log_body_weight', 'delete_weight_entry', 'get_measurements', 'log_measurement', 'get_measurement_categories', 'create_measurement_category', 'get_gallery"
        )


def register_user_tools(mcp: FastMCP):
    @mcp.tool(tags={"User"})
    async def wger_user(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_user_profile', 'get_user_statistics', 'get_user_trophies', 'get_languages', 'get_repetition_units', 'get_weight_unit_settings'"
        ),
        limit: int | None = Field(default=None, description="limit"),
        offset: int | None = Field(default=None, description="offset"),
        client=Depends(get_client),
    ) -> Any:
        """Manage user operations.

        Actions:
          - 'get_user_profile': Get the current user's profile.
          - 'get_user_statistics': Get user statistics (workout count, etc.).
          - 'get_user_trophies': List user's earned trophies.
          - 'get_languages': List available languages.
          - 'get_repetition_units': List repetition unit settings.
          - 'get_weight_unit_settings': List weight unit settings.
        """
        kwargs: dict[str, Any]
        if action == "get_user_profile":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user_profile(**kwargs)
        if action == "get_user_statistics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user_statistics(**kwargs)
        if action == "get_user_trophies":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user_trophies(**kwargs)
        if action == "get_languages":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_languages(**kwargs)
        if action == "get_repetition_units":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_repetition_units(**kwargs)
        if action == "get_weight_unit_settings":
            kwargs = {"limit": limit, "offset": offset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_weight_unit_settings(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_user_profile', 'get_user_statistics', 'get_user_trophies', 'get_languages', 'get_repetition_units', 'get_weight_unit_settings"
        )


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="wger-agent MCP",
        version=__version__,
        instructions="wger-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check() -> JSONResponse:
        return JSONResponse({"status": "OK"})

    DEFAULT_ROUTINETOOL = to_boolean(os.getenv("ROUTINETOOL", "True"))
    if DEFAULT_ROUTINETOOL:
        register_routine_tools(mcp)
    DEFAULT_ROUTINECONFIGTOOL = to_boolean(os.getenv("ROUTINECONFIGTOOL", "True"))
    if DEFAULT_ROUTINECONFIGTOOL:
        register_routineconfig_tools(mcp)
    DEFAULT_EXERCISETOOL = to_boolean(os.getenv("EXERCISETOOL", "True"))
    if DEFAULT_EXERCISETOOL:
        register_exercise_tools(mcp)
    DEFAULT_WORKOUTTOOL = to_boolean(os.getenv("WORKOUTTOOL", "True"))
    if DEFAULT_WORKOUTTOOL:
        register_workout_tools(mcp)
    DEFAULT_NUTRITIONTOOL = to_boolean(os.getenv("NUTRITIONTOOL", "True"))
    if DEFAULT_NUTRITIONTOOL:
        register_nutrition_tools(mcp)
    DEFAULT_BODYTOOL = to_boolean(os.getenv("BODYTOOL", "True"))
    if DEFAULT_BODYTOOL:
        register_body_tools(mcp)
    DEFAULT_USERTOOL = to_boolean(os.getenv("USERTOOL", "True"))
    if DEFAULT_USERTOOL:
        register_user_tools(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
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
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
