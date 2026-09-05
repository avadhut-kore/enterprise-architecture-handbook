# Banking Integration Architecture

## 1. Overview & Business Domain
Core Banking platforms are the central engines of financial institutions, managing customer accounts, deposit balances, general ledgers, credit facilities, and interest calculations.

Integrating a modern digital banking channel with a core banking platform requires bridging real-time omnichannel customer expectations with legacy transaction engines, high regulatory compliance, and strict accounting invariants.

```text
Channels (Mobile, Web, ATM, Branch)
   ↓
API Gateway (OIDC, mTLS, Rate Limiting)
   ↓
Integration / Orchestration Layer (Saga, Outbox)
   ↓
Core Banking Engine (BIAN Service Domains)
   ↓
General Ledger / Account Balances (ACID Invariants)
   ↓
Payments Clearing (FedNow, SEPA, SWIFT)
   ↓
Real-Time Fraud & Anti-Money Laundering (AML)
   ↓
Analytical Lakehouse & Regulatory Reporting
```

---

## 2. Directory Contents
* **[core-banking-architecture.md](core-banking-architecture.md)** — Architectural styles: Mainframe monolithic vs Componentized vs Modern Cloud-Native.
* **[core-banking-integration.md](core-banking-integration.md)** — Synchronous RPC vs Asynchronous posting patterns.
* **[account-services.md](account-services.md)** — Account balance inquiries, holds, reservations, and shadow balances.
* **[customer-services.md](customer-services.md)** — Customer 360, Master Person Index, and KYC identity verification.
* **[transaction-processing.md](transaction-processing.md)** — ACID transactional posting, memo posting, and final settlement.
* **[ledger-integration.md](ledger-integration.md)** — Double-entry accounting principles and General Ledger (GL) synchronization.
* **[payment-integration.md](payment-integration.md)** — Connecting channels to FedNow, SEPA Instant, and SWIFT networks.
* **[batch-processing.md](batch-processing.md)** — End-of-Day (EOD) batch windows, accrual runs, and statement generation.
* **[real-time-integration.md](real-time-integration.md)** — Sub-second balance checks and card authorization hold routing.
* **[event-driven-banking.md](event-driven-banking.md)** — Event-carried state transfer and Kafka event streams in banking.
* **[open-banking.md](open-banking.md)** — PSD2, Open Banking UK, CDR Australia, and FDX APIs.
* **[fraud-integration.md](fraud-integration.md)** — Sub-15ms inline fraud evaluation and behavioral biometrics.
* **[reconciliation.md](reconciliation.md)** — Multi-way ledger balancing and clearing break detection.
* **[settlement.md](settlement.md)** — Net settlement, gross settlement (RTGS), and interbank liquidity.
* **[audit.md](audit.md)** — SOX compliance, immutable audit trails, and financial reporting.
* **[security.md](security.md)** — Banking enclave security, HSM key management, and zero trust.
* **[reference-architecture.md](reference-architecture.md)** — Enterprise Core Banking Reference Architecture.
* **[integration-checklist.md](integration-checklist.md)** — 20-Point Banking Integration Review Checklist.
* **[examples/core-banking-event-bridge.md](examples/core-banking-event-bridge.md)** — Event Bridge integration between Legacy Core and Digital Channels.
