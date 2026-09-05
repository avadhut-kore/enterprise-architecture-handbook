# 5-Whys Root Cause Analysis (RCA) Forensic Framework

## 1. Methodology & Philosophy
The 5-Whys interrogation is not a mechanical checklist; it is an architectural excavation tool. The objective is to push past superficial human error ("the engineer committed a bad query") to uncover **systemic architectural deficiencies** ("why does our architecture permit an unindexed query to exhaust global database IOPS?").

```
[LEVEL 1: SYMPTOM]       "The mobile checkout page returned HTTP 504 Timeouts."
        │
        ▼
[LEVEL 2: COMPONENT]     "The payment microservice exhausted its database connection pool."
        │
        ▼
[LEVEL 3: MECHANISM]     "Queries on the orders table took 12 seconds due to missing index."
        │
        ▼
[LEVEL 4: ARCHITECTURE]  "We lacked an architectural connection proxy to insulate the DB."
        │
        ▼
[LEVEL 5: GOVERNANCE]    "CI/CD pipelines lacked automated query count and index verification gates."
```

---

## 2. 5-Whys Forensic Worksheet

**Incident Identifier**: `INC-XXXXX` | **Worksheet Facilitator**: `Lead Architect`

| Interrogation Depth | Question | Evidence & Telemetry Source | Architectural Finding |
| :--- | :--- | :--- | :--- |
| **Why 1 (Symptom)** | Why did customer transactions fail? | Datadog HTTP 5xx Error Rate Spike | User-facing endpoints timed out waiting for backend responses. |
| **Why 2 (Component)** | Why did backend services time out? | HikariCP Connection Pool Metrics | Worker threads were blocked waiting to acquire database connections. |
| **Why 3 (Mechanism)** | Why were database connections unavailable? | PostgreSQL `pg_stat_activity` log | Queries held connections for 15s instead of 20ms due to lock contention. |
| **Why 4 (Architecture)** | Why did lock contention paralyze the cluster? | System Topology Review | Multiple microservices shared a single database and lacked circuit breaking. |
| **Why 5 (Root Cause)** | Why was the system designed with shared locks? | Architecture Governance Audit | Architecture team took a shortcut to avoid implementing asynchronous Sagas. |

---

## 3. Validation Checklist
Before closing a 5-Whys analysis, verify that the terminal (Level 5) root cause satisfies:
- [ ] It identifies an architectural or governance defect, not human error or bad luck.
- [ ] Fixing this Level 5 defect will prevent the entire category of failure in the future.
- [ ] The chain of causality is mathematically unbroken from Level 1 down to Level 5.
