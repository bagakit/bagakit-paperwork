# One-shot Rewrite Experiment

## Goal

Use existing accumulated experience (`v1-v12`) to do a single-pass optimization of:

`/Users/bytedance/proj/priv/bagakit/skills/blogs/2026-02-21-brainstorm-self-explanatory-and-expert-review-system.md`

## Constraints

- Source file is immutable in this experiment.
- All edits stay inside this experiment directory.
- One-shot output only (`versions/v1`), no iterative rewrite loop.

## Structure

- `inputs/`: immutable source snapshot
- `versions/v1/`: optimized article + techniques + outline + markdown/doc formatting tricks
- `outputs/`: review-friendly copy
- `reports/`: integrity and execution notes

## Baseline Used

- `EXPERIENCE_PLAYBOOK.md` (v1-v12 accumulated lessons)
- `versions/v12/article.md` + `versions/v12/techniques.md`
- Baseline gate: preserve readability + executability together; avoid regression
