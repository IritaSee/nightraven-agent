---
name: ieee-manuscript-formalization
description: Standardizing research papers to IEEE format using Roman numeral sectioning, Keywords blocks, Introduction roadmaps, and technical directive language.
---

# IEEE Manuscript Formalization

Use this skill to standardize engineering or technical research papers into the formal IEEE manuscript style. This ensures structural compliance and technical precision required for IEEE conferences and journals.

## When to Use
- Preparing a draft for an IEEE conference (e.g., ICICoS, IEEE Access).
- Converting a general research draft into a formal engineering manuscript.
- Standardizing sectioning and terminology for engineering supervisors.

## Steps

1.  **Structural Reorganization**:
    *   Apply Roman numeral sectioning (e.g., I. INTRODUCTION, II. RELATED WORK).
    *   Ensure the **Keywords** block is placed immediately after the Abstract.
    *   Add a "Roadmap" paragraph at the end of the Introduction (e.g., "The remainder of this paper is organized as follows: Section II discusses...").

2.  **Technical Terminology Refinement**:
    *   Replace generic terms with precise engineering specifications (e.g., use "monocrystalline silicon" instead of "solar panel material").
    *   Explicitly name models and versions (e.g., "YOLOv8s-seg" instead of "the segmentation model").
    *   Use directive, active language for methodology.

3.  **Formatting Check**:
    *   Verify that all figures and tables are referenced sequentially in the text.
    *   Ensure mathematical notations follow IEEE standards (e.g., variables in italics, vectors in bold).

4.  **Final Review**:
    *   Check for "humanized" but technically rigorous phrasing in the Abstract and Conclusion.

## Output Format
The output should be a structured Markdown or LaTeX draft (or a `.docx` file if using `academic-docx-generator`) that follows the IEEE hierarchy.

## Example

### Input
> We used a solar panel model to check the energy in the village. Section 1 is intro, section 2 is what others did.

### Formalized Output
> **Keywords**—Solar Photovoltaic, Energy Estimation, YOLOv8s-seg.
>
> I. INTRODUCTION
> ...
> The remainder of this paper is organized as follows: Section II reviews the related literature on geospatial PV estimation; Section III details the proposed methodology using YOLOv8s-seg and monocrystalline silicon parameters; Section IV presents the results; and Section V concludes the study.
>
> II. RELATED WORK
> ...
