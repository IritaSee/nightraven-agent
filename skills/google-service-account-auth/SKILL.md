---
name: google-service-account-auth
description: Configuring GOOGLE_APPLICATION_CREDENTIALS and Service Account JSON for non-interactive Google Workspace API access.
---

# google-service-account-auth

Configure authentication for non-interactive Google Workspace API access using a Service Account.

## When to use
- When setting up automated scripts that interact with Google Drive, Docs, Sheets, or Gmail.
- When the agent needs to perform background tasks without requiring a user-interactive OAuth flow.
- When configuring the `gws` CLI or other Google Cloud SDK tools.

## Steps

1. **Locate Service Account JSON**:
   - Ensure the service account JSON key file is present at the configured path (e.g., `/home/mandabot/.config/gws/service_account.json`).

2. **Set Environment Variable**:
   - Export the `GOOGLE_APPLICATION_CREDENTIALS` environment variable pointing to the JSON file.
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/home/mandabot/.config/gws/service_account.json"
   ```

3. **Verify Configuration**:
   - Use `gws` or `gcloud` to verify the active account.
   ```bash
   /home/mandabot/.nanobot/workspace/node_modules/@googleworkspace/cli/bin/gws auth list
   ```

4. **Domain-Wide Delegation (If Required)**:
   - If accessing user data (e.g., reading a specific user's Gmail), ensure the Service Account has Domain-Wide Delegation enabled in the Google Admin Console and specify the target user email in the API client configuration.

## Output Format
- Confirmation of the environment variable being set.
- Verification output from the auth check command.

## Example
**User**: "Set up the Google auth for the background sync script."
**Agent**:
1. Checks for `/home/mandabot/.config/gws/service_account.json`.
2. Runs `export GOOGLE_APPLICATION_CREDENTIALS="/home/mandabot/.config/gws/service_account.json"`.
3. Verifies with `gws auth list`.
4. Reports: "Authentication configured using service account manda-bot@jujurly-462416.iam.gserviceaccount.com."
