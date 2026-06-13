---
name: rbac-qa-verification
description: Systematic verification of role permissions and unauthorized URL access/redirection in web platforms.
---

# rbac-qa-verification

Systematically verifies Role-Based Access Control (RBAC) by testing permissions across different user roles and checking for over-privileged access or improper redirections.

## When to use
- During QA phases of web platform development (e.g., Timgravid).
- When verifying if a specific role (e.g., Admin Operasional) can access restricted endpoints (e.g., `/app/pengaturan`).
- When testing URL-level security and redirection logic.

## Steps

1.  **Map Roles and Permissions**: Create a matrix of roles (Admin, Approver, Pengawas) and their expected access levels.
2.  **Automated Login**: Use `timgravid-access` or similar scripts to authenticate as each role.
3.  **Endpoint Probing**: Attempt to access a list of restricted URLs directly.
4.  **Analyze Response**:
    - **200 OK**: Potential over-privilege if the role should not have access.
    - **302 Redirect**: Verify if it redirects to the correct fallback (e.g., Dashboard).
    - **403 Forbidden**: Correct behavior for restricted access.
5.  **Report Findings**: Document unauthorized access or logic flaws.

## Output Format
Deliver findings in a CSV-compatible summary table for spreadsheet integration.

| Role | Endpoint | Expected | Actual | Status |
| :--- | :--- | :--- | :--- | :--- |
| Admin Operasional | /app/pengaturan | 403/Redirect | 200 OK | **FAIL** |
| Approver | /app/keuangan | 200 OK | 200 OK | PASS |

## Example
Testing Timgravid "Admin Operasional" role:
- Direct access to `/app/pengaturan` returned `200 OK` instead of redirecting to Dashboard.
- Result: Over-privileged access identified.
