# Data Mapping: Aggregation, Splitting & Normalization Patterns

## 1. Architectural Purpose & Problem Context
Combining multiple source records into a single target composite (1:N to 1:1) and decomposing single compound payloads into multiple normalized entities.

Data mapping is a mission-critical architectural layer. Ad-hoc, hardcoded field conversions in application code lead to silent data corruption, unmaintainable coupling, and disastrous integration regressions.

---

## 2. Structural Mapping Topology & Flow

```mermaid
flowchart LR
    SourceData[Source Format / Payload] --> Parser[Syntax Parser & Validator]
    Parser --> MappingRule[Mapping Specification Rules]
    MappingRule --> CodeTable[(Code Translation & Lookup)]
    CodeTable --> MappingRule
    MappingRule --> Formatter[Target Formatter & Invariant Check]
    Formatter --> TargetData[Target Domain Entity / Payload]
```

---

## 3. Production Invariants & Governance Rules
- Every data mapping must be documented via a formal [Data Mapping Specification](../../16-architecture-deliverables/DATA-MAPPING-TEMPLATE.md).
- Mapping logic must be strictly versioned and subject to automated regression unit tests.
- Code translations must provide explicit exception paths for unrecognized codes rather than failing silently.
- Financial mappings must enforce exact decimal precision and banker's rounding rules.
