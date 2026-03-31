#!/usr/bin/python


from dotenv import load_dotenv, find_dotenv
from agent_utilities.base_utilities import to_boolean
import os
import sys
import logging
from typing import Optional, Any

from pydantic import Field
from fastmcp import FastMCP
from fastmcp.utilities.logging import get_logger
from agent_utilities.mcp_utilities import (
    create_mcp_server,
)
from wger_agent.auth import get_client

__version__ = "0.1.25"
print(f"Wger MCP v{__version__}", file=sys.stderr)

logger = get_logger(name="TokenMiddleware")
logger.setLevel(logging.DEBUG)


def register_prompts(mcp: FastMCP):
    @mcp.prompt(
        name="fitness_plan",
        description="Generate a fitness plan using wger data.",
    )
    def fitness_plan_prompt(goal: str, experience_level: str = "intermediate") -> str:
        """Generate a fitness plan prompt."""
        return f"Create a {experience_level} fitness plan for the goal: '{goal}'. Use the available wger tools to search exercises, create routines, and set up progression."

    @mcp.prompt(
        name="nutrition_plan",
        description="Generate a nutrition plan using wger data.",
    )
    def nutrition_plan_prompt(calories: str = "2000", goal: str = "maintenance") -> str:
        """Generate a nutrition plan prompt."""
        return f"Create a nutrition plan targeting {calories} calories for {goal}. Use the wger nutrition tools to search ingredients and build meals."


def register_routine_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_routines",
        description="List all workout routines for the authenticated user.",
        tags={"Routine"},
    )
    def get_routines_tool(
        limit: Optional[int] = Field(default=None, description="Max results per page."),
        offset: Optional[int] = Field(
            default=None, description="Offset for pagination."
        ),
    ) -> Any:
        """List routines."""
        return get_client().get_routines(limit=limit, offset=offset)

    @mcp.tool(
        name="get_routine",
        description="Get a specific routine by ID.",
        tags={"Routine"},
    )
    def get_routine_tool(
        routine_id: int = Field(description="Routine ID."),
    ) -> Any:
        """Get routine."""
        return get_client().get_routine(routine_id)

    @mcp.tool(
        name="create_routine",
        description="Create a new workout routine.",
        tags={"Routine"},
    )
    def create_routine_tool(
        name: str = Field(description="Routine name (max 50 chars)."),
        description: str = Field(
            default="", description="Description (max 1000 chars)."
        ),
        start_date: str = Field(default="", description="Start date (YYYY-MM-DD)."),
        end_date: str = Field(default="", description="End date (YYYY-MM-DD)."),
        fit_in_week: bool = Field(default=False, description="Fit routine in a week."),
    ) -> Any:
        """Create routine."""
        return get_client().create_routine(
            name=name,
            description=description,
            start_date=start_date,
            end_date=end_date,
            fit_in_week=fit_in_week,
        )

    @mcp.tool(
        name="delete_routine",
        description="Delete a routine.",
        tags={"Routine"},
    )
    def delete_routine_tool(
        routine_id: int = Field(description="Routine ID to delete."),
    ) -> Any:
        """Delete routine."""
        return get_client().delete_routine(routine_id)

    @mcp.tool(
        name="get_days",
        description="List workout days. Filter by routine with routine=<id>.",
        tags={"Routine"},
    )
    def get_days_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        offset: Optional[int] = Field(default=None, description="Offset."),
    ) -> Any:
        """List days."""
        return get_client().get_days(limit=limit, offset=offset)

    @mcp.tool(
        name="create_day",
        description="Create a workout day in a routine.",
        tags={"Routine"},
    )
    def create_day_tool(
        routine: int = Field(description="Routine ID."),
        name: str = Field(default="", description="Day name."),
        description: str = Field(default="", description="Day description."),
        is_rest: bool = Field(default=False, description="Whether this is a rest day."),
        order: int = Field(default=1, description="Day order in the routine."),
        day_type: str = Field(
            default="custom",
            description="Type: custom, enom, amrap, hiit, tabata, edt, rft, afap.",
        ),
    ) -> Any:
        """Create day."""
        return get_client().create_day(
            routine=routine,
            name=name,
            description=description,
            is_rest=is_rest,
            order=order,
            day_type=day_type,
        )

    @mcp.tool(
        name="delete_day",
        description="Delete a workout day.",
        tags={"Routine"},
    )
    def delete_day_tool(
        day_id: int = Field(description="Day ID to delete."),
    ) -> Any:
        """Delete day."""
        return get_client().delete_day(day_id)

    @mcp.tool(
        name="get_slots",
        description="List exercise slots (sets) in workout days.",
        tags={"Routine"},
    )
    def get_slots_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        offset: Optional[int] = Field(default=None, description="Offset."),
    ) -> Any:
        """List slots."""
        return get_client().get_slots(limit=limit, offset=offset)

    @mcp.tool(
        name="create_slot",
        description="Create an exercise slot (set) in a day.",
        tags={"Routine"},
    )
    def create_slot_tool(
        day: int = Field(description="Day ID."),
        order: int = Field(default=1, description="Slot order."),
        slot_type: str = Field(
            default="normal",
            description="Type: normal, dropset, myo, partial, forced, tut, iso, jump.",
        ),
    ) -> Any:
        """Create slot."""
        return get_client().create_slot(day=day, order=order, slot_type=slot_type)

    @mcp.tool(
        name="create_slot_entry",
        description="Add an exercise to a slot.",
        tags={"Routine"},
    )
    def create_slot_entry_tool(
        slot: int = Field(description="Slot ID."),
        exercise: int = Field(description="Exercise ID."),
        order: int = Field(default=1, description="Entry order."),
    ) -> Any:
        """Create slot entry."""
        return get_client().create_slot_entry(slot=slot, exercise=exercise, order=order)

    @mcp.tool(
        name="get_templates",
        description="List user's workout templates.",
        tags={"Routine"},
    )
    def get_templates_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
    ) -> Any:
        """List templates."""
        return get_client().get_templates(limit=limit)

    @mcp.tool(
        name="get_public_templates",
        description="List publicly shared workout templates.",
        tags={"Routine"},
    )
    def get_public_templates_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
    ) -> Any:
        """List public templates."""
        return get_client().get_public_templates(limit=limit)


