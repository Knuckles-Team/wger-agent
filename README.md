# Wger - A2A | AG-UI | MCP

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

*Version: 0.11.1*

## Overview

**Wger MCP Server + A2A Agent**

Wger Workout Manager — exercise database, workout routines, nutrition plans, body measurements, and progress tracking.

This repository is actively maintained - Contributions are welcome!

## MCP

### Using as an MCP Server

The MCP Server can be run in two modes: `stdio` (for local testing) or `http` (for networked access).

#### Environment Variables

*   `WGER_INSTANCE`: The URL of the target service.
*   `WGER_ACCESS_TOKEN`: The API token or access token.

#### Run in stdio mode (default):
```bash
export WGER_INSTANCE="http://localhost:8080"
export WGER_ACCESS_TOKEN="your_token"
wger-mcp --transport "stdio"
```

#### Run in HTTP mode:
```bash
export WGER_INSTANCE="http://localhost:8080"
export WGER_ACCESS_TOKEN="your_token"
wger-mcp --transport "http" --host "0.0.0.0" --port "8000"
```

## A2A Agent

### Run A2A Server
```bash
export WGER_INSTANCE="http://localhost:8080"
export WGER_ACCESS_TOKEN="your_token"
wger-agent --provider openai --model-id gpt-4o --api-key sk-...
```

## Security & Governance

This project is built on [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities), inheriting enterprise-grade security and governance features.

### Authentication & Authorization
| Feature | Description |
|---------|-------------|
| **OIDC Token Delegation** | RFC 8693 token exchange for user-context propagation from A2A → MCP |
| **Eunomia Policies** | Fine-grained, policy-driven tool authorization (`none`, `embedded`, `remote`) |
| **Scoped Credentials** | Tools execute with the caller's scoped identity where possible |
| **3LO / OAuth / API Token** | Multiple auth strategies with graceful fallback |

### Eunomia Policy Enforcement
Eunomia provides a policy enforcement point for all tool calls:
- **Embedded mode**: Load local `mcp_policies.json` for role-based access, sensitivity gating, and audit logging
- **Remote mode**: Forward authorization decisions to a central Eunomia policy server for multi-agent governance
- Enable via CLI: `--eunomia-type embedded --eunomia-policy-file mcp_policies.json`

### Runtime Protections
| Protection | Description |
|------------|-------------|
| **Tool Guard** | Sensitivity detection with human-in-the-loop approval gating |
| **Prompt Injection Defense** | Input scanning and repetition/loop guards |
| **Content Filtering** | Output schema enforcement and cost budget controls |
| **Stuck Loop Detection** | Automatic detection and recovery from agent loops |
| **Context Limit Warnings** | Proactive alerts before context window exhaustion |

### Graph Agent Architecture
The A2A agent uses `pydantic-graph` orchestration with:
- **RouterNode**: Lightweight classifier that routes queries to specialized domains
- **DomainNode**: Focused executor with only relevant tools loaded, preventing tool hallucination
- **Approval Gates**: Policy-driven approval workflows before sensitive operations
- **Usage Guards**: Budget and rate limiting enforcement

> **Production Recommendation**: Enable `--eunomia-type embedded` (or `remote`) + OIDC delegation + containerized deployment. See [`agent-utilities` documentation](https://github.com/Knuckles-Team/agent-utilities) for full policy configuration.

## Docker

### Build

```bash
docker build -t wger-agent .
```

### Run MCP Server

```bash
docker run -d \
  --name wger-agent \
  -p 8000:8000 \
  -e TRANSPORT=http \
  -e WGER_INSTANCE="http://your-service:8080" \
  -e WGER_ACCESS_TOKEN="your_token" \
  knucklessg1/wger-agent:latest
```

### Deploy with Docker Compose

```yaml
services:
  wger-agent:
    image: knucklessg1/wger-agent:latest
    environment:
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=http
      - WGER_INSTANCE=http://your-service:8080
      - WGER_ACCESS_TOKEN=your_token
    ports:
      - 8000:8000
```

#### Configure `mcp.json` for AI Integration (e.g. Claude Desktop)

```json
{
  "mcpServers": {
    "wger": {
      "command": "uv",
      "args": [
        "run",
        "--with",
        "wger-agent",
        "wger-mcp"
      ],
      "env": {
        "WGER_INSTANCE": "http://your-service:8080",
        "WGER_ACCESS_TOKEN": "your_token"
      }
    }
  }
}
```

## Install Python Package

```bash
python -m pip install wger-agent
```
```bash
uv pip install wger-agent
```

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)


## Graph Architecture

This agent uses `pydantic-graph` orchestration for intelligent routing and optimal context management.

```mermaid
---
title: Wger Agent Graph Agent
---
stateDiagram-v2
  [*] --> RouterNode: User Query
  RouterNode --> DomainNode: Classified Domain
  RouterNode --> [*]: Low confidence / Error
  DomainNode --> [*]: Domain Result
```

- **RouterNode**: A fast, lightweight LLM (e.g., `nvidia/nemotron-3-super`) that classifies the user's query into one of the specialized domains.
- **DomainNode**: The executor node. For the selected domain, it dynamically sets environment variables to temporarily enable ONLY the tools relevant to that domain, creating a highly focused sub-agent (e.g., `gpt-4o`) to complete the request. This preserves LLM context and prevents tool hallucination.


## MCP Configuration Examples

### stdio (recommended for local development)
```json
{
  "mcpServers": {
    "wger": {
      "command": ".venv/bin/wger-mcp",
      "args": [],
      "env": {
        "WGER_INSTANCE": "",
        "WGER_ACCESS_TOKEN": ""
}
    }
  }
}
```

### Streamable HTTP (recommended for production)
```json
{
  "mcpServers": {
    "wger": {
      "url": "http://localhost:8080/wger-mcp/mcp"
    }
  }
}
```
## Available MCP Tools

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

| Tool Name | Description |
|-----------|-------------|
| `wger_body` | Consolidated Action-Routed tool for Body. Methods: get_weight_entries, log_body_weight, delete_weight_entry, get_measurements, log_measurement, get_measurement_categories, create_measurement_category, get_gallery |
| `wger_exercise` | Consolidated Action-Routed tool for Exercise. Methods: get_exercises, get_exercise_info, search_exercises, get_exercise_categories, get_equipment, get_muscles, get_exercise_images, get_variations |
| `wger_nutrition` | Consolidated Action-Routed tool for Nutrition. Methods: get_nutrition_plans, get_nutrition_plan_info, create_nutrition_plan, delete_nutrition_plan, create_meal, create_meal_item, get_ingredients, get_ingredient_info, get_nutrition_diary, log_nutrition |
| `wger_routine` | Consolidated Action-Routed tool for Routine. Methods: get_routines, get_routine, create_routine, delete_routine, get_days, create_day, delete_day, get_slots, create_slot, create_slot_entry, get_templates, get_public_templates |
| `wger_routineconfig` | Consolidated Action-Routed tool for RoutineConfig. Methods: create_weight_config, get_weight_configs, create_repetitions_config, get_repetitions_configs, create_sets_config, create_rest_config, create_rir_config |
| `wger_user` | Consolidated Action-Routed tool for User. Methods: get_user_profile, get_user_statistics, get_user_trophies, get_languages, get_repetition_units, get_weight_unit_settings |
| `wger_workout` | Consolidated Action-Routed tool for Workout. Methods: get_workout_sessions, get_workout_session, create_workout_session, delete_workout_session, get_workout_logs, create_workout_log, delete_workout_log |
