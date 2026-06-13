---
name: exhaustive-paper-search
description: Locate academic papers by searching full titles after keyword and author-specific searches fail.
---

# exhaustive-paper-search

Use this skill when initial keyword or author-based searches fail to locate a specific academic paper mentioned in context.

## Steps

1. **Full Title Search**: Wrap the entire paper title in double quotes and search via `web_search`.
2. **Repository Search**: Specifically search within known academic repositories if the title search is too broad:
   - `site:researchgate.net "Full Paper Title"`
   - `site:ieeexplore.ieee.org "Full Paper Title"`
   - `site:arxiv.org "Full Paper Title"`
3. **Author + Snippet**: If the title is unknown, combine the author's name with a unique phrase or technical term from the paper (e.g., `"Author Name" "specific algorithm name"`).
4. **DOI Lookup**: If a DOI is found in any snippet, use it to find the direct source.

## Example

If searching for "JARDIRA" papers fails:
1. Search: `"Smart Mosque Security Systems" JARDIRA`
2. Search: `site:jurnal.itg.ac.id "Smart Mosque Security Systems"` (searching the specific journal's domain)
