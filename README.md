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

*Version: 0.28.0*

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
| Tool Module | Toggle Env Var | Enabled by Default | Description & Nested Methods |
|-------------|----------------|--------------------|------------------------------|
| **Routine** | `ROUTINETOOL` | `True` | Manage wger routine operations. Action-routed methods: `create_day`, `create_routine`, `create_slot`, `create_slot_entry`, `delete_day`, `delete_routine`, `get_days`, `get_public_templates`, `get_routine`, `get_routines`, `get_slots`, `get_templates`. |
| **Routineconfig** | `ROUTINECONFIGTOOL` | `True` | Manage wger routineconfig operations. Action-routed methods: `create_repetitions_config`, `create_rest_config`, `create_rir_config`, `create_sets_config`, `create_weight_config`, `get_repetitions_configs`, `get_weight_configs`. |
| **Exercise** | `EXERCISETOOL` | `True` | Manage wger exercise operations. Action-routed methods: `get_equipment`, `get_exercise_categories`, `get_exercise_images`, `get_exercise_info`, `get_exercises`, `get_muscles`, `get_variations`, `search_exercises`. |
| **Workout** | `WORKOUTTOOL` | `True` | Manage wger workout operations. Action-routed methods: `create_workout_log`, `create_workout_session`, `delete_workout_log`, `delete_workout_session`, `get_workout_logs`, `get_workout_session`, `get_workout_sessions`. |
| **Nutrition** | `NUTRITIONTOOL` | `True` | Manage wger nutrition operations. Action-routed methods: `create_meal`, `create_meal_item`, `create_nutrition_plan`, `delete_nutrition_plan`, `get_ingredient_info`, `get_ingredients`, `get_nutrition_diary`, `get_nutrition_plan_info`, `get_nutrition_plans`, `log_nutrition`. |
| **Body** | `BODYTOOL` | `True` | Manage wger body operations. Action-routed methods: `create_measurement_category`, `delete_weight_entry`, `get_gallery`, `get_measurement_categories`, `get_measurements`, `get_weight_entries`, `log_body_weight`, `log_measurement`. |
| **User** | `USERTOOL` | `True` | Manage wger user operations. Action-routed methods: `get_languages`, `get_repetition_units`, `get_user_profile`, `get_user_statistics`, `get_user_trophies`, `get_weight_unit_settings`. |

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

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "wger-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "wger-agent",
        "wger-mcp"
      ],
      "env": {
        "WGER_URL": "your_wger_url_here",
        "WGER_API_KEY": "your_wger_api_key_here",
        "WGER_DEFAULT_EMAIL": "your_wger_default_email_here",
        "WGER_DEFAULT_PASSWORD": "your_wger_default_password_here"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (Recommended for production deployments)
Configure your client's `mcp.json` to launch the Streamable-HTTP server via `uvx` with explicit host and port definition:

```json
{
  "mcpServers": {
    "wger-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "wger-agent",
        "wger-mcp"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "WGER_URL": "your_wger_url_here",
        "WGER_API_KEY": "your_wger_api_key_here",
        "WGER_DEFAULT_EMAIL": "your_wger_default_email_here",
        "WGER_DEFAULT_PASSWORD": "your_wger_default_password_here"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed remote or local Streamable-HTTP instance:

```json
{
  "mcpServers": {
    "wger-agent": {
      "url": "http://localhost:8000/wger-agent/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name wger-agent-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e WGER_URL="your_value" \
  -e WGER_API_KEY="your_value" \
  -e WGER_DEFAULT_EMAIL="your_value" \
  -e WGER_DEFAULT_PASSWORD="your_value" \
  knucklessg1/wger-agent:latest
```

---

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export WGER_URL="your_value"
export WGER_API_KEY="your_value"
export WGER_DEFAULT_EMAIL="your_value"
export WGER_DEFAULT_PASSWORD="your_value"

# Run the agent server
wger-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  wger-agent-mcp:
    image: knucklessg1/wger-agent:latest
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

Install the Python package locally:

```bash
# Using uv (highly recommended)
uv pip install wger-agent[all]

# Using standard pip
python -m pip install wger-agent[all]
```

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
