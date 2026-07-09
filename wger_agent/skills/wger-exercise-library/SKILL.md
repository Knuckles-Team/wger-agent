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
  author: Genius
  version: '0.1.0'
---
# wger Exercise Library

Domain-typed access to the wger **exercise database** — the read-only catalog of
movements, categories, muscles, and equipment used to program routines.

## When to use
- Search or list exercises (`search_exercises`, `get_exercises`).
- Read full exercise detail (`get_exercise_info`) including translations, muscles, images.
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

`MCP_TOOL_MODE` (`condensed`|`verbose`|`both`) selects the condensed action-routed
tool vs. the 1:1 verbose surface.

## Tools & actions
| Condensed tool | Actions |
|----------------|---------|
| `wger_exercise` | `get_exercises`, `get_exercise_info`, `search_exercises`, `get_exercise_categories`, `get_equipment`, `get_muscles`, `get_exercise_images`, `get_variations` |
| `wger_ingest` | `exercises` |

## Recipes (`params_json`)
Search for an exercise by term:
```json
{"term": "bench press"}
```
List exercises in a category, English only:
```json
{"category": 8, "language": 2, "limit": 50}
```
Read full detail (muscles, equipment, images) for one exercise:
```json
{"exercise_id": 345}
```
Sync the exercise catalog into the knowledge graph (`wger_ingest`, action `exercises`):
```json
{"limit": 200}
```

## Gotchas
- The base `exercise` record carries no human name — names live in translations. Use
  `get_exercise_info` (or `get_exercise_infos`) when you need the display name; the
  `wger_ingest` mapper stores whatever `name` field is present.
- List responses are DRF-paginated under `results`; page with `limit`/`offset`.
- `language` is a numeric id (e.g. `2` = English), not an ISO code.
- KG ingestion is best-effort: `{"ingested": null}` means no engine was reachable; the
  read still succeeds. Node ids are `wellness:exercise:<id>`.

## Related
- `wger-workout-routines` — consume these exercises when building routine slots.
- `wger-nutrition-tracking` — the diet side of the same wellness graph.
- `mcp-client` — connecting to the `wger-agent` MCP server.
