---
name: academic-manuscript-sync
description: A workflow for reordering citations sequentially, synchronizing figure/table references, and applying specific academic formatting (TNR 11pt, 1.15 spacing) before Telegram delivery.
---

# academic-manuscript-sync

Use this skill when preparing a final or revised academic manuscript for delivery. It ensures that citations are sequential, figure/table references are synchronized with the text, and the document adheres to the user's specific typography preferences.

## When to use
- Before sending a manuscript draft to the user via Telegram.
- When citations have become out of order due to text edits.
- When new figures or tables have been added and need consistent numbering.

## Steps

1.  **Citation Reordering**:
    - Scan the text for citation markers (e.g., `[1]`, `[1, 2]`, or `\cite{...}`).
    - Reassign numbers based on the order of first appearance in the document.
    - Update the bibliography/references section to match the new numbering.
    - Deduplicate references (e.g., ensure the same author/paper isn't listed twice with different numbers).

2.  **Figure/Table Synchronization**:
    - Ensure all figures and tables are numbered sequentially (Fig. 1, Fig. 2, etc.).
    - Verify that every figure/table mentioned in the text exists and that the text reference matches the caption number.

3.  **Academic Formatting**:
    - Apply **Times New Roman**, **11pt** font.
    - Set line spacing to **1.15**.
    - Set margins to **1 inch** on all sides.
    - Replace em-dashes (`—`) with commas or parentheses as per user preference.

4.  **Delivery**:
    - Generate the final `.docx` file.
    - Send the file directly to the user via Telegram.

## Tools Used
- `word-docx`: For applying styles, formatting, and managing document structure.
- `python`: For regex-based citation and reference reordering.
- `telegram`: For final delivery.

## Example

**User**: "Manda, please reorder the citations in the MIFOCAT paper and send me the clean version."

**Agent**:
1. Reads the current manuscript.
2. Identifies that `[37]` appears before `[5]`.
3. Re-indexes all citations sequentially.
4. Updates the reference list.
5. Applies TNR 11pt and 1.15 spacing.
6. Saves as `MIFOCAT_v2_Final.docx`.
7. Sends to Telegram.
