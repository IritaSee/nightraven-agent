---
name: sakumedis-admin-access
description: Information and procedures for accessing the SakuMedis production admin panel.
---

# SakuMedis Admin Access (Production)

This skill documents the access procedures and technical environment for the SakuMedis production admin panel.

## Access Details

- **Production URL:** [https://admin.sakumedis.id](https://admin.sakumedis.id)
- **Security Layer:** Restricted by **Cloudflare Zero Trust**. Access is granted only to authorized internal team members.
- **Automatic Redirects:** Any attempts to access via `*.pages.dev` hostnames will be automatically redirected to the custom domain `admin.sakumedis.id`.

## Authentication & Authorization

- **Login Methods:**
  - Google Login (pukulenam.id or authorized emails)
  - Email and Password
- **Authorized Roles:**
  - `admin`
  - `super_admin`
  - `plat_admin`

## Troubleshooting

- If access is denied, ensure you are logged into the Cloudflare Zero Trust gateway with an authorized internal email.
- Verify that your user role in the database is set to one of the authorized roles mentioned above.
