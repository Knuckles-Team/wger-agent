# Usage — MCP / API / CLI

`wger-agent` exposes the same capability three ways: as **MCP tools** an agent calls,
as a **Python API** (`WgerApi`) the operator import, and as a **graph agent CLI**. The full
tool surface is summarized in [Overview](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers one typed tool per wger API
operation, named `wger_<operation>`, plus four ingestion tools (`wger_ingest_exercises`,
`wger_ingest_routines`, `wger_ingest_workout_sessions`, `wger_ingest_nutrition_plans`).

| Area | Representative tools |
|---|---|
| Routines | `wger_create_routine`, `wger_get_routines`, `wger_create_day`, `wger_get_templates` |
| Progression configs | `wger_create_sets_config`, `wger_create_weight_config`, `wger_get_repetitions_configs` |
| Exercises | `wger_search_exercises`, `wger_get_exercises`, `wger_get_muscles`, `wger_get_equipment` |
| Workouts | `wger_create_workout_session`, `wger_create_workout_log`, `wger_get_workout_logs` |
| Nutrition | `wger_create_nutrition_plan`, `wger_create_nutrition_diary_entry`, `wger_get_ingredients` |
| Body | `wger_create_weight_entry`, `wger_create_measurement`, `wger_get_weight_entries` |
| User | `wger_get_user_profile`, `wger_get_user_statistics`, `wger_get_languages` |

Example agent prompts that map onto these tools:

- *"Find a barbell bench-press exercise"* -> `wger_search_exercises`
- *"Log a body weight of 80 kg for today"* -> `wger_create_weight_entry`
- *"Show my active workout routines"* -> `wger_get_routines`

## As a Python API

`WgerApi` is a unified client composed of domain-specific sub-clients, built from the
environment via `get_client()`:

```python
from wger_agent.auth import get_client

api = get_client()  # reads WGER_URL / WGER_API_KEY from the environment / .env

# Reads
exercises = api.search_exercises("bench press")
muscles = api.get_muscles()
routines = api.get_routines()
profile = api.get_user_profile()
```

Build a client directly:

```python
from wger_agent.api_client import WgerApi

api = WgerApi(
    base_url="https://your-wger:8000",
    token="your_api_key",
)

ingredients = api.get_ingredients()
weight_entries = api.get_weight_entries()
```

### Writes

The same client performs writes once it is configured with a valid token:

```python
api.log_body_weight(weight=80.0)
api.create_nutrition_plan(description="Cutting plan")
api.create_workout_session(notes="Upper body")
```

## As an agent CLI

The integrated Pydantic-AI graph agent runs from the `wger-agent` console script. A
confidence-gated router classifies each request and enables only the relevant tool
domain, then a domain node runs against the MCP server.

```bash
export WGER_URL=https://your-wger:8000
export WGER_API_KEY=your_api_key
export MCP_URL=http://localhost:8000/mcp

wger-agent --provider openai --model-id gpt-4o
```

Enable the Agent Web UI and OpenTelemetry tracing with `--web` and `--otel`. See
[Deployment](deployment.md#agent-server) for the full Compose recipe and port wiring.
