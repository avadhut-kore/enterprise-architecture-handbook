# API Management: Consumer Subscriptions, API Keys & OAuth Governance

## 1. Architectural Purpose & Problem Context
Managing client credentials, subscription approval workflows, automated key rotation, and OAuth2 client-credentials grants.

---

## 2. API Management Topology

```mermaid
flowchart TD
    Consumer[API Consumer / Partner] --> Gateway[API Gateway / Enforcement Plane]
    Gateway --> APIM[API Management Control Plane]
    APIM --> Analytics[(Analytics & Billing Engine)]
    APIM --> Portal[Developer Portal & Key Management]
    Gateway --> Backend[Internal Enterprise Microservices]
```

---

## 3. Production Invariants
- Never expose internal service APIs directly to external consumers without passing through API Management governance.
- Always communicate rate limit quotas via standard HTTP headers (`RateLimit-Limit`, `RateLimit-Remaining`, `RateLimit-Reset`).
