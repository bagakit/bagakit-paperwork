# Experiment Version History

## Scope
- Experiment: blog rewrite quality uplift
- Source immutable: yes
- Edit boundary: experimental directory only

## Versions

| Version | Candidate File | Article File | Technique Notes | Position |
|---------|----------------|--------------|-----------------|----------|
| v1 | `versions/v1/candidate.md` | `versions/v1/article.md` | `versions/v1/techniques.md` | initial rewrite baseline |
| v2 | `versions/v2/candidate.md` | `versions/v2/article.md` | `versions/v2/techniques.md` + `versions/v2/style-extraction.md` + `versions/v2/metrics/v1-v2-style-metrics.json` | style-driven rewrite based on extracted patterns |
| v3 | `versions/v3/candidate.md` | `versions/v3/article.md` | `versions/v3/techniques.md` + `versions/v3/learning-round.md` + `versions/v3/metrics/v2-v3-style-metrics.json` | learning-round rewrite with reader-trigger headings |
| v4 | `versions/v4/candidate.md` | `versions/v4/article.md` | `versions/v4/techniques.md` + `versions/v4/outline-model.md` + `versions/v4/metrics/v3-v4-structure-metrics.json` | outline-first rewrite with explicit thinking model |
| v5 | `versions/v5/candidate.md` | `versions/v5/article.md` | `versions/v5/techniques.md` + `versions/v5/outline-model.md` + `versions/v5/metrics/v4-v5-structure-metrics.json` | hierarchical pyramid rewrite with denser examples |
| v6 | `versions/v6/candidate.md` | `versions/v6/article.md` | `versions/v6/techniques.md` + `versions/v6/outline-model.md` + `versions/v6/metrics/v5-v6-structure-metrics.json` | bullet-vs-paragraph-aware rewrite with higher human realism |
| v7 | `versions/v7/candidate.md` | `versions/v7/article.md` | `versions/v7/techniques.md` + `versions/v7/outline-model.md` + `versions/v7/technique-synthesis.md` + `versions/v7/metrics/v6-v7-structure-metrics.json` | synthesized-playbook rewrite with stronger reader-oriented structure |
| v8 | `versions/v8/candidate.md` | `versions/v8/article.md` | `versions/v8/techniques.md` + `versions/v8/outline-model.md` + `experimental/expert-panel-deep-dive-structure-techniques/deep_dive_forum.md` | audit-integrated rewrite: v7 readability + skills/blogs executability, with contradiction fix on argument order |
| v9 | `versions/v9/candidate.md` | `versions/v9/article.md` | `versions/v9/techniques.md` + `versions/v9/outline-model.md` + `versions/v9/v8-gap-analysis.md` | gap-driven rewrite with structured handbook, v8 issue mapping, and diagram-assisted architecture/process/loop expression |
| v10 | `versions/v10/candidate.md` | `versions/v10/article.md` | `versions/v10/techniques.md` + `versions/v10/outline-model.md` + `versions/v10/v9-gap-analysis.md` | anti-AI-tone rewrite using searched causes: reduced slogan/metaphor density, paragraph-primary narrative, and concrete actor/evidence binding |
| v11 | `versions/v11/candidate.md` | `versions/v11/article.md` | `versions/v11/techniques.md` + `versions/v11/outline-model.md` + `versions/v11/v10-gap-analysis.md` | audit-response rewrite: removed publish metadata, restored field-level execution gates, added H3 scan anchors, and preserved natural paragraph-first narrative |
| v12 | `versions/v12/candidate.md` | `versions/v12/article.md` | `versions/v12/techniques.md` + `versions/v12/outline-model.md` + `versions/v12/v11-gap-analysis.md` | audit-followup rewrite: unified forum terminology, separated publish narrative from execution appendix, added metric sampling protocol, and expanded mechanism-level explanations |

## Directory Layout (structured)

- Root keeps only experiment index and shared entry docs:
  - `VERSION_HISTORY.md`
  - `experiment-notes.md`
  - `OPTIMIZATION_PLAYBOOK.md`
- Execution tool:
  - `tools/check_experiment.py`
- Version assets are fully grouped under `versions/`:
  - `versions/v*/candidate.md`
  - `versions/v*/article.md`
  - `versions/v*/techniques.md`
  - `versions/v*/metrics/*.json` (when exists)

## Current review target
- Recommended for review: `versions/v12/article.md`
