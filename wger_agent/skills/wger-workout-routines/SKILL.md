---
name: wger-workout-routines
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
  author: Genius
  version: '0.1.0'
---
# wger Workout Routines

Domain-typed access to wger **routines**, their day/slot structure, and the workout
**sessions & logs** executed against them — the training-programming surface.

## When to use
- Read or audit a routine (`get_routines`, `get_routine`) and its scheduled days/slots.
- Build a routine: create it, add days, add slots and slot entries.
- Gauge adherence and training load from `get_workout_sessions` / `get_workout_logs`.
- Natively sync routines and sessions into the KG as `:WorkoutRoutine` / `:WorkoutSession`.

## When NOT to use
- Browsing exercises, categories, muscles, or equipment → `wger-exercise-library`.
- Nutrition plans, meals, diary, body weight/measurements → `wger-nutrition-tracking`.
- Raw config CRUD (weight/reps/sets/rest/rir) belongs to the `wger_routineconfig` tool.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`wger-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `WGER_INSTANCE` / `WGER_URL` | ✅ | wger base URL (defaults to `https://wger.de`) |
| `WGER_ACCESS_TOKEN` / `WGER_TOKEN` | ✅ | API token for authenticated reads/writes |
| `WGER_SSL_VERIFY` | optional | TLS verification toggle |

`MCP_TOOL_MODE` (`condensed`|`verbose`|`both`) selects the condensed action-routed
tool vs. the 1:1 verbose surface.

## Tools & actions
| Condensed tool | Actions |
|----------------|---------|
| `wger_routine` | `get_routines`, `get_routine`, `create_routine`, `delete_routine`, `get_days`, `create_day`, `delete_day`, `get_slots`, `create_slot`, `create_slot_entry`, `get_templates`, `get_public_templates` |
| `wger_workout` | `get_workout_sessions`, `get_workout_session`, `create_workout_session`, `delete_workout_session`, `get_workout_logs`, `create_workout_log`, `delete_workout_log` |
| `wger_ingest` | `routines`, `workout_sessions` |

## Recipes (`params_json`)
List routines, newest first:
```json
{"limit": 25, "ordering": "-start"}
```
Read the days of a routine:
```json
{"routine": 42}
```
Log a completed session against a routine (`impression`: 1–5, 5 = perfect):
```json
{"routine": 42, "date": "2026-07-04", "impression": "4", "notes": "solid push day"}
```
Sync all routines into the knowledge graph (`wger_ingest`, action `routines`):
```json
{"limit": 100}
```

## Gotchas
- List responses are DRF-paginated: records live under `results`, not the top level.
  The `wger_ingest` mapper already unwraps this.
- `create_workout_session` requires a `routine` id and an ISO `date`; `impression` is a
  string `"1"`–`"5"`.
- KG ingestion is best-effort: `wger_ingest` returns `{"ingested": null}` when no
  epistemic-graph engine is reachable — the API read still succeeds.
- Node ids are `wellness:routine:<id>` / `wellness:session:<id>`; a session links to its
  routine via `:sessionOfRoutine`.

## Related
- `wger-exercise-library` — the exercise catalog you populate slots from.
- `wger-nutrition-tracking` — pair training load with intake for calorie-balance reasoning.
- `mcp-client` — connecting to the `wger-agent` MCP server.
