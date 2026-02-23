# bagakit-paperwork-escalation-impact-sketch

Skill for writing 15-second organizational escalation comedy sketches using the
EIS (Escalation Impact Sketch) method.

## What problem this skill solves

Many short scripts either:

- fail to escalate fast enough,
- over-explain technical details,
- or end with weak moralizing lines.

This skill enforces a deterministic five-step structure and a cold-fact ending
contract so sketches stay fast, visual, and shareable.

## Required outputs

- `sketch.md`: performance-facing script.
- `execution_appendix.md`: beat timing and role notes.
- `review_report.md`: gate evidence and revision plan.

## Quick start

```bash
cd bagakit-paperwork-escalation-impact-sketch
bash scripts/validate-skill.sh
python3 scripts/check-sketch.py --input reference/tpl/sketch-template.md --strict --report reference/tpl/review-report-sample.md
```

## Common usage

```bash
python3 scripts/check-sketch.py \
  --input sketch.md \
  --strict \
  --report review_report.md
```

Exit code semantics:

- `0`: hard gates passed
- non-zero: at least one hard gate failed

## Packaging

```bash
cd bagakit-paperwork-escalation-impact-sketch
make package-skill
```

Output artifact:

- `dist/bagakit-paperwork-escalation-impact-sketch.skill`

## Install into local Codex skills

```bash
cd bagakit-paperwork-escalation-impact-sketch
make install-skill
```
