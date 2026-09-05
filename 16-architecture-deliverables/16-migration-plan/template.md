# Migration Plan: [MIGRATION INITIATIVE NAME]

---
**Metadata**:
```yaml
migration_id: "MIG-PLAN-[PROJECT-ID]"
title: "Enterprise Migration Plan — [Initiative Name]"
version: "1.0.0"
status: "Draft" # Draft | In Review | Approved | Executed
migration_lead: "[Migration Architect / Lead Engineer Name <email>]"
target_cutover_date: "YYYY-MM-DD"
maintenance_window: "2 Hours (Sunday 02:00 - 04:00 UTC)"
created_date: "YYYY-MM-DD"
```
---

## 1. Executive Summary & Migration Scope
* Purpose of migration (e.g., On-Premises Oracle to AWS Aurora PostgreSQL).
* Success criteria: Zero data loss (RPO=0), cutover completed within maintenance window.

## 2. As-Is vs To-Be Architecture Comparison
* **Current State**: On-premises monolithic Oracle database with direct client connections.
* **Target State**: AWS Aurora PostgreSQL multi-AZ cluster behind pgBouncer connection pool.

## 3. Coexistence & Transition Architecture
Reference transition diagrams from [[17-diagrams/04-integration-diagrams/README.md](../../17-diagrams/integration/README.md)].
* Debezium Change Data Capture (CDC) streaming continuous updates from Oracle to Kafka to Aurora.

## 4. Hour-by-Hour Cutover Runbook
| T-Minus / T-Plus | Action Item | Responsible Owner | Verification Check | Rollback Trigger |
|---|---|---|---|---|
| **T - 60 min** | Freeze administrative jobs and batch ETL | Lead DBA | Check zero active batch queries | Abort if jobs active |
| **T - 15 min** | Switch application to read-only maintenance mode | SRE Lead | HTTP 503 maintenance page visible | N/A |
| **T - 00 min** | Final CDC lag catchup (wait for 0 lag) | Data Architect | Kafka lag == 0 across all partitions | Abort if lag > 0 after 15m |
| **T + 15 min** | Switch DNS / Envoy gateway to point to Aurora | Platform Lead | Traffic arrives at target cluster | Roll back DNS if error rate > 1% |
| **T + 30 min** | Execute post-migration smoke test suite | QA Lead | 100% test pass rate on 45 smoke tests | Roll back if critical tests fail |
| **T + 45 min** | Re-enable read/write traffic to users | Release Manager | Live transactions succeeding in production | N/A |

## 5. Rollback Runbook & Contingency Plan
* Explicit decision gate: At **T + 35 min**, the Go/No-Go call is made.
* If rolled back: DNS instantly repointed to Oracle; reverse-CDC replays any transactions captured on Aurora.
