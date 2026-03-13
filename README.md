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

*Version: 0.1.15*

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
