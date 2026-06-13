---
name: gdoc-direct-editor
description: Downloads a Google Doc, performs local modifications, and overwrites the original via Google Workspace API to maintain file ID and links.
---

# gdoc-direct-editor

Use this skill to perform complex edits on Google Docs that are difficult to achieve via direct API calls (like complex regex replacements, structural changes, or using local libraries like `python-docx`) while preserving the original document's File ID, sharing permissions, and web links.

## When to use
- When you need to perform global search-and-replace across a Google Doc.
- When you need to apply formatting that is easier to handle with `python-docx`.
- When you want to update a document without creating a "Copy of..." or changing the URL.

## Steps

1. **Identify the File ID**: Use `gws drive list` or `gws files list` to find the ID of the target Google Doc.
2. **Download as DOCX**: Use the `gws` CLI to download the file.
   ```bash
   gws files get --id <FILE_ID> --mime-type application/vnd.openxmlformats-officedocument.wordprocessingml.document --output temp_doc.docx
   ```
3. **Modify Locally**: Use a Python script with `python-docx` to perform the required edits on `temp_doc.docx`.
4. **Overwrite Original**: Upload the modified file back to Google Drive, overwriting the original ID.
   ```bash
   gws files update --id <FILE_ID> --upload temp_doc.docx
   ```
5. **Cleanup**: Remove the local temporary file.

## Example Workflow (Python Script)

```python
from docx import Document

def edit_doc(path):
    doc = Document(path)
    for para in doc.paragraphs:
        if "OLD_TEXT" in para.text:
            para.text = para.text.replace("OLD_TEXT", "NEW_TEXT")
    doc.save(path)

# 1. Download (via exec)
# 2. edit_doc("temp_doc.docx")
# 3. Upload (via exec)
```

## Output Format
- Confirmation of the download.
- Summary of local changes made.
- Confirmation of the successful update/overwrite on Google Drive.
