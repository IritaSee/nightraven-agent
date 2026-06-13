---
name: anthropic-cache-formatter
description: Automatically inserts `cache_control` tags at strategic points for Anthropic Claude API requests to optimize costs and latency using a "Static-first, dynamic-last" structure.
---

# Anthropic Cache Formatter

This skill helps optimize Anthropic Claude API requests by strategically placing `cache_control` tags to maximize cache hits and minimize costs.

## When to Use
- When preparing large prompts for Anthropic Claude.
- When the prompt contains large static sections (e.g., system instructions, few-shot examples, large documents) followed by dynamic user input.
- When you want to leverage Anthropic's prompt caching feature (up to 90% discount).

## Principles
- **Static-first, dynamic-last**: Place stable, unchanging content at the beginning of the prompt.
- **Strategic Breakpoints**: Anthropic supports up to 4 `cache_control` tags.
- **TTL Awareness**: Cache resets on hit but has a 5-minute TTL.

## Steps
1. **Identify Static Content**: Group system instructions, tool definitions, and large reference documents.
2. **Identify Dynamic Content**: Isolate the specific user query or task-specific data that changes frequently.
3. **Structure the Prompt**:
    - System Message (Static)
    - Reference Documents / Few-shot Examples (Static)
    - User Query (Dynamic)
4. **Insert Tags**: Add `"cache_control": {"type": "ephemeral"}` to the end of the largest static blocks.

## Example Request Structure

```json
{
  "model": "claude-3-5-sonnet-20240620",
  "max_tokens": 1024,
  "system": [
    {
      "type": "text",
      "text": "You are a research assistant...",
      "cache_control": {"type": "ephemeral"}
    }
  ],
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "<large_document>...</large_document>",
          "cache_control": {"type": "ephemeral"}
        },
        {
          "type": "text",
          "text": "Please summarize the document above."
        }
      ]
    }
  ]
}
```

## Output Format
When asked to format a request, provide the JSON structure with `cache_control` tags appropriately placed.
