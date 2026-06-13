---
name: kol-brief-automation
description: Generates KOL briefs from Markdown to DOCX with specific academic formatting and delivers via Telegram.
---

# KOL Brief Automation

Use this skill to automate the creation and delivery of Key Opinion Leader (KOL) collaboration briefs. It combines document generation with direct communication.

## When to Use
- When a new KOL is selected for a campaign (e.g., SakuMedis).
- When you need to convert a Markdown brief into a professional `.docx` file.
- When the final document needs to be sent to the user via Telegram for immediate review or distribution.

## Steps
1. **Draft Content**: Create the brief in Markdown, including sections for Campaign Objectives, Content Pillars (e.g., "The Mawapres Secret Sauce"), and Deliverables.
2. **Format to DOCX**: Use `academic-docx-generator` or a custom script to convert the Markdown to `.docx`.
   - Font: Times New Roman, 11pt.
   - Spacing: 1.15.
   - Margins: 1-inch.
3. **Telegram Delivery**: Use the `academic-docx-telegram-delivery` workflow to send the generated file to the user's Telegram Chat ID (913909431).

## Output Format
- A `.docx` file delivered via Telegram.
- A confirmation message in the chat with the file name.

## Example
**Input Markdown:**
```markdown
# KOL Brief: @nicole.tanada
**Campaign**: SakuMedis Social Media Promotion
**Pillar**: The Mawapres Secret Sauce
...
```

**Action:**
1. Generate `KOL_Brief_Nicole_Tanada.docx`.
2. Send to Telegram.
