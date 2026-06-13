---
name: docx-targeted-patching
description: Performing targeted section insertions and global text replacements in .docx via script to preserve existing document structure.
---

# DOCX Targeted Patching

Use this skill when you need to modify a Word document (.docx) while preserving its complex formatting, styles, and structure. Instead of rewriting the whole document, this skill focuses on surgical edits.

## When to Use
- Inserting a specific section or paragraph into an existing document.
- Replacing placeholders or specific text globally without losing font/style information.
- Updating tables or adding rows to existing tables.
- Fixing "Table Grid" KeyErrors by falling back to "Normal Table".

## Workflow

1. **Analyze Structure**: Use `python-docx` to inspect the document's paragraphs and tables to identify the exact insertion point or target text.
2. **Targeted Replacement**: Iterate through `doc.paragraphs` or `table.rows` to find and replace text.
3. **Section Insertion**: To insert a section, find the paragraph *after* which you want to insert, and use the `paragraph.insert_paragraph_before()` method or similar logic.
4. **Style Safety**: If a specific style (like 'Table Grid') is missing, use 'Normal Table' to avoid script crashes.

## Example Script Snippet

```python
from docx import Document

def patch_docx(path, target_text, new_text):
    doc = Document(path)
    for p in doc.paragraphs:
        if target_text in p.text:
            # Preserve formatting by replacing text within runs
            for run in p.runs:
                if target_text in run.text:
                    run.text = run.text.replace(target_text, new_text)
    doc.save(path)
```

## Output Format
- Deliver the patched `.docx` file directly to the user (e.g., via Telegram).
- Provide a summary of the changes made.
