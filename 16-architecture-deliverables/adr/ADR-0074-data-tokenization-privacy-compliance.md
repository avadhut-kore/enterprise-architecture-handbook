# ADR-0074: Data Tokenization Proxy for PCI-DSS and Privacy Compliance

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Storing raw cardholder data (PAN) in core application databases places the entire enterprise infrastructure under high-cost PCI-DSS scope.

---

## Decision Outcome
**Chosen Option**: Implement format-preserving tokenization proxy at ingress to tokenize credit cards and government IDs before reaching application databases.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Cardholder Data Environment (CDE) scope reduced by 90%; reduced regulatory breach liability; minor latency overhead of token lookup.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