def register_routineconfig_tools(mcp: FastMCP):
    @mcp.tool(
        name="create_weight_config",
        description="Create a weight progression config for a slot entry. Controls how weight progresses across iterations.",
        tags={"RoutineConfig"},
    )
    def create_weight_config_tool(
        slot_entry: int = Field(description="Slot entry ID."),
        iteration: int = Field(
            default=1, description="Iteration number this takes effect."
        ),
        value: float = Field(
            default=0, description="Weight value (e.g., 50.0 for 50kg)."
        ),
        operation: str = Field(
            default="r",
            description="Operation: 'r' (replace), '+' (add), '-' (subtract).",
        ),
        step: str = Field(
            default="abs", description="Step: 'abs' (absolute) or 'percent'."
        ),
        repeat: bool = Field(
            default=False, description="Repeat this rule until a new one takes effect."
        ),
    ) -> Any:
        """Create weight config."""
        return get_client().create_weight_config(
            slot_entry=slot_entry,
            iteration=iteration,
            value=value,
            operation=operation,
            step=step,
            repeat=repeat,
        )

    @mcp.tool(
        name="get_weight_configs",
        description="List weight progression configs.",
        tags={"RoutineConfig"},
    )
    def get_weight_configs_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
    ) -> Any:
        """List weight configs."""
        return get_client().get_weight_configs(limit=limit)

    @mcp.tool(
        name="create_repetitions_config",
        description="Create a repetitions progression config for a slot entry.",
        tags={"RoutineConfig"},
    )
    def create_repetitions_config_tool(
        slot_entry: int = Field(description="Slot entry ID."),
        iteration: int = Field(default=1, description="Iteration number."),
        value: float = Field(default=0, description="Repetitions value."),
        operation: str = Field(default="r", description="Operation: 'r', '+', '-'."),
        step: str = Field(default="abs", description="Step: 'abs' or 'percent'."),
        repeat: bool = Field(default=False, description="Repeat until next rule."),
    ) -> Any:
        """Create repetitions config."""
        return get_client().create_repetitions_config(
            slot_entry=slot_entry,
            iteration=iteration,
            value=value,
            operation=operation,
            step=step,
            repeat=repeat,
        )

    @mcp.tool(
        name="get_repetitions_configs",
        description="List repetitions configs.",
        tags={"RoutineConfig"},
    )
    def get_repetitions_configs_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
    ) -> Any:
        """List repetitions configs."""
        return get_client().get_repetitions_configs(limit=limit)

    @mcp.tool(
        name="create_sets_config",
        description="Create a sets count progression config for a slot entry.",
        tags={"RoutineConfig"},
    )
    def create_sets_config_tool(
        slot_entry: int = Field(description="Slot entry ID."),
        iteration: int = Field(default=1, description="Iteration number."),
        value: float = Field(default=0, description="Sets value."),
        operation: str = Field(default="r", description="Operation: 'r', '+', '-'."),
        step: str = Field(default="abs", description="Step: 'abs' or 'percent'."),
        repeat: bool = Field(default=False, description="Repeat until next rule."),
    ) -> Any:
        """Create sets config."""
        return get_client().create_sets_config(
            slot_entry=slot_entry,
            iteration=iteration,
            value=value,
            operation=operation,
            step=step,
            repeat=repeat,
        )

    @mcp.tool(
        name="create_rest_config",
        description="Create a rest time progression config for a slot entry.",
        tags={"RoutineConfig"},
    )
    def create_rest_config_tool(
        slot_entry: int = Field(description="Slot entry ID."),
        iteration: int = Field(default=1, description="Iteration number."),
        value: float = Field(default=0, description="Rest value in seconds."),
        operation: str = Field(default="r", description="Operation: 'r', '+', '-'."),
        step: str = Field(default="abs", description="Step: 'abs' or 'percent'."),
        repeat: bool = Field(default=False, description="Repeat until next rule."),
    ) -> Any:
        """Create rest config."""
        return get_client().create_rest_config(
            slot_entry=slot_entry,
            iteration=iteration,
            value=value,
            operation=operation,
            step=step,
            repeat=repeat,
        )

    @mcp.tool(
        name="create_rir_config",
        description="Create a RiR (Reps in Reserve) progression config for a slot entry.",
        tags={"RoutineConfig"},
    )
    def create_rir_config_tool(
        slot_entry: int = Field(description="Slot entry ID."),
        iteration: int = Field(default=1, description="Iteration number."),
        value: float = Field(default=0, description="RiR value."),
        operation: str = Field(default="r", description="Operation: 'r', '+', '-'."),
        step: str = Field(default="abs", description="Step: 'abs' or 'percent'."),
        repeat: bool = Field(default=False, description="Repeat until next rule."),
    ) -> Any:
        """Create RiR config."""
        return get_client().create_rir_config(
            slot_entry=slot_entry,
            iteration=iteration,
            value=value,
            operation=operation,
            step=step,
            repeat=repeat,
        )


