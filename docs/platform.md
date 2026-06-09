# Backing Platform — Wger Workout Manager

`wger-agent` is a **client** of a [Wger Workout Manager](https://wger.de) instance.
This page provides a Docker recipe for deploying one locally to serve as the target
of `WGER_URL`. For production topologies, follow the upstream
[Wger documentation](https://wger.readthedocs.io/).

!!! note "Backing-system recipe"
    Each connector in the ecosystem follows the same convention — a
    `docs/platform.md` recipe for the system it integrates with, accompanied by a
    sample Compose stack that mirrors [`services/`](https://github.com/Knuckles-Team).
    Systems offered only as a managed service have no local recipe.

## Single-node deployment (Compose)

Wger publishes the `wger/server` image, which serves the application and REST API on
`:8000`, backed by PostgreSQL and Redis. The following stack runs the application
with its database, cache, and Celery worker:

```yaml
# docker/wger-platform.compose.yml
services:
  wger:
    image: docker.io/wger/server:latest
    container_name: wger
    depends_on:
      - wger-database
      - wger-cache
    ports:
      - "8000:80"
    environment:
      - DJANGO_DB_ENGINE=django.db.backends.postgresql
      - DJANGO_DB_DATABASE=wger
      - DJANGO_DB_USER=wger
      - DJANGO_DB_PASSWORD=wger
      - DJANGO_DB_HOST=wger-database
      - DJANGO_CACHE_BACKEND=django_redis.cache.RedisCache
      - DJANGO_CACHE_LOCATION=redis://wger-cache:6379/1
    volumes:
      - static:/home/wger/static
      - media:/home/wger/media
    healthcheck:
      test: ["CMD", "wget", "--no-verbose", "--tries=1", "--spider", "http://localhost"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 300s

  wger-database:
    image: docker.io/postgres:16-alpine
    environment:
      - POSTGRES_USER=wger
      - POSTGRES_PASSWORD=wger
      - POSTGRES_DB=wger
    volumes:
      - postgres-data:/var/lib/postgresql/data/

  wger-cache:
    image: docker.io/redis:latest
    volumes:
      - redis-data:/data

volumes:
  static:
  media:
  postgres-data:
  redis-data:
```

```bash
docker compose -f docker/wger-platform.compose.yml up -d

# Wait for the application to answer
curl http://localhost:8000/api/v2/
```

Create an API token from the Wger web console (Settings → API), or via the REST
token endpoint, and use it as `WGER_API_KEY`.

## Connect wger-agent

```bash
export WGER_URL=http://localhost:8000
export WGER_API_KEY=your_api_key

wger-mcp --transport streamable-http --host 0.0.0.0 --port 8001
```

## Combined deployment

A combined stack places the Wger platform and the MCP server on one Docker network,
so the server reaches Wger by container name:

```yaml
# docker/stack.compose.yml
services:
  wger:
    image: docker.io/wger/server:latest
    ports: ["8000:80"]
    environment:
      - DJANGO_DB_HOST=wger-database
      - DJANGO_DB_USER=wger
      - DJANGO_DB_PASSWORD=wger
      - DJANGO_DB_DATABASE=wger
    depends_on: [wger-database, wger-cache]

  wger-database:
    image: docker.io/postgres:16-alpine
    environment:
      - POSTGRES_USER=wger
      - POSTGRES_PASSWORD=wger
      - POSTGRES_DB=wger

  wger-cache:
    image: docker.io/redis:latest

  wger-agent-mcp:
    image: knucklessg1/wger-agent:latest
    depends_on: [wger]
    environment:
      - WGER_URL=http://wger:80
      - WGER_API_KEY=your_api_key
      - TRANSPORT=streamable-http
      - HOST=0.0.0.0
      - PORT=8001
    ports: ["8001:8001"]
```

```bash
docker compose -f docker/stack.compose.yml up -d
```
