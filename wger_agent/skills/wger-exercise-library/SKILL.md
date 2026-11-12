---
name: wger-exercise-library
skill_type: skill
description: >-
  Exercise-database operations on wger via the wger-agent MCP server — search and read
  exercises, their categories, target muscles, equipment, and images. Use when the agent
  must find an exercise, resolve its muscles/equipment for programming, or sync the
  exercise catalog into the knowledge graph as typed :Exercise nodes. Do NOT use for
  building routines/sessions (wger-workout-routines) or nutrition (wger-nutrition-tracking);
  prefer those.
license: MIT
tags: [wger, fitness, exercise, catalog, muscles, mcp]
metadata:
  author: Repository Maintainers
  version: '0.1.0'
---
# wger Exercise Library

Domain-typed access to the wger **exercise database** — the read-only catalog of
movements, categories, muscles, and equipment used to program routines.

## When to use
- Search or list exercises (`wger_search_exercises`, `wger_get_exercises`).
- Read full exercise detail (`wger_get_exercise_info`) including translations, muscles, images.
- Resolve categories, muscles, or equipment for slotting into a routine.
- Natively sync the catalog into the KG as `:Exercise` nodes.

## When NOT to use
- Creating routines, days, slots, or logging sessions → `wger-workout-routines`.
- Nutrition plans, meals, diary, body measurements → `wger-nutrition-tracking`.

## Prerequisites & environment
Connect via the `mcp-client` skill against the **`wger-agent`** MCP server.

| Variable | Required | Notes |
|----------|----------|-------|
| `WGER_INSTANCE` / `WGER_URL` | ✅ | wger base URL (defaults to `https://wger.de`) |
| `WGER_ACCESS_TOKEN` / `WGER_TOKEN` | optional | Public exercise reads work unauthenticated; a token widens access |
| `WGER_SSL_VERIFY` | optional | TLS verification toggle |

## Tools
One typed tool per API operation; list tools take `limit`, `offset` and DRF filters (`params_json`).

| Tool | Purpose |
|------|---------|
| `wger_search_exercises` | Search exercises. |
| `wger_get_exercises` | List exercises. Supports filters: language, category, muscles, equipment, etc. |
| `wger_get_exercise` | Get a specific exercise. |
| `wger_get_exercise_info` | Get detailed exercise info (includes translations, images, muscles, etc.). |
| `wger_get_exercise_infos` | List exercise infos. |
| `wger_get_exercise_translations` | List exercise translations. |
| `wger_get_exercise_categories` | List exercise categories (e.g., Arms, Legs, etc.). |
| `wger_get_exercise_category` | Get a specific exercise category. |
| `wger_get_equipment` | List equipment (e.g., Barbell, Dumbbell, etc.). |
| `wger_get_equipment_item` | Get a specific equipment. |
| `wger_get_muscles` | List muscles. |
| `wger_get_muscle` | Get a specific muscle. |
| `wger_get_variations` | List exercise variations. |
| `wger_get_exercise_images` | List exercise images. |
| `wger_get_exercise_image` | Get a specific exercise image. |
| `wger_get_exercise_videos` | List exercise videos. |
| `wger_get_exercise_comments` | List exercise comments. |
| `wger_get_exercise_aliases` | List exercise aliases. |
| `wger_ingest_exercises` | Ingest the listed exercises into the knowledge graph. |

## Recipes
Search for an exercise by term (`wger_search_exercises`):
```json
{"term": "bench press"}
```
List exercises in a category, English only (`wger_get_exercises`):
```json
{"category": 8, "language": 2, "limit": 50}
```
Read full detail (muscles, equipment, images) for one exercise (`wger_get_exercise_info`):
```json
{"exercise_id": 345}
```
Sync the exercise catalog into the knowledge graph (`wger_ingest_exercises`):
```json
{"limit": 200}
```

## Gotchas
- The base `exercise` record carries no human name — names live in translations. Use
  `wger_get_exercise_info` (or `wger_get_exercise_infos`) when you need the display name; the
  ingestion tool stores whatever `name` field is present.
- List responses are DRF-paginated under `results`; page with `limit`/`offset`.
- `language` is a numeric id (e.g. `2` = English), not an ISO code.
- KG ingestion is best-effort: `{"ingested": null}` means no engine was reachable; the
  read still succeeds. Node ids are `wellness:exercise:<id>`.

## Related
- `wger-workout-routines` — consume these exercises when building routine slots.
- `wger-nutrition-tracking` — the diet side of the same wellness graph.
- `mcp-client` — connecting to the `wger-agent` MCP server.
