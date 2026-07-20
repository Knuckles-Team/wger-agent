"""Native epistemic-graph ingestion for wger wellness records.

All writes use the required ``agent_utilities.knowledge_graph.memory.native_ingest``
primitive. Nodes use canonical ``node_type`` and edges use canonical ``relationship``;
nodes and edges commit in one native transaction. Missing engine dependencies, rejected
records, conflicts, and transaction failures propagate as ``NativeIngestError``.
"""

from __future__ import annotations

import logging
from typing import Any

from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_documents as _native_ingest_documents,
)
from agent_utilities.knowledge_graph.memory.native_ingest import (
    ingest_entities as _native_ingest_entities,
)

logger = logging.getLogger("wger_agent.kg")

_SOURCE = "wger-agent"
_DOMAIN = "wellness"

def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write canonical typed nodes and relationships in one native transaction."""
    return _native_ingest_entities(
        entities, relationships, source=source, domain=domain, client=client, graph=graph
    )


def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Write text records as canonical Document nodes."""
    return _native_ingest_documents(
        documents, source=source, domain=domain, client=client, graph=graph
    )


def _records(resp: Any) -> list[dict[str, Any]]:
    """Normalise a wger API response (DRF list dict / single dict / list) to a list."""
    if resp is None:
        return []
    if isinstance(resp, dict):
        if isinstance(resp.get("results"), list):
            return [r for r in resp["results"] if isinstance(r, dict)]
        return [resp]
    if isinstance(resp, list):
        return [r for r in resp if isinstance(r, dict)]
    return []


def ingest_exercises(
    exercises: Any,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map wger exercise records → ``:Exercise`` nodes and ingest."""
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
    return ingest_entities(entities, client=client, graph=graph)


def ingest_routines(
    routines: Any,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map wger routine records → ``:WorkoutRoutine`` nodes and ingest."""
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
    return ingest_entities(entities, client=client, graph=graph)


def ingest_workout_sessions(
    sessions: Any,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map wger workout-session records → ``:WorkoutSession`` nodes (+ routine link)."""
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
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_nutrition_plans(
    plans: Any,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int]:
    """Map wger nutrition-plan records → ``:NutritionPlan`` nodes and ingest."""
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
    return ingest_entities(entities, client=client, graph=graph)
