# Settlement Architecture: Clearing vs Settlement vs Reconciliation vs Accounting

## 1. Architectural Purpose & Problem Context
Disambiguating core enterprise financial phases: exchanging payment terms (Clearing), transferring funds (Settlement), verifying agreement (Recon), ledgering (Accounting).

---

## 2. Settlement Lifecycle Flow

```mermaid
sequenceDiagram
    autonumber
    participant Merchant as Merchant Platform
    participant Processor as Payment Processor / PSP
    participant CardNetwork as Card Scheme / Clearing Network
    participant Bank as Settlement Bank (Acquirer)

    Merchant->>Processor: End-of-Day Settlement Batch Close
    Processor->>CardNetwork: Submit Clearing Batch
    CardNetwork->>Bank: Settlement Instructions (Net Debit/Credit)
    Bank->>Merchant: Fund Transfer (ACH / Wire / RTGS)
    Bank-->>Merchant: Camt.053 / MT940 Settlement Confirmation File
```

---

## 3. Production Invariants
- Always separate clearing (obligation exchange) from settlement (actual money movement).
- Batch files must include strict cryptographic hash verification and batch total amount control sums.
- Settlement failure recovery must maintain clear operational exception queues with automated alerts.
