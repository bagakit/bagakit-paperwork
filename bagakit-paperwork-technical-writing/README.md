# bagakit-paperwork-technical-writing

Technical writing skill focused on turning engineering discussions into publishable and executable outputs.

## What this skill ships

- `SKILL.md`: runtime contract and workflow.
- `references/`: playbook, quality gates, formatting tricks, templates.
- `scripts/check-article.py`: objective checker for article structure and quality signals.
- `scripts/validate-skill.sh`: local validation entrypoint used by feat-task-harness gate.

## Quick start

```bash
cd bagakit-paperwork-technical-writing
bash scripts/validate-skill.sh
python3 scripts/check-article.py --input references/tpl/article-template.md --strict
```

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
