# ADR-0064: Zero Trust Network Architecture with Service-to-Service Mutual TLS

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Internal network sniffing and lateral movement in flat networks enable an adversary who breaches a single pod to compromise all internal microservices.

---

## Decision Outcome
**Chosen Option**: Enforce Mutual TLS (mTLS) with SPIFFE/SPIRE X.509 certificates for 100% of internal east-west microservice traffic; eliminate implicit trust based on internal VPC IP addresses.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Cryptographic proof of workload identity on every RPC; complete encryption in transit; small CPU overhead mitigated by Envoy crypto acceleration.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
