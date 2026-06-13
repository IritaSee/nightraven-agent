---
name: academic-table-consistency-check
description: Verifying N-values, accuracy, and per-class metrics against Confusion Matrix calculations in manuscripts.
---

# Academic Table Consistency Check

Use this skill when reviewing academic manuscripts to ensure that numerical data across different tables and figures are mathematically consistent, especially when derived from a Confusion Matrix.

## When to use
- Before submitting a manuscript to a journal.
- When updating results after a new training run.
- When reviewers point out numerical inconsistencies.

## Steps
1. **Extract Data**: Use `read_file` to extract the Confusion Matrix and all results tables (Accuracy, Precision, Recall, F1, N-values).
2. **Verify N-values**: Sum the rows/columns of the Confusion Matrix to verify the total sample size (N) matches the values reported in the "Data" or "Participants" sections.
3. **Recalculate Metrics**:
    - **Accuracy**: (TP + TN) / Total
    - **Precision**: TP / (TP + FP)
    - **Recall**: TP / (TP + FN)
    - **F1-Score**: 2 * (Precision * Recall) / (Precision + Recall)
4. **Cross-Table Validation**: Compare the recalculated values against the reported values in Tables 2, 3, 4, etc.
5. **Report Discrepancies**: List any mismatches found, specifying the table number, the reported value, and the calculated value.

## Output Format
- **Status**: [Consistent / Inconsistent]
- **Discrepancies**:
    - Table [X], Row [Y]: Reported [Value], Calculated [Value]
- **N-Value Check**: Reported [N], Calculated [Sum of CM]

## Example
**Input**: Confusion Matrix with TP=90, FP=10, FN=5, TN=95. Table 2 reports Accuracy=95%.
**Calculation**: (90+95)/200 = 92.5%.
**Output**: 
- **Status**: Inconsistent
- **Discrepancies**: Table 2, Accuracy: Reported 95%, Calculated 92.5%.
