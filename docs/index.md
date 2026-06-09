# wger-agent

Wger Workout Manager **MCP server + A2A agent** for the agent-utilities ecosystem
— exercise database, workout routines, nutrition plans, body measurements, and
progress tracking, exposed as typed, deterministic tools.

!!! info "Official documentation"
    This site is the canonical reference for `wger-agent`, maintained alongside every
    release.

[![PyPI](https://img.shields.io/pypi/v/wger-agent)](https://pypi.org/project/wger-agent/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/wger-agent)](https://github.com/Knuckles-Team/wger-agent/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/wger-agent)

## Overview

`wger-agent` wraps the [Wger Workout Manager](https://wger.de) REST API with
action-routed MCP tools and a Pydantic-AI graph agent. It provides:

- **`WgerApi`** — a unified Python client composed of domain-specific sub-clients
  (routine, exercise, nutrition, workout, body, user) over the Wger REST surface.
- **Action-routed MCP tools** across seven togglable domains, registered through the
  `agent-utilities` FastMCP middleware to minimize token overhead in LLM contexts.
- **An integrated graph agent** (the `wger-agent` console script) that speaks the
  Agent Control Protocol and the Agent Web UI, with a confidence-gated router that
  enables only the tools relevant to each request.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the MCP and agent servers, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the MCP tools, the `WgerApi` client, and the agent CLI.
- :material-database-cog: **[Backing Platform](platform.md)** — deploy the Wger Workout Manager with Docker.
- :material-sitemap: **[Architecture](overview.md)** — the standardized agent-package pattern.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:WGER-*` registry.

</div>

## Quick start

```bash
pip install wger-agent
wger-mcp                         # stdio MCP server (default transport)
```

Connect it to a Wger instance:

```bash
export WGER_URL=https://your-wger:8000
export WGER_API_KEY=your_api_key
wger-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, all transports, the agent server, reverse
proxy, DNS).
