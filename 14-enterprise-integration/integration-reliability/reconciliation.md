# Reliability Reconciliation and Drift Correction

## 1. The Need for Out-of-Band Reconciliation
Even with retries, DLQs, and idempotency, distributed systems will inevitably drift over time due to database rollbacks, human interventions, or network partitions. Reliability reconciliation operates as an **asynchronous audit loop** that detects and fixes cross-system discrepancies.

## 2. Daily Batch Reconciliation Loop
```
[External Bank Statement / End-of-Day File]
                    │
                    ▼
       [Reconciliation Engine] ◄── [Internal Payment Ledger DB]
                    │
           (Compare Record by Record)
                    │
          ┌─────────┴─────────┐
          ▼                   ▼
    [Matched: 99.8%]    [Breaks / Discrepancies: 0.2%]
                              │
                              ├─ Scenario A: Internal Ledger Missing -> Create Compensating Entry
                              └─ Scenario B: Amount Mismatch -> Flag for Human Compliance Triage
```
