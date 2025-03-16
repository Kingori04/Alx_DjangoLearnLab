# Django Role-Based Access Control

## 🔹 Features
- Users are assigned to groups: **Editors, Viewers, and Admins**.
- **Permissions:**
  - `can_view`: Can view articles.
  - `can_create`: Can create articles.
  - `can_edit`: Can edit articles.
  - `can_delete`: Can delete articles.

## 🔹 How to Use
1. **Create Users & Assign to Groups:**
   - Go to `/admin`.
   - Create users and assign them to **Editors, Viewers, or Admins**.
2. **Test Permissions:**
   - Log in with different users and try to **view, create, edit, or delete** articles.
   - Unauthorized users will get a **403 Forbidden** error.
