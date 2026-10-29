"""Keep shared publication, Pages, and development contracts explicit."""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _workflow(name: str):
    return yaml.safe_load((ROOT / ".github/workflows" / name).read_text())


def _actions_on(workflow: dict):
    # PyYAML's YAML 1.1 reader represents the Actions ``on`` key as True.
    return workflow["on"] if "on" in workflow else workflow[True]


def test_pages_publishes_spec_dashboard_and_supports_manual_refresh():

    config = json.loads((ROOT / ".config/spec-dashboard.json").read_text())
    assert config == {
        "version": 1,
        "sources": [{"glob": "specs/*/status.json", "kind": "spec"}],
    }


def test_release_workflow_uses_shared_connector_publishers():

    assert not (ROOT / ".github/workflows/docs.yml").exists()


def test_precommit_uses_the_canonical_pipelines_contract():
    config = yaml.safe_load((ROOT / ".pre-commit-config.yaml").read_text())
    pipelines = next(
        repo
        for repo in config["repos"]
        if repo["repo"] == "https://github.com/Knuckles-Team/pipelines"
    )
    assert pipelines["rev"] == "main"
    assert {hook["id"] for hook in pipelines["hooks"]} == {
        "connector-standard",
        "secrets",
        "spec",
        "tests-fast",
        "dependency-readiness",
    }


def test_development_skill_has_real_delivery_contract_and_actual_tests():
    skill = ROOT / "wger_agent/skills/wger-agent-development/SKILL.md"
    content = skill.read_text()

    assert "name: wger-agent-development" in content
    assert "## Rapid delivery: the 5-minute contract" in content
    for test_path in (
        "tests/test_publication_workflow.py",
        "tests/test_default_content_surfaces.py",
        "tests/test_fleet_name.py",
        "tests/test_wheel_inventory.py",
    ):
        assert test_path in content
        assert (ROOT / test_path).exists()
    assert "WGER_API_KEY" in content


def test_packaged_skill_and_version_mirrors_are_coherent():
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())["project"]
    version = project["version"]
    readme = (ROOT / "README.md").read_text()
    assert re.search(rf"\*Version: {re.escape(version)}\*", readme)
    lock = (ROOT / "uv.lock").read_text()
    assert f'name = "wger-agent"\nversion = "{version}"' in lock
    package_data = tomllib.loads((ROOT / "pyproject.toml").read_text())["tool"][
        "setuptools"
    ]["package-data"]
    assert "skills/**" in package_data["wger_agent"]
    assert (ROOT / "wger_agent/skills/wger-agent-development/SKILL.md").is_file()
