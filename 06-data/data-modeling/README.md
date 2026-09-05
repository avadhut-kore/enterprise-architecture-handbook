# Enterprise Data Modeling

Data modeling is the foundational engineering practice of abstracting real-world enterprise domain concepts into formal structural representations that balance transactional integrity, query performance, and operational maintainability.

---

## Modeling Paradigms Across the Enterprise

```mermaid
flowchart TD
    Reqs[Business Requirements & Domain Discovery] --> Conceptual[1. Conceptual Data Model]
    Conceptual --> Logical[2. Logical Data Model: Entities, Invariants, Keys]
    Logical --> Paradigms{Target Workload Selection}
    Paradigms -->|OLTP / ACID| Relational[Relational Modeling: 3NF / BCNF]
    Paradigms -->|Hierarchical / Read-Heavy| Document[Document Modeling: Embedded vs Referenced]
    Paradigms -->|High Scale Point Lookups| KV[Key-Value Modeling: Partition Keys]
    Paradigms -->|Time-Series / Telemetry| TimeSeries[Time-Series Modeling: Buckets]
    Paradigms -->|Complex Graph Networks| Graph[Graph Modeling: Nodes & Edges]
    Paradigms -->|Analytical / BI| Dimensional[Dimensional Modeling: Star / Snowflake]
    Paradigms -->|Enterprise Audit Vault| DataVault[Data Vault 2.0: Hubs, Links, Satellites]
```

---

## Knowledge Index
- [Conceptual, Logical & Physical Modeling](conceptual-logical-physical.md)
- [Relational Modeling & Normalization](relational-modeling.md)
- [Document Database Modeling](document-modeling.md)
- [Key-Value Modeling & Partition Key Design](key-value-modeling.md)
- [Wide-Column Database Modeling](wide-column-modeling.md)
- [Graph Database Modeling](graph-modeling.md)
- [Time-Series Data Modeling](time-series-modeling.md)
- [Dimensional Modeling: Star & Snowflake Schemas](dimensional-modeling-star-snowflake.md)
- [Data Vault 2.0 Modeling](data-vault-modeling.md)
- [CQRS Read & Write Models](cqrs-read-write-models.md)
- [Event Modeling & Append-Only State](event-modeling.md)
- [Schema Evolution & Compatibility Strategies](schema-evolution-compatibility.md)
