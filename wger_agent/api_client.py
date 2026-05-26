#!/usr/bin/env python

from wger_agent.api.api_client_body import Api as BodyApi
from wger_agent.api.api_client_configs import Api as ConfigsApi
from wger_agent.api.api_client_exercises import Api as ExercisesApi
from wger_agent.api.api_client_nutrition import Api as NutritionApi
from wger_agent.api.api_client_routine import Api as RoutineApi
from wger_agent.api.api_client_user_system import Api as UserSystemApi
from wger_agent.api.api_client_workout_sessions import Api as WorkoutSessionsApi


class WgerApi(
    RoutineApi,
    ConfigsApi,
    ExercisesApi,
    WorkoutSessionsApi,
    NutritionApi,
    BodyApi,
    UserSystemApi,
):
    """Unified Api client for wger, composed of domain-specific sub-clients."""

    pass
