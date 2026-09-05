# Integration Design Review Checklist
- [ ] System ownership and support contacts documented for both sides.
- [ ] Protocol and payload serialization schemas explicitly defined.
- [ ] Failure isolation, timeouts, circuit breakers, and retries specified.
- [ ] Idempotent consumer design guarantees safe replay of duplicate events.
- [ ] Dead-Letter Queue (DLQ) and alerting thresholds defined.
- [ ] Security (mTLS / OAuth2) and daily reconciliation procedures validated.
