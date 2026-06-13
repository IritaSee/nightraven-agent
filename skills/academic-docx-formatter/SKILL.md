---
name: academic-docx-formatter
description: Automates academic document formatting (TNR 11pt, 1.15 spacing, 9pt tables) using python-docx for Markdown-to-DOCX conversion.
---

# Academic DOCX Formatter

This skill automates the conversion of Markdown content into professionally formatted academic Word documents (.docx) using `python-docx`.

## When to Use
- When you need to generate a research paper draft from Markdown.
- When specific academic typography is required (Times New Roman, 11pt, 1.15 spacing).
- When tables need to be reduced to 9pt font for better fit in portrait orientation.

## Workflow
1. **Prepare Content**: Ensure the source text is in Markdown format.
2. **Execute Conversion**: Use a Python script with `python-docx` to apply styles.
3. **Apply Typography**:
   - Font: Times New Roman
   - Body Size: 11pt
   - Line Spacing: 1.15
   - Table Font: 9pt
   - Margins: 1-inch (all sides)
4. **Output**: Save as `.docx`.

## Example Script Logic
```python
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(11)

# Set spacing
paragraph_format = style.paragraph_format
paragraph_format.line_spacing = 1.15

# Set margins
for section in doc.sections:
    section.top_margin = Inches(1)
    section.bottom_margin = Inches(1)
    section.left_margin = Inches(1)
    section.right_margin = Inches(1)

# Table formatting logic
# ... iterate through tables and set font size to 9pt
```

## Output Format
A `.docx` file delivered to the user or uploaded to Google Drive.
