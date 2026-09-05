# Dead Letter Queue (DLQ) Architecture and Triage

## 1. Dead Letter Processing Lifecycle

```
[Main Topic: orders.events]
           │
           ▼
[Consumer Service] ──(Processing Fails 3 Times)──> [Retry Topic: orders.retry.1]
                                                             │
                                                             ▼ (Wait 1 min)
                                                    [Consumer Service]
                                                             │ (Fails Again)
                                                             ▼
                                                    [Retry Topic: orders.retry.2]
                                                             │
                                                             ▼ (Wait 5 min)
                                                    [Consumer Service]
                                                             │ (Final Exhaustion)
                                                             ▼
                                                    [Dead Letter Queue (DLQ)]
                                                             │
                                            ┌────────────────┴────────────────┐
                                            ▼                                 ▼
                                   [Ops Alert / Dashboard]          [Replay Tooling]
```

## 2. Dead Letter Message Metadata Envelope
Every message routed to a DLQ must be wrapped in an diagnostic envelope containing context required for triage:
```json
{
  "original_topic": "payments.clearing",
  "original_partition": 3,
  "original_offset": 9928172,
  "failure_reason": "SCHEMA_VALIDATION_ERROR",
  "exception_message": "Field 'tax_id' failed regex pattern validation",
  "stack_trace": "com.enterprise.validator.SchemaException: ...",
  "retry_count": 3,
  "first_failed_at": "2026-09-05T12:00:00Z",
  "failed_at": "2026-09-05T12:06:15Z",
  "consumer_group": "clearing-processor-v2",
  "original_payload": { ... }
}
```

## 3. Operational DLQ Governance Rules
1. **Never Let DLQs Become Black Holes**: Unmonitored DLQs silently accumulate lost revenue. Alert on any DLQ depth $> 0$.
2. **Automated vs. Manual Replay**: Transient infrastructure failures can be replayed automatically; schema and data-corruption errors require human bug fixes before replaying.
3. **Preserve Message Ordering Context**: Moving a failed message to a DLQ allows subsequent partition messages to proceed, but may violate chronological ordering. If strict ordering is mandatory, the entire partition must halt until resolved.
