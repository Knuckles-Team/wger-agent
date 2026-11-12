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
  author: Repository Maintainers
  version: '0.1.0'
---
# wger Nutrition & Progress Tracking

Domain-typed access to wger **nutrition plans**, meals, the food diary, and **body
weight/measurement** history — the diet and progress side of the wellness graph.

## When to use
- Read or build nutrition plans and their meals/items (`wger_get_nutrition_plans`, `wger_create_meal`).
- Compare logged intake against goal energy/protein/carb/fat (`wger_get_nutrition_diary`).
- Look up ingredients and their nutritional values (`wger_get_ingredients`, `wger_get_ingredient_info`).
- Track body weight and measurements over time (`wger_get_weight_entries`, `wger_get_measurements`).
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

## Tools
One typed tool per API operation.

### Nutrition
| Tool | Purpose |
|------|---------|
| `wger_get_nutrition_plans` | List nutrition plans. |
| `wger_get_nutrition_plan` | Get a specific nutrition plan. |
| `wger_get_nutrition_plan_info` | Get detailed nutrition plan info (includes meals, items, nutritional values). |
| `wger_create_nutrition_plan` | Create a nutrition plan. |
| `wger_update_nutrition_plan` | Update a nutrition plan. |
| `wger_delete_nutrition_plan` | Delete a nutrition plan. |
| `wger_get_meals` | List meals. |
| `wger_get_meal` | Get a specific meal. |
| `wger_create_meal` | Create a meal in a nutrition plan. |
| `wger_update_meal` | Update a meal. |
| `wger_delete_meal` | Delete a meal. |
| `wger_get_meal_items` | List meal items. |
| `wger_get_meal_item` | Get a specific meal item. |
| `wger_create_meal_item` | Add an ingredient to a meal. |
| `wger_update_meal_item` | Update a meal item. |
| `wger_delete_meal_item` | Delete a meal item. |
| `wger_get_ingredients` | List ingredients. Supports filters: language, name, etc. |
| `wger_get_ingredient` | Get a specific ingredient. |
| `wger_get_ingredient_info` | Get detailed ingredient info (includes weight units). |
| `wger_get_ingredient_weight_units` | List ingredient weight units. |
| `wger_get_weight_units` | List weight units. |
| `wger_get_ingredient_images` | List ingredient images. |
| `wger_get_nutrition_diary` | List nutrition diary entries. |
| `wger_create_nutrition_diary_entry` | Log a nutrition diary entry. |
| `wger_delete_nutrition_diary_entry` | Delete a nutrition diary entry. |
| `wger_ingest_nutrition_plans` | Ingest the listed nutrition plans into the knowledge graph. |

### Body progress
| Tool | Purpose |
|------|---------|
| `wger_get_weight_entries` | List body weight entries. |
| `wger_get_weight_entry` | Get a specific weight entry. |
| `wger_create_weight_entry` | Log a body weight entry. |
| `wger_update_weight_entry` | Update a weight entry. |
| `wger_delete_weight_entry` | Delete a weight entry. |
| `wger_get_measurements` | List body measurements. |
| `wger_get_measurement` | Get a specific measurement. |
| `wger_create_measurement` | Log a body measurement. |
| `wger_update_measurement` | Update a measurement. |
| `wger_delete_measurement` | Delete a measurement. |
| `wger_get_measurement_categories` | List measurement categories (e.g., Biceps, Chest, etc.). |
| `wger_get_measurement_category` | Get a specific measurement category. |
| `wger_create_measurement_category` | Create a measurement category. |
| `wger_delete_measurement_category` | Delete a measurement category. |
| `wger_get_gallery` | List progress gallery images. |

## Recipes
List nutrition plans (`wger_get_nutrition_plans`):
```json
{"limit": 25}
```
Read a plan with its meals and computed nutritional values (`wger_get_nutrition_plan_info`):
```json
{"plan_id": 12}
```
Create a nutrition plan with macro goals (`wger_create_nutrition_plan`):
```json
{"description": "Cut - 2400 kcal", "goal_energy": 2400, "goal_protein": 180, "goal_carbohydrates": 220, "goal_fat": 70}
```
Log a body-weight entry (`wger_create_weight_entry`):
```json
{"date": "2026-07-04", "weight": 82.4}
```
Sync all nutrition plans into the knowledge graph (`wger_ingest_nutrition_plans`):
```json
{"limit": 100}
```

## Gotchas
- Use `wger_get_nutrition_plan_info` (not `wger_get_nutrition_plan`) when you need meals + computed
  nutritional totals in one call.
- List responses are DRF-paginated under `results`; the ingestion tools unwrap this.
- Body weight is logged with `wger_create_weight_entry` (date + weight); measurements need a
  `category` id first - create one with `wger_create_measurement_category` if none exists.
- KG ingestion is best-effort: `{"ingested": null}` means no engine was reachable; the
  read still succeeds. Node ids are `wellness:nutritionplan:<id>`.

## Related
- `wger-workout-routines` — pair intake with training load for calorie-balance reasoning.
- `wger-exercise-library` — the movement catalog behind those routines.
- `mcp-client` — connecting to the `wger-agent` MCP server.
