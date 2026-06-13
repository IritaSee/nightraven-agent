---
name: cloudflare-otp-handler
description: Automated handling of Cloudflare 2FA/OTP for protected administrative interfaces.
---

# Cloudflare OTP Handler

Use this skill to navigate administrative interfaces protected by Cloudflare Zero Trust or 2FA/OTP requirements.

## When to Use
- Accessing `admin.sakumedis.id` or other Cloudflare-protected domains.
- Automating tasks that require bypassing or fulfilling 2FA challenges.

## Steps

1. **Trigger OTP**: Attempt to access the protected URL to trigger the Cloudflare OTP email.
2. **Retrieve OTP**: Use `gws-gmail-read` or `gws-gmail-triage` to find the most recent email from Cloudflare containing the verification code.
3. **Extract Code**: Parse the email body to extract the 6-digit or alphanumeric OTP.
4. **Submit Code**: Use the appropriate tool (e.g., `tmux` for interactive CLI sessions or `exec` with a script) to input the code into the authentication form.
5. **Verify Access**: Confirm that the session is authenticated and the target page is accessible.

## Tools
- `gws-gmail-read`: To fetch the OTP from the user's inbox.
- `tmux`: To handle interactive login prompts if using a CLI-based browser or tool.
- `exec`: To run automation scripts that handle the form submission.

## Example
1. Agent attempts to access `admin.sakumedis.id`.
2. Cloudflare prompts for an email code.
3. Agent calls `gws-gmail-read` searching for "Cloudflare" in the last 2 minutes.
4. Agent extracts `123456` and submits it via the active session.
