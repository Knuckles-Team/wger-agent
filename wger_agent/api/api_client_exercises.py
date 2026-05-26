#!/usr/bin/env python
from wger_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_exercises(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List exercises. Supports filters: language, category, muscles, equipment, etc."""
        return self._list(
            "exercise", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def search_exercises(self, term: str) -> dict:
        """Search exercises."""
        return self._get("exercise/search", params={"term": term})

    def get_exercise(self, exercise_id: int) -> dict:
        """Get a specific exercise."""
        return self._get(f"exercise/{exercise_id}")

    def get_exercise_info(self, exercise_id: int) -> dict:
        """Get detailed exercise info (includes translations, images, muscles, etc.)."""
        return self._get(f"exerciseinfo/{exercise_id}")

    def get_exercise_infos(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List exercise infos."""
        return self._list(
            "exerciseinfo", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_exercise_translations(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List exercise translations."""
        return self._list("exercise-translation", limit=limit, offset=offset, **filters)

    def get_exercise_categories(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List exercise categories (e.g., Arms, Legs, etc.)."""
        return self._list("exercisecategory", limit=limit, offset=offset)

    def get_exercise_category(self, category_id: int) -> dict:
        """Get a specific exercise category."""
        return self._get(f"exercisecategory/{category_id}")

    def get_equipment(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List equipment (e.g., Barbell, Dumbbell, etc.)."""
        return self._list("equipment", limit=limit, offset=offset)

    def get_equipment_item(self, equipment_id: int) -> dict:
        """Get a specific equipment."""
        return self._get(f"equipment/{equipment_id}")

    def get_muscles(self, limit: int | None = None, offset: int | None = None) -> dict:
        """List muscles."""
        return self._list("muscle", limit=limit, offset=offset)

    def get_muscle(self, muscle_id: int) -> dict:
        """Get a specific muscle."""
        return self._get(f"muscle/{muscle_id}")

    def get_exercise_images(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List exercise images."""
        return self._list("exerciseimage", limit=limit, offset=offset, **filters)

    def get_exercise_image(self, image_id: int) -> dict:
        """Get a specific exercise image."""
        return self._get(f"exerciseimage/{image_id}")

    def get_exercise_videos(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List exercise videos."""
        return self._list("video", limit=limit, offset=offset, **filters)

    def get_exercise_comments(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List exercise comments."""
        return self._list("exercisecomment", limit=limit, offset=offset, **filters)

    def get_exercise_aliases(
        self, limit: int | None = None, offset: int | None = None, **filters
    ) -> dict:
        """List exercise aliases."""
        return self._list("exercisealias", limit=limit, offset=offset, **filters)

    def get_variations(
        self, limit: int | None = None, offset: int | None = None
    ) -> dict:
        """List exercise variations."""
        return self._list("variation", limit=limit, offset=offset)
