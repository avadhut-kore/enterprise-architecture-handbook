# Legacy Integration: Legacy Databases & Proprietary APIs Integration

## 1. Architectural Purpose & Problem Context
Interfacing with legacy relational databases (DB2, Informix) and RPC APIs; connection management, transaction scope limits, and lock contention avoidance.

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
