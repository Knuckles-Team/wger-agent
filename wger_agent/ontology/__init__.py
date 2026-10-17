"""Wellness ontology contribution (CONCEPT:AU-KG.ontology.package-federation-migration).

Data-only subpackage: it carries ``wellness.ttl`` (the ``owl:Ontology``
``http://knuckles.team/kg/wellness`` module — exercises, workout routines,
nutrition plans, body measurements and their relationships) which the
agent-connector-sdk hub federates in via the ``agent_connector_sdk.ontology_providers``
entry-point. It holds no business logic and no heavy imports so the hub can
resolve it cheaply.
"""
