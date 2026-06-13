---
name: latex-unhighlight
description: Programmatically strip \textcolor{blue}{...} tags from LaTeX source to generate clean manuscript versions.
---

# latex-unhighlight

Use this skill to generate a "clean" version of a LaTeX manuscript by removing revision highlights (specifically `\textcolor{blue}{...}`).

## When to use
- Before final submission of a revised manuscript.
- When the user asks for a "no highlights" or "clean" version of a LaTeX file.

## Steps
1. **Identify Source**: Locate the LaTeX file containing highlights (e.g., `main.tex`).
2. **Strip Highlights**: Use a script or command to remove the `\textcolor{blue}{` prefix and the matching closing brace `}`.
   - **Regex Approach**: For simple cases without nested braces, use `sed -i 's/\\textcolor{blue}{\(.*\)}/\1/g'`.
   - **Python Approach**: For complex cases with nested braces, use a Python script that counts brace depth to correctly identify the closing brace of the `\textcolor` command.
3. **Save Output**: Write the cleaned content to a new file, typically suffixed with `_no_highlights.tex`.
4. **Verify**: Check that the document still compiles and that no essential content was deleted.

## Example
If `main.tex` contains:
`The proposed method \textcolor{blue}{improves accuracy by 5\%} compared to baseline.`

The output `main_no_highlights.tex` should contain:
`The proposed method improves accuracy by 5\% compared to baseline.`

## Tools
- `read_file`
- `write_file`
- `exec` (for running sed or python scripts)
