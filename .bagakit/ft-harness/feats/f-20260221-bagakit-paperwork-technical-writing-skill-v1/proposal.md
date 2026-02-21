# Feat Proposal: f-20260221-bagakit-paperwork-technical-writing-skill-v1

## Why
- Current repo has brainstorm outcomes but no runnable skill artifact for technical writing delivery.
- We need a publishable v1 skill package that turns writing quality rules into executable checks.

## Goal
- Implement v1 technical writing skill with brainstorm-validated quality gates, packaging path, and docs in bagakit-paperwork.

## Scope
- In scope:
  - Create `bagakit-paperwork-technical-writing` skill directory with `SKILL.md`, runtime references, scripts, and agent config.
  - Add objective article checker script for structure/clarity gates.
  - Add packaging/install docs (`README.md`, `Makefile`) and validate payload boundaries.
  - Wire feat harness gate command to run skill validation in this repo.
- Out of scope:
  - Multi-profile split (blog/rfc/postmortem) and advanced formatter integrations.
  - External publishing workflow automation.

## Impact
- Code paths:
  - `bagakit-paperwork-technical-writing/**`
  - `.bagakit/ft-harness/config.json`
- Tests:
  - `python3 bagakit-paperwork-technical-writing/scripts/check_article.py --input ... --strict`
  - `sh ../bagakit-skill-maker/scripts/bagakit_skill_maker.sh validate --skill-dir bagakit-paperwork-technical-writing`
- Rollout notes:
  - Deliver v1 as single skill package first; profile expansion moves to later feat tasks.
