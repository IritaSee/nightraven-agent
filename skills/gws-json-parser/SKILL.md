---
name: gws-json-parser
description: Extract specific sections or table data from large Google Workspace JSON outputs using local Python scripts.
---

# gws-json-parser

Use this skill when you need to extract specific data (like table content, specific headers, or nested properties) from the large JSON output of `gws` commands (e.g., `gws documents get --json`).

## When to use
- When `gws documents get` returns a massive JSON that is difficult to parse manually.
- When you need to extract table data from a Google Doc for processing in Excel or LaTeX.
- When you need to find specific structural elements (like indices) for programmatic updates.

## Steps

1. **Get the JSON**: Run the `gws` command and save the output to a temporary file.
   ```bash
   gws documents get <doc-id> --json > doc_output.json
   ```

2. **Create a Parser Script**: Write a small Python script to traverse the JSON structure.
   ```python
   import json

   def extract_table_data(json_path):
       with open(json_path, 'r') as f:
           data = json.load(f)
       
       # Example: Extracting the first table
       content = data.get('body', {}).get('content', [])
       for element in content:
           if 'table' in element:
               # Process table rows and cells
               pass
   ```

3. **Execute and Process**: Run the script and use the output for the next task (e.g., writing to a CSV or formatting a LaTeX table).

## Output Format
- Cleaned data in the desired format (CSV, Markdown table, LaTeX, etc.).
- Specific indices or IDs needed for further `gws` API calls.

## Example: Extracting Table to Markdown
```python
import json

def json_to_md_table(json_file):
    with open(json_file, 'r') as f:
        doc = json.load(f)
    
    tables = []
    for element in doc.get('body', {}).get('content', []):
        if 'table' in element:
            rows = []
            for row in element['table']['tableRows']:
                cells = []
                for cell in row['tableCells']:
                    text = "".join([
                        p.get('paragraph', {}).get('elements', [{}])[0].get('textRun', {}).get('content', '').strip()
                        for p in cell.get('content', [])
                    ])
                    cells.append(text)
                rows.append("| " + " | ".join(cells) + " |")
            
            header_sep = "| " + " | ".join(["---"] * len(rows[0].split('|'))[1:-1]) + " |"
            tables.append("\n".join([rows[0], header_sep] + rows[1:]))
    return "\n\n".join(tables)

print(json_to_md_table('doc.json'))
```
