# Wger Agent
## CLI or API | MCP | Agent

![PyPI - Version](https://img.shields.io/pypi/v/wger-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/wger-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/wger-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/wger-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/wger-agent)
![PyPI - License](https://img.shields.io/pypi/l/wger-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/wger-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/wger-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/wger-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/wger-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/wger-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/wger-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/wger-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/wger-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/wger-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/wger-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/wger-agent)

*Version: 1.0.0*

> **Documentation** — Installation, deployment, usage across the MCP, API, and agent
> interfaces, and guidance for provisioning the Wger Workout Manager platform are
> maintained in the [official documentation](https://knuckles-team.github.io/wger-agent/).

---

## Overview

**Wger Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Wger Workout Manager — exercise database, workout routines, nutrition plans, body measurements, and progress tracking..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Wger Workout Manager — exercise database, workout routines, nutrition plans, body measurements, and progress tracking. API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools

_Auto-generated from the live MCP server — do not edit by hand._

<!-- MCP-TOOLS-TABLE:START -->

#### Condensed action-routed tools (default — `MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `wger_body` | `BODYTOOL` | Manage wger body operations. |
| `wger_exercise` | `EXERCISETOOL` | Manage wger exercise operations. |
| `wger_nutrition` | `NUTRITIONTOOL` | Manage wger nutrition operations. |
| `wger_routine` | `ROUTINETOOL` | Manage wger routine operations. |
| `wger_routineconfig` | `ROUTINECONFIGTOOL` | Manage wger routineconfig operations. |
| `wger_user` | `USERTOOL` | Manage wger user operations. |
| `wger_workout` | `WORKOUTTOOL` | Manage wger workout operations. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>132 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `wger_create_day` | `APITOOL` | Create a workout day in a routine. |
| `wger_create_max_repetitions_config` | `APITOOL` | Create a max repetitions config. |
| `wger_create_max_rest_config` | `APITOOL` | Create a max rest config. |
| `wger_create_max_rir_config` | `APITOOL` | Create a max RiR config. |
| `wger_create_max_sets_config` | `APITOOL` | Create a max sets config. |
| `wger_create_max_weight_config` | `APITOOL` | Create a max weight config. |
| `wger_create_meal` | `APITOOL` | Create a meal in a nutrition plan. |
| `wger_create_meal_item` | `APITOOL` | Add an ingredient to a meal. |
| `wger_create_measurement` | `APITOOL` | Log a body measurement. |
| `wger_create_measurement_category` | `APITOOL` | Create a measurement category. |
| `wger_create_nutrition_diary_entry` | `APITOOL` | Log a nutrition diary entry. |
| `wger_create_nutrition_plan` | `APITOOL` | Create a nutrition plan. |
| `wger_create_repetitions_config` | `APITOOL` | Create a repetitions config. |
| `wger_create_rest_config` | `APITOOL` | Create a rest time config. |
| `wger_create_rir_config` | `APITOOL` | Create a RiR config. |
| `wger_create_routine` | `APITOOL` | Create a new routine. |
| `wger_create_sets_config` | `APITOOL` | Create a sets config. |
| `wger_create_slot` | `APITOOL` | Create a slot (set) in a day. |
| `wger_create_slot_entry` | `APITOOL` | Create a slot entry (add exercise to slot). |
| `wger_create_weight_config` | `APITOOL` | Create a weight progression config. |
| `wger_create_weight_entry` | `APITOOL` | Log a body weight entry. |
| `wger_create_workout_log` | `APITOOL` | Create a workout log entry. |
| `wger_create_workout_session` | `APITOOL` | Create a workout session. Impression: 1=General discomfort, 2=Could be better, 3=Neutral, 4=Good, 5=Perfect. |
| `wger_delete_day` | `APITOOL` | Delete a day. |
| `wger_delete_meal` | `APITOOL` | Delete a meal. |
| `wger_delete_meal_item` | `APITOOL` | Delete a meal item. |
| `wger_delete_measurement` | `APITOOL` | Delete a measurement. |
| `wger_delete_measurement_category` | `APITOOL` | Delete a measurement category. |
| `wger_delete_nutrition_diary_entry` | `APITOOL` | Delete a nutrition diary entry. |
| `wger_delete_nutrition_plan` | `APITOOL` | Delete a nutrition plan. |
| `wger_delete_repetitions_config` | `APITOOL` | Delete a repetitions config. |
| `wger_delete_rest_config` | `APITOOL` | Delete a rest config. |
| `wger_delete_rir_config` | `APITOOL` | Delete a RiR config. |
| `wger_delete_routine` | `APITOOL` | Delete a routine. |
| `wger_delete_sets_config` | `APITOOL` | Delete a sets config. |
| `wger_delete_slot` | `APITOOL` | Delete a slot. |
| `wger_delete_slot_entry` | `APITOOL` | Delete a slot entry. |
| `wger_delete_weight_config` | `APITOOL` | Delete a weight config. |
| `wger_delete_weight_entry` | `APITOOL` | Delete a weight entry. |
| `wger_delete_workout_log` | `APITOOL` | Delete a workout log. |
| `wger_delete_workout_session` | `APITOOL` | Delete a workout session. |
| `wger_get_day` | `APITOOL` | Get a specific day. |
| `wger_get_days` | `APITOOL` | List all workout days. |
| `wger_get_deletion_log` | `APITOOL` | List deletion log entries. |
| `wger_get_equipment` | `APITOOL` | List equipment (e.g., Barbell, Dumbbell, etc.). |
| `wger_get_equipment_item` | `APITOOL` | Get a specific equipment. |
| `wger_get_exercise` | `APITOOL` | Get a specific exercise. |
| `wger_get_exercise_aliases` | `APITOOL` | List exercise aliases. |
| `wger_get_exercise_categories` | `APITOOL` | List exercise categories (e.g., Arms, Legs, etc.). |
| `wger_get_exercise_category` | `APITOOL` | Get a specific exercise category. |
| `wger_get_exercise_comments` | `APITOOL` | List exercise comments. |
| `wger_get_exercise_image` | `APITOOL` | Get a specific exercise image. |
| `wger_get_exercise_images` | `APITOOL` | List exercise images. |
| `wger_get_exercise_info` | `APITOOL` | Get detailed exercise info (includes translations, images, muscles, etc.). |
| `wger_get_exercise_infos` | `APITOOL` | List exercise infos. |
| `wger_get_exercise_translations` | `APITOOL` | List exercise translations. |
| `wger_get_exercise_videos` | `APITOOL` | List exercise videos. |
| `wger_get_exercises` | `APITOOL` | List exercises. Supports filters: language, category, muscles, equipment, etc. |
| `wger_get_gallery` | `APITOOL` | List progress gallery images. |
| `wger_get_ingredient` | `APITOOL` | Get a specific ingredient. |
| `wger_get_ingredient_images` | `APITOOL` | List ingredient images. |
| `wger_get_ingredient_info` | `APITOOL` | Get detailed ingredient info (includes weight units). |
| `wger_get_ingredient_weight_units` | `APITOOL` | List ingredient weight units. |
| `wger_get_ingredients` | `APITOOL` | List ingredients. Supports filters: language, name, etc. |
| `wger_get_languages` | `APITOOL` | List available languages. |
| `wger_get_licenses` | `APITOOL` | List content licenses. |
| `wger_get_max_repetitions_configs` | `APITOOL` | List max repetitions configs. |
| `wger_get_max_rest_configs` | `APITOOL` | List max rest configs. |
| `wger_get_max_rir_configs` | `APITOOL` | List max RiR configs. |
| `wger_get_max_sets_configs` | `APITOOL` | List max sets configs. |
| `wger_get_max_weight_configs` | `APITOOL` | List max weight configs. |
| `wger_get_meal` | `APITOOL` | Get a specific meal. |
| `wger_get_meal_item` | `APITOOL` | Get a specific meal item. |
| `wger_get_meal_items` | `APITOOL` | List meal items. |
| `wger_get_meals` | `APITOOL` | List meals. |
| `wger_get_measurement` | `APITOOL` | Get a specific measurement. |
| `wger_get_measurement_categories` | `APITOOL` | List measurement categories (e.g., Biceps, Chest, etc.). |
| `wger_get_measurement_category` | `APITOOL` | Get a specific measurement category. |
| `wger_get_measurements` | `APITOOL` | List body measurements. |
| `wger_get_muscle` | `APITOOL` | Get a specific muscle. |
| `wger_get_muscles` | `APITOOL` | List muscles. |
| `wger_get_nutrition_diary` | `APITOOL` | List nutrition diary entries. |
| `wger_get_nutrition_plan` | `APITOOL` | Get a specific nutrition plan. |
| `wger_get_nutrition_plan_info` | `APITOOL` | Get detailed nutrition plan info (includes meals, items, nutritional values). |
| `wger_get_nutrition_plans` | `APITOOL` | List nutrition plans. |
| `wger_get_public_templates` | `APITOOL` | List public workout templates. |
| `wger_get_repetition_units` | `APITOOL` | List repetition unit settings. |
| `wger_get_repetitions_configs` | `APITOOL` | List repetitions configs. |
| `wger_get_rest_configs` | `APITOOL` | List rest time configs. |
| `wger_get_rir_configs` | `APITOOL` | List RiR configs. |
| `wger_get_routine` | `APITOOL` | Get a specific routine by ID. |
| `wger_get_routines` | `APITOOL` | List all routines. |
| `wger_get_sets_configs` | `APITOOL` | List sets configs. |
| `wger_get_slot` | `APITOOL` | Get a specific slot. |
| `wger_get_slot_entries` | `APITOOL` | List all slot entries. |
| `wger_get_slot_entry` | `APITOOL` | Get a specific slot entry. |
| `wger_get_slots` | `APITOOL` | List all slots (sets). |
| `wger_get_template` | `APITOOL` | Get a specific template. |
| `wger_get_templates` | `APITOOL` | List user's workout templates. |
| `wger_get_trophies` | `APITOOL` | List available trophies. |
| `wger_get_user_profile` | `APITOOL` | Get the current user's profile. |
| `wger_get_user_statistics` | `APITOOL` | Get user statistics (workout count, etc.). |
| `wger_get_user_trophies` | `APITOOL` | List user's earned trophies. |
| `wger_get_variations` | `APITOOL` | List exercise variations. |
| `wger_get_weight_config` | `APITOOL` | Get a specific weight config. |
| `wger_get_weight_configs` | `APITOOL` | List weight progression configs. |
| `wger_get_weight_entries` | `APITOOL` | List body weight entries. |
| `wger_get_weight_entry` | `APITOOL` | Get a specific weight entry. |
| `wger_get_weight_unit_settings` | `APITOOL` | List weight unit settings. |
| `wger_get_weight_units` | `APITOOL` | List weight units. |
| `wger_get_workout_log` | `APITOOL` | Get a specific workout log. |
| `wger_get_workout_logs` | `APITOOL` | List workout logs. |
| `wger_get_workout_session` | `APITOOL` | Get a specific workout session. |
| `wger_get_workout_sessions` | `APITOOL` | List workout sessions. |
| `wger_search_exercises` | `APITOOL` | Search exercises. |
| `wger_update_day` | `APITOOL` | Update a day. |
| `wger_update_meal` | `APITOOL` | Update a meal. |
| `wger_update_meal_item` | `APITOOL` | Update a meal item. |
| `wger_update_measurement` | `APITOOL` | Update a measurement. |
| `wger_update_nutrition_plan` | `APITOOL` | Update a nutrition plan. |
| `wger_update_repetitions_config` | `APITOOL` | Update a repetitions config. |
| `wger_update_rest_config` | `APITOOL` | Update a rest config. |
| `wger_update_rir_config` | `APITOOL` | Update a RiR config. |
| `wger_update_routine` | `APITOOL` | Update a routine. |
| `wger_update_sets_config` | `APITOOL` | Update a sets config. |
| `wger_update_slot` | `APITOOL` | Update a slot. |
| `wger_update_slot_entry` | `APITOOL` | Update a slot entry. |
| `wger_update_user_profile` | `APITOOL` | Update user profile. Fields: age, height, gender, etc. |
| `wger_update_weight_config` | `APITOOL` | Update a weight config. |
| `wger_update_weight_entry` | `APITOOL` | Update a weight entry. |
| `wger_update_workout_log` | `APITOOL` | Update a workout log. |
| `wger_update_workout_session` | `APITOOL` | Update a workout session. |

</details>

_7 action-routed tool(s) (default) · 132 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (`condensed` default · `verbose` 1:1 · `both`). Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](docs/mcp.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

<!-- MCP-CONFIG-EXAMPLES:START -->

> **Install the slim `[mcp]` extra.** All examples install `wger-agent[mcp]` — the
> MCP-server extra that pulls only the FastMCP / FastAPI tooling (`agent-utilities[mcp]`).
> It deliberately **excludes** the heavy agent runtime (`pydantic-ai`, the epistemic-graph
> engine, `dspy`, `llama-index`), so `uvx` / container installs are far smaller. Use the
> full `[agent]` extra only when you need the integrated Pydantic AI agent.

#### stdio Transport (local IDEs — Cursor, Claude Desktop, VS Code)

```json
{
  "mcpServers": {
    "wger-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "wger-agent[mcp]",
        "wger-mcp"
      ],
      "env": {
        "MCP_TOOL_MODE": "condensed",
        "BODYTOOL": "True",
        "EXERCISETOOL": "True",
        "NUTRITIONTOOL": "True",
        "ROUTINECONFIGTOOL": "True",
        "ROUTINETOOL": "True",
        "USERTOOL": "True",
        "WGER_ACCESS_TOKEN": "your_api_token_here",
        "WGER_TOKEN": "your_api_token_here",
        "WGER_URL": "http://localhost:8000",
        "WGER_VERIFY": "True",
        "WORKOUTTOOL": "True"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (networked / production)

```json
{
  "mcpServers": {
    "wger-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "wger-agent[mcp]",
        "wger-mcp",
        "--transport",
        "streamable-http",
        "--port",
        "8000"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "MCP_TOOL_MODE": "condensed",
        "BODYTOOL": "True",
        "EXERCISETOOL": "True",
        "NUTRITIONTOOL": "True",
        "ROUTINECONFIGTOOL": "True",
        "ROUTINETOOL": "True",
        "USERTOOL": "True",
        "WGER_ACCESS_TOKEN": "your_api_token_here",
        "WGER_TOKEN": "your_api_token_here",
        "WGER_URL": "http://localhost:8000",
        "WGER_VERIFY": "True",
        "WORKOUTTOOL": "True"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed Streamable-HTTP instance by `url`:

```json
{
  "mcpServers": {
    "wger-mcp": {
      "url": "http://localhost:8000/wger-mcp/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name wger-mcp-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e HOST=0.0.0.0 \
  -e PORT=8000 \
  -e MCP_TOOL_MODE=condensed \
  -e BODYTOOL=True \
  -e EXERCISETOOL=True \
  -e NUTRITIONTOOL=True \
  -e ROUTINECONFIGTOOL=True \
  -e ROUTINETOOL=True \
  -e USERTOOL=True \
  -e WGER_ACCESS_TOKEN=your_api_token_here \
  -e WGER_TOKEN=your_api_token_here \
  -e WGER_URL=http://localhost:8000 \
  -e WGER_VERIFY=True \
  -e WORKOUTTOOL=True \
  knucklessg1/wger-agent:mcp
```

_Auto-generated from the code-read env surface (`MCP_TOOL_MODE` + package vars) — do not edit._
<!-- MCP-CONFIG-EXAMPLES:END -->

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`wger-agent` can also run as a **local container** (Docker / Podman / `uv`) or be
consumed from a **remote deployment**. The
[Deployment guide](https://knuckles-team.github.io/wger-agent/deployment/) has full, copy-paste
`mcp_config.json` for all four transports — **stdio**, **streamable-http**,
**local container / uv**, and **remote URL**:

- **Local container / uv** — launch the server from `mcp_config.json` via `uvx`,
  `docker run`, or `podman run`, or point at a local streamable-http container by `url`.
- **Remote URL** — connect to a server deployed behind Caddy at
  `http://wger-mcp.arpa/mcp` using the `"url"` key.
<!-- END GENERATED: additional-deployment-options -->

---

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | `pk-...` |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | `sk-...` |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `WGER_URL` | `http://localhost:8000` | Wger instance base URL (preferred) |
| `WGER_INSTANCE` | `https://wger.de` | Wger instance base URL (fallback when WGER_URL is unset) |
| `WGER_TOKEN` | `your_api_token_here` | Wger API token (preferred auth) |
| `WGER_ACCESS_TOKEN` | `your_api_token_here` | Wger API token (fallback when WGER_TOKEN is unset) |
| `WGER_SSL_VERIFY` | `True` | Verify TLS certificates (preferred) |
| `WGER_VERIFY` | `True` | Verify TLS certificates (fallback when WGER_SSL_VERIFY is unset) |
| `ROUTINETOOL` | `True` |  |
| `ROUTINECONFIGTOOL` | `True` |  |
| `EXERCISETOOL` | `True` |  |
| `WORKOUTTOOL` | `True` |  |
| `NUTRITIONTOOL` | `True` |  |
| `BODYTOOL` | `True` |  |
| `USERTOOL` | `True` |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_TOOL_MODE` | `condensed` | Tool surface: `condensed` | `verbose` | `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP auth (`oidc-client-credentials` for fleet calls) |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET` | — | OIDC client secret (service-account auth) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_24 package + 14 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads, grouped by purpose.

### Connection & Credentials
| Variable | Description | Default |
|----------|-------------|---------|
| `WGER_URL` | Base URL of the Wger Workout Manager instance (preferred) | `http://localhost:8000` |
| `WGER_INSTANCE` | Base URL fallback when `WGER_URL` is unset | `https://wger.de` |
| `WGER_TOKEN` | Wger API token (preferred auth) | — |
| `WGER_ACCESS_TOKEN` | Wger API token fallback when `WGER_TOKEN` is unset | — |
| `WGER_SSL_VERIFY` | Verify TLS certificates (preferred) | `True` |
| `WGER_VERIFY` | Verify TLS certificates fallback when `WGER_SSL_VERIFY` is unset | `True` |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse` | `stdio` |
| `HOST` | Bind host (HTTP transports) | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both` | `condensed` |
| `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS` | Comma-separated tool allow/deny list | — |
| `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS` | Comma-separated tag allow/deny list | — |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |

### Tool toggles
Each action-routed tool can be disabled individually via its toggle env var (set to `false`).
The full list is in the [Available MCP Tools](#available-mcp-tools) table above.

| Variable | Description | Default |
|----------|-------------|---------|
| `ROUTINETOOL` | Enable the routine tool | `True` |
| `ROUTINECONFIGTOOL` | Enable the routine-config tool | `True` |
| `EXERCISETOOL` | Enable the exercise tool | `True` |
| `WORKOUTTOOL` | Enable the workout tool | `True` |
| `NUTRITIONTOOL` | Enable the nutrition tool | `True` |
| `BODYTOOL` | Enable the body-measurement tool | `True` |
| `USERTOOL` | Enable the user tool | `True` |

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`) | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote` | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL | — |

### Agent CLI (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_URL` | URL of the MCP server the agent connects to | `http://localhost:8000/mcp` |
| `PROVIDER` | LLM provider (e.g. `openai`) | `openai` |
| `MODEL_ID` | Model id (e.g. `gpt-4o`) | `gpt-4o` |
| `ENABLE_WEB_UI` | Serve the AG-UI web interface | `True` |

See [`.env.example`](.env.example) for a copy-paste starting point.

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export WGER_URL="your_value"
export WGER_TOKEN="your_value"

# Run the agent server
wger-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  wger-agent-mcp:
    image: knucklessg1/wger-agent:mcp
    container_name: wger-agent-mcp
    hostname: wger-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  wger-agent-agent:
    image: knucklessg1/wger-agent:latest
    container_name: wger-agent-agent
    hostname: wger-agent-agent
    restart: always
    depends_on:
      - wger-agent-mcp
    env_file:
      - ../.env
    command: [ "wger-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://wger-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](docs/agent.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `wger-agent[mcp]` | Slim MCP server only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only run the **MCP server** (smallest install / image) |
| `wger-agent[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** |
| `wger-agent[all]` | Everything (`mcp` + `agent` + `logfire`) | Development / both surfaces |

```bash
# MCP server only (recommended for tool hosting — slim deps)
uv pip install "wger-agent[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "wger-agent[agent]"

# Everything (development)
uv pip install "wger-agent[all]"      # or: python -m pip install "wger-agent[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `knucklessg1/wger-agent:mcp` | `--target mcp` | `wger-agent[mcp]` — **slim**, no engine/`pydantic-ai`/`dspy`/`llama-index`/`tree-sitter` | `wger-mcp` |
| `knucklessg1/wger-agent:latest` | `--target agent` (default) | `wger-agent[agent]` — **full** agent runtime + epistemic-graph engine | `wger-agent` |

```bash
docker build --target mcp   -t knucklessg1/wger-agent:mcp    docker/   # slim MCP server
docker build --target agent -t knucklessg1/wger-agent:latest docker/   # full agent
```

`docker/mcp.compose.yml` runs the slim `:mcp` server; `docker/agent.compose.yml` runs the
agent (`:latest`) with a co-located `:mcp` sidecar.

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]` / `:latest`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` server does **not** require the database.

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/wger-agent/) and is the
recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/wger-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/wger-agent/deployment/) | run the MCP and agent servers, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/wger-agent/usage/) | the MCP tools, the `WgerApi` client, the agent CLI |
| [Backing Platform](https://knuckles-team.github.io/wger-agent/platform/) | deploy the Wger Workout Manager with Docker |
| [Overview](https://knuckles-team.github.io/wger-agent/overview/) | the standardized agent-package pattern |
| [Concepts](https://knuckles-team.github.io/wger-agent/concepts/) | concept registry (`CONCEPT:WGER-*`) |

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `wger-agent` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx wger-mcp` · or `uv tool install wger-agent` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/wger-agent:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
