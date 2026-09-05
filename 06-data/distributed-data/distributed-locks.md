# Distributed Locks & Fencing Tokens

## 1. The Perils of Distributed Locking (Kleppmann's Critique)
A distributed lock ensures mutually exclusive access across distinct network processes. However, relying purely on lock leases (e.g., Redis TTL) without **Fencing Tokens** leads to silent data corruption:

```mermaid
sequenceDiagram
    autonumber
    participant C1 as Client 1
    participant Lock as Redis Lock
    participant DB as Storage (File / DB)
    participant C2 as Client 2
    
    C1->>Lock: Acquire Lock (Lease 10s)
    Note over C1: Client 1 enters Full GC STW Pause for 15s!
    Note over Lock: Lock Lease Expires!
    C2->>Lock: Acquire Lock (Lease 10s)
    C2->>DB: Write Data (Token 101)
    Note over C1: Client 1 Wakes Up! Believes it STILL holds lock!
    C1->>DB: Overwrites Data! (Token 100 - Outdated!) -> DATA CORRUPTION!
```

---

## 2. Fencing Token Defense
1. The lock service returns a monotonically increasing **Fencing Token** on lock acquisition (e.g., Token 102).
2. The storage engine validates that every incoming write presents a token strictly higher than the last accepted write.
3. Client 1's write (Token 100) is rejected because Token 101 was already processed.
