# Poison Message Handling and Quarantine Patterns

## 1. What is a Poison Message?
A poison message is a message that cannot be processed successfully under any circumstances due to invalid syntax, corrupted data, or unhandled software edge cases. Unlike transient failures (e.g., database timeout), repeatedly consuming a poison message crashes or halts the consumer service, creating an infinite failure loop.

## 2. Quarantine Pattern

```
[Consumer Application]
       │
       ├─ Step 1: Read Message
       ├─ Step 2: Increment Local In-Memory / Redis Counter: attempts[msg_id]++
       │
       ▼
   (attempts > 3?)
       │
       ├─ YES ──> [Bypass Business Logic]
       │          [Write Message to Quarantine Bucket / S3]
       │          [Commit Offset in Kafka / Ack in RabbitMQ]
       │          [Emit Severity:CRITICAL SIEM Alert]
       │
       └─ NO  ──> [Execute Business Logic]
```

## 3. Preventive Architecture
- **Ingress Schema Validation**: Catch malformed payloads at the edge API gateway or message interceptor before they enter event brokers.
- **Fail-Safe Deserialization**: Use custom deserialization error handlers (e.g., Spring Kafka `ErrorHandlingDeserializer`) so that corrupt bytes do not crash the consumer thread before application logic executes.
