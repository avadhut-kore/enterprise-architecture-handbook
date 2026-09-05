# Message Replay and Recovery Architecture

## 1. The Need for Replay
Enterprise integration systems must possess the capability to replay historical events from event logs (Kafka, EventStore) into processing pipelines:
- **Disaster Recovery**: Rebuilding downstream state after database corruption or loss.
- **Bug Fix Remediation**: Reprocessing events that were miscalculated due to a software bug.
- **New System Onboarding**: Hydrating a newly deployed service with historical transactional state.

## 2. Replay Topologies

```
[Kafka Topic: payments] (Log Retention: 30 Days)
   Offset: 0 ──────────────────────────── Offset: 50,000 (Current Head)
                ▲
                │ Rewind Consumer Group Offset to Offset 12,000
                │
   [Target Consumer Service] (Hydrating State with Idempotent Writes)
```

## 3. Replay Safety Rules
1. **Mute Outbound Side Effects**: When replaying historical events, outbound notifications (customer SMS, external payment dispatch, webhook triggers) must be disabled via an execution flag (`is_replay = true`).
2. **Enforce Downstream Idempotency**: Downstream database writes must use UPSERT (`INSERT ON CONFLICT DO UPDATE`) or state version checks (`WHERE version = expected_version`).