def register_exercise_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_exercises",
        description="List exercises from the exercise database. Supports filters: language, category, muscles, equipment.",
        tags={"Exercise"},
    )
    def get_exercises_tool(
        limit: Optional[int] = Field(default=20, description="Max results per page."),
        offset: Optional[int] = Field(default=None, description="Offset."),
        ordering: Optional[str] = Field(
            default=None, description="Order by field. Prefix with - for descending."
        ),
        language: Optional[int] = Field(
            default=None, description="Filter by language ID."
        ),
        category: Optional[int] = Field(
            default=None, description="Filter by exercise category ID."
        ),
    ) -> Any:
        """List exercises."""
        filters = {}
        if language:
            filters["language"] = language
        if category:
            filters["category"] = category
        return get_client().get_exercises(
            limit=limit, offset=offset, ordering=ordering, **filters
        )

    @mcp.tool(
        name="get_exercise_info",
        description="Get detailed exercise info including translations, images, muscles worked, and equipment.",
        tags={"Exercise"},
    )
    def get_exercise_info_tool(
        exercise_id: int = Field(description="Exercise ID."),
    ) -> Any:
        """Get exercise info."""
        return get_client().get_exercise_info(exercise_id)

    @mcp.tool(
        name="search_exercises",
        description="Search exercises by name. Returns exercise info entries matching the search term.",
        tags={"Exercise"},
    )
    def search_exercises_tool(
        term: str = Field(description="Search term."),
        language: Optional[int] = Field(
            default=2, description="Language ID (2=English)."
        ),
        limit: Optional[int] = Field(default=20, description="Max results."),
    ) -> Any:
        """Search exercises."""
        filters = {"language": language, "format": "json"}
        return get_client().get_exercise_infos(limit=limit, **filters)

    @mcp.tool(
        name="get_exercise_categories",
        description="List exercise categories (e.g., Arms, Legs, Chest, Back, etc.).",
        tags={"Exercise"},
    )
    def get_exercise_categories_tool(
        limit: Optional[int] = Field(default=100, description="Max results."),
    ) -> Any:
        """List categories."""
        return get_client().get_exercise_categories(limit=limit)

    @mcp.tool(
        name="get_equipment",
        description="List available equipment (e.g., Barbell, Dumbbell, Kettlebell, etc.).",
        tags={"Exercise"},
    )
    def get_equipment_tool(
        limit: Optional[int] = Field(default=100, description="Max results."),
    ) -> Any:
        """List equipment."""
        return get_client().get_equipment(limit=limit)

    @mcp.tool(
        name="get_muscles",
        description="List muscles (e.g., Biceps, Pectoralis, Quadriceps, etc.).",
        tags={"Exercise"},
    )
    def get_muscles_tool(
        limit: Optional[int] = Field(default=100, description="Max results."),
    ) -> Any:
        """List muscles."""
        return get_client().get_muscles(limit=limit)

    @mcp.tool(
        name="get_exercise_images",
        description="List exercise images. Filter by exercise with exercise_base=<id>.",
        tags={"Exercise"},
    )
    def get_exercise_images_tool(
        limit: Optional[int] = Field(default=20, description="Max results."),
        exercise_base: Optional[int] = Field(
            default=None, description="Filter by exercise base ID."
        ),
    ) -> Any:
        """List exercise images."""
        filters = {}
        if exercise_base:
            filters["exercise_base"] = exercise_base
        return get_client().get_exercise_images(limit=limit, **filters)

    @mcp.tool(
        name="get_variations",
        description="List exercise variation groups.",
        tags={"Exercise"},
    )
    def get_variations_tool(
        limit: Optional[int] = Field(default=20, description="Max results."),
    ) -> Any:
        """List variations."""
        return get_client().get_variations(limit=limit)


