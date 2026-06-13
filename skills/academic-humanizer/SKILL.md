---
name: academic-humanizer
description: Workflow for reducing AI detection scores in papers by targeting specific sections, varying sentence length (burstiness), and replacing AI-fingerprint transitions.
---

# academic-humanizer

Use this skill to reduce AI detection scores in academic manuscripts by increasing "perplexity" (unpredictability) and "burstiness" (sentence length variation).

## When to Use
- When a manuscript (especially Abstract, Introduction, or Conclusion) flags high AI detection scores.
- When the writing feels "sterile," over-polished, or uses repetitive academic connectors.

## Steps

1.  **Target Key Sections**: Focus humanization efforts on the **Abstract**, **Introduction**, and **Conclusion**. These are the most scrutinized by detectors.
2.  **Increase Perplexity**:
    - Use active voice instead of passive where appropriate.
    - Replace generic academic phrasing with more specific, nuanced descriptions.
    - Avoid "sterile" or overly perfect grammar that lacks character.
3.  **Increase Burstiness**:
    - Mix sentence lengths. Follow a long, complex sentence with a short, punchy one.
    - Break up long chains of medium-length sentences.
4.  **Replace AI Fingerprints**:
    - Remove or replace excessive connectors like "Furthermore," "Moreover," "Additionally," and "In conclusion."
    - Avoid generic opening hooks like "In recent years..." or "X represents a massive challenge."
5.  **Verification**:
    - Re-read the text to ensure it sounds like a researcher explaining their work, not a model summarizing a topic.

## Tools
- `read_file`: To analyze the current text.
- `write_file` / `edit_file`: To apply the humanized changes.

## Example
**Before (AI-like):**
"Furthermore, the results demonstrate a significant improvement in efficiency. Moreover, the model achieves high accuracy across all datasets. In conclusion, this research provides a robust framework for future studies."

**After (Humanized):**
"The results show a clear efficiency boost. While the model maintains high accuracy across all datasets, the real value lies in the framework's robustness for future applications."
