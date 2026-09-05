# Financial Reference Architecture: Payment Gateway Integration Reference Architecture

## 1. Architectural Vision & Context
Resilient PSP integration adapter: webhook signature validation, webhook retry queues, authorization hold management, and timeout reversal automation.

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
