# Token Storage in Web Clients (Cookies vs LocalStorage vs Memory)

## Executive Summary

Storing tokens in frontend clients introduces a direct trade-off between **Cross-Site Scripting (XSS)** and **Cross-Site Request Forgery (CSRF)** vulnerabilities.

---

## Storage Strategy Comparison

| Storage Mechanism | XSS Vulnerability | CSRF Vulnerability | Refresh Mechanism | Architectural Recommendation |
| :--- | :---: | :---: | :--- | :--- |
| **`localStorage` / `sessionStorage`** | **CRITICAL**: Any XSS payload can immediately steal the token. | Immune (Header-based) | Manual JavaScript timer | **Strictly Prohibited** for enterprise tokens containing sensitive claims. |
| **JavaScript In-Memory (Closure)** | High: XSS can steal in-memory variables. | Immune | Lost on page refresh; requires iframe/worker | Acceptable for transient access tokens paired with secure cookie refresh. |
| **`HttpOnly`, `Secure`, `SameSite=Strict` Cookie** | **IMMUNE**: JavaScript cannot read `HttpOnly` cookies. | **Protected**: `SameSite=Strict` + Anti-CSRF token stops CSRF. | Automatic browser transmission | **Enterprise Standard** for browser-based web applications. |
