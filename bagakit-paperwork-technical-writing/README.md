# bagakit-paperwork-technical-writing

Technical writing skill for converting engineering discussion into artifacts that are
both publishable and executable.

## What problem this skill solves

Many technical drafts are readable but hard to execute, or executable but hard to
publish. This skill enforces a two-layer output model:

- narrative layer for publication (`article.md`)
- execution layer for operation and handoff (`execution_appendix.md`)

It also adds an objective review layer (`review_report.md`) so quality is inspectable
instead of subjective.

Recent guardrails:

- block internal directive leakage in publish article (`[[BAGAKIT]]`, stage footer)
- require version baseline note (`keep/add/tighten`) to reduce rewrite regression
- support baseline comparison for suspicious one-pass compression
- compare evidence-pack density against baseline to catch framework-only rewrites
- require agent-gate decision with severity findings
- enforce first-draft profile density floors (words/cases/diagram/full-sample)
- enforce readability floors (H2 restatable propositions, anchor loop, long-sentence ratio<25%, short breaks)
- keep memory-hook quality in agent-gate review (heuristic hints only)
- keep AI-tone lexicon checks as warning-only lint via `gate/anti-patterns/ai-tone-terms.txt`

## What ships in this package

- `SKILL.md`
  runtime contract, trigger boundary, workflow, handoff rules
- `references/writing-techniques.md`
  writing patterns for structure, evidence, anti-regression, and anti-template tone
- `references/markdown-formatting.md`
  practical formatting rules for GitHub Markdown and Mermaid
- `references/quality-gates.md`
  hard/warning gate definitions and release policy
- `references/agent-gate-rubric.md`
  scoring and finding format for agent-led review
- `references/tpl/*.md`
  templates for article, execution appendix, and review report
- `gate/anti-patterns/*`
  complexity-guardrail validation protocol (`rules.toml` + `check-anti-patterns.py`)
- `gate/anti-patterns/ai-tone-terms.txt`
  warning-level lexicon for AI-tone lint hints in article checking
- `scripts/check-article.py`
  objective checker for structure, placeholder hygiene, publish leakage, and warning signals
- `scripts/validate-skill.sh`
  local validation entrypoint used by gate commands

## Expected input package

At minimum:

- topic and target reader
- one source of truth (notes, draft, transcript, or existing article)

Recommended:

- success criteria
- length/tone constraints
- audit feedback from previous versions

## Expected output package

- `article.md`
  publish-facing narrative with clear claim and evidence chain
- `execution_appendix.md`
  execution fields, verification commands, recovery path
- `review_report.md`
  gate result, structural delta, unresolved risks

## Workflow at a glance

1. Define reader, task, and decision boundary.
2. Outline first (`H2` in 3-5 range, `H3` as scan anchors).
3. Draft with evidence chain.
4. Run `check-article.py` and fix hard failures.
5. Run baseline comparison when previous version exists.
6. Record warning + agent-gate judgments in `review_report.md`.
7. Hand off with explicit destination and status.

## Quick start

```bash
cd bagakit-paperwork-technical-writing
bash scripts/validate-skill.sh
python3 scripts/check-article.py --input references/tpl/article-template.md --strict
```

## Common usage example

```bash
python3 scripts/check-article.py \
  --input article.md \
  --strict \
  --profile protocol \
  --report review_report.md

python3 scripts/check-article.py \
  --input article.md \
  --strict \
  --profile infrastructure \
  --baseline previous.md \
  --report review_report.md
```

Exit code semantics:

- `0`: hard gates passed
- non-zero: at least one hard gate failed

## Packaging

```bash
cd bagakit-paperwork-technical-writing
make package-skill
```

Output artifact:

- `dist/bagakit-paperwork-technical-writing.skill`

## Install into local Codex skills

```bash
cd bagakit-paperwork-technical-writing
make install-skill
```

## Validation and maintenance

- run `make validate` before publishing changes
- keep templates and gate definitions aligned
- treat warning additions as contract changes and document rationale
