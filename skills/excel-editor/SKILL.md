---
name: excel-editor
description: Read, analyze, edit, format, and create Microsoft Excel (.xlsx, .xls) files using pandas and openpyxl.
---

# Excel Editor

This skill provides tools and guidance to read, analyze, edit, format, and create Microsoft Excel (.xlsx, .xls) files.

## Core Tool

A pre-configured CLI helper script is available at:
`/home/mandabot/.nanobot/workspace/skills/excel-editor/scripts/excel_tool.py`

This script runs in the correct Python environment with `pandas`, `openpyxl`, and `xlsxwriter` pre-installed.

### Common CLI Commands

Always run the helper script using `/home/mandabot/venv/bin/python3` or directly as an executable.

#### 1. Get Workbook Info (Sheets, Columns, Dimensions)
```bash
/home/mandabot/.nanobot/workspace/skills/excel-editor/scripts/excel_tool.py --file "path/to/file.xlsx" --action info
```

#### 2. Read a Sheet (Markdown Table)
```bash
/home/mandabot/.nanobot/workspace/skills/excel-editor/scripts/excel_tool.py --file "path/to/file.xlsx" --sheet "Sheet1" --action read --limit 20
```
*Options:*
- `--limit N`: Max rows to display (default 50).
- `--offset N`: Row offset to start reading from (default 0).
- `--format markdown|json|csv`: Output format (default markdown).

#### 3. Write/Edit a Single Cell
```bash
/home/mandabot/.nanobot/workspace/skills/excel-editor/scripts/excel_tool.py --file "path/to/file.xlsx" --sheet "Sheet1" --action write-cell --cell "B2" --value "New Value"
```

#### 4. Append or Insert a Row
```bash
/home/mandabot/.nanobot/workspace/skills/excel-editor/scripts/excel_tool.py --file "path/to/file.xlsx" --sheet "Sheet1" --action write-row --row-data '["Val1", "Val2", 123]'
```
*Options:*
- `--row-index N`: Insert row at 1-based index `N` (shifts existing rows down).

#### 5. Format a Range (Bold, Colors, Alignment)
```bash
/home/mandabot/.nanobot/workspace/skills/excel-editor/scripts/excel_tool.py --file "path/to/file.xlsx" --sheet "Sheet1" --action format --cell "A1:D1" --bold --bg-color "4F81BD" --font-color "FFFFFF" --align "center"
```
*Colors must be 6-character HEX codes (without `#`).*

#### 6. Run Custom Python Code on Workbook
For complex logic, you can pass a python string. The workbook `wb` is preloaded and automatically saved.
```bash
/home/mandabot/.nanobot/workspace/skills/excel-editor/scripts/excel_tool.py --file "path/to/file.xlsx" --action run-code --code "ws = wb.active; ws['A1'] = 'Hello'; ws.column_dimensions['A'].width = 20"
```

---

## Direct Python Usage

If the CLI tool is insufficient, you can write and execute a standalone Python script using `/home/mandabot/venv/bin/python3`.

### Reading with Pandas (Fast Data Analysis)
```python
import pandas as pd

# Read specific sheet
df = pd.read_excel("file.xlsx", sheet_name="Sheet1")

# Analyze data
print(df.describe())
```

### Editing with Openpyxl (Preserves Formatting)
```python
import openpyxl
from openpyxl.styles import Font, PatternFill

wb = openpyxl.load_workbook("file.xlsx")
ws = wb["Sheet1"]

# Edit cells
ws["A1"] = "Header"
ws["A1"].font = Font(bold=True, color="FF0000")

# Save workbook
wb.save("file.xlsx")
```
