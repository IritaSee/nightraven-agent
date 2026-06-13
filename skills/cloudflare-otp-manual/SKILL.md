---
name: cloudflare-otp-manual
description: Trigger Cloudflare OTP to email for manual user entry to bypass Zero Trust panels.
---

# cloudflare-otp-manual

A manual fallback workflow to bypass Cloudflare Zero Trust panels by triggering an OTP to the user's email.

## When to use
- When automated Cloudflare bypass tools fail.
- When accessing protected domains like `admin.sakumedis.id`.
- When the agent needs the user to provide a one-time code from their email.

## Steps
1. Attempt to access the protected URL.
2. Identify the Cloudflare Zero Trust login page.
3. Enter the authorized email address (e.g., `iga@pukulenam.id`).
4. Inform the user that an OTP has been sent to their email.
5. Prompt the user to provide the code in the chat.
6. Use the provided code to complete the authentication (e.g., via `tmux` or form submission).

## Output Format
- A clear request to the user for the OTP code.

## Example
"I've triggered a Cloudflare OTP for `admin.sakumedis.id`. Please check your email (`iga@pukulenam.id`) and provide the 6-digit code here so I can proceed."
