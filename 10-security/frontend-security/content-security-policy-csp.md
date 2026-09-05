# Strict Content Security Policy (CSP) Architecture

## Executive Summary

Content Security Policy (CSP Level 3) is the primary browser-side defense against Cross-Site Scripting (XSS) and data exfiltration.

---

## 1. Enterprise Strict CSP Header Standard

```http
Content-Security-Policy: 
    default-src 'none';
    script-src 'strict-dynamic' 'nonce-R4nd0mN0nc3' 'sha256-abc...';
    style-src 'self' 'nonce-R4nd0mN0nc3';
    img-src 'self' data: https://cdn.enterprise.com;
    connect-src 'self' https://api.enterprise.com;
    font-src 'self' https://fonts.gstatic.com;
    object-src 'none';
    base-uri 'none';
    form-action 'self';
    frame-ancestors 'none';
    upgrade-insecure-requests;
```

### Invariants:
- `object-src 'none'`: Completely disables legacy Flash/Java applets.
- `base-uri 'none'`: Prevents `<base>` tag injection attacks.
- `frame-ancestors 'none'`: Completely blocks clickjacking (replaces `X-Frame-Options: DENY`).
- `script-src 'strict-dynamic' 'nonce-...'`: Bans `'unsafe-inline'` and `'unsafe-eval'`.
