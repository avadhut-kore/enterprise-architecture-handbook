# API Versioning & Deprecation Policy

## 1. Versioning Strategy
* **URI Path Versioning**: Major versions appear in the URI: `/v1/`, `/v2/`.
* **Minor / Patch Changes**: Non-breaking changes (adding optional fields) are published without bumping major versions.

## 2. Deprecation Governance
* Formal deprecation notice requires a minimum 6-month notice period before decommissioning.
* Deprecated APIs MUST include standard HTTP response headers:
  - `Deprecation: @1759276800` (Unix timestamp)
  - `Sunset: Sat, 01 Jan 2028 00:00:00 GMT`
  - `Link: <https://api.enterprise.com/docs/v2-migration>; rel="successor-version"`
