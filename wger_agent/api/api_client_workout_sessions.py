#!/usr/bin/env python
from wger_agent.api.api_client_base import BaseApiClient


class Api(BaseApiClient):
    def get_workout_sessions(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List workout sessions."""
        return self._list(
            "workoutsession", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_workout_session(self, session_id: int) -> dict:
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
    ) -> dict:
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

    def update_workout_session(self, session_id: int, **kwargs) -> dict:
        """Update a workout session."""
        return self._patch(f"workoutsession/{session_id}", data=kwargs)

    def delete_workout_session(self, session_id: int) -> bool:
        """Delete a workout session."""
        return self._delete(f"workoutsession/{session_id}")

    def get_workout_logs(
        self,
        limit: int | None = None,
        offset: int | None = None,
        ordering: str | None = None,
        **filters,
    ) -> dict:
        """List workout logs."""
        return self._list(
            "workoutlog", limit=limit, offset=offset, ordering=ordering, **filters
        )

    def get_workout_log(self, log_id: int) -> dict:
        """Get a specific workout log."""
        return self._get(f"workoutlog/{log_id}")

    def create_workout_log(
        self,
        exercise: int,
        routine: int,
        date: str,
        repetitions: int = 0,
        weight: float = 0,
        rir: str | None = None,
        **kwargs,
    ) -> dict:
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

    def update_workout_log(self, log_id: int, **kwargs) -> dict:
        """Update a workout log."""
        return self._patch(f"workoutlog/{log_id}", data=kwargs)

    def delete_workout_log(self, log_id: int) -> bool:
        """Delete a workout log."""
        return self._delete(f"workoutlog/{log_id}")
