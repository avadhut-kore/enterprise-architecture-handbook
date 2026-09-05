# MDM Architecture: Deduplication & Survivorship Rules Architecture

## 1. Architectural Purpose & Problem Context
Establishing golden attribute values: Most Recent, Source System Trust Ranking, Highest Quality Completeness, and manual steward overrides.

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
