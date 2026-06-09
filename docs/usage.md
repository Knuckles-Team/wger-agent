# Usage — MCP / API / CLI

`wger-agent` exposes the same capability three ways: as **MCP tools** an agent calls,
as a **Python API** (`WgerApi`) you import, and as a **graph agent CLI**. The full
tool surface is summarized in [Overview](overview.md).

## As an MCP server

Once [deployed](deployment.md), the server registers seven action-routed tool
domains, each grouping related methods to keep the LLM context lean. Every domain is
togglable through its environment variable (all default `True`):

| Tool domain | Toggle | Representative actions |
|---|---|---|
| Routine | `ROUTINETOOL` | `create_routine`, `get_routines`, `create_day`, `get_templates` |
| Routine config | `ROUTINECONFIGTOOL` | `create_sets_config`, `create_weight_config`, `get_repetitions_configs` |
| Exercise | `EXERCISETOOL` | `search_exercises`, `get_exercises`, `get_muscles`, `get_equipment` |
| Workout | `WORKOUTTOOL` | `create_workout_session`, `create_workout_log`, `get_workout_logs` |
| Nutrition | `NUTRITIONTOOL` | `create_nutrition_plan`, `log_nutrition`, `get_ingredients` |
| Body | `BODYTOOL` | `log_body_weight`, `log_measurement`, `get_weight_entries` |
| User | `USERTOOL` | `get_user_profile`, `get_user_statistics`, `get_languages` |

Example agent prompts that map onto these tools:

- *"Find a barbell bench-press exercise"* → `search_exercises`
- *"Log a body weight of 80 kg for today"* → `log_body_weight`
- *"Show my active workout routines"* → `get_routines`

## As a Python API

`WgerApi` is a unified client composed of domain-specific sub-clients, built from the
environment via `get_client()`:

```python
from wger_agent.auth import get_client

api = get_client()        # reads WGER_URL / WGER_API_KEY from the environment / .env

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
    verify=True,
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
domain, then a domain node executes against the MCP server.

```bash
export WGER_URL=https://your-wger:8000
export WGER_API_KEY=your_api_key
export MCP_URL=http://localhost:8000/mcp

wger-agent --provider openai --model-id gpt-4o
```

Enable the Agent Web UI and OpenTelemetry tracing with `--web` and `--otel`. See
[Deployment](deployment.md#agent-server) for the full Compose recipe and port wiring.
