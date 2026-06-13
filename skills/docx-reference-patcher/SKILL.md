---
name: docx-reference-patcher
description: Targeted patching of .docx file references using python-docx to preserve document structure and styles.
---

# docx-reference-patcher

Perform surgical updates to citations and references within a `.docx` file without disrupting the overall document formatting, styles, or structure.

## When to use
- When updating a list of references in a manuscript.
- When fixing specific citation numbers or text within paragraphs.
- When you need to ensure that the "Normal" style and other custom styles are preserved during the edit.

## Steps
1. **Load Document**: Use `docx.Document(path)` to load the target file.
2. **Locate Target**: Iterate through paragraphs or tables to find the specific text or section (e.g., "References" header).
3. **Surgical Replacement**:
    - For simple text replacement: Use `paragraph.text = paragraph.text.replace(old, new)` if formatting within the paragraph is uniform.
    - For run-level replacement (preserving bold/italic): Iterate through `paragraph.runs` to find and replace text.
4. **Reference List Update**: If replacing the entire reference list, find the starting paragraph and replace subsequent paragraphs or clear them and add new ones with the same style.
5. **Save**: Save the document to a new path or overwrite the existing one.

## Tools
- `python-docx` (available in the environment).

## Example
```python
from docx import Document

doc = Document('manuscript.docx')
for para in doc.paragraphs:
    if '[1]' in para.text:
        para.text = para.text.replace('[1]', '[2]')
doc.save('manuscript_updated.docx')
```
