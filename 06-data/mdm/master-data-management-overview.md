# MDM Architecture: Master Data Management Overview & Topologies

## 1. Architectural Purpose & Problem Context
Evaluating Registry vs Consolidation vs Co-existence vs Transactional/Centralized MDM implementation models.

---

## 2. MDM Golden Record Pipeline

```mermaid
flowchart LR
    CRM[CRM Customer Record] --> Ingest[MDM Ingestion & Cleanse]
    ERP[ERP Customer Record] --> Ingest
    Billing[Billing System Record] --> Ingest
    Ingest --> Match[Deterministic & Probabilistic Matching]
    Match --> Survive[Survivorship Engine]
    Survive --> Golden[(Master Golden Record)]
    Golden -->|Syndicate Updates| Downstream[Enterprise Applications]
```

---

## 3. Production Invariants
- Survivorship rules must be deterministic, transparent, and fully auditable.
- Unmatched records within the borderline confidence interval must be routed to human data stewards rather than automatically merged.
