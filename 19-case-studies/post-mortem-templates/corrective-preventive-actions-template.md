# Corrective and Preventive Actions (CAPA) Tracking Matrix

## 1. Purpose
This matrix ensures that forensic findings from incident post-mortems are transformed into durable, verifiable engineering deliverables. Actions are divided into **Corrective Actions** (immediate containment to restore safety) and **Preventive Actions** (structural architectural changes to eliminate the failure category).

---

## 2. CAPA Deliverables Matrix

| CAPA ID | Type | Architectural Category | Remediation Task Description | Risk Addressed | Directly Responsible Individual (DRI) | Target Milestone | Verification Proof / Test Metric | Sign-off Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`CAPA-01`** | Corrective | Infrastructure Tuning | Increase Linux `nofile` socket descriptor limit to 1,048,576 | Socket exhaustion | Platform SRE Lead | Week 1 | `/proc/sys/fs/file-nr` inspection | `[APPROVED]` |
| **`CAPA-02`** | Corrective | Code Patch | Replace `@OneToMany(fetch=EAGER)` with explicit DTO projections | ORM N+1 query explosion | Lead Java Developer | Week 2 | QuickPerf CI query count test ($\le 3$) | `[PENDING]` |
| **`CAPA-03`** | Preventive | Security Architecture | Enforce PostgreSQL Row-Level Security (RLS) across all multi-tenant tables | Cross-tenant data leak | Lead Database Architect | Month 2 | Multi-tenant automated security test suite | `[PLANNED]` |
| **`CAPA-04`** | Preventive | Integration Resilience | Deploy Envoy Proxy egress circuit breakers with exponential jitter | Unbounded retry storm | Cloud Edge Architect | Month 3 | Chaos Mesh fault injection testing | `[PLANNED]` |
| **`CAPA-05`** | Preventive | Platform Governance | Implement mandatory automated architectural fitness functions in CI (ArchUnit) | Architecture erosion & boundary bypass | Enterprise Architect | Month 6 | Zero pull-request boundary violations | `[PLANNED]` |

---

## 3. Governance & Closure Policy
- **P0 / P1 Actions**: Must be completed within 14 calendar days; require Chief Architect sign-off.
- **Verification Gate**: No CAPA item may be marked "Closed" without documented proof from a simulated chaos test or automated CI validation script.
