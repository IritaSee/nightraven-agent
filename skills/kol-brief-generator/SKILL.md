---
name: kol-brief-generator
description: Creating KOL collaboration briefs in Word (TNR 11pt, 1.15 spacing) with persona-aligned content pillars.
---

# KOL Brief Generator

Use this skill to generate professional collaboration briefs for Key Opinion Leaders (KOLs). This workflow ensures that the brief aligns with specific brand personas and content pillars while maintaining strict academic-style formatting in Word.

## When to Use
- When initiating a new KOL collaboration for SakuMedis or other projects.
- When a structured, professional brief is required in `.docx` format.
- When you need to align content requests with established "Content Pillars".

## Steps

1.  **Identify the KOL & Persona**: Retrieve the KOL's handle and persona details from `MEMORY.md` (e.g., dr. Audrey Beatricia Suwandi, "Aesthetic MD").
2.  **Select Content Pillars**: Choose relevant pillars (e.g., "The Aesthetic Clinical Toolkit", "The 30-Second Life Saver").
3.  **Draft Content**: Create a Markdown draft of the brief including:
    -   Campaign Objective
    -   KOL Deliverables (e.g., 1x Reel, 2x Stories)
    -   Key Messaging (aligned with pillars)
    -   Visual Guidelines
    -   Timeline & Reporting
4.  **Format & Generate**: Use `word-docx` or `academic-docx-generator` to convert the Markdown to a `.docx` file with the following specs:
    -   Font: Times New Roman, 11pt.
    -   Line Spacing: 1.15.
    -   Margins: 1-inch all sides.
5.  **Delivery**: Deliver the file via Telegram using `academic-docx-telegram-delivery`.

## Output Format
- A `.docx` file delivered via Telegram.
- Professional, structured sections with clear headings.

## Example
**User**: "Manda, buatkan brief untuk dr. Audrey (@beatriciaaudrey) buat promo SakuMedis. Pake pillar 'The 30-Second Life Saver'."

**Agent Workflow**:
1.  Retrieves dr. Audrey's "Aesthetic MD" persona from memory.
2.  Drafts a brief focusing on how SakuMedis helps aesthetic doctors make quick, life-saving clinical decisions in 30 seconds.
3.  Generates `KOL_Brief_Audrey_SakuMedis.docx` with TNR 11pt and 1.15 spacing.
4.  Sends the file to the user on Telegram.
