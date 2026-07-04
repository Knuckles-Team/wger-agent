"""wger source-connector contribution (CONCEPT:AU-KG.ingest.mcp-tool-connector).

Data-only subpackage: it carries ``mcp_source_presets.json`` (Tier-1 ``mcp_tool``
source presets that sync wger wellness data into the KG via the wger-agent MCP
server) which the agent-utilities hub discovers via the
``agent_utilities.source_connector_providers`` entry-point. It holds no business
logic and no heavy imports so the hub can resolve it cheaply.
"""
