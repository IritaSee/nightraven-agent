---
name: gdrive-python-editor
description: Programmatically update .docx content and formatting on Google Drive using custom Python scripts to resolve file editing failures.
---

# gdrive-python-editor

Use this skill when standard Google Workspace API calls fail to edit complex `.docx` files or when precise formatting control (like specific fonts or table styles) is required on Google Drive.

## Steps

1. **Download**: Use `gws files get` to download the target `.docx` file from Google Drive.
2. **Edit Locally**: Write and execute a Python script using `python-docx` to perform the required edits.
   - Use `docx-style-safe-update` or `docx-style-fallback` to handle style issues.
   - Perform surgical edits to preserve existing structure.
3. **Upload/Update**: Use `gws files update --upload` to overwrite the original file on Google Drive. This preserves the file ID and any existing sharing links.

## Example

```bash
# 1. Download
gws files get [FILE_ID] --output temp.docx

# 2. Edit (via python script)
python3 edit_script.py

# 3. Update
gws files update [FILE_ID] --upload temp.docx
```

## Tools
- `gws` CLI
- `python-docx` library
- `exec` tool for running scripts
