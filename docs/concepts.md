# Concept Registry — wger-agent

> **Prefix**: `CONCEPT:WGER-*`
> **Version**: 0.14.0
> **Bridge**: [`CONCEPT:AU-ECO.messaging.native-backend-abstraction`](https://github.com/Knuckles-Team/agent-utilities/blob/main/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:WG-OS.governance.wger` | Body Measurements | MCP tool domain `body` — Action-routed dynamic tool registration |
| `CONCEPT:WG-OS.governance.wger-2` | Exercise Library | MCP tool domain `exercise` — Action-routed dynamic tool registration |
| `CONCEPT:WG-OS.governance.wger-3` | Nutrition Tracking | MCP tool domain `nutrition` — Action-routed dynamic tool registration |
| `CONCEPT:WG-OS.governance.wger-4` | Routine Management | MCP tool domain `routine` — Action-routed dynamic tool registration |
| `CONCEPT:WG-OS.governance.wger-5` | Routineconfig Operations | MCP tool domain `routineconfig` — Action-routed dynamic tool registration |
| `CONCEPT:WG-OS.governance.wger-6` | User & Identity Management | MCP tool domain `user` — Action-routed dynamic tool registration |
| `CONCEPT:WG-OS.governance.wger-7` | Workout Logging | MCP tool domain `workout` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-utilities)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:AU-ECO.messaging.native-backend-abstraction` | Unified Toolkit Ingestion | agent-utilities |
| `CONCEPT:AU-ORCH.adapter.hot-cache-invalidation` | Confidence-Gated Router | agent-utilities |
| `CONCEPT:AU-OS.config.secrets-authentication` | Prompt Injection Defense | agent-utilities |
| `CONCEPT:AU-OS.state.cognitive-scheduler-preemption` | Cognitive Scheduler | agent-utilities |
| `CONCEPT:AU-OS.governance.reactive-multi-axis-budget` | Guardrail Engine | agent-utilities |
| `CONCEPT:AU-OS.governance.wasm-micro-agent-sandbox` | Audit Logging | agent-utilities |
| `CONCEPT:AU-KG.query.object-graph-mapper` | Knowledge Graph Core | agent-utilities |

## Synergy with agent-utilities

This project integrates with `agent-utilities` via `CONCEPT:AU-ECO.messaging.native-backend-abstraction` (Unified Toolkit Ingestion). The `wger_agent` MCP server registers its tools with the agent-utilities FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all WGER-* concepts.
