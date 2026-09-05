# Frontend Web Security Architecture (`frontend-security/`)

## Executive Summary

Frontend web security focuses on protecting web applications executing inside untrusted client web browsers against Cross-Site Scripting (XSS), Cross-Site Request Forgery (CSRF), clickjacking, and malicious third-party script supply chains.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`browser-security-model.md`](browser-security-model.md) | Browser Sandbox | Same-Origin Policy (SOP), DOM isolation |
| [`content-security-policy-csp.md`](content-security-policy-csp.md) | CSP Architecture | Strict CSP, nonces, SHA-256 hashes, banning inline scripts |
| [`cors-architecture-and-governance.md`](cors-architecture-and-governance.md) | CORS Governance | Cross-Origin Resource Sharing, preflight caching, origin whitelisting |
| [`xss-and-csrf-defenses.md`](xss-and-csrf-defenses.md) | Attack Mitigations | Contextual encoding, SameSite=Strict cookies, anti-CSRF tokens |
| [`third-party-script-governance.md`](third-party-script-governance.md) | Supply Chain at Edge | Subresource Integrity (SRI), sandbox iframes, script proxying |
