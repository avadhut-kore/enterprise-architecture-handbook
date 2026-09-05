# Enterprise Integration Reliability Review Checklist

## Timeouts & Backoff
- [ ] Does every HTTP, gRPC, and database client have an explicit, bounded socket and connection timeout?
- [ ] Do deadlines decrease progressively down the call stack?
- [ ] Are retries configured exclusively with exponential backoff and randomized full jitter?

## Idempotency & Fault Isolation
- [ ] Are all mutating REST APIs protected by server-side `Idempotency-Key` validation?
- [ ] Are circuit breakers configured on all synchronous cross-system RPC calls?
- [ ] Do consumers handle poison messages without entering infinite crash loops?

## Asynchronous Resilience
- [ ] Do all asynchronous queues route permanently failing messages to a monitored Dead Letter Queue?
- [ ] Is there an automated or tested runbook for replaying DLQ messages after defect remediation?
- [ ] Are dependencies categorized into hard and soft tiers to prevent partial failure cascades?
