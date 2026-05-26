# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Modularized MCP server structure under new `wger_agent/mcp/` directory.
- Created `wger_agent/mcp/tools.py` housing registration functions for modular tool decomposition.
- Created `wger_agent/mcp/mcp_server.py` to decouple core server boot process from individual tool collections.
- Added Starlette `/health` endpoint for robust uptime checks on the FastMCP instance.
- Exposed 7 granular toggle environment variables (`ROUTINETOOL`, `ROUTINECONFIGTOOL`, etc.) in `.env.example` and `README.md` to customize tool availability.
- Isolated test suite from pytest CLI arguments via automated `sys.argv` autouse mocking in `tests/conftest.py`.

### Changed
- Converted `wger_agent/mcp_server.py` into a lightweight, backward-compatible redirect wrapper.
- Significantly boosted overall test coverage to 99.87% through comprehensive unit and modular integration testing.

## [0.1.29] - 2026-04-29

### Added
- Initial release
