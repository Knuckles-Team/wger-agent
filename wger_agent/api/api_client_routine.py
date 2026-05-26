#!/usr/bin/env python
from wger_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_routines(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List all routines."""
        return self._list(
            "routine", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_routine(self, routine_id: int) -> dict:
        """Get a specific routine by ID."""
        return self._get(f"routine/{routine_id}")

    def create_routine(
        self,
        name: str,
        description: str = "",
        start_date: str = "",
        end_date: str = "",
        fit_in_week: bool = False,
    ) -> dict:
        """Create a new routine."""
        data = {"name": name, "description": description, "fit_in_week": fit_in_week}
        if start_date:
            data["start_date"] = start_date
        if end_date:
            data["end_date"] = end_date
        return self._post("routine", data=data)

    def update_routine(self, routine_id: int, **kwargs) -> dict:
        """Update a routine."""
        return self._patch(f"routine/{routine_id}", data=kwargs)

    def delete_routine(self, routine_id: int) -> bool:
        """Delete a routine."""
        return self._delete(f"routine/{routine_id}")

    def get_templates(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List user's workout templates."""
        return self._list("templates", limit=limit, offset=offset, **filters)

    def get_template(self, template_id: int) -> dict:
        """Get a specific template."""
        return self._get(f"templates/{template_id}")

    def get_public_templates(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List public workout templates."""
        return self._list("public-templates", limit=limit, offset=offset, **filters)

    def get_days(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List all workout days."""
        return self._list(
            "day", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_day(self, day_id: int) -> dict:
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
    ) -> dict:
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

    def update_day(self, day_id: int, **kwargs) -> dict:
        """Update a day."""
        return self._patch(f"day/{day_id}", data=kwargs)

    def delete_day(self, day_id: int) -> bool:
        """Delete a day."""
        return self._delete(f"day/{day_id}")

    def get_slots(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List all slots (sets)."""
        return self._list("slot", limit=limit, offset=offset, **filters)

    def get_slot(self, slot_id: int) -> dict:
        """Get a specific slot."""
        return self._get(f"slot/{slot_id}")

    def create_slot(
        self, day: int, order: int = 1, slot_type: str = "normal", **kwargs
    ) -> dict:
        """Create a slot (set) in a day."""
        data = {"day": day, "order": order, "type": slot_type, **kwargs}
        return self._post("slot", data=data)

    def update_slot(self, slot_id: int, **kwargs) -> dict:
        """Update a slot."""
        return self._patch(f"slot/{slot_id}", data=kwargs)

    def delete_slot(self, slot_id: int) -> bool:
        """Delete a slot."""
        return self._delete(f"slot/{slot_id}")

    def get_slot_entries(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List all slot entries."""
        return self._list("slot-entry", limit=limit, offset=offset, **filters)

    def get_slot_entry(self, entry_id: int) -> dict:
        """Get a specific slot entry."""
        return self._get(f"slot-entry/{entry_id}")

    def create_slot_entry(
        self, slot: int, exercise: int, order: int = 1, **kwargs
    ) -> dict:
        """Create a slot entry (add exercise to slot)."""
        data = {"slot": slot, "exercise": exercise, "order": order, **kwargs}
        return self._post("slot-entry", data=data)

    def update_slot_entry(self, entry_id: int, **kwargs) -> dict:
        """Update a slot entry."""
        return self._patch(f"slot-entry/{entry_id}", data=kwargs)

    def delete_slot_entry(self, entry_id: int) -> bool:
        """Delete a slot entry."""
        return self._delete(f"slot-entry/{entry_id}")
