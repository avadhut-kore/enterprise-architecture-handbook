# Third-Party Script Governance & Subresource Integrity (SRI)

## Executive Summary

Embedding third-party analytics, chat widgets, or tracking tags directly in production HTML grants external vendors full JavaScript execution rights within your application context (the "Magecart" attack vector).

---

## Architectural Controls
1. **Subresource Integrity (SRI)**:
   ```html
   <script src="https://cdn.vendor.com/sdk.js"
           integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
           crossorigin="anonymous"></script>
   ```
   If the vendor's CDN is compromised and the script is altered, the browser detects the hash mismatch and refuses to execute the script.
2. **Sandboxed Iframes**: Render untrusted third-party widgets inside `<iframe sandbox="allow-scripts">` to isolate them from the parent application DOM and cookies.
