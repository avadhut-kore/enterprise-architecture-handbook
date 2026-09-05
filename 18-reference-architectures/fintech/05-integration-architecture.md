# Integration Architecture: Real-Time Payment Rails

## 1. FedNow / RTP ISO 20022 Integration
- Instant payments execute via ISO 20022 `pacs.008.001.08` Financial Institutional Customer Credit Transfer.
- Funds must be irrevocably credited to the receiver's account within **15 seconds** of initiation under federal operating circulars.

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
