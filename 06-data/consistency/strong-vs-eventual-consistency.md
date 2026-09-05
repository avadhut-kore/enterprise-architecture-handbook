# Data Consistency: Strong vs Eventual Consistency: Architectural Trade-offs

## 1. Architectural Purpose & Problem Context
Balancing user experience, availability, latency, and operational complexity; when eventual consistency is acceptable vs dangerous.

---

## 2. Consistency Continuum Spectrum

```mermaid
flowchart LR
    Strict["Strict Linearizability (ACID)"] --> Sequential["Sequential Consistency"]
    Sequential --> Causal["Causal Consistency"]
    Causal --> RYW["Read-Your-Writes"]
    RYW --> Eventual["Eventual Consistency (BASE)"]
```

---

## 3. Production Invariants
- Financial ledgers, monetary balances, and inventory reservations require strong consistency within their aggregate boundary.
- Do not use Last-Write-Wins (LWW) for critical business data; clock drift will cause silent data loss.
- Always communicate eventual consistency states clearly to user interfaces via optimistic updates and progress indicators.
