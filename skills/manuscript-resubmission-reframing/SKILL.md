---
name: manuscript-resubmission-reframing
description: Adapting rejected research for new journals by shifting narrative focus (e.g., clinical to engineering) and justifying "optimal" results via stability/boundary metrics rather than raw IoU.
---

# manuscript-resubmission-reframing

Use this skill when a paper has been rejected and needs a strategic pivot in narrative or technical emphasis to fit a different journal's scope (e.g., moving from a clinical journal to an engineering/technical journal).

## When to use
- After a rejection where the feedback suggests a lack of "fit" or "novelty" in the original domain.
- When resubmitting to a journal with a different primary audience (e.g., IJIES to IREA).
- When raw performance metrics (IoU, Accuracy) are not the strongest selling point, but stability or efficiency are.

## Steps
1. **Identify the Pivot**: Determine the new narrative angle.
    - *Clinical -> Engineering*: Focus on loss function stability, computational speed, and mathematical robustness.
    - *Engineering -> Clinical*: Focus on diagnostic utility, boundary accuracy (MSD/HD), and interpretability.
2. **Re-evaluate Metrics**: Shift focus from standard metrics to "stability" metrics.
    - Use Mean Surface Distance (MSD) or Hausdorff Distance (HD) to justify boundary accuracy.
    - Highlight cross-validation stability and inference speed (e.g., "68x faster").
3. **Update Introduction/Discussion**:
    - Rewrite the problem statement to align with the new journal's "Engineering Aspects" or "Clinical Needs".
    - Frame the contribution as a "Multi-Objective Optimization" or "Unified Framework" if moving to technical journals.
4. **Justify Hyperparameters**: Provide mathematical or empirical justification for specific weights (e.g., r1, r2, r3) to satisfy engineering reviewers.
5. **Reference Alignment**: Update the bibliography to include recent (2025-2026) papers from the target journal or related technical domains.

## Output Format
- Strategic pivot plan (bullet points).
- Revised Abstract and Introduction sections.
- New "Technical Contribution" or "Clinical Utility" section.

## Example
**User**: "MIFOCAT was rejected by IJIES. They said it's too technical. Let's try IREA."
**Agent**: "Understood. For IREA (Electrical Engineering), we will pivot the narrative from 'Myocardium Segmentation' to 'Multi-Objective Loss Optimization for Real-time Medical Imaging'. I will emphasize the 68x speedup and the mathematical stability of the MSE+Focal+CCE composite loss."
