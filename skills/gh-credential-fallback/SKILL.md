---
name: gh-credential-fallback
description: Extract credentials from .git-credentials when standard GitHub CLI login is unavailable.
---

# gh-credential-fallback

Extract GitHub credentials from the local `.git-credentials` file when `gh auth status` fails or the environment lacks interactive login capabilities.

## When to use
- When `gh` commands fail due to authentication errors.
- When the environment is non-interactive and `gh auth login` cannot be used.
- When you need to manually construct an authenticated URL or set `GITHUB_TOKEN`.

## Steps
1. Locate the `.git-credentials` file (usually in `~/.git-credentials` or the project root).
2. Read the file using `read_file`.
3. Parse the URL-encoded credentials (format: `https://user:token@github.com`).
4. Extract the token.
5. Export the token as an environment variable or use it directly in `gh` commands with `--with-token`.

## Output Format
- The extracted token or a confirmation that it has been applied to the current session.

## Example
```bash
# Reading the credentials file
cat ~/.git-credentials
# Output: https://username:ghp_yourtokenhere@github.com

# Using the token with gh
echo "ghp_yourtokenhere" | gh auth login --with-token
```
