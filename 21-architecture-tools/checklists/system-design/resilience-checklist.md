# System Design Checklist: Resilience & Fault Tolerance

## 1. Defensive Patterns
- [ ] Hard timeouts configured on **every** network call (e.g., connect: 500ms, read: 2s)?
- [ ] Retries configured with Exponential Backoff and Full Jitter?
- [ ] Circuit Breakers (e.g., Resilience4j/Polly) wrap all remote external calls?
- [ ] Bulkheads isolate critical resources from non-critical third-party integrations?

## 2. Overload Protection
- [ ] Load shedding configured at gateway when CPU or queue depth exceeds 85%?
- [ ] Dead-Letter Queues (DLQ) capture poison messages after 3 failed attempts?
