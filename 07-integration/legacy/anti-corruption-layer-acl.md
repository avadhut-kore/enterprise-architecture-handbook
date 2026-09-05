# Legacy Integration: Anti-Corruption Layer (ACL) for Legacy Systems

## 1. Architectural Purpose & Problem Context
Isolating modern domain models from legacy vocabulary: bi-directional mapping, facade adapters, and preventing legacy domain bleeding.

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
