---
name: wger-user-profile
skill_type: skill
description: >-
  Read and update the wger user profile, statistics and trophies, and read the
  instance reference data (languages, licenses, repetition and weight units,
  deletion log) via the wger-agent MCP server. Use when the agent must resolve a
  language or unit id, read the user's profile or statistics before programming
  training, or audit what was deleted. Do NOT use for exercises (wger-exercise-library),
  routines and logs (wger-workout-routines) or nutrition and body progress
  (wger-nutrition-tracking); prefer those.
license: MIT
tags: [wger, fitness, profile, reference, mcp]
metadata:
  author: Repository Maintainers
  version: '0.1.0'
---
# wger User Profile and Reference Data

Profile, statistics and instance reference data that the other wger skills depend on.

## When to use
- Read the profile (`wger_get_user_profile`) before programming for age, height or unit preferences.
- Update the profile (`wger_update_user_profile`) when the user states new values.
- Resolve a language id, unit id or license id used by other records.

## When NOT to use
- Exercise search, routines, sessions, nutrition or body measurements; use the skill for that area.

## Tools
One typed tool per API operation.

| Tool | Purpose |
|------|---------|
| `wger_get_user_profile` | Get the current user's profile. |
| `wger_update_user_profile` | Update user profile. Only the fields that are set are changed. |
| `wger_get_user_statistics` | Get user statistics (workout count, etc.). |
| `wger_get_trophies` | List available trophies. |
| `wger_get_user_trophies` | List user's earned trophies. |
| `wger_get_languages` | List available languages. |
| `wger_get_licenses` | List content licenses. |
| `wger_get_deletion_log` | List deletion log entries. |
| `wger_get_repetition_units` | List repetition unit settings. |
| `wger_get_weight_unit_settings` | List weight unit settings. |

## Gotchas
- `language` and unit fields on other records are numeric ids; resolve them here, not by guessing.
- `wger_update_user_profile` changes only the fields passed.
- Profile data is personal; report only the fields the request needs.

## Related
- `wger-workout-routines` and `wger-nutrition-tracking` use the unit ids resolved here.
