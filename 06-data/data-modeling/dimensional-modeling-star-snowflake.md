# Data Modeling: Dimensional Modeling: Star & Snowflake Schemas

## 1. Architectural Purpose & Problem Context
Designing analytical data marts: Fact tables (additive, semi-additive), Dimension tables, Conformed dimensions, and Slowly Changing Dimensions (SCD Types 1, 2, 3, 6).

Data models dictate the latency, throughput, consistency boundaries, and evolution agility of enterprise platforms. Flawed data modeling cannot be repaired by scaling hardware.

---

## 2. Structural Model & Conceptual Blueprint

```mermaid
classDiagram
    class BusinessAggregate {
        +UUID AggregateId
        +String BusinessKey
        +DateTime CreatedAt
        +ApplyEvent()
        +ValidateInvariants()
    }
    class ReadProjection {
        +UUID Id
        +String SummaryView
        +JSON Payload
    }
    BusinessAggregate --> ReadProjection : "Asynchronous Projection / CDC"
```

---

## 3. Production Invariants & Modeling Guidelines
- Model according to access patterns and business invariants, not arbitrary technical preferences.
- Keep transaction boundaries aligned with aggregate boundaries.
- Never allow unbounded nested collections in document databases.
- Ensure all historical updates maintain an unambiguous temporal audit trail.
