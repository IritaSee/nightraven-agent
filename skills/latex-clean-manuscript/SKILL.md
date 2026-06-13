---
name: latex-clean-manuscript
description: Programmatically stripping highlight commands (e.g., \hl{}) from LaTeX source while preserving inner text for final submissions.
---

# latex-clean-manuscript

Use this skill to generate a "clean" version of a LaTeX manuscript by removing revision highlighting commands (specifically `\hl{...}` from the `soul` package) while keeping the content inside the commands intact.

## When to use
- Preparing a final submission after a revision phase.
- Generating a version of the paper for readers who do not need to see tracked changes.
- When manual removal of dozens of `\hl{}` tags is prone to error or time-consuming.

## Steps
1. **Identify Target File**: Locate the LaTeX source file (e.g., `main.tex`) containing `\hl{...}` commands.
2. **Run Cleaning Script**: Use a Python script (like `remove_highlights.py`) or a regex-based replacement to strip the tags.
   - Regex pattern: `\\hl\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}`
3. **Verify Integrity**: Ensure that nested braces or special characters within the highlights were handled correctly.
4. **Save Output**: Write the cleaned content to a new file (e.g., `main_no_highlights.tex`).
5. **Compile**: Run LaTeX compilation on the new file to ensure no syntax errors were introduced.

## Tools Used
- `read_file`: To read the original LaTeX source.
- `write_file`: To save the cleaned version.
- `exec`: To run a Python script or `sed`/`perl` command for the replacement.

## Example
If the input is:
`The proposed model achieves \hl{94.84\% accuracy} in field trials.`

The output will be:
`The proposed model achieves 94.84\% accuracy in field trials.`
