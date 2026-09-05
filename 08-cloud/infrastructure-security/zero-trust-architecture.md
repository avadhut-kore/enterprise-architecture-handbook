# Zero Trust Cloud Architecture

## Executive Summary

Zero Trust is a strategic architectural initiative based on the principle: **Assume Breach. Never Trust. Always Verify.** In modern cloud infrastructure, every request is dynamically authenticated, authorized, and encrypted.

---

## 1. The Zero Trust Decision Engine

```mermaid
graph TD
    Request[Incoming Request: User or Service] --> Engine[Policy Decision Point (PDP)]
    Engine --> Check1{Valid Cryptographic Identity? (mTLS / OIDC)}
    Engine --> Check2{Device / Host Health Compliant?}
    Engine --> Check3{Contextual Risk Acceptable? (Geo / Anomaly)}
    Engine --> Check4{Least Privilege Role Authorized?}

    Check1 & Check2 & Check3 & Check4 -->|All Passed| Allow[Grant Ephemeral Access]
    Check1 & Check2 & Check3 & Check4 -.->|Any Failed| Deny[ACCESS DENIED & Logged]
```

---

## 2. Eliminating Legacy Corporate VPNs (BeyondCorp Model)

- **The Problem with Corporate VPNs**: Once an employee or compromised device connects to a traditional corporate VPN, they receive flat Layer 3 access to the entire private internal subnet.
- **Identity-Aware Proxies (IAP)**: Deprecate corporate VPNs for internal application access. Deploy **Identity-Aware Proxies** (Google Cloud IAP, AWS Verified Access, Cloudflare Access). Users authenticate against corporate Entra ID with mandatory MFA; the proxy terminates the request and forwards traffic exclusively to the specific application authorized for that user role.
