# Integration Architecture: Enterprise SSO & SCIM

## 1. Federated Identity & SCIM 2.0 Provisioning
- **Enterprise SSO**: Supports SAML 2.0 and OIDC federated login, redirecting users to their corporate Okta or Microsoft Entra ID tenant.
- **SCIM 2.0**: Automatically provisions and de-provisions user accounts in real-time when employees join or depart the customer's corporate directory.

## 2. Interface Contracts & Resiliency Patterns
- **Idempotency & Deduplication**: All mutating API endpoints require an `Idempotency-Key` header cached in Redis for 24 hours.
- **Circuit Breakers & Timeouts**: Enforce 2.5s connection timeouts and 5.0s read timeouts; trip circuit breakers if downstream partner error rates exceed 50% over a 30-second sliding window.
- **Dead Letter Queues (DLQ)**: Non-transient payload parse failures are routed to dead-letter topics with operational Slack/PagerDuty alerts.
