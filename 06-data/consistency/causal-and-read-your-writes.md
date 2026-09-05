# Data Consistency: Causal Consistency & Read-Your-Writes Guarantees

## 1. Architectural Purpose & Problem Context
Preserving causal order without global synchronization locks; implementing sticky session routing and version-vector read-your-writes.

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
