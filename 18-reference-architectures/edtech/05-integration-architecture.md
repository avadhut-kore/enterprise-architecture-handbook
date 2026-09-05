# Integration Architecture: LTI 1.3 & SIS Interoperability

## 1. Learning Tools Interoperability (LTI 1.3)
- Implements IMS Global LTI 1.3 using OAuth 2.0 and JSON Web Tokens (JWT) for secure Single Sign-On and grade passback to external institutional LMS systems (Canvas, Blackboard, Moodle).

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
