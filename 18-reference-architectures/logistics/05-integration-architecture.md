# Integration Architecture: EDI Carrier Interchange

## 1. B2B Logistics EDI Rails
- **EDI 204 (Motor Carrier Load Tender)**: Dispatched to external partner carriers via AS2 (Applicability Statement 2) protocol over encrypted TLS with SHA-256 signatures.
- **EDI 214 (Transportation Carrier Shipment Status Message)**: Ingested to update delivery milestones across corporate customer portals.

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
