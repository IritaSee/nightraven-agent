---
name: gws-doc-table-patching
description: Programmatically updating Google Doc tables using `gws` CLI with JSON payloads and index-shift management.
---

# gws-doc-table-patching

Use this skill to programmatically update tables within Google Docs using the `gws` CLI. This is particularly useful for automated manuscript updates where table data (e.g., accuracy metrics, sample sizes) changes frequently.

## When to Use
- Updating specific cells in a Google Doc table without overwriting the entire document.
- Injecting experimental results into a manuscript draft.
- Handling multiple table updates in a single session where text length changes might shift indices.

## Steps

### 1. Identify Table Indices
Fetch the document's JSON structure to locate the `startIndex` and `endIndex` of the table cells you wish to update.
```bash
gws docs get --id <DOC_ID> --json > doc_structure.json
```
Search for `table` elements and identify the `content` indices for specific `tableCells`.

### 2. Construct the JSON Payload
Create a `requests` array for the `batchUpdate` command. Use `insertText` or `deleteContentRange` requests.
- **Note**: Use camelCase for all keys in the JSON payload (e.g., `batchUpdate`, `insertText`, `location`).

Example `payload.json`:
```json
{
  "requests": [
    {
      "insertText": {
        "location": { "index": 105 },
        "text": "97.24%"
      }
    }
  ]
}
```

### 3. Execute the Update
Use the `gws` CLI to send the batch update.
```bash
gws docs batchUpdate --id <DOC_ID> --json "$(cat payload.json)"
```

### 4. Manage Index Shifts
If performing multiple updates that change the length of the text:
- **Option A (Reverse Order)**: Apply updates from the end of the document to the beginning. This prevents earlier updates from shifting the indices of later ones.
- **Option B (Fresh State)**: Re-fetch the document structure (`gws docs get`) after each update to obtain the new, accurate indices.

## Output Format
The command will return a JSON response confirming the applied updates. Verify the changes by reading the document or checking the revision history.

## Example: Updating a Result Cell
To update a cell at index 500 with a new accuracy value:
1. Fetch doc: `gws docs get --id 1fQb... > doc.json`
2. Find cell index: 500.
3. Create `req.json`: `{"requests": [{"insertText": {"location": {"index": 500}, "text": "98.1%"}}]}`
4. Run: `gws docs batchUpdate --id 1fQb... --json "$(cat req.json)"`
