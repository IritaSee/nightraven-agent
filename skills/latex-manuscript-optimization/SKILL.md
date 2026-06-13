---
name: latex-manuscript-optimization
description: Converting image-based tables to native LaTeX and managing IEEEtran/BibTeX workflows for conference submissions.
---

# latex-manuscript-optimization

Use this skill to optimize LaTeX manuscripts, specifically for IEEEtran templates, and to convert non-native elements (like image-based tables) into clean LaTeX code.

## When to use
- Preparing a paper for an IEEE conference (e.g., ICICoS).
- Converting screenshots of tables into LaTeX `tabular` environments.
- Managing BibTeX bibliographies and ensuring citation consistency.
- Optimizing space (squeezing text) while maintaining template compliance.

## Steps
1. **Template Setup**: Ensure `IEEEtran.cls` is used and configured correctly (conference vs. journal mode).
2. **Table Conversion**: Use OCR or manual transcription to convert image-based tables into LaTeX code using `booktabs` for professional quality.
3. **Bibliography Management**: Clean `.bib` files, ensure all entries have required fields, and use `\cite` correctly.
4. **Reviewer Identification**: Implement a system (e.g., using `xcolor` or `\textit{\textbf{...}}`) to highlight changes for reviewers.
5. **Compilation Check**: Verify that the document compiles without errors or overfull hbox warnings.

## Output Format
- Clean `.tex` source code.
- Compiled `.pdf` (if environment allows).
- Optimized `.bib` file.

## Example
**User**: "Convert this table image to LaTeX for my IEEEtran paper and highlight the new results in blue."
**Agent**: [Generates the LaTeX code for the table, adds `\usepackage{xcolor}`, and wraps the new results in `\textcolor{blue}{...}`.]
