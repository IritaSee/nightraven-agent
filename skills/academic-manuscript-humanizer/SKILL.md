---
name: academic-manuscript-humanizer
description: Paraphrases academic text (Abstract, Intro, Conclusion) into .docx files to lower AI detection while maintaining technical rigor.
---

# Academic Manuscript Humanizer

Paraphrase and restructure academic text to reduce AI detection scores while preserving technical accuracy and formal tone.

## When to use
- A manuscript shows high AI detection scores in preliminary checks.
- Preparing the Abstract, Introduction, or Conclusion for final submission.
- The text feels "sterile" or uses repetitive AI-style transitions (e.g., "Furthermore", "Moreover").

## Steps
1. **Targeting**: Focus on the Abstract, Introduction, and Conclusion as these are most prone to AI detection.
2. **Perplexity & Burstiness**:
    - Increase **perplexity** by using active voice and varied vocabulary.
    - Increase **burstiness** by mixing short, punchy sentences with longer, complex ones.
3. **Transition Replacement**: Replace generic AI transitions with context-specific connectors or structural transitions.
4. **Hook Refinement**: Avoid generic hooks like "In recent years..." or "X represents a massive challenge." Use specific clinical or technical problem statements.
5. **Technical Rigor Check**: Ensure that paraphrasing does not alter the meaning of technical terms, formulas, or specific findings.
6. **Document Generation**: Use `python-docx` to generate a new `.docx` file with the humanized text, maintaining TNR 11pt and 1.15 spacing.

## Output Format
- A `.docx` file containing the humanized sections.
- A summary of changes (e.g., "Reduced AI score from 85% to 12%").

## Example
**Original**: "Furthermore, the results demonstrate that the model is highly effective. In recent years, deep learning has become popular."
**Humanized**: "Beyond raw performance, the model's stability across datasets suggests clinical viability. While deep learning adoption has surged, specific bottlenecks in boundary detection remain."
