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
    workflow = _workflow("pages.yml")
    publisher = workflow["jobs"]["publish-pages"]
    push = _actions_on(workflow)["push"]

    assert publisher["uses"] == (
        "Knuckles-Team/pipelines/.github/workflows/pages_pipeline.yml@main"
    )
    assert publisher["with"] == {
        "content_source": "docs",
        "spec_dashboard_enabled": True,
        "spec_dashboard_config": ".config/spec-dashboard.json",
    }
    assert "workflow_dispatch" in _actions_on(workflow)
    assert {
        "docs/**",
        "mkdocs.yml",
        "README.md",
        "specs/**",
        ".config/spec-dashboard.json",
        ".github/workflows/pages.yml",
    } <= set(push["paths"])

    config = json.loads((ROOT / ".config/spec-dashboard.json").read_text())
    assert config == {
        "version": 1,
        "sources": [{"glob": "specs/*/status.json", "kind": "spec"}],
    }


def test_release_workflow_uses_shared_connector_publishers():
    workflow = _workflow("pipeline.yml")
    jobs = workflow["jobs"]
    assert set(jobs) == {"publish-pypi", "publish-docker"}

    pypi = jobs["publish-pypi"]
    assert pypi["uses"].endswith("/python_pipeline.yml@main")
    assert pypi["with"] == {"connector": True}

    docker = jobs["publish-docker"]
    assert docker["needs"] == "publish-pypi"
    assert docker["uses"].endswith("/container_pipeline.yml@main")
    assert docker["with"] == {"render_connector": True}
    for publisher in (pypi, docker):
        assert "if" not in publisher
        assert not publisher.get("continue-on-error", False)

    assert not (ROOT / ".github/workflows/docs.yml").exists()
    assert not (ROOT / ".github/workflows/container-release.yml").exists()


def test_sdk_rebuild_workflow_exposes_only_reviewed_manual_repair():
    workflow = _workflow("sdk-rebuild.yml")
    actions = _actions_on(workflow)
    assert set(actions) == {"workflow_dispatch"}
    inputs = actions["workflow_dispatch"]["inputs"]
    assert set(inputs) == {
        "release_repair",
        "release_source_sha",
        "release_source_epoch",
    }
    assert inputs["release_repair"] == {
        "description": "Republish the already published container after the reviewed public-wheel guard.",
        "required": False,
        "default": False,
        "type": "boolean",
    }
    for name, description in (
        (
            "release_source_sha",
            "Full SHA of the original package source that produced the public wheel.",
        ),
        (
            "release_source_epoch",
            "Exact SOURCE_DATE_EPOCH used to generate the public connector payload.",
        ),
    ):
        assert inputs[name] == {
            "description": description,
            "required": False,
            "default": "",
            "type": "string",
        }

    assert workflow["permissions"] == {"contents": "read"}
    assert set(workflow["jobs"]) == {"rebuild"}
    rebuild = workflow["jobs"]["rebuild"]
    assert rebuild["uses"] == (
        "Knuckles-Team/pipelines/.github/workflows/connector_sdk_rebuild_pipeline.yml@main"
    )
    assert rebuild["with"] == {
        "release_repair": "${{ inputs.release_repair || false }}",
        "release_source_sha": "${{ inputs.release_source_sha || '' }}",
        "release_source_epoch": "${{ inputs.release_source_epoch || '' }}",
    }
    assert rebuild["secrets"] == "inherit"


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
