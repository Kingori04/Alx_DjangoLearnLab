# Django Security Implementation

## ✅ Configured Secure Settings
- `DEBUG = False` in production.
- `CSRF_COOKIE_SECURE = True` & `SESSION_COOKIE_SECURE = True` (Cookies over HTTPS only).
- `SECURE_BROWSER_XSS_FILTER = True` (Prevents cross-site scripting).
- `SECURE_HSTS_SECONDS = 31536000` (Enforces HTTPS for 1 year).
- **CSP** (Restricts loading of external scripts to prevent XSS).

## ✅ Protected Views
- **CSRF Tokens** used in forms (`{% csrf_token %}`).
- **SQL Injection Prevented** via Django ORM (`Book.objects.filter(Q(...))`).
- **XSS Protection** by sanitizing user inputs (`escape()` in `views.py`).

## ✅ Security Tests Performed
1. **XSS Attack Simulation**
   - Tested inserting `<script>alert("XSS")</script>` into form fields.
   - JavaScript did **not** execute (input escaped properly).

2. **CSRF Attack Prevention**
   - Attempted to submit a form without a CSRF token.
   - **Django blocked the request** with a CSRF error.

3. **SQL Injection Attempt**
   - Tested input: `" OR 1=1 --` in search fields.
   - **Django ORM prevented database access.**

---
**Your Django app is now secured against major threats.** 🚀
