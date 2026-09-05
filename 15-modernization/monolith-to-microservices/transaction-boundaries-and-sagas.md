# Distributed Transactions: Saga Orchestration vs. Choreography

## 1. Why 2PC / XA Fails in Microservices
Two-Phase Commit (2PC) coordinates atomic distributed transactions across network nodes. However, 2PC is an anti-pattern in cloud microservices:
- **Lock Amplification**: Resource locks are held across network round-trips; a single slow service blocks all participating databases.
- **Availability Fragility**: If the transaction coordinator or any participant crashes during the commit phase, locks remain held indefinitely.

---

## 2. The Saga Pattern
A Saga is a sequence of independent local transactions. Each local transaction updates the database and publishes an event. If a step fails, the Saga executes **compensating transactions** to reverse preceding mutations.

```
Orchestrated Saga: E-Commerce Checkout
[Saga Orchestrator]
       │
       ├─ Step 1: Create Order ──────────────► [Orders Service] (Status: PENDING)
       ├─ Step 2: Reserve Inventory ─────────► [Inventory Service] (Stock Decremented)
       ├─ Step 3: Authorize Card ────────────► [Payments Service] (FAILED: Insufficient Funds)
       │
       ▼ [EXECUTE COMPENSATION]
       ├─ Compensate 2: Unreserve Inventory ─► [Inventory Service] (Stock Restored)
       └─ Compensate 1: Cancel Order ────────► [Orders Service] (Status: REJECTED)
```
