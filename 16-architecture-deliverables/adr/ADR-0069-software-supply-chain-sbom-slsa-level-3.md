# ADR-0069: Software Supply Chain Security: Mandatory CycloneDX SBOM and SLSA Level 3

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Supply chain attacks (tampered dependencies, compromised build runners) bypass traditional perimeter defenses and infect trusted enterprise distributions.

---

## Decision Outcome
**Chosen Option**: Mandate automated CycloneDX SBOM generation and cryptographic image signing (Cosign) adhering to SLSA Level 3 build provenance for all production artifacts.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Instantaneous vulnerability discovery across 10,000 repos during zero-day events (Log4j class); verified artifact integrity at cluster admission.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