def register_workout_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_workout_sessions",
        description="List workout sessions.",
        tags={"Workout"},
    )
    def get_workout_sessions_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        offset: Optional[int] = Field(default=None, description="Offset."),
        ordering: Optional[str] = Field(default=None, description="Order by field."),
    ) -> Any:
        """List workout sessions."""
        return get_client().get_workout_sessions(
            limit=limit, offset=offset, ordering=ordering
        )

    @mcp.tool(
        name="get_workout_session",
        description="Get a specific workout session.",
        tags={"Workout"},
    )
    def get_workout_session_tool(
        session_id: int = Field(description="Session ID."),
    ) -> Any:
        """Get session."""
        return get_client().get_workout_session(session_id)

    @mcp.tool(
        name="create_workout_session",
        description="Create a workout session. Impression: 1=Discomfort, 2=Could be better, 3=Neutral, 4=Good, 5=Perfect.",
        tags={"Workout"},
    )
    def create_workout_session_tool(
        routine: int = Field(description="Routine ID."),
        date: str = Field(description="Date (YYYY-MM-DD)."),
        impression: str = Field(default="3", description="1-5 scale."),
        notes: str = Field(default="", description="Session notes."),
        time_start: str = Field(default="", description="Start time (HH:MM)."),
        time_end: str = Field(default="", description="End time (HH:MM)."),
    ) -> Any:
        """Create session."""
        return get_client().create_workout_session(
            routine=routine,
            date=date,
            impression=impression,
            notes=notes,
            time_start=time_start,
            time_end=time_end,
        )

    @mcp.tool(
        name="delete_workout_session",
        description="Delete a workout session.",
        tags={"Workout"},
    )
    def delete_workout_session_tool(
        session_id: int = Field(description="Session ID."),
    ) -> Any:
        """Delete session."""
        return get_client().delete_workout_session(session_id)

    @mcp.tool(
        name="get_workout_logs",
        description="List workout log entries.",
        tags={"Workout"},
    )
    def get_workout_logs_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        offset: Optional[int] = Field(default=None, description="Offset."),
        ordering: Optional[str] = Field(default=None, description="Order by field."),
    ) -> Any:
        """List workout logs."""
        return get_client().get_workout_logs(
            limit=limit, offset=offset, ordering=ordering
        )

    @mcp.tool(
        name="create_workout_log",
        description="Log a set performed during a workout (exercise, weight, reps, date).",
        tags={"Workout"},
    )
    def create_workout_log_tool(
        exercise: int = Field(description="Exercise ID."),
        routine: int = Field(description="Routine ID."),
        date: str = Field(description="Date (YYYY-MM-DD)."),
        repetitions: int = Field(default=0, description="Number of reps."),
        weight: float = Field(default=0, description="Weight used."),
        rir: Optional[str] = Field(default=None, description="Reps in reserve."),
    ) -> Any:
        """Create workout log."""
        return get_client().create_workout_log(
            exercise=exercise,
            routine=routine,
            date=date,
            repetitions=repetitions,
            weight=weight,
            rir=rir,
        )

    @mcp.tool(
        name="delete_workout_log",
        description="Delete a workout log entry.",
        tags={"Workout"},
    )
    def delete_workout_log_tool(
        log_id: int = Field(description="Log ID."),
    ) -> Any:
        """Delete log."""
        return get_client().delete_workout_log(log_id)


