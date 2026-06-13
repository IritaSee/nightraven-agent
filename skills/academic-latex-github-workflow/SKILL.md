---
name: academic-latex-github-workflow
description: Drafting IEEE conference manuscripts in LaTeX and managing version control via GitHub.
---

# Academic LaTeX & GitHub Workflow

Drafting IEEE conference manuscripts in LaTeX and managing version control via GitHub to ensure collaborative rigor and document integrity.

## When to Use
- When starting a new IEEE conference paper.
- When collaborating on LaTeX manuscripts using GitHub repositories.
- When managing revisions and version history for academic submissions.

## Steps

### 1. Repository Setup
- Initialize a GitHub repository for the paper.
- Include the `IEEEtran` class file and necessary `.bib` files.
- Set up a `.gitignore` to exclude LaTeX build artifacts (e.g., `.aux`, `.log`, `.pdf`).

### 2. Drafting in LaTeX
- Use the IEEE two-column template.
- Organize content into sections: Abstract, Introduction, Related Work, Methodology, Results, Discussion, and Conclusion.
- Use `\cite{}` for references and `\ref{}` for figures/tables.

### 3. Version Control with GitHub
- Commit changes frequently with descriptive messages (e.g., "Drafted Methodology section", "Updated Table 1 results").
- Use branches for major revisions or experimental sections.
- Push to GitHub to sync with collaborators.

### 4. Revision Management
- Use the `soul` package for highlighting changes (`\hl{...}`) if required by reviewers.
- Maintain a "clean" branch for the final submission version.

## Tools Used
- `gh` CLI for repository management.
- `write_file` for creating/editing `.tex` and `.bib` files.
- `exec` for running LaTeX build commands or scripts (e.g., `remove_highlights.py`).

## Output Format
- A structured GitHub repository containing `.tex` source files, figures, and bibliography.
- Compiled PDF (if local build tools are available).

## Example
```bash
# Initialize repo
gh repo create my-ieee-paper --public --clone
cd my-ieee-paper

# Create main.tex from template
# (Agent writes LaTeX content to main.tex)

# Commit and push
git add .
git commit -m "Initial draft of IEEE conference paper"
git push origin main
```
