---
name: wger-agent-development
skill_type: skill
domain: development
description: >-
  Develop, test, gate, and release the wger-agent connector. Use this skill when
  changing Wger API mappings, MCP tools, agent entry points, packaging,
  documentation, or repository gates.
license: MIT
tags: [wger-agent, development, connector, test, gates, wger]
tier: repository
metadata:
  author: Repository Maintainers
  version: '0.1.0'
---

# wger-agent development

This repository owns the Wger transport, API mappings, MCP tools, agent entry
points, packaged skills, and connector documentation. Shared connector
contracts and transports belong to `scion-sdk`; admission, serving, and durable
graph state belong to their owning repositories. Read `AGENTS.md` before
changing code and keep provider credentials and endpoints out of source, logs,
and skill content.

## Rapid delivery: the 5-minute contract

Specs are already designed. Deliver small, reviewable slices and cite the
owning spec row in the commit trailer.

- Find the owning row first with `git grep -n "<term>" -- specs` and extend
  that spec before adding new requirement text.
- Reuse existing SDK clients, transport policies, auth boundaries, and tool
  factories. Do not create a second implementation of a connector capability.
- Keep changes scoped to this connector. A change owned by the SDK, Arbora, or
  the knowledge graph belongs in that repository instead.
- Every delivered requirement needs a bound test. Generated `status.json` files
  are produced by `pipelines-hook spec-status`; never hand-edit them.
- One logical change per commit, with `Spec: <ID>` and the assisting agent
  trailer adjacent in the final paragraph.

## Setup and gates

Use the pinned environment from `uv sync --locked`, then run the repository gate
from the checkout root:

```bash
uv sync --locked
uvx pre-commit run --all-files
```

For focused feedback, run the actual repository tests with the pinned
environment:

```bash
uv run --all-extras pytest tests/test_publication_workflow.py -q
uv run --all-extras pytest tests/test_default_content_surfaces.py -q
uv run --all-extras pytest tests/test_fleet_name.py -q
uv run --all-extras pytest tests/test_wheel_inventory.py -q
```

The canonical `.pre-commit-config.yaml` delegates `connector-standard`,
`secrets`, `spec`, `tests-fast`, and `dependency-readiness` to
`Knuckles-Team/pipelines` at `rev: main`. Do not replace those shared hooks
with local copies or bypass a failing check.

## Connector-specific checks

- Preserve MCP and agent tool parity with `scion-sdk` and the existing Wger API
  client modules.
- Validate `WGER_URL`, `WGER_API_KEY`, and TLS settings before provider calls;
  handle missing credentials without leaking secrets.
- Mock external Wger calls in tests; never use live credentials in a local gate.
- Keep the source ontology mappings, fixtures, skills, and packaged prompts
  intact when adding or changing content; provider-generated shape and
  certification artifacts are created by the shared release gate.
- Documentation lives under `docs/` and is published by the shared Pages
  workflow; generated source status records live under `specs/`.

## Delivery discipline

Work in a real Git worktree based on `origin/main`. Inspect the complete diff,
stage only reviewed paths, and verify `git status --short` after every gate. Do
not use `git stash`, `git add -A`, or `git add .`; do not claim Pages publication
until a successful exact-source workflow run and the public page are both
observed.
