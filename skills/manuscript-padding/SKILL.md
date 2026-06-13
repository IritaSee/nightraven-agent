---
name: manuscript-padding
description: Expanding specific sections and adding technical tables to meet journal-specific length and percentage requirements.
---

# Manuscript Padding

Use this skill when a manuscript draft falls short of the required page count, word count, or specific section percentage requirements (e.g., "Results & Discussion must be 40-50% of the paper").

## Steps

1. **Analyze Requirements**: Identify the target length (pages/words) and the current deficit. Check if specific sections need to be a certain percentage of the total.
2. **Identify Expansion Areas**:
    - **Introduction**: Add more context on the problem's significance or expand the State of the Art (SOTA) with more recent references.
    - **Methodology**: Add more granular steps, flowcharts (described in text), or parameter tables.
    - **Results & Discussion**: This is usually the best area for padding. Add per-class accuracy tables, ablation studies, or qualitative error analysis.
    - **Literature Review**: Group papers into themes and provide 1-2 paragraphs per theme.
3. **Generate Content**:
    - Use `web_search` to find additional relevant citations (2024-2025).
    - Create technical tables (e.g., "Comparison of Hyperparameters", "Detailed Metric Breakdown").
    - Elaborate on "Implications" and "Future Work".
4. **Verify Integrity**: Ensure the added content is technically sound and doesn't contradict existing results. Use placeholders for missing empirical data.
5. **Format**: Apply the required typography and margins using `academic-docx-formatter`.

## Output Format

- A revised `.docx` file (delivered via Telegram if requested).
- A summary of which sections were expanded and by how much.

## Example

**User**: "The Al-Quddus paper is only 4 pages, but JARDIRA needs at least 6. Also, the Results section is too short."

**Agent**:
1. Identifies that 2 more pages are needed.
2. Decides to add a "Qualitative Error Analysis" section and a "Hyperparameter Sensitivity" table.
3. Expands the Discussion to include a "Research in Context" panel.
4. Delivers the padded draft.