def register_nutrition_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_nutrition_plans",
        description="List nutrition plans.",
        tags={"Nutrition"},
    )
    def get_nutrition_plans_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
    ) -> Any:
        """List plans."""
        return get_client().get_nutrition_plans(limit=limit)

    @mcp.tool(
        name="get_nutrition_plan_info",
        description="Get detailed nutrition plan with meals, items, and nutritional totals.",
        tags={"Nutrition"},
    )
    def get_nutrition_plan_info_tool(
        plan_id: int = Field(description="Nutrition plan ID."),
    ) -> Any:
        """Get plan info."""
        return get_client().get_nutrition_plan_info(plan_id)

    @mcp.tool(
        name="create_nutrition_plan",
        description="Create a nutrition plan with optional macro goals.",
        tags={"Nutrition"},
    )
    def create_nutrition_plan_tool(
        description: str = Field(default="", description="Plan description."),
        goal_energy: Optional[float] = Field(
            default=None, description="Target calories."
        ),
        goal_protein: Optional[float] = Field(
            default=None, description="Target protein (g)."
        ),
        goal_carbohydrates: Optional[float] = Field(
            default=None, description="Target carbs (g)."
        ),
        goal_fat: Optional[float] = Field(default=None, description="Target fat (g)."),
    ) -> Any:
        """Create plan."""
        return get_client().create_nutrition_plan(
            description=description,
            goal_energy=goal_energy,
            goal_protein=goal_protein,
            goal_carbohydrates=goal_carbohydrates,
            goal_fat=goal_fat,
        )

    @mcp.tool(
        name="delete_nutrition_plan",
        description="Delete a nutrition plan.",
        tags={"Nutrition"},
    )
    def delete_nutrition_plan_tool(
        plan_id: int = Field(description="Plan ID."),
    ) -> Any:
        """Delete plan."""
        return get_client().delete_nutrition_plan(plan_id)

    @mcp.tool(
        name="create_meal",
        description="Create a meal in a nutrition plan.",
        tags={"Nutrition"},
    )
    def create_meal_tool(
        plan: int = Field(description="Nutrition plan ID."),
        name: str = Field(default="", description="Meal name."),
        time: str = Field(default="", description="Meal time (HH:MM)."),
    ) -> Any:
        """Create meal."""
        return get_client().create_meal(plan=plan, name=name, time=time)

    @mcp.tool(
        name="create_meal_item",
        description="Add an ingredient to a meal.",
        tags={"Nutrition"},
    )
    def create_meal_item_tool(
        meal: int = Field(description="Meal ID."),
        ingredient: int = Field(description="Ingredient ID."),
        amount: float = Field(description="Amount in grams."),
        weight_unit: Optional[int] = Field(
            default=None, description="Optional weight unit ID."
        ),
    ) -> Any:
        """Create meal item."""
        return get_client().create_meal_item(
            meal=meal, ingredient=ingredient, amount=amount, weight_unit=weight_unit
        )

    @mcp.tool(
        name="get_ingredients",
        description="List/search ingredients from the food database.",
        tags={"Nutrition"},
    )
    def get_ingredients_tool(
        limit: Optional[int] = Field(default=20, description="Max results."),
        offset: Optional[int] = Field(default=None, description="Offset."),
        language: Optional[int] = Field(default=None, description="Language ID."),
        name: Optional[str] = Field(default=None, description="Filter by name."),
    ) -> Any:
        """List ingredients."""
        filters = {}
        if language:
            filters["language"] = language
        if name:
            filters["name"] = name
        return get_client().get_ingredients(limit=limit, offset=offset, **filters)

    @mcp.tool(
        name="get_ingredient_info",
        description="Get detailed ingredient info including nutritional values and weight units.",
        tags={"Nutrition"},
    )
    def get_ingredient_info_tool(
        ingredient_id: int = Field(description="Ingredient ID."),
    ) -> Any:
        """Get ingredient info."""
        return get_client().get_ingredient_info(ingredient_id)

    @mcp.tool(
        name="get_nutrition_diary",
        description="List nutrition diary entries.",
        tags={"Nutrition"},
    )
    def get_nutrition_diary_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        ordering: Optional[str] = Field(default=None, description="Order by field."),
    ) -> Any:
        """List diary."""
        return get_client().get_nutrition_diary(limit=limit, ordering=ordering)

    @mcp.tool(
        name="log_nutrition",
        description="Log a nutrition diary entry (what was actually eaten).",
        tags={"Nutrition"},
    )
    def log_nutrition_tool(
        plan: int = Field(description="Nutrition plan ID."),
        ingredient: int = Field(description="Ingredient ID."),
        amount: float = Field(description="Amount in grams."),
        meal: Optional[int] = Field(default=None, description="Optional meal ID."),
    ) -> Any:
        """Log nutrition."""
        return get_client().create_nutrition_diary_entry(
            plan=plan, ingredient=ingredient, amount=amount, meal=meal
        )


