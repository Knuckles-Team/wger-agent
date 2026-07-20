"""Native epistemic-graph typed-node ingestion — Wire-First coverage.

Exercises the real ``ingest_entities`` + wger record mappers with a fake engine
client (no engine required), asserting the txn add_node/commit + edge calls and the
wger record → :Exercise / :WorkoutRoutine / :WorkoutSession / :NutritionPlan mapping.
CONCEPT:AU-KG.ingest.enterprise-source-extractor.
"""

from __future__ import annotations

import pytest
from agent_utilities.knowledge_graph.memory.native_ingest import NativeIngestError

from wger_agent.kg_ingest import (
    ingest_entities,
    ingest_exercises,
    ingest_nutrition_plans,
    ingest_routines,
    ingest_workout_sessions,
)


class _FakeTxn:
    def __init__(self):
        self.nodes = {}
        self.edges = []
        self.committed = False

    def begin(self, graph=None):
        self.graph = graph
        return "txn-1"

    def add_node(self, txn, node_id, props):
        self.nodes[node_id] = props

    def add_edge(self, txn, source, target, props):
        self.edges.append((source, target, props))

    def commit(self, txn):
        self.committed = True
        return True


class _FakeClient:
    def __init__(self):
        self.txn = _FakeTxn()


def test_ingest_entities_writes_nodes_and_edges():
    c = _FakeClient()
    res = ingest_entities(
        [
            {"id": "a", "node_type": "WorkoutSession"},
            {"id": "b", "node_type": "WorkoutRoutine"},
        ],
        [{"source": "a", "target": "b", "relationship": "sessionOfRoutine"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 2, "edges": 1}
    assert c.txn.committed is True
    assert set(c.txn.nodes) == {"a", "b"}
    # provenance is stamped
    assert c.txn.nodes["a"]["source"] == "wger-agent"
    assert c.txn.nodes["a"]["domain"] == "wellness"
    assert c.txn.edges == [("a", "b", {"relationship": "sessionOfRoutine"})]


def test_ingest_exercises_maps_typed_nodes():
    c = _FakeClient()
    res = ingest_exercises(
        {"results": [{"id": 345, "name": "Bench Press", "category": 11}]},
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["wellness:exercise:345"]
    assert node["node_type"] == "Exercise"
    assert node["name"] == "Bench Press"
    assert node["externalToolId"] == "345"


def test_ingest_routines_maps_typed_nodes():
    c = _FakeClient()
    res = ingest_routines(
        [{"id": 42, "name": "PPL", "description": "push/pull/legs"}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["wellness:routine:42"]
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
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 1}
    assert c.txn.nodes["wellness:session:9"]["node_type"] == "WorkoutSession"
    assert c.txn.edges == [
        ("wellness:session:9", "wellness:routine:42", {"relationship": "sessionOfRoutine"})
    ]


def test_ingest_nutrition_plans_maps_goals():
    c = _FakeClient()
    res = ingest_nutrition_plans(
        [{"id": 12, "description": "Cut", "goal_energy": 2400, "goal_protein": 180}],
        client=c,
        graph="__commons__",
    )
    assert res == {"nodes": 1, "edges": 0}
    node = c.txn.nodes["wellness:nutritionplan:12"]
    assert node["node_type"] == "NutritionPlan"
    assert node["goalEnergy"] == 2400
    assert node["goalProtein"] == 180


def test_retired_structural_alias_is_rejected():
    with pytest.raises(NativeIngestError, match="canonical node_type"):
        ingest_entities([{"id": "a", "type": "Exercise"}], client=_FakeClient())


def test_empty_native_ingest_is_rejected():
    with pytest.raises(NativeIngestError, match="at least one entity"):
        ingest_entities([], client=_FakeClient())
