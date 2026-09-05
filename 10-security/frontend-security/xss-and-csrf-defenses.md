# XSS and CSRF Architectural Defenses

## Executive Summary

- **XSS Defense**: Strict CSP nonces, context-aware templating (React/Angular automatic JSX encoding), sanitizing markdown with DOMPurify.
- **CSRF Defense**: Setting session cookies with `SameSite=Strict; Secure; HttpOnly`. For cross-origin POST APIs, require custom headers (`X-Requested-With` or `Authorization: Bearer <token>`) which browsers block from simple HTML cross-site forms.
