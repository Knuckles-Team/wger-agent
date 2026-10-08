---
name: wger-nutrition-tracking
skill_type: skill
description: >-
  Nutrition and body-progress operations on wger via the wger-agent MCP server — read and
  build nutrition plans, meals, diary entries, ingredients, and track body weight and
  measurements over time. Use when the agent must plan or audit diet against macro goals,
  reason about calorie balance vs. training, track composition trends, or sync nutrition
  plans/measurements into the knowledge graph. Do NOT use for routines/sessions
  (wger-workout-routines) or the exercise catalog (wger-exercise-library); prefer those.
license: MIT
tags: [wger, nutrition, diet, macros, body-measurement, mcp]
metadata:
  author: Genius
  version: '0.1.0'
---
# wger Nutrition & Progress Tracking

Domain-typed access to wger **nutrition plans**, meals, the food diary, and **body
weight/measurement** history — the diet and progress side of the wellness graph.

## When to use
- Read or build nutrition plans and their meals/items (`get_nutrition_plans`, `create_meal`).
- Compare logged intake against goal energy/protein/carb/fat (`get_nutrition_diary`).
- Look up ingredients and their nutritional values (`get_ingredients`, `get_ingredient_info`).
- Track body weight and measurements over time (`get_weight_entries`, `get_measurements`).
- Natively sync plans into the KG as `:NutritionPlan` (and measurements as `:BodyMeasurement`).

## When NOT to use
- Routines, days, slots, sessions, logs → `wger-workout-routines`.
- Exercise search / muscles / equipment → `wger-exercise-library`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`wger-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `WGER_INSTANCE` / `WGER_URL` | ✅ | wger base URL (defaults to `https://wger.de`) |
| `WGER_ACCESS_TOKEN` / `WGER_TOKEN` | ✅ | API token — nutrition/body data is user-scoped |
| `WGER_SSL_VERIFY` | optional | TLS verification toggle |

`MCP_TOOL_MODE` (`condensed`|`verbose`|`both`) selects the condensed action-routed
tool vs. the 1:1 verbose surface.

## Tools & actions
| Condensed tool | Actions |
|----------------|---------|
| `wger_nutrition` | `get_nutrition_plans`, `get_nutrition_plan_info`, `create_nutrition_plan`, `delete_nutrition_plan`, `create_meal`, `create_meal_item`, `get_ingredients`, `get_ingredient_info`, `get_nutrition_diary`, `log_nutrition` |
| `wger_body` | `get_weight_entries`, `log_body_weight`, `get_measurements`, `log_measurement`, `get_measurement_categories`, `create_measurement_category`, `get_gallery` |
| `wger_ingest` | `nutrition_plans` |

## Recipes (`params_json`)
List nutrition plans:
```json
{"limit": 25}
```
Read a plan with its meals and computed nutritional values:
```json
{"plan_id": 12}
```
Create a nutrition plan with macro goals:
```json
{"description": "Cut - 2400 kcal", "goal_energy": 2400, "goal_protein": 180, "goal_carbohydrates": 220, "goal_fat": 70}
```
Log a body-weight entry:
```json
{"date": "2026-07-04", "weight": 82.4}
```
Sync all nutrition plans into the knowledge graph (`wger_ingest`, action `nutrition_plans`):
```json
{"limit": 100}
```

## Gotchas
- Use `get_nutrition_plan_info` (not `get_nutrition_plan`) when you need meals + computed
  nutritional totals in one call.
- List responses are DRF-paginated under `results`; the `wger_ingest` mapper unwraps this.
- Body weight is logged via `log_body_weight` (date + weight); measurements need a
  `category` id first — create one with `create_measurement_category` if none exists.
- KG ingestion is best-effort: `{"ingested": null}` means no engine was reachable; the
  read still succeeds. Node ids are `wellness:nutritionplan:<id>`.

## Related
- `wger-workout-routines` — pair intake with training load for calorie-balance reasoning.
- `wger-exercise-library` — the movement catalog behind those routines.
- `mcp-client` — connecting to the `wger-agent` MCP server.
