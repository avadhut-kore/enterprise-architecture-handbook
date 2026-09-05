# Integration Architecture: Banking & EDI Rails

## 1. ISO 20022 Financial Integration
- **Vendor Payment Batches**: Outbound disbursement files are generated in standard ISO 20022 `pain.001.001.09` XML format and transmitted to corporate banking partner networks.
- **Automated Bank Reconciliation**: Daily bank statement feeds in `camt.053.001.08` are ingested to automatically clear open cash ledger balances against verified bank settlement transactions.

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
