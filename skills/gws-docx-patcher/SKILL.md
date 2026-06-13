---
name: gws-docx-patcher
description: Workflow for editing .docx files on Google Drive by downloading with `gws files get`, editing locally with `python-docx`, and re-uploading with `gws files update --upload`.
---

# gws-docx-patcher

Use this skill to programmatically edit Word documents stored on Google Drive while preserving the original file ID and sharing links.

## When to Use
- When you need to make surgical edits to a `.docx` file on Google Drive.
- When the user prefers overwriting the existing file rather than creating a new one.

## Steps

1.  **Download**: Use `gws files get <file_id> --output local_file.docx` to retrieve the document.
2.  **Edit Locally**: Use a Python script with the `python-docx` library to perform the required edits (e.g., text replacement, style updates, table population).
3.  **Upload (Overwrite)**: Use `gws files update <file_id> --upload local_file.docx` to push the changes back to Google Drive. This preserves the file ID and existing links.

## Example Script (Local Edit)
```python
from docx import Document

def patch_document(path, old_text, new_text):
    doc = Document(path)
    for p in doc.paragraphs:
        if old_text in p.text:
            p.text = p.text.replace(old_text, new_text)
    doc.save(path)

patch_document('local_file.docx', 'OLD_VALUE', 'NEW_VALUE')
```

## Tools
- `exec`: To run `gws` commands and Python editing scripts.
- `gws`: For Drive file management.
