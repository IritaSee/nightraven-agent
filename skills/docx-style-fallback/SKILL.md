---
name: docx-style-fallback
description: Use 'TableNormal' or verify available styles in python-docx when 'Table Grid' is missing to prevent script failure.
---

# docx-style-fallback

Use this skill when a `python-docx` script fails because a specific style (commonly 'Table Grid') is missing from the document's style definitions.

## Steps

1. **Identify the Failure**: Check the error message for `KeyError: "no style with name 'Table Grid'"` or similar.
2. **Inspect Available Styles**: Use a script to list all available styles in the document to find a suitable alternative.
   ```python
   from docx import Document
   doc = Document('path/to/file.docx')
   for style in doc.styles:
       print(style.name)
   ```
3. **Apply Fallback**:
   - Use `'TableNormal'` as the safest universal fallback for tables.
   - Use `'Normal'` for paragraph styles.
4. **Implement Try-Except**: Wrap the style assignment in a try-except block to handle missing styles gracefully.
   ```python
   try:
       table.style = 'Table Grid'
   except KeyError:
       table.style = 'TableNormal'
   ```

## Example

If a script is appending results to a table and fails on a template without 'Table Grid':

```python
# Instead of:
# table.style = 'Table Grid'

# Use:
try:
    table.style = 'Table Grid'
except KeyError:
    # Fallback to standard table style
    table.style = 'TableNormal'
```
