---
name: latex-revision-workflow
description: Manage manuscript revisions using the soul package for yellow highlights and automate clean-version generation.
---

# LaTeX Revision Workflow

Use this skill to manage manuscript revisions when the user requires changes to be highlighted in yellow and a clean version to be generated automatically.

## When to Use
- When revising a LaTeX manuscript (e.g., for conference/journal resubmission).
- When the user specifies yellow highlights (`\hl`) instead of colored text.
- When a "clean" version (no highlights) is required for final submission.

## Steps

### 1. Setup Preamble
Ensure the following packages are in the LaTeX preamble:
```latex
\usepackage{color}
\usepackage{soul}
```

### 2. Apply Highlights
Wrap all revised text in the `\hl{...}` command.
- **Constraint**: Do NOT include `\cite{...}` or `\ref{...}` commands inside `\hl{}` as it will cause compilation errors.
- **Constraint**: Do NOT wrap entire environments (like `enumerate` or `itemize`) in `\hl{}`. Highlight the text inside the items instead.

### 3. Generate Clean Version
Use a Python script (e.g., `remove_highlights.py`) to strip the `\hl{...}` tags.

**Example `remove_highlights.py` logic:**
```python
import re

def remove_highlights(tex_content):
    # Regex to find \hl{...} and replace with just ...
    # Handles nested braces to a reasonable degree
    return re.sub(r'\\hl\{((?:[^{}]|\{[^{}]*\})*)\}', r'\1', tex_content)
```

### 4. Verification
- Compile the highlighted version to check for `soul` package errors.
- Compile the clean version to ensure no syntax was broken during stripping.

## Output Format
- `main.tex`: The version with `\hl` highlights.
- `main_no_highlights.tex`: The clean version.

## Example
**Input:**
"The proposed model uses YOLOv11."

**Revised:**
"The proposed model \hl{utilizes the YOLOv11-nano architecture} \cite{redmon2016}."

**Clean Output:**
"The proposed model utilizes the YOLOv11-nano architecture \cite{redmon2016}."