def register_body_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_weight_entries",
        description="List body weight entries over time.",
        tags={"Body"},
    )
    def get_weight_entries_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        ordering: Optional[str] = Field(
            default=None, description="Order by field (e.g., '-date')."
        ),
    ) -> Any:
        """List weight entries."""
        return get_client().get_weight_entries(limit=limit, ordering=ordering)

    @mcp.tool(
        name="log_body_weight",
        description="Log a body weight entry.",
        tags={"Body"},
    )
    def log_body_weight_tool(
        date: str = Field(description="Date (YYYY-MM-DD)."),
        weight: float = Field(description="Body weight."),
    ) -> Any:
        """Log weight."""
        return get_client().create_weight_entry(date=date, weight=weight)

    @mcp.tool(
        name="delete_weight_entry",
        description="Delete a body weight entry.",
        tags={"Body"},
    )
    def delete_weight_entry_tool(
        entry_id: int = Field(description="Entry ID."),
    ) -> Any:
        """Delete weight entry."""
        return get_client().delete_weight_entry(entry_id)

    @mcp.tool(
        name="get_measurements",
        description="List body measurements (biceps, chest, waist, etc.).",
        tags={"Body"},
    )
    def get_measurements_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
        ordering: Optional[str] = Field(default=None, description="Order by field."),
    ) -> Any:
        """List measurements."""
        return get_client().get_measurements(limit=limit, ordering=ordering)

    @mcp.tool(
        name="log_measurement",
        description="Log a body measurement.",
        tags={"Body"},
    )
    def log_measurement_tool(
        category: int = Field(description="Measurement category ID."),
        date: str = Field(description="Date (YYYY-MM-DD)."),
        value: float = Field(description="Measurement value."),
    ) -> Any:
        """Log measurement."""
        return get_client().create_measurement(
            category=category, date=date, value=value
        )

    @mcp.tool(
        name="get_measurement_categories",
        description="List measurement categories (e.g., Biceps, Chest, Waist).",
        tags={"Body"},
    )
    def get_measurement_categories_tool(
        limit: Optional[int] = Field(default=100, description="Max results."),
    ) -> Any:
        """List categories."""
        return get_client().get_measurement_categories(limit=limit)

    @mcp.tool(
        name="create_measurement_category",
        description="Create a new measurement category.",
        tags={"Body"},
    )
    def create_measurement_category_tool(
        name: str = Field(description="Category name."),
        unit: str = Field(default="cm", description="Unit of measurement."),
    ) -> Any:
        """Create category."""
        return get_client().create_measurement_category(name=name, unit=unit)

    @mcp.tool(
        name="get_gallery",
        description="List progress gallery photos.",
        tags={"Body"},
    )
    def get_gallery_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
    ) -> Any:
        """List gallery."""
        return get_client().get_gallery(limit=limit)


