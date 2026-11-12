---
name: wger-workout-routines
skill_type: skill
description: >-
  Training-program operations on wger via the wger-agent MCP server — read, build,
  and audit workout routines, their scheduled days/slots, and the sessions/logs
  performed against them. Use when the agent must design or inspect a routine,
  gauge training adherence and load from logged sessions, or sync a routine into the
  knowledge graph. Do NOT use for browsing the exercise database (wger-exercise-library)
  or diet/nutrition work (wger-nutrition-tracking); prefer those.
license: MIT
tags: [wger, fitness, workout, routine, training, mcp]
metadata:
  author: Repository Maintainers
  version: '0.1.0'
---
# wger Workout Routines

Domain-typed access to wger **routines**, their day/slot structure, and the workout
**sessions & logs** executed against them — the training-programming surface.

## When to use
- Read or audit a routine (`wger_get_routines`, `wger_get_routine`) and its scheduled days/slots.
- Build a routine: create it, add days, add slots and slot entries.
- Gauge adherence and training load from `wger_get_workout_sessions` / `wger_get_workout_logs`.
- Natively sync routines and sessions into the KG as `:WorkoutRoutine` / `:WorkoutSession`.

## When NOT to use
- Browsing exercises, categories, muscles, or equipment → `wger-exercise-library`.
- Nutrition plans, meals, diary, body weight/measurements → `wger-nutrition-tracking`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`wger-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `WGER_INSTANCE` / `WGER_URL` | ✅ | wger base URL (defaults to `https://wger.de`) |
| `WGER_ACCESS_TOKEN` / `WGER_TOKEN` | ✅ | API token for authenticated reads/writes |
| `WGER_SSL_VERIFY` | optional | TLS verification toggle |

## Tools
One typed tool per API operation.

### Routines, templates, days, slots and entries
| Tool | Purpose |
|------|---------|
| `wger_get_routines` | List all routines. |
| `wger_get_routine` | Get a specific routine by ID. |
| `wger_create_routine` | Create a new routine. |
| `wger_update_routine` | Update a routine. |
| `wger_delete_routine` | Delete a routine. |
| `wger_get_templates` | List user's workout templates. |
| `wger_get_template` | Get a specific template. |
| `wger_get_public_templates` | List public workout templates. |
| `wger_get_days` | List all workout days. |
| `wger_get_day` | Get a specific day. |
| `wger_create_day` | Create a workout day in a routine. |
| `wger_update_day` | Update a day. |
| `wger_delete_day` | Delete a day. |
| `wger_get_slots` | List all slots (sets). |
| `wger_get_slot` | Get a specific slot. |
| `wger_create_slot` | Create a slot (set) in a day. |
| `wger_update_slot` | Update a slot. |
| `wger_delete_slot` | Delete a slot. |
| `wger_get_slot_entries` | List all slot entries. |
| `wger_get_slot_entry` | Get a specific slot entry. |
| `wger_create_slot_entry` | Create a slot entry (add exercise to slot). |
| `wger_update_slot_entry` | Update a slot entry. |
| `wger_delete_slot_entry` | Delete a slot entry. |

### Slot progression configs
| Tool | Purpose |
|------|---------|
| `wger_get_weight_config` | Get a specific weight config. |
| `wger_get_weight_configs` | List weight progression configs. |
| `wger_create_weight_config` | Create a weight progression config. |
| `wger_update_weight_config` | Update a weight config. |
| `wger_delete_weight_config` | Delete a weight config. |
| `wger_get_max_weight_configs` | List max weight configs. |
| `wger_create_max_weight_config` | Create a max weight config. |
| `wger_get_repetitions_configs` | List repetitions configs. |
| `wger_create_repetitions_config` | Create a repetitions config. |
| `wger_update_repetitions_config` | Update a repetitions config. |
| `wger_delete_repetitions_config` | Delete a repetitions config. |
| `wger_get_max_repetitions_configs` | List max repetitions configs. |
| `wger_create_max_repetitions_config` | Create a max repetitions config. |
| `wger_get_sets_configs` | List sets configs. |
| `wger_create_sets_config` | Create a sets config. |
| `wger_update_sets_config` | Update a sets config. |
| `wger_delete_sets_config` | Delete a sets config. |
| `wger_get_max_sets_configs` | List max sets configs. |
| `wger_create_max_sets_config` | Create a max sets config. |
| `wger_get_rest_configs` | List rest time configs. |
| `wger_create_rest_config` | Create a rest time config. |
| `wger_update_rest_config` | Update a rest config. |
| `wger_delete_rest_config` | Delete a rest config. |
| `wger_get_max_rest_configs` | List max rest configs. |
| `wger_create_max_rest_config` | Create a max rest config. |
| `wger_get_rir_configs` | List RiR configs. |
| `wger_create_rir_config` | Create a RiR config. |
| `wger_update_rir_config` | Update a RiR config. |
| `wger_delete_rir_config` | Delete a RiR config. |
| `wger_get_max_rir_configs` | List max RiR configs. |
| `wger_create_max_rir_config` | Create a max RiR config. |

### Sessions and logs
| Tool | Purpose |
|------|---------|
| `wger_get_workout_sessions` | List workout sessions. |
| `wger_get_workout_session` | Get a specific workout session. |
| `wger_create_workout_session` | Create a workout session. Impression: 1=General discomfort, 2=Could be better, 3=Neutral, 4=Good, 5=Perfect. |
| `wger_update_workout_session` | Update a workout session. |
| `wger_delete_workout_session` | Delete a workout session. |
| `wger_get_workout_logs` | List workout logs. |
| `wger_get_workout_log` | Get a specific workout log. |
| `wger_create_workout_log` | Create a workout log entry. |
| `wger_update_workout_log` | Update a workout log. |
| `wger_delete_workout_log` | Delete a workout log. |
| `wger_ingest_routines` | Ingest the listed routines into the knowledge graph. |
| `wger_ingest_workout_sessions` | Ingest the listed workout sessions into the knowledge graph. |

## Recipes
List routines, newest first (`wger_get_routines`):
```json
{"limit": 25, "ordering": "-start"}
```
Read the days of a routine (`wger_get_days`):
```json
{"routine": 42}
```
Log a completed session against a routine (`wger_create_workout_session`; `impression`: 1-5, 5 = perfect):
```json
{"routine": 42, "date": "2026-07-04", "impression": "4", "notes": "solid push day"}
```
Sync all routines into the knowledge graph (`wger_ingest_routines`):
```json
{"limit": 100}
```

## Gotchas
- List responses are DRF-paginated: records live under `results`, not the top level.
  The ingestion tools already unwrap this.
- `create_workout_session` requires a `routine` id and an ISO `date`; `impression` is a
  string `"1"`–`"5"`.
- KG ingestion is best-effort: the ingestion tools return `{"ingested": null}` when no
  medulla engine is reachable — the API read still succeeds.
- Node ids are `wellness:routine:<id>` / `wellness:session:<id>`; a session links to its
  routine via `:sessionOfRoutine`.

## Related
- `wger-exercise-library` — the exercise catalog you populate slots from.
- `wger-nutrition-tracking` — pair training load with intake for calorie-balance reasoning.
- `mcp-client` — connecting to the `wger-agent` MCP server.
