---
name: wger-agent-operations
skill_type: skill
description: >-
  Operate wger-agent through its governed MCP and Arbora capabilities, including wger agent docs, wger exercise library, wger nutrition tracking, wger workout routines. Use when a request requires this provider's read, change, automation, ingestion, troubleshooting, or evidence workflows.
---

# Wger Agent Operations

Use the provider's governed MCP tools through Arbora delegation.

## Workflow

1. Establish the verified GraphSession and tenant before discovery or retrieval.
2. Discover the current condensed tool surface; never assume a stale tool name or schema.
3. Prefer read-only inspection first. For changes, present impact and use the provider's
   dry-run or preview mode when available.
4. Execute mutations as fenced WorkItems so retries remain idempotent and auditable.
5. Ingest source data only through the signed connector preset and ChangeEnvelope path.
6. Verify the durable result and its trace/evidence before reporting completion.

## Safety contract

- Never persist credentials, endpoints, raw personal identifiers, hostnames, or local paths.
- Resolve TLS trust and verification from environment/configuration; never hardcode bypasses.
- Treat unknown ACL, tenant, schema, or tool-contract state as a hard failure.
- Require explicit approval for destructive, externally visible, or irreversible actions.
- Keep runtime traces policy-scoped and privacy-sanitized.

## Steps

1. Confirm the session and tenant with `find(intent="wger")`. Verify Arbora reports the GraphSession and tenant.
2. Discover the tool surface with `find(intent="wger workout")`. Verify the tool you plan to call appears with its parameter schema.
3. Inspect read-only first with `act(op="fleet.call", params={"server": "wger-agent", "tool": "wger_get_routines", "arguments": {"limit": 5}})`. Verify the response holds a `results` list.
4. Run a change as a fenced WorkItem with `act(op="fleet.call", ...)` after previewing it and getting approval. Verify the preview names the object and effect before you execute.
5. Check the outcome with the matching read tool such as `wger_get_routine`. Verify the object shows the expected values and a trace id exists.

## Failure recovery

| Failure | Cause | Recovery |
|---------|-------|----------|
| Tool not found | Stale tool name | Call `find(intent="wger")` again and use the name it returns |
| 401 from the connector | `WGER_ACCESS_TOKEN` missing in the deployment | Ask the deployment owner to set `WGER_ACCESS_TOKEN` and call `wger_get_user_profile` to confirm |
| Mutation refused | Approval not given or ACL unknown | Present the impact to the requester, obtain explicit approval and resubmit with the returned plan reference |

## Specialized workflows

Read [the workflow catalog](references/catalog.md) only when the request needs a
provider-specific procedure, parameter map, script, or reference asset.
