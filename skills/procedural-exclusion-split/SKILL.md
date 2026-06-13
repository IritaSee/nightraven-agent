---
name: procedural-exclusion-split
description: Grouping medical images by visual topology and timestamps to prevent data leakage in patient-blind datasets.
---

# procedural-exclusion-split

A heuristic-based data splitting method for medical image datasets where patient identifiers are unavailable (de-identified). It prevents data leakage by grouping images from the same procedural "sweep" or session.

## When to use
- When working with de-identified medical datasets (e.g., IRB-cleared clinical cohorts) that lack Patient IDs.
- When multiple images are captured from the same patient during a single procedure (e.g., endoscopy, ultrasound).
- To ensure that images with similar visual artifacts or mucosal topology do not appear in both training and validation sets.

## Steps

1. **Extract Metadata**:
   - Read image timestamps and sequence numbers from EXIF data or filenames.
   - Identify visual artifacts (e.g., scope model overlays, specific lighting patterns).

2. **Cluster by Proximity**:
   - Group images that are captured within a short time window (e.g., < 5 minutes) or have sequential filenames.
   - Use visual similarity (e.g., mucosal topology, specific lesions) to verify clusters.

3. **Assign Clusters to Splits**:
   - Instead of splitting individual images, split the *clusters*.
   - Assign all images in a cluster to either Training, Validation, or Test set (e.g., 80/10/10).

4. **Verify Independence**:
   - Check that no two images from the same procedural sweep exist in different splits.

## Output Format
- A manifest or CSV file mapping filenames to their assigned split (Train/Val/Test).
- A summary of the number of clusters and images per split.

## Example
**User**: "Split the NTUH dataset for training, but make sure we don't have data leakage since we don't have Patient IDs."
**Agent**:
1. Analyzes timestamps and visual artifacts in the dataset.
2. Groups images into 150 "procedural clusters" based on temporal proximity.
3. Randomly assigns 120 clusters to Train, 15 to Val, and 15 to Test.
4. Generates `dataset_split.csv` ensuring all images from a single sweep stay together.
