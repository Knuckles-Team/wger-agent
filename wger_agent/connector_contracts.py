"""Surface contracts: tool use, links, data locations and business roles."""

from scion_sdk.surface_contracts import (
    BusinessRole,
    DataLocation,
    Refusal,
    SurfaceLink,
    ToolStep,
    ToolUseContract,
)

CONTRACTS = (
    ToolUseContract(
        "find-an-exercise",
        (
            ToolStep(
                "wger_search_exercises",
                params=("term",),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_exercises",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_exercise",
                params=("exercise_id",),
                result=("id", "name", "category", "muscles", "equipment"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_exercise_info",
                params=("exercise_id",),
                result=("id", "name", "category", "muscles", "equipment"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_exercise_infos",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_exercise_translations",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "name"),
            ),
        ),
    ),
    ToolUseContract(
        "browse-exercise-reference",
        (
            ToolStep(
                "wger_get_exercise_categories",
                params=("limit", "offset"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_exercise_category",
                params=("category_id",),
                result=("id", "name", "category", "muscles", "equipment"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_equipment",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_equipment_item",
                params=("equipment_id",),
                result=("id",),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_muscles",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_muscle",
                params=("muscle_id",),
                result=("id",),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_variations",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
        ),
    ),
    ToolUseContract(
        "inspect-exercise-media",
        (
            ToolStep(
                "wger_get_exercise_images",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_exercise_image",
                params=("image_id",),
                result=("id", "name", "category", "muscles", "equipment"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_exercise_videos",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_exercise_comments",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_exercise_aliases",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "name"),
            ),
        ),
    ),
    ToolUseContract(
        "manage-routines",
        (
            ToolStep(
                "wger_get_routines",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_routine",
                params=("routine_id",),
                result=("id", "name", "start", "end"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_routine",
                params=("name", "description", "start_date", "end_date", "fit_in_week"),
                result=("id", "name", "start", "end"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_routine",
                params=("routine_id", "params_json"),
                result=("id", "name", "start", "end"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_routine",
                params=("routine_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_templates",
                params=("limit", "offset", "params_json"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_template",
                params=("template_id",),
                result=("id",),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_public_templates",
                params=("limit", "offset", "params_json"),
                result=("results", "count"),
            ),
        ),
    ),
    ToolUseContract(
        "build-routine-days",
        (
            ToolStep(
                "wger_get_routine",
                params=("routine_id",),
                result=("id", "name", "start", "end"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_days",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_day",
                params=("day_id",),
                result=("id", "name", "routine", "is_rest"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_day",
                params=(
                    "routine",
                    "name",
                    "description",
                    "is_rest",
                    "order",
                    "day_type",
                    "need_logs_to_advance",
                ),
                result=("id", "name", "routine", "is_rest"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_day",
                params=("day_id", "params_json"),
                result=("id", "name", "routine", "is_rest"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_day",
                params=("day_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "build-slots-and-entries",
        (
            ToolStep(
                "wger_get_day",
                params=("day_id",),
                result=("id", "name", "routine", "is_rest"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_slots",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "day"),
            ),
            ToolStep(
                "wger_get_slot",
                params=("slot_id",),
                result=("id", "day", "order"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_slot",
                params=("day", "order", "slot_type", "params_json"),
                result=("id", "day", "order"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_slot",
                params=("slot_id", "params_json"),
                result=("id", "day", "order"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_slot",
                params=("slot_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_slot_entries",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "day"),
            ),
            ToolStep(
                "wger_get_slot_entry",
                params=("entry_id",),
                result=("id", "day", "order"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_slot_entry",
                params=("slot", "exercise", "order", "params_json"),
                result=("id", "day", "order"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_slot_entry",
                params=("entry_id", "params_json"),
                result=("id", "day", "order"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_slot_entry",
                params=("entry_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "tune-slot-progression",
        (
            ToolStep(
                "wger_get_slot_entry",
                params=("entry_id",),
                result=("id", "day", "order"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_weight_config",
                params=("config_id",),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_weight_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_weight_config",
                params=(
                    "slot_entry",
                    "iteration",
                    "value",
                    "operation",
                    "step",
                    "repeat",
                    "params_json",
                ),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_weight_config",
                params=("config_id", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_weight_config",
                params=("config_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_max_weight_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_max_weight_config",
                params=("slot_entry", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_get_repetitions_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_repetitions_config",
                params=(
                    "slot_entry",
                    "iteration",
                    "value",
                    "operation",
                    "step",
                    "repeat",
                    "params_json",
                ),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_repetitions_config",
                params=("config_id", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_repetitions_config",
                params=("config_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_max_repetitions_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_max_repetitions_config",
                params=("slot_entry", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_get_sets_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_sets_config",
                params=(
                    "slot_entry",
                    "iteration",
                    "value",
                    "operation",
                    "step",
                    "repeat",
                    "params_json",
                ),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_sets_config",
                params=("config_id", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_sets_config",
                params=("config_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_max_sets_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_max_sets_config",
                params=("slot_entry", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_get_rest_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_rest_config",
                params=(
                    "slot_entry",
                    "iteration",
                    "value",
                    "operation",
                    "step",
                    "repeat",
                    "params_json",
                ),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_rest_config",
                params=("config_id", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_rest_config",
                params=("config_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_max_rest_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_max_rest_config",
                params=("slot_entry", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_get_rir_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_rir_config",
                params=(
                    "slot_entry",
                    "iteration",
                    "value",
                    "operation",
                    "step",
                    "repeat",
                    "params_json",
                ),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_rir_config",
                params=("config_id", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_rir_config",
                params=("config_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_max_rir_configs",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "slot_entry"),
            ),
            ToolStep(
                "wger_create_max_rir_config",
                params=("slot_entry", "params_json"),
                result=("id", "slot_entry", "iteration", "value", "operation"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "log-a-workout",
        (
            ToolStep(
                "wger_get_routine",
                params=("routine_id",),
                result=("id", "name", "start", "end"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_workout_sessions",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "routine"),
            ),
            ToolStep(
                "wger_get_workout_session",
                params=("session_id",),
                result=("id", "routine", "date", "impression"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_workout_session",
                params=(
                    "routine",
                    "date",
                    "impression",
                    "notes",
                    "time_start",
                    "time_end",
                ),
                result=("id", "routine", "date", "impression"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_workout_session",
                params=("session_id", "params_json"),
                result=("id", "routine", "date", "impression"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_workout_session",
                params=("session_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_workout_logs",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "exercise"),
            ),
            ToolStep(
                "wger_get_workout_log",
                params=("log_id",),
                result=("id", "exercise", "date", "repetitions", "weight"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_workout_log",
                params=(
                    "exercise",
                    "routine",
                    "date",
                    "repetitions",
                    "weight",
                    "rir",
                    "params_json",
                ),
                result=("id", "exercise", "date", "repetitions", "weight"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_workout_log",
                params=("log_id", "params_json"),
                result=("id", "exercise", "date", "repetitions", "weight"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_workout_log",
                params=("log_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "plan-nutrition",
        (
            ToolStep(
                "wger_get_nutrition_plans",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "description"),
            ),
            ToolStep(
                "wger_get_nutrition_plan",
                params=("plan_id",),
                result=("id", "description", "goal_energy"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_nutrition_plan_info",
                params=("plan_id",),
                result=("id", "description", "goal_energy"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_nutrition_plan",
                params=(
                    "description",
                    "only_logging",
                    "goal_energy",
                    "goal_protein",
                    "goal_carbohydrates",
                    "goal_fat",
                    "_goal_fiber",
                ),
                result=("id", "description", "goal_energy"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_nutrition_plan",
                params=("plan_id", "params_json"),
                result=("id", "description", "goal_energy"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_nutrition_plan",
                params=("plan_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "build-meals",
        (
            ToolStep(
                "wger_get_nutrition_plan",
                params=("plan_id",),
                result=("id", "description", "goal_energy"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_meals",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "plan"),
            ),
            ToolStep(
                "wger_get_meal",
                params=("meal_id",),
                result=("id", "plan", "name", "time"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_meal",
                params=("plan", "name", "time", "order"),
                result=("id", "plan", "name", "time"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_meal",
                params=("meal_id", "params_json"),
                result=("id", "plan", "name", "time"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_meal",
                params=("meal_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_meal_items",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "plan"),
            ),
            ToolStep(
                "wger_get_meal_item",
                params=("item_id",),
                result=("id", "plan", "name", "time"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_meal_item",
                params=("meal", "ingredient", "amount", "weight_unit"),
                result=("id", "plan", "name", "time"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_meal_item",
                params=("item_id", "params_json"),
                result=("id", "plan", "name", "time"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_meal_item",
                params=("item_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "log-food-intake",
        (
            ToolStep(
                "wger_get_nutrition_plan_info",
                params=("plan_id",),
                result=("id", "description", "goal_energy"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_nutrition_diary",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "plan"),
            ),
            ToolStep(
                "wger_create_nutrition_diary_entry",
                params=("plan", "ingredient", "amount", "meal", "weight_unit"),
                result=("id", "slot", "exercise"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_nutrition_diary_entry",
                params=("entry_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "look-up-ingredients",
        (
            ToolStep(
                "wger_get_ingredients",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_ingredient",
                params=("ingredient_id",),
                result=("id", "name", "energy", "protein"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_ingredient_info",
                params=("ingredient_id",),
                result=("id", "name", "energy", "protein"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_get_ingredient_weight_units",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "name"),
            ),
            ToolStep(
                "wger_get_weight_units",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_ingredient_images",
                params=("limit", "offset", "params_json"),
                result=("results", "count", "name"),
            ),
        ),
    ),
    ToolUseContract(
        "track-body-weight",
        (
            ToolStep(
                "wger_get_weight_entries",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "date"),
            ),
            ToolStep(
                "wger_get_weight_entry",
                params=("entry_id",),
                result=("id", "slot", "exercise"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_weight_entry",
                params=("date", "weight"),
                result=("id", "slot", "exercise"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_weight_entry",
                params=("entry_id", "params_json"),
                result=("id", "slot", "exercise"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_weight_entry",
                params=("entry_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
        ),
    ),
    ToolUseContract(
        "track-measurements",
        (
            ToolStep(
                "wger_get_measurements",
                params=("limit", "offset", "ordering", "params_json"),
                result=("results", "count", "category"),
            ),
            ToolStep(
                "wger_get_measurement",
                params=("measurement_id",),
                result=("id", "category", "date", "value"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_measurement",
                params=("category", "date", "value"),
                result=("id", "category", "date", "value"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_update_measurement",
                params=("measurement_id", "params_json"),
                result=("id", "category", "date", "value"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_measurement",
                params=("measurement_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_measurement_categories",
                params=("limit", "offset"),
                result=("results", "count", "category"),
            ),
            ToolStep(
                "wger_get_measurement_category",
                params=("category_id",),
                result=("id", "category", "date", "value"),
                refusals=(Refusal("NOT_FOUND", "no object has the id"),),
            ),
            ToolStep(
                "wger_create_measurement_category",
                params=("name", "unit"),
                result=("id", "category", "date", "value"),
                refusals=(
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_delete_measurement_category",
                params=("category_id",),
                result=("status",),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "CONFIRMATION_REQUIRED", "the user has not approved the change"
                    ),
                ),
            ),
            ToolStep(
                "wger_get_gallery",
                params=("limit", "offset", "ordering"),
                result=("results", "count"),
            ),
        ),
    ),
    ToolUseContract(
        "review-user-profile",
        (
            ToolStep(
                "wger_get_user_profile",
                result=("results", "count", "age"),
            ),
            ToolStep(
                "wger_update_user_profile",
                params=(
                    "age",
                    "height",
                    "gender",
                    "birthdate",
                    "weight_unit",
                    "sleep_hours",
                    "workout_duration",
                ),
                result=("id", "age", "height", "gender"),
                refusals=(
                    Refusal("NOT_FOUND", "no object has the id"),
                    Refusal(
                        "INVALID_VALUES",
                        "the instance rejects the values or ids supplied",
                    ),
                ),
            ),
            ToolStep(
                "wger_get_user_statistics",
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_trophies",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_user_trophies",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
        ),
    ),
    ToolUseContract(
        "read-reference-data",
        (
            ToolStep(
                "wger_get_languages",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_licenses",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_deletion_log",
                params=("limit", "offset"),
                result=("results", "count", "exercise"),
            ),
            ToolStep(
                "wger_get_repetition_units",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
            ToolStep(
                "wger_get_weight_unit_settings",
                params=("limit", "offset"),
                result=("results", "count"),
            ),
        ),
    ),
    ToolUseContract(
        "sync-wellness-to-graph",
        (
            ToolStep(
                "wger_ingest_exercises",
                params=("limit", "offset", "ordering"),
                result=("listed", "ingested"),
                refusals=(
                    Refusal(
                        "NO_ENGINE",
                        "no knowledge-graph engine is reachable, ingested is null",
                    ),
                ),
            ),
            ToolStep(
                "wger_ingest_routines",
                params=("limit", "offset", "ordering"),
                result=("listed", "ingested"),
                refusals=(
                    Refusal(
                        "NO_ENGINE",
                        "no knowledge-graph engine is reachable, ingested is null",
                    ),
                ),
            ),
            ToolStep(
                "wger_ingest_workout_sessions",
                params=("limit", "offset", "ordering"),
                result=("listed", "ingested"),
                refusals=(
                    Refusal(
                        "NO_ENGINE",
                        "no knowledge-graph engine is reachable, ingested is null",
                    ),
                ),
            ),
            ToolStep(
                "wger_ingest_nutrition_plans",
                params=("limit", "offset"),
                result=("listed", "ingested"),
                refusals=(
                    Refusal(
                        "NO_ENGINE",
                        "no knowledge-graph engine is reachable, ingested is null",
                    ),
                ),
            ),
        ),
    ),
)

LINKS = (
    SurfaceLink(
        "find-an-exercise",
        tools=(
            "wger_search_exercises",
            "wger_get_exercises",
            "wger_get_exercise",
            "wger_get_exercise_info",
            "wger_get_exercise_infos",
            "wger_get_exercise_translations",
        ),
        prompts=("wger-operator", "wger-workout-planner"),
        skills=("wger-exercise-library",),
    ),
    SurfaceLink(
        "browse-exercise-reference",
        tools=(
            "wger_get_exercise_categories",
            "wger_get_exercise_category",
            "wger_get_equipment",
            "wger_get_equipment_item",
            "wger_get_muscles",
            "wger_get_muscle",
            "wger_get_variations",
        ),
        prompts=("wger-operator", "wger-workout-planner"),
        skills=("wger-exercise-library",),
    ),
    SurfaceLink(
        "inspect-exercise-media",
        tools=(
            "wger_get_exercise_images",
            "wger_get_exercise_image",
            "wger_get_exercise_videos",
            "wger_get_exercise_comments",
            "wger_get_exercise_aliases",
        ),
        prompts=("wger-operator", "wger-workout-planner"),
        skills=("wger-exercise-library",),
    ),
    SurfaceLink(
        "manage-routines",
        tools=(
            "wger_get_routines",
            "wger_get_routine",
            "wger_create_routine",
            "wger_update_routine",
            "wger_delete_routine",
            "wger_get_templates",
            "wger_get_template",
            "wger_get_public_templates",
        ),
        prompts=("wger-operator", "wger-workout-planner"),
        skills=("wger-workout-routines",),
    ),
    SurfaceLink(
        "build-routine-days",
        tools=(
            "wger_get_routine",
            "wger_get_days",
            "wger_get_day",
            "wger_create_day",
            "wger_update_day",
            "wger_delete_day",
        ),
        prompts=("wger-operator", "wger-workout-planner"),
        skills=("wger-workout-routines",),
    ),
    SurfaceLink(
        "build-slots-and-entries",
        tools=(
            "wger_get_day",
            "wger_get_slots",
            "wger_get_slot",
            "wger_create_slot",
            "wger_update_slot",
            "wger_delete_slot",
            "wger_get_slot_entries",
            "wger_get_slot_entry",
            "wger_create_slot_entry",
            "wger_update_slot_entry",
            "wger_delete_slot_entry",
        ),
        prompts=("wger-operator", "wger-workout-planner"),
        skills=("wger-workout-routines",),
    ),
    SurfaceLink(
        "tune-slot-progression",
        tools=(
            "wger_get_slot_entry",
            "wger_get_weight_config",
            "wger_get_weight_configs",
            "wger_create_weight_config",
            "wger_update_weight_config",
            "wger_delete_weight_config",
            "wger_get_max_weight_configs",
            "wger_create_max_weight_config",
            "wger_get_repetitions_configs",
            "wger_create_repetitions_config",
            "wger_update_repetitions_config",
            "wger_delete_repetitions_config",
            "wger_get_max_repetitions_configs",
            "wger_create_max_repetitions_config",
            "wger_get_sets_configs",
            "wger_create_sets_config",
            "wger_update_sets_config",
            "wger_delete_sets_config",
            "wger_get_max_sets_configs",
            "wger_create_max_sets_config",
            "wger_get_rest_configs",
            "wger_create_rest_config",
            "wger_update_rest_config",
            "wger_delete_rest_config",
            "wger_get_max_rest_configs",
            "wger_create_max_rest_config",
            "wger_get_rir_configs",
            "wger_create_rir_config",
            "wger_update_rir_config",
            "wger_delete_rir_config",
            "wger_get_max_rir_configs",
            "wger_create_max_rir_config",
        ),
        prompts=("wger-operator", "wger-workout-planner"),
        skills=("wger-workout-routines",),
    ),
    SurfaceLink(
        "log-a-workout",
        tools=(
            "wger_get_routine",
            "wger_get_workout_sessions",
            "wger_get_workout_session",
            "wger_create_workout_session",
            "wger_update_workout_session",
            "wger_delete_workout_session",
            "wger_get_workout_logs",
            "wger_get_workout_log",
            "wger_create_workout_log",
            "wger_update_workout_log",
            "wger_delete_workout_log",
        ),
        prompts=("wger-operator", "wger-progress-tracker"),
        skills=("wger-workout-routines",),
    ),
    SurfaceLink(
        "plan-nutrition",
        tools=(
            "wger_get_nutrition_plans",
            "wger_get_nutrition_plan",
            "wger_get_nutrition_plan_info",
            "wger_create_nutrition_plan",
            "wger_update_nutrition_plan",
            "wger_delete_nutrition_plan",
        ),
        prompts=("wger-operator", "wger-nutrition-coach"),
        skills=("wger-nutrition-tracking",),
    ),
    SurfaceLink(
        "build-meals",
        tools=(
            "wger_get_nutrition_plan",
            "wger_get_meals",
            "wger_get_meal",
            "wger_create_meal",
            "wger_update_meal",
            "wger_delete_meal",
            "wger_get_meal_items",
            "wger_get_meal_item",
            "wger_create_meal_item",
            "wger_update_meal_item",
            "wger_delete_meal_item",
        ),
        prompts=("wger-operator", "wger-nutrition-coach"),
        skills=("wger-nutrition-tracking",),
    ),
    SurfaceLink(
        "log-food-intake",
        tools=(
            "wger_get_nutrition_plan_info",
            "wger_get_nutrition_diary",
            "wger_create_nutrition_diary_entry",
            "wger_delete_nutrition_diary_entry",
        ),
        prompts=("wger-operator", "wger-nutrition-coach"),
        skills=("wger-nutrition-tracking",),
    ),
    SurfaceLink(
        "look-up-ingredients",
        tools=(
            "wger_get_ingredients",
            "wger_get_ingredient",
            "wger_get_ingredient_info",
            "wger_get_ingredient_weight_units",
            "wger_get_weight_units",
            "wger_get_ingredient_images",
        ),
        prompts=("wger-operator", "wger-nutrition-coach"),
        skills=("wger-nutrition-tracking",),
    ),
    SurfaceLink(
        "track-body-weight",
        tools=(
            "wger_get_weight_entries",
            "wger_get_weight_entry",
            "wger_create_weight_entry",
            "wger_update_weight_entry",
            "wger_delete_weight_entry",
        ),
        prompts=("wger-operator", "wger-progress-tracker"),
        skills=("wger-nutrition-tracking",),
    ),
    SurfaceLink(
        "track-measurements",
        tools=(
            "wger_get_measurements",
            "wger_get_measurement",
            "wger_create_measurement",
            "wger_update_measurement",
            "wger_delete_measurement",
            "wger_get_measurement_categories",
            "wger_get_measurement_category",
            "wger_create_measurement_category",
            "wger_delete_measurement_category",
            "wger_get_gallery",
        ),
        prompts=("wger-operator", "wger-progress-tracker"),
        skills=("wger-nutrition-tracking",),
    ),
    SurfaceLink(
        "review-user-profile",
        tools=(
            "wger_get_user_profile",
            "wger_update_user_profile",
            "wger_get_user_statistics",
            "wger_get_trophies",
            "wger_get_user_trophies",
        ),
        prompts=("wger-operator", "wger-progress-tracker", "wger-data-steward"),
        skills=("wger-user-profile",),
    ),
    SurfaceLink(
        "read-reference-data",
        tools=(
            "wger_get_languages",
            "wger_get_licenses",
            "wger_get_deletion_log",
            "wger_get_repetition_units",
            "wger_get_weight_unit_settings",
        ),
        prompts=("wger-operator", "wger-data-steward"),
        skills=("wger-user-profile",),
    ),
    SurfaceLink(
        "sync-wellness-to-graph",
        tools=(
            "wger_ingest_exercises",
            "wger_ingest_routines",
            "wger_ingest_workout_sessions",
            "wger_ingest_nutrition_plans",
        ),
        prompts=("wger-operator", "wger-data-steward"),
        skills=("wger-exercise-library",),
    ),
    SurfaceLink(
        "wger-agent-operations",
        tools=(
            "wger_get_routines",
            "wger_get_exercises",
            "wger_get_nutrition_plans",
            "wger_get_workout_sessions",
        ),
        skills=("wger-agent-operations",),
    ),
    SurfaceLink(
        "wger-agent-docs",
        tools=("wger_get_user_profile", "wger_get_languages"),
        skills=("wger-agent-docs",),
    ),
)

LOCATIONS = (
    DataLocation(
        "wger-exercises",
        ("Exercise",),
        "WGER_URL",
        "wger_get_exercises",
        federation_key="id",
    ),
    DataLocation(
        "wger-routines",
        ("WorkoutRoutine",),
        "WGER_URL",
        "wger_get_routines",
        federation_key="id",
    ),
    DataLocation(
        "wger-workout-logs",
        ("WorkoutSession", "ExerciseSet"),
        "WGER_URL",
        "wger_get_workout_sessions",
        federation_key="id",
    ),
    DataLocation(
        "wger-nutrition",
        ("NutritionPlan", "MealEntry", "Ingredient"),
        "WGER_URL",
        "wger_get_nutrition_plans",
        federation_key="id",
    ),
    DataLocation(
        "wger-body",
        ("BodyMeasurement",),
        "WGER_URL",
        "wger_get_measurements",
        federation_key="id",
    ),
)

ROLES = (
    BusinessRole(
        "workout-planner",
        tasks=(
            "find-an-exercise",
            "browse-exercise-reference",
            "inspect-exercise-media",
            "manage-routines",
            "build-routine-days",
            "build-slots-and-entries",
            "tune-slot-progression",
        ),
    ),
    BusinessRole(
        "nutrition-coach",
        tasks=(
            "plan-nutrition",
            "build-meals",
            "log-food-intake",
            "look-up-ingredients",
        ),
    ),
    BusinessRole(
        "progress-tracker",
        tasks=(
            "log-a-workout",
            "track-body-weight",
            "track-measurements",
            "review-user-profile",
        ),
    ),
    BusinessRole(
        "data-steward", tasks=("read-reference-data", "sync-wellness-to-graph")
    ),
)
