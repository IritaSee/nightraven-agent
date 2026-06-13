---
name: excel-task-append
description: Appending text to existing Excel cell content using openpyxl to preserve original data during updates.
---

# excel-task-append

Append text to existing content in specific Excel cells while preserving the original data. This is useful for logging, adding notes, or updating status fields without overwriting.

## When to use
- When you need to add information to an Excel cell that already contains data.
- When using `pandas` would risk losing formatting or complex cell structures that `openpyxl` can preserve.
- For task tracking or audit logs within a spreadsheet.

## Steps
1. Identify the target file, sheet name, row/column index (or header name), and the text to append.
2. Use a Python script with `openpyxl` to:
    - Load the workbook.
    - Select the sheet.
    - Locate the cell.
    - Read the existing value.
    - Concatenate the new text (with a separator like a newline or semicolon).
    - Save the workbook.
3. Verify the update by reading the cell back.

## Tools
- `exec`: To run the Python script.
- `read_file`: To inspect the Excel file structure if needed (via `excel-editor`).

## Example

### Appending a status note
**Input:**
- File: `tasks.xlsx`
- Sheet: `Sheet1`
- Cell: `C2`
- Text: `[2026-05-25] Completed QA check.`

**Script:**
```python
import openpyxl
wb = openpyxl.load_workbook('tasks.xlsx')
ws = wb['Sheet1']
cell = ws['C2']
existing = cell.value if cell.value else ""
cell.value = f"{existing}\n[2026-05-25] Completed QA check."
wb.save('tasks.xlsx')
```

## Output Format
- Confirmation of the append operation.
- The new content of the cell.
