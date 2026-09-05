# Integration Pattern: Retry & Dead Letter Channel Patterns

## 1. Pattern Purpose & Context
Automated retry policies with backoff, isolating unprocessable poison messages into a Dead Letter Channel (DLC) for manual triage.

---

## 2. Structural Pattern Topology

```mermaid
flowchart LR
    InChannel[Incoming Message Channel] --> PatternComponent[Enterprise Integration Component]
    PatternComponent --> OutChannel[Outgoing Destination Channel]
```

---

## 3. Production Invariants & Evaluation
- Prefer simple standard messaging constructs before introducing complex multi-step routing graphs.
- Protect enricher components with local caching to prevent saturating external reference databases.
- Ensure all split messages retain an immutable correlation ID to enable deterministic downstream aggregation.
