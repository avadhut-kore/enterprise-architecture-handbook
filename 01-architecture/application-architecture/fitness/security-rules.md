# Automated Security Fitness Rules

## 1. Rules
- Assert that every public API endpoint has an explicit `[Authorize]` attribute unless marked `[AllowAnonymous]`.
- Enforce that plain-text passwords never appear in variable names.
