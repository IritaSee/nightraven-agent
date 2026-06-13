---
name: gdoc-format-preservation
description: Re-applying original styles (font, spacing, alignment) after programmatic text insertion in Google Docs to fix API formatting shifts.
---

# gdoc-format-preservation

Fixes formatting shifts (font resets, spacing changes) that occur when programmatically inserting or replacing text in Google Docs via API.

## When to use
- After using `gws-docs-write` or `gws-doc-table-patching`.
- When the user requires strict adherence to existing document styles (e.g., Times New Roman, 1.15 spacing).
- When programmatic updates cause text to revert to "Arial" or "Normal" style.

## Steps

1.  **Identify Target Styles**: Before editing, use `gws docs get --id <DOC_ID>` to inspect the `textStyle` and `paragraphStyle` of the target range.
2.  **Perform Update**: Execute the text insertion or replacement.
3.  **Capture New Indices**: Note the start and end indices of the modified text.
4.  **Re-apply Formatting**: Use a Python script with the Google Docs API (via `exec`) to send a `batchUpdate` request with `updateTextStyle` and `updateParagraphStyle`.

### Example batchUpdate Payload
```json
{
  "requests": [
    {
      "updateTextStyle": {
        "range": { "startIndex": 10, "endIndex": 50 },
        "textStyle": {
          "weightedFontFamily": { "fontFamily": "Times New Roman" },
          "fontSize": { "magnitude": 11, "unit": "PT" }
        },
        "fields": "weightedFontFamily,fontSize"
      }
    },
    {
      "updateParagraphStyle": {
        "range": { "startIndex": 10, "endIndex": 50 },
        "paragraphStyle": {
          "lineSpacing": 115,
          "alignment": "START"
        },
        "fields": "lineSpacing,alignment"
      }
    }
  ]
}
```

## Output Format
- Confirmation of the formatting applied.
- Verification of the final document state.
