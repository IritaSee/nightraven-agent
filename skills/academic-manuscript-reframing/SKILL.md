---
name: academic-manuscript-reframing
description: Reframing research papers to specific journal styles (e.g., eClinicalMedicine) including specific statistical reporting (95% CI, ablation studies) and structural requirements.
---

# academic-manuscript-reframing

Use this skill when a manuscript needs to be adapted from one journal's style to another (e.g., moving from a general engineering conference to a Lancet-family medical journal like eClinicalMedicine).

## When to use
- Target journal change.
- Reviewer requests for specific statistical reporting (95% CI, p-values).
- Need for ablation studies or specific clinical reporting guidelines (STARD-AI, CONSORT).

## Steps
1. **Analyze Target Journal**: Identify structural requirements (e.g., Research in Context panel, specific section order).
2. **Statistical Enhancement**: Ensure all metrics include 95% Confidence Intervals (CI) and relevant statistical significance tests.
3. **Ablation Study Design**: Create or format tables showing the contribution of each model component.
4. **Clinical Contextualization**: Reframe technical contributions into clinical impact (e.g., "accuracy" to "diagnostic yield" or "reduction in false positives").
5. **Reporting Guidelines**: Verify compliance with relevant guidelines (STARD-AI, TRIPOD).

## Output Format
- Revised manuscript sections in `.docx` (via `word-docx` or `academic-docx-telegram-delivery`) or LaTeX.
- Summary of changes made for reviewer identification (bold italics or color).

## Example
**User**: "Reframe my ColonoMind paper for eClinicalMedicine. We need to add 95% CIs and an ablation study."
**Agent**: [Analyzes current draft, calculates CIs, designs ablation table, and updates the manuscript structure to include 'Research in Context' and 'Clinical Implications' sections.]
