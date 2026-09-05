# Legacy Integration: Event Publication from Legacy Platforms

## 1. Architectural Purpose & Problem Context
Emitting domain events from legacy systems: CDC log scrapers, database trigger tables, MQ message adapters, and outbox table relays.

---

## 2. Legacy Strangler & Anti-Corruption Topology

```mermaid
flowchart LR
    Consumer[Modern Consumer / Web Client] --> Proxy[API Gateway / Reverse Proxy]
    Proxy -->|New Migrated Endpoints| ModernService[Modern Microservice Domain]
    Proxy -->|Legacy Route| ACL[Anti-Corruption Layer ACL]
    ACL --> LegacyCore[(Legacy Mainframe / Core DB)]
    ModernService --> CleanDB[(Modern Cloud Database)]
```

---

## 3. Production Invariants
- Never allow legacy data structures or terminology to permeate modern bounded contexts without an explicit ACL.
- Every legacy migration milestone must be fully reversible with automated fallback capabilities.
