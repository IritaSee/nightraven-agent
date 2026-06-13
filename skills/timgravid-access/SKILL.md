---
name: timgravid-access
description: Automated multi-role login and data extraction for the Timgravid platform using CSRF and session management.
---

# timgravid-access

Automate interactions with the Timgravid platform (`https://timgravid.baysatriow.com`) using Python scripts that handle CSRF tokens and session persistence.

## When to use
- When you need to log in to the Timgravid platform with specific roles (Super Admin, Admin Operasional, Approver, Pengawas).
- When you need to extract data or perform actions that require an authenticated session.

## Steps
1. **Identify Role**: Determine which role is required for the task.
2. **Use Client Script**: Utilize `timgravid_client.py` (located in the project directory) to initiate the session.
3. **CSRF Handling**: Ensure the script fetches the login page first to extract the CSRF token from the HTML using `BeautifulSoup`.
4. **Authentication**: Post credentials along with the CSRF token to the login endpoint.
5. **Data Extraction**: Use the authenticated session object to make subsequent GET/POST requests to the platform's internal endpoints.

## Output Format
- Data extracted should be presented in a structured format (JSON, CSV, or Markdown table).
- Confirmation of successful login or action.

## Example
```python
from timgravid_client import TimgravidClient

client = TimgravidClient(role='super_admin')
if client.login():
    data = client.get_dashboard_stats()
    print(data)
```
