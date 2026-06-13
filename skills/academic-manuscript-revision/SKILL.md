---
name: academic-manuscript-revision
description: Workflow for IEEE paper revisions including page-limit compression (prioritizing tables over figures) and blue-text change tracking.
---

# Academic Manuscript Revision

Use this skill when revising an academic manuscript (specifically IEEE format) to track changes and manage page constraints.

## When to Use
- During the revision phase after receiving reviewer feedback.
- When the manuscript exceeds the conference/journal page limit (e.g., 6 pages for ICICoS).
- When specific change tracking (blue text) is required.

## Steps

### 1. Change Tracking
- Wrap all new or modified text in the LaTeX source using the `\textcolor{blue}{...}` command.
- Ensure the `xcolor` package is included in the preamble: `\usepackage{xcolor}`.

### 2. Page Limit Compression
If the manuscript exceeds the allowed page count:
- **Prioritize Tables**: Keep tables that present core results, as they are often more data-dense and harder to summarize than figures.
- **Reduce Figures**: Identify redundant or illustrative figures that can be removed or merged without losing the primary argument.
- **Textual Trimming**: Look for wordy sentences or redundant descriptions in the Introduction or Discussion sections.
- **Formatting**: Check for large vertical spaces around figures/tables and use `\vspace` sparingly if permitted by the template.

## Output Format
- Updated `.tex` file with `\textcolor{blue}{...}` tags.
- A summary of removed/merged elements to meet page limits.

## Example

**Input (Over-limit):**
A 6.5-page manuscript with 4 figures and 2 tables.

**Action:**
1. Wrap revised sections in `\textcolor{blue}{...}`.
2. Identify Figure 3 (illustrative flowchart) as redundant since the process is described in the text.
3. Remove Figure 3.
4. Adjust Figure 1 and 2 sizes slightly.

**Result:**
A 6-page manuscript with all changes highlighted in blue and critical tables preserved.
