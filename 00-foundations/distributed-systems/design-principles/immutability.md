# Distributed Design Principle: Immutability

## 1. Core Principle Definition

Immutability states that once an entity, record, or event is created, it can **never be modified or deleted in-place**.

State transformations are modeled strictly as new append-only events or new versions of an entity, creating a complete, tamper-proof historical log of every transition the system has ever undergone.

---

## 2. In-Place Mutation vs Append-Only Immutability

```
In-Place Mutation (Destructive):
UPDATE accounts SET balance = 500 WHERE id = 123;
(Previous balance of 1000 is lost forever; audit trail destroyed)

Append-Only Immutability (Event Sourced):
INSERT INTO ledger (account_id, delta, type, timestamp) VALUES
  (123, +1000, 'INITIAL_DEPOSIT', '2026-01-01'),
  (123, -500,  'ATM_WITHDRAWAL',  '2026-01-05');
(Current balance is the mathematical fold of all historic events)
```

---

## 3. Distributed Advantages

- **Zero Lock Contention**: Append-only writes do not require row-level update locks or table-level locks.
- **Cache Invalidation Simplification**: Immutable objects can be cached aggressively at the edge and on client devices indefinitely using immutable cache headers (`Cache-Control: immutable, max-age=31536000`).
- **Verifiable Auditability**: Meets strict enterprise compliance standards (SOX, HIPAA, PCI-DSS) by guaranteeing that historic records cannot be silently rewritten.
