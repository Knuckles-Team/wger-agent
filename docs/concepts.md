# Concept Registry — wger-agent

> **Prefix**: `CONCEPT:WGER-*`
> **Version**: 0.14.0
> **Bridge**: [`CONCEPT:ECO-4.0`](https://github.com/Knuckles-Team/agent-utilities/blob/main/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:WGER-001` | Body Measurements | MCP tool domain `body` — Action-routed dynamic tool registration |
| `CONCEPT:WGER-002` | Exercise Library | MCP tool domain `exercise` — Action-routed dynamic tool registration |
| `CONCEPT:WGER-003` | Nutrition Tracking | MCP tool domain `nutrition` — Action-routed dynamic tool registration |
| `CONCEPT:WGER-004` | Routine Management | MCP tool domain `routine` — Action-routed dynamic tool registration |
| `CONCEPT:WGER-005` | Routineconfig Operations | MCP tool domain `routineconfig` — Action-routed dynamic tool registration |
| `CONCEPT:WGER-006` | User & Identity Management | MCP tool domain `user` — Action-routed dynamic tool registration |
| `CONCEPT:WGER-007` | Workout Logging | MCP tool domain `workout` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-utilities)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:ECO-4.0` | Unified Toolkit Ingestion | agent-utilities |
| `CONCEPT:ORCH-1.2` | Confidence-Gated Router | agent-utilities |
| `CONCEPT:OS-5.1` | Prompt Injection Defense | agent-utilities |
| `CONCEPT:OS-5.2` | Cognitive Scheduler | agent-utilities |
| `CONCEPT:OS-5.3` | Guardrail Engine | agent-utilities |
| `CONCEPT:OS-5.4` | Audit Logging | agent-utilities |
| `CONCEPT:KG-2.0` | Knowledge Graph Core | agent-utilities |

## Synergy with agent-utilities

This project integrates with `agent-utilities` via `CONCEPT:ECO-4.0` (Unified Toolkit Ingestion). The `wger_agent` MCP server registers its tools with the agent-utilities FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all WGER-* concepts.
