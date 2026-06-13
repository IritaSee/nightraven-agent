---
name: gdoc-manuscript-collaboration
description: Converting .docx to Google Docs format to enable programmatic editing and real-time collaboration.
---

# gdoc-manuscript-collaboration

Convert local `.docx` manuscripts to native Google Docs format to facilitate real-time collaboration and programmatic editing via the Google Workspace API.

## When to use
- When the user wants to collaborate on a manuscript draft in real-time.
- When the agent needs to perform complex edits or formatting updates on a document that is shared with others.
- When moving from a local-first workflow to a cloud-collaborative workflow.

## Steps

1. **Upload and Convert**:
   - Use `gws-drive-upload` with the `--convert` flag (or equivalent API parameter) to upload the `.docx` file and convert it to Google Docs format.
   ```bash
   gws drive upload path/to/manuscript.docx --convert
   ```

2. **Retrieve File ID**:
   - Capture the File ID of the newly created Google Doc from the upload output.

3. **Share with Collaborators**:
   - Use `gws-drive` to grant edit permissions to the user or other team members.
   ```bash
   gws drive share [FILE_ID] --role writer --type user --email user@example.com
   ```

4. **Perform Edits**:
   - Use `gws-docs` or `gws-docs-write` to append content, update sections, or apply formatting programmatically.

5. **Provide Link**:
   - Share the Google Doc URL with the user for immediate access.

## Output Format
- The URL of the converted Google Doc.
- Confirmation of sharing permissions.

## Example
**User**: "Move the ColonoMind draft to Google Docs so we can both edit it."
**Agent**:
1. Uploads `ColonoMind_Draft.docx` using `gws drive upload --convert`.
2. Grants edit access to the user's email.
3. Responds: "The manuscript has been converted to Google Docs. You can access and edit it here: https://docs.google.com/document/d/[FILE_ID]/edit"
