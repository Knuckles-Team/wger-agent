# Installation

`wger-agent` is a standard Python package and a prebuilt container image. Pick the
path that matches how you want to run it.

## Requirements

- **Python 3.11 – 3.14**.
- A reachable **Wger Workout Manager** instance — see [Backing Platform](platform.md)
  to deploy one locally.

## From PyPI (recommended)

```bash
pip install wger-agent
```

### Optional extras

The base install ships the MCP server runtime. Install the extra for what you need:

| Extra | Install | Pulls in |
|---|---|---|
| _(base)_ | `pip install wger-agent` | `agent-utilities[mcp]` — the FastMCP MCP-server runtime |
| `agent` | `pip install "wger-agent[agent]"` | Pydantic-AI agent + Logfire tracing |
| `all` | `pip install "wger-agent[all]"` | MCP server, agent, and Logfire tracing |
| `test` | `pip install "wger-agent[test]"` | `pytest`, `pytest-asyncio`, `pytest-cov`, `pytest-xdist` |

```bash
# Typical: run the MCP server and the graph agent together
pip install "wger-agent[all]"
```

## From source

```bash
git clone https://github.com/Knuckles-Team/wger-agent.git
cd wger-agent
pip install -e ".[all]"          # editable install with every extra
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv pip install -e ".[all]"
uv run wger-mcp
```

## Prebuilt Docker image

A multi-stage, slim image is published on every release (entrypoint `wger-mcp`):

```bash
docker pull knucklessg1/wger-agent:latest

docker run --rm -i \
  -e WGER_URL=https://your-wger:8000 \
  -e WGER_API_KEY=your_api_key \
  knucklessg1/wger-agent:latest        # stdio transport (default)
```

For an HTTP server with a published port, or to run the agent server, see
[Deployment](deployment.md).

## Verify the install

```bash
wger-mcp --help
wger-agent --help
python -c "import wger_agent; print(wger_agent.__version__)"
```

## Next steps

- **[Deployment](deployment.md)** — run it as a long-lived MCP server and agent behind Caddy + DNS.
- **[Usage](usage.md)** — call the tools, the API, and the agent CLI.
- **[Configuration](deployment.md#configuration-environment)** — every environment variable.
