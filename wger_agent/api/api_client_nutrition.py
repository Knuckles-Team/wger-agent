#!/usr/bin/env python
from wger_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_nutrition_plans(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List nutrition plans."""
        return self._list("nutritionplan", limit=limit, offset=offset, **filters)

    def get_nutrition_plan(self, plan_id: int) -> dict:
        """Get a specific nutrition plan."""
        return self._get(f"nutritionplan/{plan_id}")

    def get_nutrition_plan_info(self, plan_id: int) -> dict:
        """Get detailed nutrition plan info (includes meals, items, nutritional values)."""
        return self._get(f"nutritionplaninfo/{plan_id}")

    def create_nutrition_plan(
        self,
        description: str = "",
        only_logging: bool = False,
        goal_energy: float | None = None,
        goal_protein: float | None = None,
        goal_carbohydrates: float | None = None,
        goal_fat: float | None = None,
        _goal_fiber: float | None = None,
    ) -> dict:
        """Create a nutrition plan."""
        data: dict[str, object] = {
            "description": description,
            "only_logging": only_logging,
        }
        if goal_energy is not None:
            data["goal_energy"] = goal_energy
        if goal_protein is not None:
            data["goal_protein"] = goal_protein
        if goal_carbohydrates is not None:
            data["goal_carbohydrates"] = goal_carbohydrates
        if goal_fat is not None:
            data["goal_fat"] = goal_fat
        if _goal_fiber is not None:
            data["_goal_fiber"] = _goal_fiber
        return self._post("nutritionplan", data=data)

    def update_nutrition_plan(self, plan_id: int, **kwargs) -> dict:
        """Update a nutrition plan."""
        return self._patch(f"nutritionplan/{plan_id}", data=kwargs)

    def delete_nutrition_plan(self, plan_id: int) -> bool:
        """Delete a nutrition plan."""
        return self._delete(f"nutritionplan/{plan_id}")

    def get_meals(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List meals."""
        return self._list("meal", limit=limit, offset=offset, **filters)

    def get_meal(self, meal_id: int) -> dict:
        """Get a specific meal."""
        return self._get(f"meal/{meal_id}")

    def create_meal(
        self, plan: int, name: str = "", time: str = "", order: int = 1
    ) -> dict:
        """Create a meal in a nutrition plan."""
        data = {"plan": plan, "name": name, "order": order}
        if time:
            data["time"] = time
        return self._post("meal", data=data)

    def update_meal(self, meal_id: int, **kwargs) -> dict:
        """Update a meal."""
        return self._patch(f"meal/{meal_id}", data=kwargs)

    def delete_meal(self, meal_id: int) -> bool:
        """Delete a meal."""
        return self._delete(f"meal/{meal_id}")

    def get_meal_items(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List meal items."""
        return self._list("mealitem", limit=limit, offset=offset, **filters)

    def get_meal_item(self, item_id: int) -> dict:
        """Get a specific meal item."""
        return self._get(f"mealitem/{item_id}")

    def create_meal_item(
        self,
        meal: int,
        ingredient: int,
        amount: float,
        weight_unit: int | None = None,
    ) -> dict:
        """Add an ingredient to a meal."""
        data = {"meal": meal, "ingredient": ingredient, "amount": str(amount)}
        if weight_unit:
            data["weight_unit"] = weight_unit
        return self._post("mealitem", data=data)

    def update_meal_item(self, item_id: int, **kwargs) -> dict:
        """Update a meal item."""
        return self._patch(f"mealitem/{item_id}", data=kwargs)

    def delete_meal_item(self, item_id: int) -> bool:
        """Delete a meal item."""
        return self._delete(f"mealitem/{item_id}")

    def get_ingredients(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List ingredients. Supports filters: language, name, etc."""
        return self._list(
            "ingredient", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_ingredient(self, ingredient_id: int) -> dict:
        """Get a specific ingredient."""
        return self._get(f"ingredient/{ingredient_id}")

    def get_ingredient_info(self, ingredient_id: int) -> dict:
        """Get detailed ingredient info (includes weight units)."""
        return self._get(f"ingredientinfo/{ingredient_id}")

    def get_ingredient_weight_units(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List ingredient weight units."""
        return self._list("ingredientweightunit", limit=limit, offset=offset, **filters)

    def get_weight_units(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List weight units."""
        return self._list("weightunit", limit=limit, offset=offset)

    def get_nutrition_diary(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List nutrition diary entries."""
        return self._list(
            "nutritiondiary", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def create_nutrition_diary_entry(
        self,
        plan: int,
        ingredient: int,
        amount: float,
        meal: int | None = None,
        weight_unit: int | None = None,
    ) -> dict:
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
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List ingredient images."""
        return self._list("ingredient-image", limit=limit, offset=offset, **filters)
