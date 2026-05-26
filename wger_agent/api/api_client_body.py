#!/usr/bin/env python
from wger_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_weight_entries(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List body weight entries."""
        return self._list(
            "weightentry", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_weight_entry(self, entry_id: int) -> dict:
        """Get a specific weight entry."""
        return self._get(f"weightentry/{entry_id}")

    def create_weight_entry(self, date: str, weight: float) -> dict:
        """Log a body weight entry."""
        return self._post("weightentry", data={"date": date, "weight": str(weight)})

    def update_weight_entry(self, entry_id: int, **kwargs) -> dict:
        """Update a weight entry."""
        return self._patch(f"weightentry/{entry_id}", data=kwargs)

    def delete_weight_entry(self, entry_id: int) -> bool:
        """Delete a weight entry."""
        return self._delete(f"weightentry/{entry_id}")

    def get_measurements(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List body measurements."""
        return self._list(
            "measurement", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_measurement(self, measurement_id: int) -> dict:
        """Get a specific measurement."""
        return self._get(f"measurement/{measurement_id}")

    def create_measurement(self, category: int, date: str, value: float) -> dict:
        """Log a body measurement."""
        return self._post(
            "measurement",
            data={"category": category, "date": date, "value": str(value)},
        )

    def update_measurement(self, measurement_id: int, **kwargs) -> dict:
        """Update a measurement."""
        return self._patch(f"measurement/{measurement_id}", data=kwargs)

    def delete_measurement(self, measurement_id: int) -> bool:
        """Delete a measurement."""
        return self._delete(f"measurement/{measurement_id}")

    def get_measurement_categories(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List measurement categories (e.g., Biceps, Chest, etc.)."""
        return self._list("measurement-category", limit=limit, offset=offset)

    def get_measurement_category(self, category_id: int) -> dict:
        """Get a specific measurement category."""
        return self._get(f"measurement-category/{category_id}")

    def create_measurement_category(self, name: str, unit: str = "cm") -> dict:
        """Create a measurement category."""
        return self._post("measurement-category", data={"name": name, "unit": unit})

    def delete_measurement_category(self, category_id: int) -> bool:
        """Delete a measurement category."""
        return self._delete(f"measurement-category/{category_id}")

    def get_gallery(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
    ) -> dict:
        """List progress gallery images."""
        return self._list("gallery", limit=limit, offset=offset, ordering=ordering)
