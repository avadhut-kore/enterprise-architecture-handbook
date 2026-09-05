# API Architecture: API Versioning, Deprecation & Sunset Policies

## 1. Architectural Purpose & Problem Context
URI path vs header vs query param versioning; enforcing the `Sunset` and `Deprecation` HTTP headers and maintaining backward compatibility windows.

---

## 2. API Governance Lifecycle

```mermaid
flowchart LR
    Design[1. OpenAPI Spec Design] --> Review[2. Architecture Review Board]
    Review --> Mock[3. Mock Server & Client Tests]
    Mock --> Deploy[4. Production Deployment]
    Deploy --> Monitor[5. Observability & SLO Tracking]
    Monitor --> Deprecate[6. Sunset & Deprecation]
```

---

## 3. Production Invariants
- All public and internal inter-service APIs must maintain an up-to-date, machine-readable OpenAPI specification.
- Never introduce breaking changes (e.g., removing fields, changing types) in minor API releases; maintain a minimum 12-month deprecation window.
