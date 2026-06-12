# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`wger-agent` exposes its MCP server (console script `wger-mcp`) four ways. Pick the row that
matches where the server runs relative to your MCP client, then copy the matching
`mcp_config.json` below. Replace the `<your-…>` placeholders with the values from the **Configuration / Environment Variables** section.

| # | Option | Transport | Where it runs | `mcp_config.json` key |
|---|--------|-----------|---------------|------------------------|
| 1 | stdio | `stdio` | client launches a subprocess | `command` |
| 2 | Streamable-HTTP (local) | `streamable-http` | a local network port | `command` or `url` |
| 3 | Local container / uv | `stdio` or `streamable-http` | Docker / Podman / uv on this host | `command` or `url` |
| 4 | Remote URL | `streamable-http` | a remote host behind Caddy | `url` |

### 1. stdio (local subprocess)

The client launches the server over stdio via `uvx` — best for local IDEs
(Cursor, Claude Desktop, VS Code):

```json
{
  "mcpServers": {
    "wger-mcp": {
      "command": "uvx",
      "args": ["--from", "wger-agent", "wger-mcp"],
      "env": {
        "WGER_URL": "<your-wger_url>",
        "WGER_API_KEY": "<your-wger_api_key>"
      }
    }
  }
}
```

### 2. Streamable-HTTP (local process)

Run the server as a long-lived HTTP process:

```bash
uvx --from wger-agent wger-mcp --transport streamable-http --host 0.0.0.0 --port 8000
curl -s http://localhost:8000/health        # {"status":"OK"}
```

Then either let the client launch it:

```json
{
  "mcpServers": {
    "wger-mcp": {
      "command": "uvx",
      "args": ["--from", "wger-agent", "wger-mcp", "--transport", "streamable-http", "--port", "8000"],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "WGER_URL": "<your-wger_url>",
        "WGER_API_KEY": "<your-wger_api_key>"
      }
    }
  }
}
```

…or connect to the already-running process by URL:

```json
{
  "mcpServers": {
    "wger-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

### 3. Local container / uv

**(a) Launch a container directly from `mcp_config.json`** (stdio over the container —
no ports to manage). Swap `docker` for `podman` for a daemonless runtime:

```json
{
  "mcpServers": {
    "wger-mcp": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "TRANSPORT=stdio",
        "-e", "WGER_URL=<your-wger_url>",
        "-e", "WGER_API_KEY=<your-wger_api_key>",
        "knucklessg1/wger-agent:latest"
      ]
    }
  }
}
```

**(b) Run a local streamable-http container, then connect by URL:**

```bash
docker run -d --name wger-mcp -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e WGER_URL="<your-wger_url>" \
  -e WGER_API_KEY="<your-wger_api_key>" \
  knucklessg1/wger-agent:latest
