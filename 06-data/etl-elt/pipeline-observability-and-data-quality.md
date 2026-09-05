# ETL/ELT: Pipeline Observability & Data Quality Gates

## 1. Architectural Purpose & Problem Context
Monitoring SLA delivery times, data freshness metrics, volume anomaly detection, and automated circuit breaking on schema drift.

---

## 2. ELT Pipeline Flow

```mermaid
flowchart LR
    Extract[Extract Source Data] --> Load[Load Raw to Lakehouse]
    Load --> Transform[Transform in-place using dbt / SQL]
    Transform --> Test{"Automated Quality Assertions"}
    Test -->|Pass| Serve[Publish to Analytical Consumers]
    Test -->|Fail| Quarantine[Quarantine Partition & Alert]
```

---

## 3. Production Invariants
- Pipeline jobs must be strictly idempotent; re-running a job for date partition `T` must produce identical state without duplicate rows.
- Always execute data quality assertions before publishing data to production downstream consumers.
