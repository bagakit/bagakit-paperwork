# Expert Learning Round: Writing Techniques

## Goal
- Learn concrete, repeatable writing techniques before next rewrite.
- Convert techniques into explicit edits for `v3`.

## Expert A (structure & information design)
- Focus: section architecture, heading strategy, reader scanning.
- Sources:
  - https://developers.google.com/tech-writing/one/audience
  - https://learn.microsoft.com/en-us/style-guide/scannable-content/headings
  - https://www.archives.gov/open/plain-writing/10-principles.html
- Techniques extracted:
  - Start with the reader's core question, not the author's process.
  - Put major point first, then supporting detail (inverted emphasis inside section).
  - Headings should be specific and meaningful enough to stand alone.
  - Keep one central idea per paragraph cluster.

## Expert B (sentence craft & transitions)
- Focus: sentence rhythm, transition clarity, concision.
- Sources:
  - https://developers.google.com/tech-writing/one/active-voice
  - https://owl.purdue.edu/owl/general_writing/mechanics/transitions_and_transitional_devices/index.html
  - https://owl.purdue.edu/owl/general_writing/academic_writing/paramedic_method.html
- Techniques extracted:
  - Prefer active voice to reduce indirection.
  - Use functional transitions (`however`, `therefore`, `given this`) to show logic moves.
  - Alternate long explanatory lines with short control lines.
  - Trim prepositional clutter and nominalization-heavy phrasing.

## Expert C (quality gate & plain language)
- Focus: publication-grade clarity checks.
- Sources:
  - https://learn.microsoft.com/en-us/style-guide/checklists/grammar-and-parts-of-speech-checklist
  - https://www.opm.gov/information-management/plain-language/
  - https://www.archives.gov/open/plain-writing/checklist.html
- Techniques extracted:
  - Maintain tense consistency (prefer present tense for claims/rules).
  - Keep subject-verb-object close; avoid unnecessary detours.
  - Explain technical terms at first mention.
  - Validate readability with checklist, not intuition.

## Techniques adopted for v3
1. Replace generic headings with reader-trigger headings.
2. Add explicit failure-mode paragraph before mechanism proposal.
3. Use decomposition sentence to bridge diagnosis and design.
4. Add transition operators at section entries to reduce logic jumps.
5. Enforce mixed sentence cadence (long/short/medium).
6. Keep terminology stable and defined on first use.
