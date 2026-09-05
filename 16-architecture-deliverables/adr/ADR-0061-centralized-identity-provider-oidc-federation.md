# ADR-0061: Centralized Identity Provider with OpenID Connect Federation

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Fragmented identity stores across hundreds of microservices created massive security debt, prevented centralized MFA enforcement, and made instantaneous employee deprovisioning impossible.

---

## Decision Outcome
**Chosen Option**: Establish Microsoft Entra ID / Okta as the enterprise Single Source of Truth IdP, deprecating local application user tables and mandating OIDC federation for all applications.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Centralized audit trails, instant account deactivation via SCIM, unified passkey MFA; dependency on central IdP availability mitigated by distributed token validation.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
