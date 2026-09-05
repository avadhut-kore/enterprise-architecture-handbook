# Business Architecture & Requirements: Fintech Engine

## 1. Business Context & Core Principles
- **Financial Immutability**: Balances are calculated dynamically by summing historical posted ledger entries; direct updates to balance columns (`UPDATE accounts SET balance = balance + 100`) are architecturally prohibited.
- **Double-Entry Balance Invariant**: Every financial movement must balance to zero:
  $$\sum \text{Debits} - \sum \text{Credits} = 0$$

---

## 2. Scale Model & Capacity Assumptions

| Scale Parameter | Mid-Scale Neobank | Tier-1 Global Fintech |
| :--- | :--- | :--- |
| **Active Customer Accounts** | 1,000,000 accounts | 25,000,000 accounts |
| **Continuous Baseline TPS** | 250 TPS | 5,000 TPS |
| **Peak Black Friday TPS** | 2,500 TPS | 35,000 TPS |
| **Card Authorization Latency Budget**| $< 50\text{ ms}$ (p99) | $< 35\text{ ms}$ (p99) |
| **Ledger Storage Growth** | 50 GB / month | 1.5 TB / month |

---

## 3. Measurable NFR Budgets

| NFR Metric | Target Budget | Measurement & Enforcement Point |
| :--- | :--- | :--- |
| **Card Authorization P99 Latency** | $< 50\text{ ms}$ | Measured at network ingress edge from Visa/Mastercard |
| **Ledger Availability** | 99.999% ($< 5.25\text{ min}$/yr) | Multi-AZ active-active database clustering |
| **Idempotency Guarantee** | 100% duplicate rejection | Enforced via unique idempotency keys in Redis/DB |
| **Reconciliation Break Rate** | $< 0.001\%$ of transactions | Daily automated multi-way matching engine |
