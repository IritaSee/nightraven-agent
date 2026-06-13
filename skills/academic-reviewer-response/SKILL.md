---
name: academic-reviewer-response
description: Drafting structured responses to academic reviewers by aligning to manuscript sections, framing innovations as mathematical frameworks, and citing specific locations.
---

# academic-reviewer-response

Use this skill to draft formal "Response to Reviewers" documents for journal resubmissions or revisions. This workflow ensures every reviewer comment is addressed with precision, citing exact locations in the revised manuscript.

## When to Use
- When preparing a rebuttal or response document after receiving peer review.
- When resubmitting a rejected paper to a new journal and needing to address previous feedback.

## Steps

1.  **Extract Reviewer Comments**: List each reviewer comment verbatim.
2.  **Align with Manuscript**: Identify the specific section, paragraph, and line numbers in the *revised* manuscript where the change was made.
3.  **Frame the Response**:
    *   Use formal, structured English.
    *   Frame technical innovations as rigorous frameworks (e.g., "Multi-Objective Optimization (MOO) framework" instead of "combined loss").
    *   Acknowledge the reviewer's insight ("The reviewer makes an excellent point regarding...").
4.  **Cite Specific Locations**: Every response must include:
    *   **Section**: e.g., Section 3.2.
    *   **Paragraph**: e.g., Paragraph 3.
    *   **Quote**: Provide the exact text added or modified.
5.  **Format the Output**: Use a clear "Reviewer Comment" vs. "Author Response" structure.

## Output Format

**Reviewer [X], Comment [Y]**:
"[Verbatim comment from reviewer]"

**Author Response**:
"We thank the reviewer for this insightful suggestion. We have addressed this by [description of change]. Specifically, we have [reframed/added/modified] the [concept] as a [mathematical/theoretical framework].

**Location in Revised Manuscript**:
- **Section**: [Section Number/Title]
- **Paragraph**: [Paragraph Number]
- **Revised Text**: "[Exact quote from the manuscript]"

## Example

**Reviewer 1, Comment 1**:
"The justification for the combined loss function is unclear. Why use these three specific components?"

**Author Response**:
"We appreciate the reviewer's request for clarification. We have now reframed the proposed MIFOCAT loss function as a Multi-Objective Optimization (MOO) framework that balances pixel-wise intensity (MSE), class imbalance (Focal Loss), and structural entropy (CCE). This unification ensures gradient stability and prevents the false-positive artifacts observed in baseline models.

**Location in Revised Manuscript**:
- **Section**: 3. Loss Function Unification
- **Paragraph**: 2
- **Revised Text**: "The MIFOCAT framework is formulated as a multi-objective optimization problem, where the composite loss $\mathcal{L}_{total} = \lambda_1 \mathcal{L}_{MSE} + \lambda_2 \mathcal{L}_{Focal} + \lambda_3 \mathcal{L}_{CCE}$ is designed to stabilize the manifold of the gradient flow..."
