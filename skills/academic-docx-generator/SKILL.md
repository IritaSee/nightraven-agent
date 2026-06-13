---
name: academic-docx-generator
description: Converts Markdown to DOCX enforcing Times New Roman 11pt, 9pt tables, 1.15 spacing, and 1-inch margins.
---

# Academic DOCX Generator

Use this skill to convert Markdown research drafts or manuscript sections into professionally formatted Microsoft Word (.docx) files that adhere to specific academic standards.

## When to Use
- When you have a Markdown draft that needs to be submitted or shared as a Word document.
- When you need to ensure consistent typography (Times New Roman) and spacing (1.15) across a document.
- When tables need to be downsized to 9pt to fit portrait orientation.

## Steps
1. **Prepare Markdown**: Ensure the source text is in Markdown format.
2. **Run Conversion Script**: Use a Python script (utilizing `python-docx`) to:
    - Set font to **Times New Roman**, size **11pt**.
    - Set line spacing to **1.15**.
    - Set margins to **1 inch** on all sides.
    - Identify tables and set their font size to **9pt**.
    - Replace em-dashes (—) with commas or parentheses as per user preference.
3. **Verify Layout**: Check that tables and figures are correctly positioned.
4. **Output**: Save the file with a `.docx` extension.

## Output Format
- A `.docx` file delivered to the workspace or sent via Telegram.
- Typography: Times New Roman, 11pt (Body), 9pt (Tables).
- Spacing: 1.15 lines.
- Margins: 1-inch (2.54 cm).

## Example
**Input (Markdown):**
```markdown
# Introduction
Ulcerative colitis (UC) is a chronic inflammatory bowel disease...
```

**Output:**
A Word document with the text in 11pt Times New Roman, 1.15 spacing, and 1-inch margins.
