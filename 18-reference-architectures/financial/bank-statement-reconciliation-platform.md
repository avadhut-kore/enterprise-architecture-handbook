# Financial Reference Architecture: Bank Statement Reconciliation Platform Architecture

## 1. Architectural Vision & Context
Ingesting banking statement files (ISO 20022 camt.053, MT940, BAI2), parsing bank reference keys, matching against treasury ledgers, and posting cash adjustments.

---

## 2. Financial Pipeline Blueprint

```mermaid
flowchart LR
    Order[Order Checkout System] --> PaymentEngine[Payment Processing Hub]
    PaymentEngine --> PSP[Payment Gateway / Acquirer]
    PSP --> Clearing[Card Network Clearing]
    Clearing --> SettleBank[Settlement Bank Payout]
    PaymentEngine --> Recon[Automated Reconciliation Hub]
    PSP -.->|Settlement Report| Recon
    SettleBank -.->|Bank Statement File| Recon
    Recon --> GL[General Ledger Sub-Ledger]
```

---

## 3. Core Architectural Invariants & Financial Controls
- Strict idempotency keys required on all financial transaction initiation endpoints.
- Monetary calculations must use integer minor units or arbitrary-precision decimals; never floating-point.
- Reconciliation exceptions must be routed to four-eyes authorization queues for manual investigation.
