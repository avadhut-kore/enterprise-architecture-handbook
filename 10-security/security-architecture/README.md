# Core Security Architecture Principles & Foundations

## Overview

The `security-architecture/` directory establishes the architectural tenets, mental models, and structural disciplines required to engineer trustworthy, resilient, and verifiable enterprise systems.

---

## Architectural Guides in this Directory

| Guide | Focus Area | Architectural Impact |
| :--- | :--- | :--- |
| [`defense-in-depth.md`](defense-in-depth.md) | Multi-Layered Security | Layered controls across network, host, identity, application, and data |
| [`least-privilege.md`](least-privilege.md) | Privilege Minimization | Scoped entitlements, zero standing access, JIT workflows |
| [`secure-by-design.md`](secure-by-design.md) | Architectural Security | Threat modeling, secure primitives, and non-bypassable invariants |
| [`secure-by-default.md`](secure-by-default.md) | Default Hardening | Zero open ports, deny-all network policies, mandatory encryption |
| [`fail-securely.md`](fail-securely.md) | Failure Modes | Fail-closed vs fail-open trade-offs during component degradation |
| [`assume-breach.md`](assume-breach.md) | Zero Trust Mindset | Lateral movement prevention, internal hostility, mutual verification |
| [`minimize-blast-radius.md`](minimize-blast-radius.md) | Failure Containment | Account partitioning, cell-based isolation, database tenancy |
| [`separation-of-duties.md`](separation-of-duties.md) | Dual Control | Four-eyes principle, segregation of duties in CI/CD and operations |
| [`identity-vs-data-centric.md`](identity-vs-data-centric.md) | Security Paradigms | Identity-as-perimeter vs cryptographic data-centric protection |
| [`risk-based-security.md`](risk-based-security.md) | Risk Economics | Quantifying risk vs cost, prioritizing controls via ALE formulas |
