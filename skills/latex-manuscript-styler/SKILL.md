---
name: latex-manuscript-styler
description: Standardizes LaTeX tables, decimal notation, and highlights (\hl) for IEEE/Lancet templates.
---

# LaTeX Manuscript Styler

Standardize LaTeX manuscripts to meet IEEE and Lancet template requirements, focusing on table formatting, decimal notation, and highlight management.

## When to use
- Preparing a LaTeX manuscript for submission to IEEE or Lancet-family journals.
- Standardizing decimal points and removing redundant operators.
- Managing highlights (`\hl`) for revisions without breaking citations or lists.

## Steps
1. **Decimal Standardization**: Replace all `\cdot` used as decimals with standard `.` notation.
2. **Operator Cleanup**: Remove redundant `\arg` operators or other non-standard mathematical notations as per IEEE style.
3. **Table Formatting**:
    - Use `resizebox` to ensure tables fit within columns.
    - Standardize confusion matrices to a 4-column format.
    - Ensure 9pt font size for tables to maintain readability.
4. **Highlight Management**:
    - Use the `soul` package for `\hl{...}`.
    - Ensure `\hl` blocks do not wrap `\cite` commands or `enumerate`/`itemize` environments to prevent compilation errors.
5. **Asset Management**: Verify all images are correctly referenced and unused assets are kept in the repository for future use.

## Output Format
- Updated `.tex` files with standardized formatting.
- A summary of changes made (e.g., "Standardized 15 decimal points", "Fixed 3 highlight blocks").

## Example
**Input**:
```latex
The value is $0\cdot75$. \hl{This is important \cite{ref1}}.
```

**Output**:
```latex
The value is $0.75$. \hl{This is important} \cite{ref1}.
```
