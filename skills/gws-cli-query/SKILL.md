---
name: gws-cli-query
description: Correct syntax for performing search queries using the gws CLI tool.
---

# GWS CLI Query

Use this skill when you need to search for files, messages, or events using the `gws` command-line interface.

## Steps

1.  **Use --params**: Instead of using direct flags for queries (like `-q`), use the `--params` flag followed by a JSON string.
2.  **JSON Structure**: The JSON string should contain the query key (e.g., `"q"`) and the search string.
3.  **Escaping**: Ensure the JSON string is properly escaped for the shell.

## Output Format

The command should follow this pattern:
`gws <service> <resource> list --params '{"q": "your search query"}'`

## Example

Searching for a file in Google Drive:
```bash
gws drive files list --params '{"q": "name = \'Colonomind-new\'"}'
```

Searching for an email in Gmail:
```bash
gws gmail messages list --params '{"q": "from:suryo"}'
```