def register_user_tools(mcp: FastMCP):
    @mcp.tool(
        name="get_user_profile",
        description="Get the authenticated user's profile (age, height, gender, etc.).",
        tags={"User"},
    )
    def get_user_profile_tool() -> Any:
        """Get profile."""
        return get_client().get_user_profile()

    @mcp.tool(
        name="get_user_statistics",
        description="Get user statistics (workout counts, etc.).",
        tags={"User"},
    )
    def get_user_statistics_tool() -> Any:
        """Get stats."""
        return get_client().get_user_statistics()

    @mcp.tool(
        name="get_user_trophies",
        description="List user's earned trophies/achievements.",
        tags={"User"},
    )
    def get_user_trophies_tool(
        limit: Optional[int] = Field(default=None, description="Max results."),
    ) -> Any:
        """List trophies."""
        return get_client().get_user_trophies(limit=limit)

    @mcp.tool(
        name="get_languages",
        description="List available languages.",
        tags={"User"},
    )
    def get_languages_tool() -> Any:
        """List languages."""
        return get_client().get_languages(limit=100)

    @mcp.tool(
        name="get_repetition_units",
        description="List repetition unit settings (e.g., Repetitions, Until failure, etc.).",
        tags={"User"},
    )
    def get_repetition_units_tool() -> Any:
        """List rep units."""
        return get_client().get_repetition_units(limit=100)

    @mcp.tool(
        name="get_weight_unit_settings",
        description="List weight unit settings (kg, lb, plates, etc.).",
        tags={"User"},
    )
    def get_weight_unit_settings_tool() -> Any:
        """List weight units."""
        return get_client().get_weight_unit_settings(limit=100)


def get_mcp_instance() -> tuple[Any, Any, Any, Any]:
    """Initialize and return the MCP instance, args, and middlewares."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="Wger MCP",
        version=__version__,
        instructions="Wger Workout Manager MCP Server - Manage exercises, routines, nutrition plans, body measurements, and workout logs.",
    )

    if to_boolean(os.getenv("ROUTINETOOL", "True")):
        register_routine_tools(mcp)
    if to_boolean(os.getenv("ROUTINECONFIGTOOL", "True")):
        register_routineconfig_tools(mcp)
    if to_boolean(os.getenv("EXERCISETOOL", "True")):
        register_exercise_tools(mcp)
    if to_boolean(os.getenv("WORKOUTTOOL", "True")):
        register_workout_tools(mcp)
    if to_boolean(os.getenv("NUTRITIONTOOL", "True")):
        register_nutrition_tools(mcp)
    if to_boolean(os.getenv("BODYTOOL", "True")):
        register_body_tools(mcp)
    if to_boolean(os.getenv("USERTOOL", "True")):
        register_user_tools(mcp)

    register_prompts(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    registered_tags = []
    return mcp, args, middlewares, registered_tags


def mcp_server() -> None:
    mcp, args, middlewares, registered_tags = get_mcp_instance()
    print(f"{args.name or 'wger-agent'} MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)
    print(f"  Dynamic Tags Loaded: {len(set(registered_tags))}", file=sys.stderr)

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
