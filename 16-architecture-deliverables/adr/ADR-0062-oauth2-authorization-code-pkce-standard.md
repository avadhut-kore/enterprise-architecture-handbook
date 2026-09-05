# ADR-0062: Mandatory OAuth 2.0 Authorization Code with PKCE for Client Applications

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Legacy implicit flows expose access tokens in browser history and URL fragments, while ROPC encourages credential handling by client code.

---

## Decision Outcome
**Chosen Option**: Mandate OAuth 2.0 Authorization Code flow with PKCE (RFC 7636) for all client applications; formally ban the OAuth 2.0 Implicit Grant and Resource Owner Password Credentials (ROPC) grant.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Immunity to authorization code interception; eliminated client credential handling; minor engineering overhead to generate cryptographic code verifiers.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
