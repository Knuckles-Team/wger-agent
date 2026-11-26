---
name: wger-agent-docs
skill_type: skill
description: Wger Workout Manager documentation
crawl_depth: 2
source_url: https://wger.readthedocs.io/en/latest/
categories: [Documentation, Knowledge Base, Reference]
tags: [docs, reference, wger-agent-docs, knowledge-base]
---

# Wger Agent Docs Documentation

Wger Workout Manager documentation

**Original Sources**:
- [https://wger.readthedocs.io/en/latest/](https://wger.readthedocs.io/en/latest/)

**Contains**: 16 markdown files with full folder structure (crawled at depth 2).
*Last updated: March 04, 2026*

## Steps

1. Pick the page for the question from the table of contents below with `grep -n "<topic>" SKILL.md`. Verify one `references/` link matches the topic.
2. Open the page with `cat references/<file>.md`. Verify the page heading matches the topic you wanted.
3. Find the exact passage with `grep -n "<term>" references/<file>.md`. Verify the match lines contain the term in context.
4. Quote the passage and cite the file name and the original source URL from the front matter `source_url`. Verify the quote is copied verbatim from the page.

## Failure recovery

| Failure | Cause | Recovery |
|---------|-------|----------|
| Link target not found | Page was not crawled at this depth | Search all pages with `grep -rn "<term>" references/` and use the file that matches |
| No match for the term | Docs use a different word | Search a synonym or list pages with `ls references/` and open the closest page |
| Content looks outdated | Crawl dated in the header | State the crawl date from the header and point to `source_url` for the current page |

## 📚 Table of Contents

- [ Images Logo.Png](references/_images_logo.png.md)
- [Authentication Proxy (SSO)[](https://wger.readthedocs.io/en/latest/administration/auth_proxy.html#authentication-proxy-sso "Link to this heading")](references/administration_auth_proxy.html.md)
- [Commands[](https://wger.readthedocs.io/en/latest/administration/commands.html#commands "Link to this heading")](references/administration_commands.html.md)
- [Gym administration[](https://wger.readthedocs.io/en/latest/administration/gym.html#gym-administration "Link to this heading")](references/administration_gym.html.md)
- [Settings[](https://wger.readthedocs.io/en/latest/administration/settings.html#settings "Link to this heading")](references/administration_settings.html.md)
- [Using the API[](https://wger.readthedocs.io/en/latest/api/api.html#using-the-api "Link to this heading")](references/api_api.html.md)
- [Using the routine API[](https://wger.readthedocs.io/en/latest/api/routines.html#using-the-routine-api "Link to this heading")](references/api_routines.html.md)
- [Changelog[](https://wger.readthedocs.io/en/latest/changelog.html#changelog "Link to this heading")](references/changelog.html.md)
- [Contributing[](https://wger.readthedocs.io/en/latest/contributing.html#contributing "Link to this heading")](references/contributing.html.md)
- [Backend[](https://wger.readthedocs.io/en/latest/development/backend.html#backend "Link to this heading")](references/development_backend.html.md)
- [Frontend[](https://wger.readthedocs.io/en/latest/development/frontend.html#frontend "Link to this heading")](references/development_frontend.html.md)
- [Mobile App[](https://wger.readthedocs.io/en/latest/development/mobile_app.html#mobile-app "Link to this heading")](references/development_mobile_app.html.md)
- [Welcome to the wger 2.5 documentation[](https://wger.readthedocs.io/en/latest/#welcome-to-the-wger-version-documentation "Link to this heading")](references/en_latest.md)
- [Using the routines[](https://wger.readthedocs.io/en/latest/manual/routines.html#using-the-routines "Link to this heading")](references/manual_routines.html.md)
- [Docker compose[](https://wger.readthedocs.io/en/latest/production/docker.html#docker-compose "Link to this heading")](references/production_docker.html.md)
- [Manual installation[](https://wger.readthedocs.io/en/latest/production/installation.html#manual-installation "Link to this heading")](references/production_installation.html.md)

## 🤖 Agent Usage Guide

- When the user asks anything about **Wger Agent Docs**, consult the reference files.
- Prefer exact quotes and direct links to the relevant file/section.
- The hierarchical TOC above makes navigation fast and intuitive.
- All images and assets are preserved so links work perfectly.
