# Terminal Systems and Screen Scraping (TN3270 / TN5250)

## 1. When Screen Scraping is Unavoidable
When no backend APIs, MQ queues, or database access exist:
- **RPA / Terminal Emulation**: Emulate a 3270 green screen over Telnet, send keystrokes, and read screen buffer memory.
- **Anti-Pattern Warning**: Screen scraping is fragile. A change of one character on screen breaks the integration. Treat as an absolute last resort.

## 2. Production Architecture Best Practices
- **Strict Boundary Validation**: Never trust incoming payloads implicitly; enforce schema contracts and payload size limits at the ingress layer.
- **Fail-Safe Idempotency**: State-mutating operations must track idempotency keys in a low-latency distributed cache (e.g., Redis) with an appropriate time-to-live.
- **Circuit Breaking & Fallback**: Integrate circuit breakers with sensible failure rate thresholds (typically 50% over a 30s sliding window) to prevent cascading dependency failure.

## 3. Security & Operational Checklist
- [ ] Enforce mutual TLS (mTLS) with TLS 1.3 across all inter-system communications.
- [ ] Mandate distributed trace context (`traceparent`) and business correlation IDs on every hop.
- [ ] Ensure non-transient failures are isolated to a Dead Letter Queue with real-time alerting.
