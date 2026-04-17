#!/usr/bin/python

"""
Wger API Wrapper — Complete REST client for the wger Workout Manager API v2.

Covers all 52 endpoints across 7 domains:
  Routine, RoutineConfig, Exercise, Workout, Nutrition, Body, User.

Authentication: Bearer token (JWT access token) or permanent Token header.
Pagination: All list methods support `limit` and `offset`.
Filtering: All list methods support `ordering` and domain-specific filters via `**filters`.
"""

import logging
from typing import Any, Dict, Optional

import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


class WgerApi:
    """REST client for the wger Workout Manager API v2."""

    def __init__(
        self,
        base_url: str = "https://wger.de",
        token: str = "",
        verify: bool = True,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_base = f"{self.base_url}/api/v2"
        self.session = requests.Session()
        self.session.verify = verify
        if token:
            self.session.headers.update({"Authorization": f"Token {token}"})
        self.session.headers.update({"Accept": "application/json"})

        try:

            response = self.session.get(f"{self.api_base}/workout/")
            if response.status_code == 401:
                from agent_utilities.exceptions import AuthError

                raise AuthError("Wger authentication failed: Invalid API key.")
            elif response.status_code == 403:
                from agent_utilities.exceptions import UnauthorizedError

                raise UnauthorizedError(
                    "Wger access forbidden: Insufficient permissions."
                )
            response.raise_for_status()
        except Exception as e:
            if isinstance(e, (AuthError, UnauthorizedError)):
                raise e

            pass

    def _url(self, endpoint: str) -> str:
        return f"{self.api_base}/{endpoint.strip('/')}/"

    def _get(self, endpoint: str, params: Optional[Dict] = None) -> Any:
        resp = self.session.get(self._url(endpoint), params=params)
        resp.raise_for_status()
        return resp.json()

    def _post(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        resp = self.session.post(self._url(endpoint), json=data)
        resp.raise_for_status()
        return resp.json()

    def _put(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        resp = self.session.put(self._url(endpoint), json=data)
        resp.raise_for_status()
        return resp.json()

    def _patch(self, endpoint: str, data: Optional[Dict] = None) -> Any:
        resp = self.session.patch(self._url(endpoint), json=data)
        resp.raise_for_status()
        return resp.json()

    def _delete(self, endpoint: str) -> bool:
        resp = self.session.delete(self._url(endpoint))
        resp.raise_for_status()
        return True

    def _list(
        self,
        endpoint: str,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        params = {k: v for k, v in filters.items() if v is not None}
        if limit is not None:
            params["limit"] = limit
        if offset is not None:
            params["offset"] = offset
        if ordering:
            params["ordering"] = ordering
        return self._get(endpoint, params=params)

    def get_routines(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List all routines."""
        return self._list(
            "routine", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_routine(self, routine_id: int) -> Dict:
        """Get a specific routine by ID."""
        return self._get(f"routine/{routine_id}")

    def create_routine(
        self,
        name: str,
        description: str = "",
        start_date: str = "",
        end_date: str = "",
        fit_in_week: bool = False,
    ) -> Dict:
        """Create a new routine."""
        data = {"name": name, "description": description, "fit_in_week": fit_in_week}
        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        return self._post("routine", data=data)

    def update_routine(self, routine_id: int, **kwargs) -> Dict:
        """Update a routine."""
        return self._patch(f"routine/{routine_id}", data=kwargs)

    def delete_routine(self, routine_id: int) -> bool:
        """Delete a routine."""
        return self._delete(f"routine/{routine_id}")

    def get_templates(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List user's workout templates."""
        return self._list("templates", limit=limit, offset=offset, **filters)

    def get_template(self, template_id: int) -> Dict:
        """Get a specific template."""
        return self._get(f"templates/{template_id}")

    def get_public_templates(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List public workout templates."""
        return self._list("public-templates", limit=limit, offset=offset, **filters)

    def get_days(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List all workout days."""
        return self._list(
            "day", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_day(self, day_id: int) -> Dict:
        """Get a specific day."""
        return self._get(f"day/{day_id}")

    def create_day(
        self,
        routine: int,
        name: str = "",
        description: str = "",
        is_rest: bool = False,
        order: int = 1,
        day_type: str = "custom",
        need_logs_to_advance: bool = False,
    ) -> Dict:
        """Create a workout day in a routine."""
        data = {
            "routine": routine,
            "name": name,
            "description": description,
            "is_rest": is_rest,
            "order": order,
            "type": day_type,
            "need_logs_to_advance": need_logs_to_advance,
        }
        return self._post("day", data=data)

    def update_day(self, day_id: int, **kwargs) -> Dict:
        """Update a day."""
        return self._patch(f"day/{day_id}", data=kwargs)

    def delete_day(self, day_id: int) -> bool:
        """Delete a day."""
        return self._delete(f"day/{day_id}")

    def get_slots(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List all slots (sets)."""
        return self._list("slot", limit=limit, offset=offset, **filters)

    def get_slot(self, slot_id: int) -> Dict:
        """Get a specific slot."""
        return self._get(f"slot/{slot_id}")

    def create_slot(
        self, day: int, order: int = 1, slot_type: str = "normal", **kwargs
    ) -> Dict:
        """Create a slot (set) in a day."""
        data = {"day": day, "order": order, "type": slot_type, **kwargs}
        return self._post("slot", data=data)

    def update_slot(self, slot_id: int, **kwargs) -> Dict:
        """Update a slot."""
        return self._patch(f"slot/{slot_id}", data=kwargs)

    def delete_slot(self, slot_id: int) -> bool:
        """Delete a slot."""
        return self._delete(f"slot/{slot_id}")

    def get_slot_entries(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List all slot entries."""
        return self._list("slot-entry", limit=limit, offset=offset, **filters)

    def get_slot_entry(self, entry_id: int) -> Dict:
        """Get a specific slot entry."""
        return self._get(f"slot-entry/{entry_id}")

    def create_slot_entry(
        self, slot: int, exercise: int, order: int = 1, **kwargs
    ) -> Dict:
        """Create a slot entry (add exercise to slot)."""
        data = {"slot": slot, "exercise": exercise, "order": order, **kwargs}
        return self._post("slot-entry", data=data)

    def update_slot_entry(self, entry_id: int, **kwargs) -> Dict:
        """Update a slot entry."""
        return self._patch(f"slot-entry/{entry_id}", data=kwargs)

    def delete_slot_entry(self, entry_id: int) -> bool:
        """Delete a slot entry."""
        return self._delete(f"slot-entry/{entry_id}")

    def _config_crud(
        self,
        config_type: str,
        config_id: Optional[int] = None,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        **kwargs,
    ):
        """Generic CRUD for config endpoints (weight, reps, sets, rest, rir)."""
        if config_id and not kwargs:
            return self._get(f"{config_type}/{config_id}")
        elif config_id and kwargs.get("_delete"):
            return self._delete(f"{config_type}/{config_id}")
        elif config_id:
            return self._patch(f"{config_type}/{config_id}", data=kwargs)
        elif kwargs:
            return self._post(config_type, data=kwargs)
        else:
            return self._list(config_type, limit=limit, offset=offset)

    def get_weight_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List weight progression configs."""
        return self._list("weight-config", limit=limit, offset=offset, **filters)

    def get_weight_config(self, config_id: int) -> Dict:
        """Get a specific weight config."""
        return self._get(f"weight-config/{config_id}")

    def create_weight_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> Dict:
        """Create a weight progression config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("weight-config", data=data)

    def update_weight_config(self, config_id: int, **kwargs) -> Dict:
        """Update a weight config."""
        return self._patch(f"weight-config/{config_id}", data=kwargs)

    def delete_weight_config(self, config_id: int) -> bool:
        """Delete a weight config."""
        return self._delete(f"weight-config/{config_id}")

    def get_max_weight_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List max weight configs."""
        return self._list("max-weight-config", limit=limit, offset=offset, **filters)

    def create_max_weight_config(self, slot_entry: int, **kwargs) -> Dict:
        """Create a max weight config."""
        return self._post(
            "max-weight-config", data={"slot_entry": slot_entry, **kwargs}
        )

    def get_repetitions_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List repetitions configs."""
        return self._list("repetitions-config", limit=limit, offset=offset, **filters)

    def create_repetitions_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> Dict:
        """Create a repetitions config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("repetitions-config", data=data)

    def update_repetitions_config(self, config_id: int, **kwargs) -> Dict:
        """Update a repetitions config."""
        return self._patch(f"repetitions-config/{config_id}", data=kwargs)

    def delete_repetitions_config(self, config_id: int) -> bool:
        """Delete a repetitions config."""
        return self._delete(f"repetitions-config/{config_id}")

    def get_max_repetitions_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List max repetitions configs."""
        return self._list(
            "max-repetitions-config", limit=limit, offset=offset, **filters
        )

    def create_max_repetitions_config(self, slot_entry: int, **kwargs) -> Dict:
        """Create a max repetitions config."""
        return self._post(
            "max-repetitions-config", data={"slot_entry": slot_entry, **kwargs}
        )

    def get_sets_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List sets configs."""
        return self._list("sets-config", limit=limit, offset=offset, **filters)

    def create_sets_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> Dict:
        """Create a sets config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("sets-config", data=data)

    def update_sets_config(self, config_id: int, **kwargs) -> Dict:
        """Update a sets config."""
        return self._patch(f"sets-config/{config_id}", data=kwargs)

    def delete_sets_config(self, config_id: int) -> bool:
        """Delete a sets config."""
        return self._delete(f"sets-config/{config_id}")

    def get_max_sets_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List max sets configs."""
        return self._list("max-sets-config", limit=limit, offset=offset, **filters)

    def create_max_sets_config(self, slot_entry: int, **kwargs) -> Dict:
        """Create a max sets config."""
        return self._post("max-sets-config", data={"slot_entry": slot_entry, **kwargs})

    def get_rest_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List rest time configs."""
        return self._list("rest-config", limit=limit, offset=offset, **filters)

    def create_rest_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> Dict:
        """Create a rest time config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("rest-config", data=data)

    def update_rest_config(self, config_id: int, **kwargs) -> Dict:
        """Update a rest config."""
        return self._patch(f"rest-config/{config_id}", data=kwargs)

    def delete_rest_config(self, config_id: int) -> bool:
        """Delete a rest config."""
        return self._delete(f"rest-config/{config_id}")

    def get_max_rest_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List max rest configs."""
        return self._list("max-rest-config", limit=limit, offset=offset, **filters)

    def create_max_rest_config(self, slot_entry: int, **kwargs) -> Dict:
        """Create a max rest config."""
        return self._post("max-rest-config", data={"slot_entry": slot_entry, **kwargs})

    def get_rir_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List RiR configs."""
        return self._list("rir-config", limit=limit, offset=offset, **filters)

    def create_rir_config(
        self,
        slot_entry: int,
        iteration: int = 1,
        value: float = 0,
        operation: str = "r",
        step: str = "abs",
        repeat: bool = False,
        **kwargs,
    ) -> Dict:
        """Create a RiR config."""
        data = {
            "slot_entry": slot_entry,
            "iteration": iteration,
            "value": value,
            "operation": operation,
            "step": step,
            "repeat": repeat,
            **kwargs,
        }
        return self._post("rir-config", data=data)

    def update_rir_config(self, config_id: int, **kwargs) -> Dict:
        """Update a RiR config."""
        return self._patch(f"rir-config/{config_id}", data=kwargs)

    def delete_rir_config(self, config_id: int) -> bool:
        """Delete a RiR config."""
        return self._delete(f"rir-config/{config_id}")

    def get_max_rir_configs(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List max RiR configs."""
        return self._list("max-rir-config", limit=limit, offset=offset, **filters)

    def create_max_rir_config(self, slot_entry: int, **kwargs) -> Dict:
        """Create a max RiR config."""
        return self._post("max-rir-config", data={"slot_entry": slot_entry, **kwargs})

    def get_exercises(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List exercises. Supports filters: language, category, muscles, equipment, etc."""
        return self._list(
            "exercise", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_exercise(self, exercise_id: int) -> Dict:
        """Get a specific exercise."""
        return self._get(f"exercise/{exercise_id}")

    def get_exercise_info(self, exercise_id: int) -> Dict:
        """Get detailed exercise info (includes translations, images, muscles, etc.)."""
        return self._get(f"exerciseinfo/{exercise_id}")

    def get_exercise_infos(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List exercise infos."""
        return self._list(
            "exerciseinfo", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_exercise_translations(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List exercise translations."""
        return self._list("exercise-translation", limit=limit, offset=offset, **filters)

    def get_exercise_categories(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List exercise categories (e.g., Arms, Legs, etc.)."""
        return self._list("exercisecategory", limit=limit, offset=offset)

    def get_exercise_category(self, category_id: int) -> Dict:
        """Get a specific exercise category."""
        return self._get(f"exercisecategory/{category_id}")

    def get_equipment(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List equipment (e.g., Barbell, Dumbbell, etc.)."""
        return self._list("equipment", limit=limit, offset=offset)

    def get_equipment_item(self, equipment_id: int) -> Dict:
        """Get a specific equipment."""
        return self._get(f"equipment/{equipment_id}")

    def get_muscles(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List muscles."""
        return self._list("muscle", limit=limit, offset=offset)

    def get_muscle(self, muscle_id: int) -> Dict:
        """Get a specific muscle."""
        return self._get(f"muscle/{muscle_id}")

    def get_exercise_images(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List exercise images."""
        return self._list("exerciseimage", limit=limit, offset=offset, **filters)

    def get_exercise_image(self, image_id: int) -> Dict:
        """Get a specific exercise image."""
        return self._get(f"exerciseimage/{image_id}")

    def get_exercise_videos(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List exercise videos."""
        return self._list("video", limit=limit, offset=offset, **filters)

    def get_exercise_comments(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List exercise comments."""
        return self._list("exercisecomment", limit=limit, offset=offset, **filters)

    def get_exercise_aliases(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List exercise aliases."""
        return self._list("exercisealias", limit=limit, offset=offset, **filters)

    def get_variations(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List exercise variations."""
        return self._list("variation", limit=limit, offset=offset)

    def get_workout_sessions(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List workout sessions."""
        return self._list(
            "workoutsession", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_workout_session(self, session_id: int) -> Dict:
        """Get a specific workout session."""
        return self._get(f"workoutsession/{session_id}")

    def create_workout_session(
        self,
        routine: int,
        date: str,
        impression: str = "3",
        notes: str = "",
        time_start: str = "",
        time_end: str = "",
    ) -> Dict:
        """Create a workout session. Impression: 1=General discomfort, 2=Could be better, 3=Neutral, 4=Good, 5=Perfect."""
        data = {
            "routine": routine,
            "date": date,
            "impression": impression,
            "notes": notes,
        }
        if time_start:
            data["time_start"] = time_start
        if time_end:
            data["time_end"] = time_end
        return self._post("workoutsession", data=data)

    def update_workout_session(self, session_id: int, **kwargs) -> Dict:
        """Update a workout session."""
        return self._patch(f"workoutsession/{session_id}", data=kwargs)

    def delete_workout_session(self, session_id: int) -> bool:
        """Delete a workout session."""
        return self._delete(f"workoutsession/{session_id}")

    def get_workout_logs(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List workout logs."""
        return self._list(
            "workoutlog", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_workout_log(self, log_id: int) -> Dict:
        """Get a specific workout log."""
        return self._get(f"workoutlog/{log_id}")

    def create_workout_log(
        self,
        exercise: int,
        routine: int,
        date: str,
        repetitions: int = 0,
        weight: float = 0,
        rir: Optional[str] = None,
        **kwargs,
    ) -> Dict:
        """Create a workout log entry."""
        data = {
            "exercise": exercise,
            "routine": routine,
            "date": date,
            "repetitions": repetitions,
            "weight": str(weight),
            **kwargs,
        }
        if rir is not None:
            data["rir"] = rir
        return self._post("workoutlog", data=data)

    def update_workout_log(self, log_id: int, **kwargs) -> Dict:
        """Update a workout log."""
        return self._patch(f"workoutlog/{log_id}", data=kwargs)

    def delete_workout_log(self, log_id: int) -> bool:
        """Delete a workout log."""
        return self._delete(f"workoutlog/{log_id}")

    def get_nutrition_plans(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List nutrition plans."""
        return self._list("nutritionplan", limit=limit, offset=offset, **filters)

    def get_nutrition_plan(self, plan_id: int) -> Dict:
        """Get a specific nutrition plan."""
        return self._get(f"nutritionplan/{plan_id}")

    def get_nutrition_plan_info(self, plan_id: int) -> Dict:
        """Get detailed nutrition plan info (includes meals, items, nutritional values)."""
        return self._get(f"nutritionplaninfo/{plan_id}")

    def create_nutrition_plan(
        self,
        description: str = "",
        only_logging: bool = False,
        goal_energy: Optional[float] = None,
        goal_protein: Optional[float] = None,
        goal_carbohydrates: Optional[float] = None,
        goal_fat: Optional[float] = None,
        _goal_fiber: Optional[float] = None,
    ) -> Dict:
        """Create a nutrition plan."""
        data = {"description": description, "only_logging": only_logging}
        for field in [
            "goal_energy",
            "goal_protein",
            "goal_carbohydrates",
            "goal_fat",
            "_goal_fiber",
        ]:
            val = locals()[field]
            if val is not None:
                data[field] = val
        return self._post("nutritionplan", data=data)

    def update_nutrition_plan(self, plan_id: int, **kwargs) -> Dict:
        """Update a nutrition plan."""
        return self._patch(f"nutritionplan/{plan_id}", data=kwargs)

    def delete_nutrition_plan(self, plan_id: int) -> bool:
        """Delete a nutrition plan."""
        return self._delete(f"nutritionplan/{plan_id}")

    def get_meals(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List meals."""
        return self._list("meal", limit=limit, offset=offset, **filters)

    def get_meal(self, meal_id: int) -> Dict:
        """Get a specific meal."""
        return self._get(f"meal/{meal_id}")

    def create_meal(
        self, plan: int, name: str = "", time: str = "", order: int = 1
    ) -> Dict:
        """Create a meal in a nutrition plan."""
        data = {"plan": plan, "name": name, "order": order}
        if time:
            data["time"] = time
        return self._post("meal", data=data)

    def update_meal(self, meal_id: int, **kwargs) -> Dict:
        """Update a meal."""
        return self._patch(f"meal/{meal_id}", data=kwargs)

    def delete_meal(self, meal_id: int) -> bool:
        """Delete a meal."""
        return self._delete(f"meal/{meal_id}")

    def get_meal_items(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List meal items."""
        return self._list("mealitem", limit=limit, offset=offset, **filters)

    def get_meal_item(self, item_id: int) -> Dict:
        """Get a specific meal item."""
        return self._get(f"mealitem/{item_id}")

    def create_meal_item(
        self,
        meal: int,
        ingredient: int,
        amount: float,
        weight_unit: Optional[int] = None,
    ) -> Dict:
        """Add an ingredient to a meal."""
        data = {"meal": meal, "ingredient": ingredient, "amount": str(amount)}
        if weight_unit:
            data["weight_unit"] = weight_unit
        return self._post("mealitem", data=data)

    def update_meal_item(self, item_id: int, **kwargs) -> Dict:
        """Update a meal item."""
        return self._patch(f"mealitem/{item_id}", data=kwargs)

    def delete_meal_item(self, item_id: int) -> bool:
        """Delete a meal item."""
        return self._delete(f"mealitem/{item_id}")

    def get_ingredients(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List ingredients. Supports filters: language, name, etc."""
        return self._list(
            "ingredient", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_ingredient(self, ingredient_id: int) -> Dict:
        """Get a specific ingredient."""
        return self._get(f"ingredient/{ingredient_id}")

    def get_ingredient_info(self, ingredient_id: int) -> Dict:
        """Get detailed ingredient info (includes weight units)."""
        return self._get(f"ingredientinfo/{ingredient_id}")

    def get_ingredient_weight_units(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List ingredient weight units."""
        return self._list("ingredientweightunit", limit=limit, offset=offset, **filters)

    def get_weight_units(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List weight units."""
        return self._list("weightunit", limit=limit, offset=offset)

    def get_nutrition_diary(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List nutrition diary entries."""
        return self._list(
            "nutritiondiary", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def create_nutrition_diary_entry(
        self,
        plan: int,
        ingredient: int,
        amount: float,
        meal: Optional[int] = None,
        weight_unit: Optional[int] = None,
    ) -> Dict:
        """Log a nutrition diary entry."""
        data = {"plan": plan, "ingredient": ingredient, "amount": str(amount)}
        if meal:
            data["meal"] = meal
        if weight_unit:
            data["weight_unit"] = weight_unit
        return self._post("nutritiondiary", data=data)

    def delete_nutrition_diary_entry(self, entry_id: int) -> bool:
        """Delete a nutrition diary entry."""
        return self._delete(f"nutritiondiary/{entry_id}")

    def get_ingredient_images(
        self, limit: Optional[int] = None, offset: Optional[int] = None, **filters
    ) -> Dict:
        """List ingredient images."""
        return self._list("ingredient-image", limit=limit, offset=offset, **filters)

    def get_weight_entries(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List body weight entries."""
        return self._list(
            "weightentry", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_weight_entry(self, entry_id: int) -> Dict:
        """Get a specific weight entry."""
        return self._get(f"weightentry/{entry_id}")

    def create_weight_entry(self, date: str, weight: float) -> Dict:
        """Log a body weight entry."""
        return self._post("weightentry", data={"date": date, "weight": str(weight)})

    def update_weight_entry(self, entry_id: int, **kwargs) -> Dict:
        """Update a weight entry."""
        return self._patch(f"weightentry/{entry_id}", data=kwargs)

    def delete_weight_entry(self, entry_id: int) -> bool:
        """Delete a weight entry."""
        return self._delete(f"weightentry/{entry_id}")

    def get_measurements(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
        **filters,
    ) -> Dict:
        """List body measurements."""
        return self._list(
            "measurement", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_measurement(self, measurement_id: int) -> Dict:
        """Get a specific measurement."""
        return self._get(f"measurement/{measurement_id}")

    def create_measurement(self, category: int, date: str, value: float) -> Dict:
        """Log a body measurement."""
        return self._post(
            "measurement",
            data={"category": category, "date": date, "value": str(value)},
        )

    def update_measurement(self, measurement_id: int, **kwargs) -> Dict:
        """Update a measurement."""
        return self._patch(f"measurement/{measurement_id}", data=kwargs)

    def delete_measurement(self, measurement_id: int) -> bool:
        """Delete a measurement."""
        return self._delete(f"measurement/{measurement_id}")

    def get_measurement_categories(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List measurement categories (e.g., Biceps, Chest, etc.)."""
        return self._list("measurement-category", limit=limit, offset=offset)

    def get_measurement_category(self, category_id: int) -> Dict:
        """Get a specific measurement category."""
        return self._get(f"measurement-category/{category_id}")

    def create_measurement_category(self, name: str, unit: str = "cm") -> Dict:
        """Create a measurement category."""
        return self._post("measurement-category", data={"name": name, "unit": unit})

    def delete_measurement_category(self, category_id: int) -> bool:
        """Delete a measurement category."""
        return self._delete(f"measurement-category/{category_id}")

    def get_gallery(
        self,
        limit: Optional[int] = None,
        offset: Optional[int] = None,
        ordering: Optional[str] = None,
    ) -> Dict:
        """List progress gallery images."""
        return self._list("gallery", limit=limit, offset=offset, ordering=ordering)

    def get_user_profile(self) -> Dict:
        """Get the current user's profile."""
        result = self._get("userprofile")
        if isinstance(result, dict) and "results" in result:
            return result["results"][0] if result["results"] else result
        return result

    def update_user_profile(self, **kwargs) -> Dict:
        """Update user profile. Fields: age, height, gender, etc."""
        profile = self.get_user_profile()
        if "id" in profile:
            return self._patch(f"userprofile/{profile['id']}", data=kwargs)
        return self._patch("userprofile", data=kwargs)

    def get_user_statistics(self) -> Dict:
        """Get user statistics (workout count, etc.)."""
        return self._get("user-statistics")

    def get_trophies(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List available trophies."""
        return self._list("trophy", limit=limit, offset=offset)

    def get_user_trophies(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List user's earned trophies."""
        return self._list("user-trophy", limit=limit, offset=offset)

    def get_languages(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List available languages."""
        return self._list("language", limit=limit, offset=offset)

    def get_licenses(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List content licenses."""
        return self._list("license", limit=limit, offset=offset)

    def get_deletion_log(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List deletion log entries."""
        return self._list("deletion-log", limit=limit, offset=offset)

    def get_repetition_units(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List repetition unit settings."""
        return self._list("setting-repetitionunit", limit=limit, offset=offset)

    def get_weight_unit_settings(
        self, limit: Optional[int] = None, offset: Optional[int] = None
    ) -> Dict:
        """List weight unit settings."""
        return self._list("setting-weightunit", limit=limit, offset=offset)
