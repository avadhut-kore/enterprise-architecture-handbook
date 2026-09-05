# Legacy Integration: File-Based & Batch Interfaces Integration

## 1. Architectural Purpose & Problem Context
Processing daily flat-file batch drops: SFTP/MFT, PGP encryption, control headers/trailers, checksum verification, and streaming ETL ingestion.

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
