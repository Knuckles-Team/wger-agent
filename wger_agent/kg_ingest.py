"""Epistemic-graph ingestion for wger wellness records.

CONCEPT:AU-KG.ingest.enterprise-source-extractor. The wger-agent connector pushes
wger wellness records into the ONE epistemic-graph knowledge graph as **typed OWL
nodes** (``:Exercise``, ``:WorkoutRoutine``, ``:WorkoutSession``, ``:NutritionPlan``)
+ links through ``agent_connector_sdk.ingest`` -- the generated ``SourceIngest``
client, not a local ingestion helper. Node ids follow ``wellness:<class>:<externalId>``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_connector_sdk.ingest import (
    ChangeSet,
    Document,
    Entity,
    IngestBinding,
    IngestError,
    KnowledgeIngest,
    Relationship,
    current_ingest,
)

logger = logging.getLogger("wger_agent.kg")

_BINDING = IngestBinding(connector="wger-agent", stream="fitness")

_ENTITY_RESERVED_KEYS = frozenset({"id", "node_type"})
_RELATIONSHIP_RESERVED_KEYS = frozenset({"source", "target", "relationship"})


def _to_entity(record: dict[str, Any]) -> Entity:
    return Entity(
        id=record.get("id"),
        node_type=record.get("node_type"),
        properties={
            key: value
            for key, value in record.items()
            if key not in _ENTITY_RESERVED_KEYS
        },
    )


def _to_relationship(record: dict[str, Any]) -> Relationship:
    properties = {
        key: value
        for key, value in record.items()
        if key not in _RELATIONSHIP_RESERVED_KEYS
    }
    return Relationship(
        source=record["source"],
        target=record["target"],
        relationship=record["relationship"],
        properties=properties or None,
    )


async def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Write typed OWL nodes (+ edges) into epistemic-graph via the SDK ingest facade.

    Uses canonical ``node_type`` / ``relationship`` structural fields and surfaces
    a malformed change set or a refused commit as ``IngestError``.
    """
    if not entities:
        raise IngestError("ingest_entities needs at least one entity")
    change_set = ChangeSet(
        entities=tuple(_to_entity(entity) for entity in entities),
        relationships=tuple(
            _to_relationship(relationship) for relationship in relationships or ()
        ),
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


async def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Write text records as ``:Document`` nodes (semantic-search fodder).

    Each doc: ``{"id":..., "text":..., "title"?:..., "source_uri"?:..., ...props}``.
    """
    if not documents:
        raise IngestError("ingest_documents needs at least one document")
    change_set = ChangeSet(
        documents=tuple(
            Document(
                id=doc["id"],
                text=doc["text"],
                title=doc.get("title"),
                source_uri=doc.get("source_uri"),
                properties={
                    key: value
                    for key, value in doc.items()
                    if key not in {"id", "text", "title", "source_uri"}
                },
            )
            for doc in documents
        )
    )
    service = ingest or current_ingest()
    receipt = await service.submit(_BINDING, change_set)
    return {"nodes": receipt.affected_count, "edges": receipt.relationship_count}


def _dict_items(items: Any) -> list[dict[str, Any]]:
    """Return only the dict elements of an iterable, dropping anything else."""
    return [item for item in items if isinstance(item, dict)]


def _records(resp: Any) -> list[dict[str, Any]]:
    """Normalise a wger API response (DRF list dict / single dict / list) to a list."""
    if resp is None:
        return []
    if isinstance(resp, list):
        return _dict_items(resp)
    if not isinstance(resp, dict):
        return []
    results = resp.get("results")
    if isinstance(results, list):
        return _dict_items(results)
    return [resp]


async def ingest_exercises(
    exercises: Any,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map wger exercise records -> ``:Exercise`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for ex in _records(exercises):
        eid = ex.get("id")
        if eid is None:
            continue
        entities.append(
            {
                "id": f"wellness:exercise:{eid}",
                "node_type": "Exercise",
                "name": ex.get("name"),
                "uuid": ex.get("uuid"),
                "category": ex.get("category"),
                "last_update": ex.get("last_update"),
                "externalToolId": str(eid),
            }
        )
    return await ingest_entities(entities, ingest=ingest)


async def ingest_routines(
    routines: Any,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map wger routine records -> ``:WorkoutRoutine`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for rt in _records(routines):
        rid = rt.get("id")
        if rid is None:
            continue
        entities.append(
            {
                "id": f"wellness:routine:{rid}",
                "node_type": "WorkoutRoutine",
                "name": rt.get("name"),
                "description": rt.get("description"),
                "start_date": rt.get("start") or rt.get("start_date"),
                "end_date": rt.get("end") or rt.get("end_date"),
                "externalToolId": str(rid),
            }
        )
    return await ingest_entities(entities, ingest=ingest)


async def ingest_workout_sessions(
    sessions: Any,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map wger workout-session records -> ``:WorkoutSession`` nodes (+ routine link)."""
    entities: list[dict[str, Any]] = []
    relationships: list[dict[str, Any]] = []
    for s in _records(sessions):
        sid = s.get("id")
        if sid is None:
            continue
        node_id = f"wellness:session:{sid}"
        entities.append(
            {
                "id": node_id,
                "node_type": "WorkoutSession",
                "date": s.get("date"),
                "impression": s.get("impression"),
                "notes": s.get("notes"),
                "time_start": s.get("time_start"),
                "time_end": s.get("time_end"),
                "externalToolId": str(sid),
            }
        )
        routine = s.get("routine")
        if routine is not None:
            relationships.append(
                {
                    "source": node_id,
                    "target": f"wellness:routine:{routine}",
                    "relationship": "sessionOfRoutine",
                }
            )
    return await ingest_entities(entities, relationships, ingest=ingest)


async def ingest_nutrition_plans(
    plans: Any,
    *,
    ingest: KnowledgeIngest | None = None,
) -> dict[str, int]:
    """Map wger nutrition-plan records -> ``:NutritionPlan`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for p in _records(plans):
        pid = p.get("id")
        if pid is None:
            continue
        entities.append(
            {
                "id": f"wellness:nutritionplan:{pid}",
                "node_type": "NutritionPlan",
                "description": p.get("description"),
                "only_logging": p.get("only_logging"),
                "goalEnergy": p.get("goal_energy"),
                "goalProtein": p.get("goal_protein"),
                "goal_carbohydrates": p.get("goal_carbohydrates"),
                "goal_fat": p.get("goal_fat"),
                "creation_date": p.get("creation_date"),
                "externalToolId": str(pid),
            }
        )
    return await ingest_entities(entities, ingest=ingest)
