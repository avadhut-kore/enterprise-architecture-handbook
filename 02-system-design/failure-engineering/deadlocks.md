# Distributed Deadlocks

## 1. Problem Definition

A distributed deadlock occurs when two or more transactions or services hold locks on separate resources across different nodes and are mutually blocked waiting to acquire locks held by each other, resulting in permanent standstill.

```
Transaction 1: Holds Lock(Record A) ───► Waiting for Lock(Record B)
                        ▲                         │
                        │                         ▼
Transaction 2: Waiting for Lock(Record A) ◄─── Holds Lock(Record B)
```

---

## 2. Deadlock Conditions (Coffman Conditions)

All 4 conditions must hold simultaneously for a deadlock to exist:
1. **Mutual Exclusion**: Resources cannot be shared.
2. **Hold and Wait**: Process holds one resource while requesting another.
3. **No Preemption**: Resources cannot be forcibly revoked.
4. **Circular Wait**: Closed chain of processes waiting on each other.

---

## 3. Architectural Prevention & Detection

### A. Strict Global Lock Ordering
Eliminate Circular Wait by enforcing a strict global sorting rule on all acquired resources:
- Any transaction needing multiple locks must acquire them in ascending lexicographical order of their resource IDs (`ID_A < ID_B < ID_C`).
- Circular wait is mathematically impossible under strict global ordering.

### B. Wait-Die vs Wound-Wait Schemes
Assign timestamps to transactions:
- **Wait-Die (Non-preemptive)**: Older transactions are allowed to wait; younger transactions die (abort and retry).
- **Wound-Wait (Preemptive)**: Older transactions "wound" (preempt and abort) younger transactions to take the lock immediately. Younger transactions wait for older ones.

### C. Lease Timeouts
Never acquire a distributed lock without an explicit Time-To-Live (TTL). If a node dies or blocks indefinitely, the lease expires and unblocks competing transactions.
