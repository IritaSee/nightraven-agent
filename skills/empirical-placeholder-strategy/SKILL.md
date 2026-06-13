---
name: empirical-placeholder-strategy
description: Using bracketed placeholders for missing data in drafts to ensure data integrity.
---

# Empirical Placeholder Strategy

Use this skill when drafting or revising academic manuscripts where specific empirical values (numbers, percentages, dates) are unknown or haven't been finalized. This prevents hallucination and alerts the user to provide the data.

## When to Use
- Drafting a paper before experiments are fully completed.
- Paraphrasing text where the original numbers are unclear.
- Meeting length requirements by adding tables with pending data.

## Steps

1. **Identify Missing Data**: Note any point where a specific value is required but not available in the current context.
2. **Insert Bracketed Placeholders**: Use clear, descriptive labels inside square brackets.
    - Format: `[Label]` or `[Value: Description]`
    - Examples: `[Jumlah Unit]`, `[Accuracy %]`, `[p-value]`, `[Date of Observation]`.
3. **Highlight (Optional)**: If using LaTeX, wrap the placeholder in `\hl{...}` to make it visible.
4. **Notify User**: Explicitly list the placeholders used in the response so the user knows what data is missing.

## Output Format

Text or document containing placeholders like:
> "The proposed system was tested on [Jumlah Unit] residential units, achieving an average efficiency of [Efficiency %]."

## Example

**User**: "Draft the results section for the solar study. I don't have the final unit count yet."

**Agent**:
"The field validation was conducted in Penglipuran Village. A total of **[Jumlah Unit]** residential rooftops were analyzed. The YOLOv8s-seg model identified **[Total Area]** m² of viable roof space, leading to an estimated annual yield of **[GWh/year]**."
