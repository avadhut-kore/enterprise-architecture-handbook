# Financial Transactions: Idempotency Keys & Duplicate Prevention Architecture

## 1. Architectural Purpose & Problem Context
Cryptographic / UUID idempotency keys, atomic database reservations, caching response payloads, and handling race conditions on concurrent retries.

---

## 2. End-to-End Transaction Lifecycle Flow

```mermaid
flowchart LR
    Init[1. Initiation & Auth] --> Cap[2. Capture & Hold]
    Cap --> Clear[3. Clearing Batch]
    Clear --> Settle[4. Settlement Payout]
    Settle --> Recon[5. Automated Reconciliation]
    Recon --> GL[6. General Ledger Post]
```

---

## 3. Production Invariants
- All monetary math must use integer minor units or arbitrary-precision decimals; never use floating-point types (`float`, `double`).
- All state-mutating financial endpoints must require a unique client-generated idempotency key.
- Financial transaction records must be strictly append-only; update mutations on historical balances are prohibited.
