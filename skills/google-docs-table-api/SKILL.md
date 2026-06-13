---
name: google-docs-table-api
description: Best practices for manipulating tables in Google Docs via API to ensure structural integrity and avoid common errors.
---

# Google Docs Table API

Use this skill when programmatically creating or modifying tables in Google Docs using tools like `gws-docs` or custom scripts.

## Steps

1.  **Structure First**: Always create the table structure (rows and columns) first before attempting to fill cells.
2.  **Insertion Bounds**: Ensure the insertion index for a table is within the paragraph bounds. Inserting at the very end of a document or inside certain elements can cause errors.
3.  **Cell Filling**: Use the `insertText` request with the specific `location` (index) of the cell.
4.  **Deletion Safety**: When deleting ranges that include tables or are adjacent to them, avoid including the final newline character of a paragraph if it's the last element, as this can lead to "Index out of bounds" errors.

## Output Format

When describing table operations, specify:
- Table start index
- Row/Column coordinates
- Text content

## Example

```json
{
  "requests": [
    {
      "insertTable": {
        "rows": 3,
        "columns": 2,
        "location": { "index": 1 }
      }
    }
  ]
}
```
