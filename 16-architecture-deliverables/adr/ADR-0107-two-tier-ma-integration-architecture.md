# ADR-0107: Two-Tier M&A Technology Integration Architecture

* **Status**: Approved
* **Date**: 2026-09-05
* **Deciders**: Chief Architect, Enterprise Architecture Office, Architecture Review Board (ARB)
* **Consulted**: CISO, Head of Engineering, Product VPs, Legal & Compliance
* **Informed**: Global Engineering Community

---

## 1. Context & Problem Statement
Forced immediate absorption of acquired fintech startups destroyed their agility and talent retention.

Adopt a two-tier integration strategy for fast-moving technology acquisitions.

---

## 2. Decision Drivers
* Align capital expenditures with corporate strategic priorities.
* Enforce security, regulatory compliance, and operational resilience by design.
* Minimize 5-year Total Cost of Ownership (TCO) and eliminate capability redundancy.
* Provide clear, predictable paved roads for software engineering teams.

---

## 3. Considered Options
* **Option 1: Status Quo / Tactical Autonomy** (Rejected: leads to unmanaged sprawl, high risk, and ballooning TCO).
* **Option 2: Rigid Centralized Mandate** (Rejected: slows local velocity and causes shadow IT).
* **Option 3: Governed Paved Road Standard (Approved)** (Balances enterprise guardrails with delivery team speed).

---

## 4. Decision Outcome
**Acquired company retains modern cloud stack; integrates with parent company via API façades and financial ledgers.**

### Positive Consequences
* Clear enterprise-wide alignment and accountability.
* Measurable reduction in operational defects, security vulnerabilities, and infrastructure costs.
* Rapid onboarding of engineers via standardized paved roads.

### Negative Consequences / Trade-offs
* Requires initial governance overhead and transition investment.
* Edge-case workloads must submit formal architecture exception waivers.

---

## 5. Compliance & Verification
* Automated architectural fitness functions running in CI/CD pipelines verify conformance.
* Non-compliant projects are flagged during quarterly ARB portfolio audits.
