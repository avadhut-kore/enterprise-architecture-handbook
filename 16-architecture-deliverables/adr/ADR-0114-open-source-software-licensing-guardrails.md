# ADR-0114: Open Source Software (OSS) Licensing & Supply Chain Guardrails

* **Status**: Approved
* **Date**: 2026-09-05
* **Deciders**: Chief Architect, Enterprise Architecture Office, Architecture Review Board (ARB)
* **Consulted**: CISO, Head of Engineering, Product VPs, Legal & Compliance
* **Informed**: Global Engineering Community

---

## 1. Context & Problem Statement
Unmonitored developer dependencies risked mandatory open-sourcing of proprietary corporate intellectual property.

Prohibit viral copyleft licenses (GPL v3, AGPL) in proprietary commercial software; automate SBOM scanning.

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
**Automated CI/CD dependency linters block viral copyleft licenses and critical CVEs prior to merging code.**

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
