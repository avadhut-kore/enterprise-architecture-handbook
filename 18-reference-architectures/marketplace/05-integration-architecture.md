# Integration Architecture: Payout Rails & Identity

## 1. Merchant Payout Orchestration (Stripe Connect)
- Leverages **Stripe Connect Custom / Express** accounts.
- Automated 1099-K tax reporting: Ingests annual gross sales volume per merchant and automatically generates IRS tax filings for sellers crossing federal reporting thresholds.

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
