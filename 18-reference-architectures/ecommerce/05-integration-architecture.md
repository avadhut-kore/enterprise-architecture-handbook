# Integration Architecture: Payment Gateways & Logistics

## 1. Payment Orchestration Architecture
- The platform uses a smart routing payment orchestrator connecting to multiple acquirers (Stripe, Adyen, Braintree).
- If primary acquirer latency exceeds 1.5s or returns HTTP 5xx, transactions dynamically fail over to the secondary acquirer within the same checkout session.
- Real-time tax calculation is executed via cached Avalara API calls with pre-computed fallback tax tables if the external tax API fails.

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
