# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`wger-agent` supports local stdio, a loopback-only development listener, a
least-privilege stdio container, and a remote authenticated HTTPS boundary.
Provider endpoint, credential, selector, identity, and trust material are supplied
at runtime through `AgentConfig`; none is stored in this repository.

### Installed stdio process

```json
{
  "mcpServers": {
    "wger": {
      "command": "wger-mcp",
      "args": [],
      "env": {"MCP_TOOL_MODE": "intent"}
    }
  }
}
```

### Loopback development listener

```bash
wger-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

Do not expose this listener beyond loopback. Network deployments require direct TLS
or an explicitly trusted TLS-terminating ingress, configured authentication, exact
`MCP_ALLOWED_HOSTS`, and an exact trusted-proxy CIDR policy.

### Least-privilege local container

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  registry.example.invalid/wger-agent@sha256:<digest> wger-mcp
```

The operator projects the selected AgentConfig profile into the process at runtime;
the image remains immutable and contains no environment connection profile.

### Remote authenticated HTTPS endpoint

```json
{
  "mcpServers": {
    "wger": {"url": "https://service.example.invalid/mcp"}
  }
}
```

Store the real remote URL, outbound identity reference, and TLS-profile reference in
`AgentConfig`, not in MCP client JSON or documentation.
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
Copy it to `.env` and populate only what the operator use; the connector remains inactive when
credentials are absent.

## Docker Compose

The repo ships [`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/wger-agent/blob/main/docker/mcp.compose.yml).
It reads a sibling `.env` and publishes the HTTP server on `:8000`:

```yaml
services:
  wger-agent-mcp:
    image: example/wger-agent@sha256:<digest>
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
    image: example/wger-agent@sha256:<digest>
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
    image: example/wger-agent@sha256:<digest>
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

Expose the HTTP server on a hostname with automatic TLS. Add to the operator's `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .example.invalid zone
wger-agent.example.invalid {
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
curl -s "http://technitium.example.invalid:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=wger-agent.example.invalid" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=192.0.2.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `wger-agent.example.invalid → <caddy-host-ip>` in the Technitium web
console (`http://technitium.example.invalid:5380`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to the operator's client's `mcp_config.json`:

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

For a remote HTTP server, point the client at `http://wger-agent.example.invalid/mcp` instead.
