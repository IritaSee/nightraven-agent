---
name: git-latex-sync
description: Resolve remote LaTeX/Overleaf conflicts using git rebase and git stash to maintain a clean history.
---

# git-latex-sync

Use this skill when you need to synchronize a local LaTeX project with a remote repository (like Overleaf via Git) and encounter merge conflicts or a "diverged" history. This workflow prioritizes a clean, linear history using `rebase` instead of merge commits.

## When to use
- When `git push` is rejected because the remote contains work you do not have locally.
- When working with Overleaf's Git integration, which often results in small, frequent remote commits.
- When you want to apply your local LaTeX changes on top of the latest remote version without creating "Merge branch..." commits.

## Steps

1. **Stash local changes**:
   If you have uncommitted changes, move them to the stash to ensure a clean working directory.
   ```bash
   git stash
   ```

2. **Fetch and Rebase**:
   Pull the latest changes from the remote and re-apply your local commits on top of them.
   ```bash
   git pull --rebase origin master
   ```
   *(Replace `master` with the appropriate branch name if different, e.g., `main`)*.

3. **Resolve Conflicts (if any)**:
   If the rebase stops due to conflicts in `.tex` or `.bib` files:
   - Open the conflicted files.
   - Look for `<<<<<<<`, `=======`, and `>>>>>>>` markers.
   - Manually merge the LaTeX content.
   - Stage the resolved files: `git add <file>`.
   - Continue the rebase: `git rebase --continue`.

4. **Pop Stash**:
   Bring back your uncommitted changes.
   ```bash
   git stash pop
   ```
   - If this causes conflicts, resolve them manually as in Step 3.

5. **Verify and Push**:
   Ensure the manuscript still compiles (e.g., check with `pdflatex` or `latexmk` if available) and push.
   ```bash
   git push origin master
   ```

## Output Format
Provide a summary of the synchronization:
- Number of commits rebased.
- Files resolved (if conflicts occurred).
- Final status of the local and remote branches.

## Example
**User**: "I can't push my changes to the Overleaf repo, it says the remote has changes I don't have."

**Agent**:
1. Runs `git stash`.
2. Runs `git pull --rebase origin master`.
3. (If conflict in `main.tex`) Resolves the LaTeX overlap in the introduction.
4. Runs `git add main.tex` and `git rebase --continue`.
5. Runs `git stash pop`.
6. Runs `git push origin master`.
7. **Response**: "Successfully synchronized with the remote repository. Rebased 2 local commits onto the latest remote changes. Resolved one conflict in `main.tex` (Introduction section). Local branch is now up-to-date and pushed."