# or, from a clone of this repo:
docker compose -f docker/mcp.compose.yml up -d
```

```json
{
  "mcpServers": {
    "wger-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

**(c) From a local checkout with `uv`:**

```bash
uv run wger-mcp --transport streamable-http --port 8000
```

### 4. Remote URL (deployed behind Caddy)

When the server is deployed remotely (e.g. as a Docker service) and published through
Caddy on the internal `*.arpa` zone, connect with the `"url"` key — no local process or
image required:

```json
{
  "mcpServers": {
    "wger-mcp": { "url": "http://wger-mcp.arpa/mcp" }
  }
}
```

Caddy reverse-proxies `http://wger-mcp.arpa` to the container's `:8000`
streamable-http listener; `http://wger-mcp.arpa/health` returns
`{"status":"OK"}` when the service is live.
<!-- END GENERATED: deployment-options -->

This page covers running `wger-agent` as long-lived servers: the transports, a Docker
Compose stack, the optional graph agent, putting it behind a Caddy reverse proxy, and
giving it a DNS name with Technitium. To provision the **Wger platform** it connects
to, see [Backing Platform](platform.md).

> `wger-agent` ships **two console scripts**: an **MCP server** (`wger-mcp`) and a
> **Pydantic-AI graph agent** (`wger-agent`). The MCP server is a typed, deterministic
> tool surface; the agent server orchestrates those tools behind the Agent Control
> Protocol and the Agent Web UI.

## Run the MCP server

The transport is selected with `--transport` (or the `TRANSPORT` env var):

=== "stdio (default)"

    ```bash
    wger-mcp
    ```
    For IDE / desktop MCP clients that launch the server as a subprocess.

=== "streamable-http"

    ```bash
    wger-mcp --transport streamable-http --host 0.0.0.0 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    wger-mcp --transport sse --host 0.0.0.0 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"OK"}
```

## Configuration (environment)

`wger-agent` is configured entirely from the environment. The **required** set:

| Var | Default | Meaning |
|---|---|---|
| `WGER_URL` | `https://wger.de` | Wger instance base URL |
| `WGER_API_KEY` | _(none)_ | Wger API token |
| `WGER_DEFAULT_EMAIL` | _(none)_ | Default account email |
| `WGER_DEFAULT_PASSWORD` | _(none)_ | Default account password |
| `TRANSPORT` | `stdio` | `stdio`, `streamable-http`, or `sse` |
| `HOST` | `0.0.0.0` | Bind address (HTTP transports) |
| `PORT` | `8000` | Bind port (HTTP transports) |

Each tool domain is registered through a toggle variable — `ROUTINETOOL`,
`ROUTINECONFIGTOOL`, `EXERCISETOOL`, `WORKOUTTOOL`, `NUTRITIONTOOL`, `BODYTOOL`,
`USERTOOL` (all default `True`). Telemetry (`ENABLE_OTEL`, OTLP exporter settings)
and access governance (`EUNOMIA_TYPE`, `EUNOMIA_POLICY_FILE`) are configured the same
way. The full set is documented in
[`.env.example`](https://github.com/Knuckles-Team/wger-agent/blob/main/.env.example).
Copy it to `.env` and populate only what you use; the connector remains inactive when
credentials are absent.

## Docker Compose

The repo ships [`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/wger-agent/blob/main/docker/mcp.compose.yml).
It reads a sibling `.env` and publishes the HTTP server on `:8000`:

```yaml
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
```

```bash
cp .env.example .env          # then edit WGER_* values
docker compose -f docker/mcp.compose.yml up -d
docker compose -f docker/mcp.compose.yml logs -f
```

## Agent server

To run the integrated Pydantic-AI graph agent, use the `wger-agent` console script.
It connects to the MCP server over `MCP_URL`, exposes the Agent Control Protocol and
the Agent Web UI on its own port (`9004` by convention), and routes each request to
the relevant tool domain.

```bash
export WGER_URL=https://your-wger:8000
export WGER_API_KEY=your_api_key
export MCP_URL=http://wger-agent-mcp:8000/mcp

wger-agent --provider openai --model-id gpt-4o
```

The repo ships
[`docker/agent.compose.yml`](https://github.com/Knuckles-Team/wger-agent/blob/main/docker/agent.compose.yml),
which deploys the MCP server and the agent together on one network so the agent
reaches the MCP server by container name:

```yaml
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

  wger-agent-agent:
    image: knucklessg1/wger-agent:latest
    container_name: wger-agent-agent
    hostname: wger-agent-agent
    restart: always
    depends_on:
      - wger-agent-mcp
    env_file:
      - ../.env
    command: ["wger-agent"]
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
```

```bash
docker compose -f docker/agent.compose.yml up -d
```

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .arpa zone
wger-agent.arpa {
    tls internal
    reverse_proxy wger-agent-mcp:8000
}
```

```caddy
# Public — automatic Let's Encrypt
wger-agent.example.com {
    reverse_proxy wger-agent-mcp:8000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "http://technitium.arpa:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=wger-agent.arpa" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=10.0.0.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `wger-agent.arpa → <caddy-host-ip>` in the Technitium web
console (`http://technitium.arpa:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to your client's `mcp_config.json`:

```json
{
  "mcpServers": {
    "wger-agent": {
      "command": "uvx",
      "args": ["--from", "wger-agent", "wger-mcp"],
      "env": {
        "WGER_URL": "https://your-wger:8000",
        "WGER_API_KEY": "your_api_key"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://wger-agent.arpa/mcp` instead.
