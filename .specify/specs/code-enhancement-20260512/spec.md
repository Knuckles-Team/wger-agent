# Code Enhancement: wger-agent

> Automated code enhancement review for wger-agent. Covers 17 analysis domains.

## User Stories

- As a **developer**, I want to **address Project Analysis findings (grade: C, score: 74)**, so that **improve project project analysis from C to at least B (80+)**.
- As a **developer**, I want to **address Test Coverage findings (grade: C, score: 70)**, so that **improve project test coverage from C to at least B (80+)**.
- As a **developer**, I want to **address Architecture & Design Patterns findings (grade: C, score: 75)**, so that **improve project architecture & design patterns from C to at least B (80+)**.
- As a **developer**, I want to **address Concept Traceability findings (grade: F, score: 44)**, so that **improve project concept traceability from F to at least B (80+)**.
- As a **developer**, I want to **address Linting & Formatting findings (grade: F, score: 0)**, so that **improve project linting & formatting from F to at least B (80+)**.
- As a **developer**, I want to **address Changelog Audit findings (grade: C, score: 75)**, so that **improve project changelog audit from C to at least B (80+)**.
- As a **developer**, I want to **address Environment Variables findings (grade: C, score: 75)**, so that **improve project environment variables from C to at least B (80+)**.

## Functional Requirements

- **FR-001**: Detected 1 agent skill(s) — will grade in CE-026
- **FR-002**: 1 functions exceed 200 lines (actionable refactoring targets): register_routine_tools (211L)
- **FR-003**: Monolithic: mcp_server.py (1165L) — 1 functions with high complexity (worst: register_routine_tools at 211L, CC=3); Low cohesion: 12 distinct concepts in one file
- **FR-004**: Needs attention: api_client.py (1025L) — God class: WgerApi (140 methods) — consider mixins/composition
- **FR-005**: Test suite lacks intent diversity (only one type)
- **FR-006**: 18 potential doc-test drift items
- **FR-007**: README.md missing sections: installation, usage|quick start
- **FR-008**: README missing: MCP tools mapping table with descriptions
- **FR-009**: README missing: Has a Table of Contents
- **FR-010**: README missing: Has usage examples with code blocks
- **FR-011**: README missing: References /docs directory material
- **FR-012**: README missing: Has MCP tools mapping table with descriptions
- **FR-013**: SRP: 2 modules exceed 500 lines (god modules)
- **FR-014**: SRP: 1 classes have >15 methods
- **FR-015**: No discernible layer architecture (no domain/service/adapter separation)
- **FR-016**: Low traceability ratio: 0% concepts fully traced
- **FR-017**: 3 test functions missing concept markers
- **FR-018**: 64 significant functions (>10 lines) missing concept markers in docstrings
- **FR-019**: Total lint findings: 58 (high/error: 58, medium/warning: 0, low: 0)
- **FR-020**: 2 hook(s) may be outdated: ruff-pre-commit, uv-pre-commit
- **FR-021**: CHANGELOG.md exists but could not be parsed — check format compliance
- **FR-022**: No changelog entries within the last 30 days
- **FR-023**: keepachangelog not installed — pip install 'universal-skills[code-enhancer]'
- **FR-024**: Partial env var documentation: 38% coverage
- **FR-025**: Undocumented env vars: ALLOWED_CLIENT_REDIRECT_URIS, AUTH_TYPE, EUNOMIA_POLICY_FILE, EUNOMIA_REMOTE_URL, EUNOMIA_TYPE, OAUTH_BASE_URL, OAUTH_UPSTREAM_AUTH_ENDPOINT, OAUTH_UPSTREAM_CLIENT_ID, OAUTH_UPSTREAM_CLIENT_SECRET, OAUTH_UPSTREAM_TOKEN_ENDPOINT
- **FR-026**: 11 Python env vars not in .env.example: BODYTOOL, DEFAULT_AGENT_NAME, EXERCISETOOL, NUTRITIONTOOL, ROUTINECONFIGTOOL

## Success Criteria

- Overall GPA: 2.76 → 3.0
- Domains at B or above: 10 → 17
- Actionable findings: 26 → 0
