"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` + wger record mappers with a fake engine
client (no engine required), asserting the txn add_node/commit + edge calls and the
wger record → :Exercise / :WorkoutRoutine / :WorkoutSession / :NutritionPlan mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

from typing import Any

import msgpack
import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError
from agent_utilities.security.brain_context import ActorContext, use_actor
from agent_utilities.security.actor_identity import ActorType
from agent_utilities.knowledge_graph.core.session import GraphSession, use_session

from wger_agent.kg_ingest import (
    _records,
    ingest_entities,
    ingest_exercises,
    ingest_nutrition_plans,
    ingest_routines,
    ingest_workout_sessions,
)


@pytest.fixture(autouse=True)
def _governed_session():
    actor = ActorContext(
        actor_id="subject:opaque:synthetic",
        actor_type=ActorType.AUTOMATED_SERVICE,
        roles=(),
        tenant_id="tenant:opaque:synthetic",
        authenticated=True,
    )
    session = GraphSession(
        actor=actor,
        tenant=actor.tenant_id,
        scopes=frozenset({"kg:write"}),
        graph="graph:opaque:synthetic",
        policy_version="policy:opaque:synthetic",
        audience="epistemic-graph",
    )
    with use_actor(actor), use_session(session):
        yield


class _FakeNodes:
    def __init__(self) -> None:
        self.values: dict[str, dict[str, Any]] = {}

    def properties(self, node_id: str) -> dict[str, Any] | None:
        return self.values.get(node_id)

    def list(self) -> list[tuple[str, dict[str, Any]]]:
        return list(self.values.items())


class _FakeChanges:
    def __init__(self, nodes: _FakeNodes) -> None:
        self.nodes = nodes
        self.edges: list[tuple[str, str, dict[str, Any]]] = []
        self.applied: list[dict[str, Any]] = []
        self.records: dict[str, dict[str, Any]] = {}
        self.versions: dict[str, dict[str, Any]] = {}

    def get(self, envelope_id: str) -> dict[str, Any] | None:
        return self.records.get(envelope_id)

    def content_version(self, object_id: str) -> dict[str, Any] | None:
        return self.versions.get(object_id)

    def cursor(self, _source: str, _partition: str = "") -> None:
        return None

    def apply(self, envelope: dict[str, Any]) -> dict[str, Any]:
        self.applied.append(envelope)
        mutation = envelope["mutation"]
        for operation in mutation["operations"]:
            method = operation["method"]
            params = method["params"]
            properties = msgpack.unpackb(params["properties_msgpack"], raw=False)
            if method["method"] == "AddNode":
                self.nodes.values[params["node_id"]] = properties
            elif method["method"] == "AddEdge":
                self.edges.append(
                    (params["source_id"], params["target_id"], properties)
                )
        version = envelope["content_version"]
        self.versions[version["object_id"]] = version
        self.records[envelope["envelope_id"]] = envelope
        return {
            "batch_id": mutation["batch_id"],
            "replayed": False,
            "projection_pending": False,
        }


class _FakeRdf:
    def validate_shacl(self, _shapes: str, _data_graph: str) -> dict[str, Any]:
        return {"conforms": True, "results": []}


class _FakeClient:
    def __init__(self) -> None:
        self.nodes = _FakeNodes()
        self.changes = _FakeChanges(self.nodes)
        self.rdf = _FakeRdf()

    @staticmethod
    def supports(operation: str) -> bool:
        return operation == "ApplyChangeEnvelope"

    @staticmethod
    def shacl_validate_committed(_data_graph: str) -> Any:
        """EG's committed-GraphSchema SHACL authority (agent-utilities EH-385)."""
        from epistemic_graph.generated.rdf_report import ShaclValidationReport

        digest = "sha256:" + "0" * 64
        return ShaclValidationReport(
            conforms=True, results=[], composed_digest=digest, schema_digests=[digest]
        )


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "WorkoutSession"},
            {"id": "b", "node_type": "WorkoutRoutine"},
        ],
        [{"source": "a", "target": "b", "relationship": "sessionOfRoutine"}],
        client=c,
    )
    assert res == {"nodes": 2, "edges": 1}
    assert len(c.changes.applied) == 1
    assert set(c.nodes.values) == {"a", "b"}
    # provenance is stamped
    assert c.nodes.values["a"]["source"] == "wger-agent"
    assert c.nodes.values["a"]["domain"] == "wellness"
    assert c.changes.edges == [("a", "b", {"relationship": "sessionOfRoutine"})]


def test_ingest_exercises_maps_typed_nodes():
    c = _FakeClient()
    res = ingest_exercises(
        {"results": [{"id": 345, "name": "Bench Press", "category": 11}]},
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["wellness:exercise:345"]
    assert node["node_type"] == "Exercise"
    assert node["name"] == "Bench Press"
    assert node["externalToolId"] == "345"


def test_ingest_routines_maps_typed_nodes():
    c = _FakeClient()
    res = ingest_routines(
        [{"id": 42, "name": "PPL", "description": "push/pull/legs"}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["wellness:routine:42"]
    assert node["node_type"] == "WorkoutRoutine"
    assert node["name"] == "PPL"


def test_ingest_workout_sessions_links_routine():
    c = _FakeClient()
    res = ingest_workout_sessions(
        {
            "results": [
                {"id": 9, "routine": 42, "date": "2026-07-04", "impression": "4"}
            ]
        },
        client=c,
    )
    assert res == {"nodes": 1, "edges": 1}
    assert c.nodes.values["wellness:session:9"]["node_type"] == "WorkoutSession"
    assert c.changes.edges == [
        ("wellness:session:9", "wellness:routine:42", {"relationship": "sessionOfRoutine"})
    ]


def test_ingest_nutrition_plans_maps_goals():
    c = _FakeClient()
    res = ingest_nutrition_plans(
        [{"id": 12, "description": "Cut", "goal_energy": 2400, "goal_protein": 180}],
        client=c,
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.nodes.values["wellness:nutritionplan:12"]
    assert node["node_type"] == "NutritionPlan"
    assert node["goalEnergy"] == 2400
    assert node["goalProtein"] == 180


def test_retired_structural_alias_is_rejected():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "a", "type": "Exercise"}], client=_FakeClient())


def test_empty_native_ingest_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())


def test_records_normalizes_wger_response_shapes():
    """Pins ``_records``'s response-shape normalisation (DRF list dict / single
    dict / plain list / None / an unrecognised type), including that non-dict
    items are filtered out of both the DRF ``results`` list and a bare list."""
    assert _records(None) == []
    assert _records({"id": 1, "name": "solo"}) == [{"id": 1, "name": "solo"}]
    assert _records({"results": [{"id": 1}, "not-a-dict", {"id": 2}]}) == [
        {"id": 1},
        {"id": 2},
    ]
    assert _records([{"id": 1}, "not-a-dict", {"id": 2}]) == [{"id": 1}, {"id": 2}]
    assert _records("unexpected-type") == []
    assert _records(42) == []
