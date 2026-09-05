# ADR-0066: Envelope Encryption Standard with KMS Customer-Managed Keys (CMK)

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Encrypting large datasets directly via KMS API hits rate limits and creates latency bottlenecks; default cloud-managed keys do not provide client-controlled revocation.

---

## Decision Outcome
**Chosen Option**: Mandate AES-256-GCM envelope encryption with KMS Customer Managed Keys (CMKs) and automated 365-day rotation for all data stores, databases, and backups.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Local sub-millisecond encryption performance; mathematical cryptographic shredding capability; customer retains root key custody.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
