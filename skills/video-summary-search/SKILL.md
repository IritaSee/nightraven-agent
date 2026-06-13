---
name: video-summary-search
description: Use web search for video summaries when specialized CLI tools are missing.
---

# video-summary-search

A fallback workflow to obtain video summaries using web search when specialized tools like `summarize` or YouTube transcript extractors are unavailable or fail.

## When to use
- When the `summarize` tool fails to process a video URL.
- When the environment lacks video/audio processing libraries.
- When the video is long and a quick external summary is needed to maintain context momentum.

## Steps
1. Extract the video title or ID from the URL.
2. Perform a `web_search` using queries like:
   - `"[Video Title]" summary`
   - `"[Video Title]" key takeaways`
   - `"[Video Title]" transcript`
3. Synthesize the search results into a concise summary.
4. Focus on "Context Momentum"—extracting only the most relevant points to the current research task.

## Output Format
- A structured summary including:
  - **Core Message**
  - **Key Takeaways**
  - **Relevance to Current Project**

## Example
**User**: "Summarize this video: https://www.youtube.com/watch?v=example"
**Agent**: (After tool failure) "I couldn't process the video directly, but based on a web search for '[Video Title]', here are the key takeaways..."
