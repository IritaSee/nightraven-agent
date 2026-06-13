---
name: docx-style-safe-update
description: Use python-docx for run-level highlighting and "Normal Table" fallbacks to preserve complex formatting and prevent KeyErrors.
---

# docx-style-safe-update

Use this skill when programmatically updating Microsoft Word (.docx) files where preserving existing styles, complex formatting, or applying highlights is required. This approach prevents common `KeyError` exceptions when specific styles (like 'Table Grid') are missing from a document's style definition.

## When to Use
- Applying highlights to specific text segments (revisions).
- Creating or updating tables in documents with inconsistent style definitions.
- Preserving run-level formatting (bold, italic, font size) while modifying text.

## Steps

### 1. Safe Table Styling
When creating or modifying tables, always check for the existence of the preferred style. Fall back to 'Normal Table' if the target style is missing.

```python
from docx import Document

doc = Document("manuscript.docx")
table = doc.add_table(rows=1, cols=3)

# Safe style assignment
try:
    table.style = 'Table Grid'
except KeyError:
    table.style = 'Normal Table'
```

### 2. Run-Level Highlighting
To highlight specific text without losing surrounding formatting, iterate through the `runs` of a paragraph.

```python
from docx.enum.text import WD_COLOR_INDEX

def highlight_text(paragraph, target_text, color=WD_COLOR_INDEX.YELLOW):
    for run in paragraph.runs:
        if target_text in run.text:
            # If the run contains exactly the target, highlight it
            if run.text == target_text:
                run.font.highlight_color = color
            else:
                # Logic for partial run matching (split run if necessary)
                pass 
```

### 3. Preserving Document Structure
- Use `edit_file` for simple text replacements if formatting is not a concern.
- Use `python-docx` via a temporary script for structural changes (tables, highlights).
- Always save to a new filename or verify the output before delivering via Telegram.

## Output Format
- A Python script that performs the safe update.
- The resulting `.docx` file delivered to the user.

## Example: Safe Table Creation
```python
import sys
from docx import Document

def create_safe_table(path):
    doc = Document(path)
    table = doc.add_table(rows=2, cols=2)
    try:
        table.style = 'Table Grid'
    except KeyError:
        table.style = 'Normal Table'
    
    table.cell(0, 0).text = "Metric"
    table.cell(0, 1).text = "Value"
    doc.save("updated_manuscript.docx")

if __name__ == "__main__":
    create_safe_table(sys.argv[1])
```
