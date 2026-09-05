# Architectural Teardown: Tier-1 Global Bank: Mainframe Core Modernization

## 1. System Topology Before vs. After

```
BEFORE: Monolithic Spaghetti Integration
[Channel 1] ───(Direct DB Link)───┐
[Channel 2] ───(Hardcoded SOAP)───┼──> [Monolithic Legacy System] ◄── [Custom Cron Batches]
[Channel 3] ───(3270 Terminal)────┘

AFTER: Decoupled Event-Driven Integration Mesh
[Channels] ──> [API Gateway / WAF / Token Exchange]
                      │
                      ▼
     [Autonomous Microservices & Sidecars]
                      │
                      ▼
        [Enterprise Event Backbone (Kafka)]
                      │
    ┌─────────────────┴─────────────────┐
    ▼                                   ▼
[Cloud Aurora DB]              [Legacy System via ACL & Outbox]
```

## 2. Critical Failure Modes & How They Were Resolved
- **Failure Mode 1: Mainframe MIPS Starvation**: Resolved by routing balance inquiries to a Redis read-replica cache kept fresh via Debezium CDC.
- **Failure Mode 2: Distributed Data Inconsistency**: Solved by replacing dual-writes with the Transactional Outbox pattern.
- **Failure Mode 3: Silent Data Corruption**: Prevented through automated end-of-day reconciliation matching engines.

## 3. Key Architectural Lessons
1. Never attempt a "big bang" migration of core systems.
2. Ensure every state-mutating API call is idempotent from day one.
3. Decouple reporting and read queries from the transactional system of record.
