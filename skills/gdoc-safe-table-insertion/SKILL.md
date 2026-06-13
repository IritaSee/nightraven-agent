---
name: gdoc-safe-table-insertion
description: Ensuring insertion indices are within existing paragraph bounds when programmatically populating Google Docs tables.
---

# Google Docs Safe Table Insertion

This skill provides a workflow for safely populating Google Docs tables programmatically, specifically addressing the "Invalid index" errors that occur when an insertion index falls outside the bounds of a cell's paragraph.

## When to Use
- When using the `gws` CLI or Google Docs API to insert text into table cells.
- When performing batch updates where previous insertions shift the indices of subsequent targets.
- When encountering "Index out of bounds" or "Invalid insertion location" errors.

## Procedural Steps

### 1. Fetch Fresh Document State
Always fetch the latest document JSON before calculating indices. Indices are absolute and shift with every modification.
```bash
gws docs get <document-id> --json
```

### 2. Locate the Target Cell
Traverse the document JSON: `body` -> `content` -> `table` -> `tableRows` -> `tableCells`.
Each cell contains a `content` array, usually starting with a `paragraph`.

### 3. Validate Index Bounds
An insertion index MUST be between the `startIndex` and `endIndex` of a structural element (like a paragraph) within the cell.
- **Rule**: `paragraph.startIndex <= targetIndex < paragraph.endIndex`.
- **Note**: Inserting at `paragraph.endIndex` (which is the newline character) is often the cause of failures if not handled correctly. Aim for `paragraph.endIndex - 1` to insert before the trailing newline.

### 4. Manage Index Shifts
If sending multiple `insertText` requests in a single `batchUpdate`:
- **Option A**: Process requests from largest index to smallest index. This prevents earlier insertions from shifting the indices of later ones.
- **Option B**: Calculate the cumulative offset (number of characters added) and add it to subsequent `targetIndex` values.

### 5. Execute with gws CLI
Construct the JSON payload for `batchUpdate`.

```json
{
  "requests": [
    {
      "insertText": {
        "location": {
          "index": 123
        },
        "text": "Validated Content"
      }
    }
  ]
}
```

## Example: Safe Insertion Logic
If a cell's paragraph has `startIndex: 100` and `endIndex: 101` (empty cell with just a newline):
- **Safe Index**: 100.
- **Unsafe Index**: 101 or higher.

If you insert "Hello" (5 chars) at index 100, the new `endIndex` becomes 106. The next safe insertion point in that paragraph would be between 100 and 106.
