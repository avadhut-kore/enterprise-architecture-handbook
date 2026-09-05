# Cross-Origin Resource Sharing (CORS) Architecture

## Executive Summary

CORS is a browser relaxation mechanism that allows servers to declare which foreign origins are permitted to read their HTTP responses.

---

## 1. Fatal CORS Anti-Patterns
- **The Wildcard Reflector**: Echoing the `Origin` header directly into `Access-Control-Allow-Origin` with `Access-Control-Allow-Credentials: true`. This completely destroys the Same-Origin Policy, allowing any malicious site to make credentialed requests to your API!
- **Overly Broad Wildcards**: `Access-Control-Allow-Origin: *` on authenticated endpoints.

---

## 2. Enterprise CORS Governance Standard
1. **Explicit Whitelist**: Match `Origin` strictly against a hardcoded list of verified corporate subdomains.
2. **Preflight Caching**: Configure `Access-Control-Max-Age: 86400` to cache `OPTIONS` preflight checks for 24 hours, eliminating latency overhead.
