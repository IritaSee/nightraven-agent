---
name: academic-roadmap-generator
description: Generates academic roadmaps and task breakdowns for research projects.
---

# Academic Roadmap Generator

Create structured roadmaps and detailed task breakdowns for academic research projects, from inception to publication.

## When to use
- Starting a new research project or thesis.
- Planning the submission timeline for a journal or conference.
- Breaking down complex research goals into actionable weekly or monthly tasks.

## Steps
1. **Define Scope**: Identify the core research question, target journal/conference, and hard deadlines.
2. **Phase Breakdown**: Divide the project into standard academic phases:
    - Literature Review & Gap Analysis
    - Methodology Design & Ethical Clearance
    - Data Collection/Simulation
    - Implementation & Experimentation
    - Results Analysis & Visualization
    - Manuscript Drafting & Internal Review
    - Submission & Response to Reviewers
3. **Task Granularity**: Break each phase into specific tasks (e.g., "Implement YOLOv11-nano backbone", "Draft Research in Context panel").
4. **Timeline Estimation**: Assign realistic durations to each phase based on historical performance and complexity.
5. **Validation Gates**: Define specific criteria for moving between phases (e.g., "mAP > 0.90 required before drafting results").

## Output Format
- A Markdown-formatted roadmap with headers for each phase.
- A checklist of tasks with `[ ]` markers.
- A summary table of key milestones and deadlines.

## Example
**Input**: "Create a roadmap for a 3-month project on tongue-based diabetes detection for ICICoS 2026."

**Output**:
### Phase 1: Dataset & Ethics (Weeks 1-2)
- [ ] Finalize dataset of 4,000+ images.
- [ ] Obtain KEPK ethical clearance.
### Phase 2: Model Development (Weeks 3-6)
- [ ] Train YOLOv11-nano on tongue dataset.
- [ ] Perform field validation (n=200).
...
