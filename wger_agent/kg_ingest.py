"""Native epistemic-graph ingestion for wger records (typed graph nodes).

CONCEPT:AU-KG.ingest.enterprise-source-extractor. The wger connector natively pushes
its wellness data into the ONE epistemic-graph knowledge graph as **typed OWL nodes**
(``:Exercise``, ``:WorkoutRoutine``, ``:WorkoutSession``, ``:NutritionPlan``,
``:BodyMeasurement``) + links, matching the classes federated by
``wger_agent.ontology`` (the ``http://knuckles.team/kg/wellness`` module).

This is a **thin mapper** over the shared fleet primitive
``agent_utilities.knowledge_graph.memory.native_ingest``. The import is guarded: when
that primitive (or the whole KG stack / a reachable engine) is absent, a self-contained
transaction fallback over the lightweight ``GraphComputeEngine()._client`` is used, and
if even that is unreachable every entry point **no-ops** (returns ``None``) so the
connector runs with zero KG infrastructure. Node ids follow
``wellness:<class>:<externalId>``.
"""

from __future__ import annotations

import logging
from typing import Any

logger = logging.getLogger("wger_agent.kg")

_SOURCE = "wger-agent"
_DOMAIN = "wellness"
_DEFAULT_GRAPH = "__commons__"

try:  # Prefer the shared fleet primitive when it is installed.
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        ingest_documents as _shared_ingest_documents,
    )
    from agent_utilities.knowledge_graph.memory.native_ingest import (
        ingest_entities as _shared_ingest_entities,
    )
except Exception:  # noqa: BLE001 — primitive not yet in installed agent_utilities
    _shared_ingest_entities = None
    _shared_ingest_documents = None


def _client() -> tuple[Any | None, str]:
    """Return ``(engine_client, graph_name)`` or ``(None, "")`` when unavailable."""
    try:
        from agent_utilities.knowledge_graph.core.graph_compute import (
            GraphComputeEngine,
        )
    except Exception as e:  # noqa: BLE001 — KG stack absent
        logger.debug("KG ingest unavailable (import): %s", e)
        return None, ""
    try:
        engine = GraphComputeEngine()
        client = getattr(engine, "_client", None)
        if client is None:
            return None, ""
        return client, (getattr(engine, "graph_name", None) or _DEFAULT_GRAPH)
    except Exception as e:  # noqa: BLE001 — engine unreachable
        logger.debug("KG ingest: engine unreachable: %s", e)
        return None, ""


def _fallback_write(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None,
    *,
    client: Any | None,
    graph: str | None,
) -> dict[str, int] | None:
    """Self-contained txn write path used when the shared primitive is absent."""
    if client is None:
        client, graph = _client()
    if client is None:
        return None
    graph = graph or _DEFAULT_GRAPH
    try:
        txn = client.txn.begin(graph=graph)
        for ent in entities:
            props = {k: v for k, v in ent.items() if k != "id" and v is not None}
            props.setdefault("source", _SOURCE)
            props.setdefault("domain", _DOMAIN)
            client.txn.add_node(txn, ent["id"], props)
        committed = client.txn.commit(txn)
    except Exception as e:  # noqa: BLE001 — engine/txn failure is non-fatal
        logger.warning("KG ingest: txn failed: %s", e)
        return None
    if not committed:
        logger.warning("KG ingest: txn not committed (conflict)")
        return None

    edges = 0
    for rel in relationships or []:
        try:
            client.edges.add(
                rel["source"], rel["target"], {"type": rel.get("type", "RELATED")}
            )
            edges += 1
        except Exception as e:  # noqa: BLE001 — pure edge link, best-effort
            logger.debug("KG ingest: edge skipped: %s", e)

    logger.info("KG ingest: wrote %d nodes, %d edges", len(entities), edges)
    return {"nodes": len(entities), "edges": edges}


def ingest_entities(
    entities: list[dict[str, Any]],
    relationships: list[dict[str, Any]] | None = None,
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write typed OWL nodes (+ edges) into epistemic-graph.

    ``entities``: ``[{"id":..., "type":<owl:Class>, ...props}]``.
    ``relationships``: ``[{"source":id, "target":id, "type":rel}]``.
    Returns ``{"nodes":n, "edges":m}`` or ``None`` (never raises). When ``client`` is
    injected (tests) or the shared primitive is unavailable, the self-contained txn
    fallback is used; otherwise the shared fleet primitive handles the write.
    """
    entities = [e for e in (entities or []) if e.get("id")]
    if not entities:
        return None
    if _shared_ingest_entities is not None and client is None:
        return _shared_ingest_entities(
            entities, relationships, source=source, domain=domain
        )
    return _fallback_write(entities, relationships, client=client, graph=graph)


def ingest_documents(
    documents: list[dict[str, Any]],
    *,
    source: str = _SOURCE,
    domain: str = _DOMAIN,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Write text records as ``:Document`` nodes (semantic-search fodder)."""
    documents = [d for d in (documents or []) if d.get("id") and d.get("text")]
    if not documents:
        return None
    if _shared_ingest_documents is not None and client is None:
        return _shared_ingest_documents(documents, source=source, domain=domain)
    nodes = [{**d, "type": "Document"} for d in documents]
    return _fallback_write(nodes, None, client=client, graph=graph)


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
) -> dict[str, int] | None:
    """Map wger exercise records → ``:Exercise`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for ex in _records(exercises):
        eid = ex.get("id")
        if eid is None:
            continue
        entities.append(
            {
                "id": f"wellness:exercise:{eid}",
                "type": "Exercise",
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
) -> dict[str, int] | None:
    """Map wger routine records → ``:WorkoutRoutine`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for rt in _records(routines):
        rid = rt.get("id")
        if rid is None:
            continue
        entities.append(
            {
                "id": f"wellness:routine:{rid}",
                "type": "WorkoutRoutine",
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
) -> dict[str, int] | None:
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
                "type": "WorkoutSession",
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
                    "type": "sessionOfRoutine",
                }
            )
    return ingest_entities(entities, relationships, client=client, graph=graph)


def ingest_nutrition_plans(
    plans: Any,
    *,
    client: Any | None = None,
    graph: str | None = None,
) -> dict[str, int] | None:
    """Map wger nutrition-plan records → ``:NutritionPlan`` nodes and ingest."""
    entities: list[dict[str, Any]] = []
    for p in _records(plans):
        pid = p.get("id")
        if pid is None:
            continue
        entities.append(
            {
                "id": f"wellness:nutritionplan:{pid}",
                "type": "NutritionPlan",
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
