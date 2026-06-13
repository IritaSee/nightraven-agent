---
name: academic-docx-telegram-delivery
description: Format academic drafts in Word (.docx) with specific typography (Times New Roman, 11pt, 1.15 line spacing, 1-inch margins, no em-dashes) and deliver directly via Telegram.
---

# Academic DOCX & Telegram Delivery

This skill guides the formatting of academic drafts in Word (.docx) according to specific user preferences and delivering them directly via Telegram.

## When to Use
Use this skill when the user requests academic document drafts, paper revisions, or generated academic files, and wants them formatted in a professional academic style and delivered directly to their Telegram.

## Formatting Requirements
- **File Format**: Microsoft Word (.docx)
- **Font**: Times New Roman, 11pt
- **Line Spacing**: 1.15
- **Paragraph Indent**: Hanging indent for references/citations
- **Margins**: 1-inch (2.54 cm) on all sides
- **Punctuation**: No em-dashes (—). Replace all em-dashes with commas or parentheses as appropriate for the context.

## Steps for Execution

1. **Draft/Edit Content**: Prepare or revise the academic text according to the user's request. Ensure all em-dashes are replaced with commas or parentheses.
2. **Generate DOCX**: Use python-docx or the `word-docx` skill to create a `.docx` document. Apply the formatting rules:
   - Font: Times New Roman, 11pt
   - Line Spacing: 1.15
   - Margins: 1 inch
   - Hanging indent for bibliography/references
3. **Deliver via Telegram**: Send the generated `.docx` file directly to the user's Telegram chat ID (1297084530) using the appropriate delivery mechanism or notification tool.

## Output Format
- A professionally formatted `.docx` file delivered directly to the user's Telegram.
- A brief confirmation message in the chat indicating that the file has been sent.

## Example Workflow

### User Request
"Please draft the methodology section for our new paper and send it to my Telegram."

### Execution Steps
1. Draft the methodology text, ensuring no em-dashes are used.
2. Create a Python script using `python-docx` to generate the document:
   ```python
   import docx
   from docx.shared import Pt, Inches

   doc = docx.Document()
   # Set margins to 1 inch
   for section in doc.sections:
       section.top_margin = Inches(1)
       section.bottom_margin = Inches(1)
       section.left_margin = Inches(1)
       section.right_margin = Inches(1)

   # Set style
   style = doc.styles['Normal']
   font = style.font
   font.name = 'Times New Roman'
   font.size = Pt(11)
   style.paragraph_format.line_spacing = 1.15

   # Add content...
   doc.save('methodology_draft.docx')
   ```
3. Send `methodology_draft.docx` to Telegram Chat ID `1297084530`.
4. Reply to the user: "I have drafted the methodology section and sent the formatted .docx file directly to your Telegram!"
