# ADR-0075: Centralized SIEM Event Streaming with Real-Time Detection Engineering

## Status
**Accepted** - 2026-09-05

---

## Context & Problem Statement
Siloed log storage prevents cross-domain correlation, leaving multi-stage advanced persistent threats (APTs) undetected for months.

---

## Decision Outcome
**Chosen Option**: Stream all security audit logs, cloud activity, and authentication events into a centralized SIEM (Microsoft Sentinel / Splunk) using the OCSF standard.

---

## Architectural Rationale
1. **Security & Resilience**: Directly enforces defense-in-depth and least-privilege invariants.
2. **Operational Operability**: Eliminates manual toil and provides automated guardrails.
3. **Compliance & Audit**: Provides mathematical proof and verifiable audit trails for regulatory scrutiny.

---

## Positive & Negative Consequences
- Real-time threat detection; automated SOAR response playbooks; satisfies regulatory audit retention mandates across all jurisdictions.

---

## Compliance & Governance Mapping
- **NIST SP 800-53 / 800-207**: Mapped directly to enterprise security controls.
- **CIS Benchmarks**: Enforced programmatically via automated CI/CD and IaC linters.
