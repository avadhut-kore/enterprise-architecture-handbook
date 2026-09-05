# Operational Readiness Architecture (`operational-readiness/`)

## Executive Summary

Operational readiness bridges the gap between software design and production operability. While systems may achieve functional correctness in staging environments, unmanaged operational dependencies, ambiguous team ownership boundaries, and untested on-call escalations inevitably produce catastrophic cascading outages under production load.

This domain codifies the architecture of operational readiness, establishing deterministic service ownership models, structured on-call topologies, and automated service dependency mapping.

---

## Core Operational Readiness Disciplines

```mermaid
flowchart LR
    A["Service Catalog & Metadata"] --> B["Service Ownership Matrix"]
    B --> C["On-Call & Paging Topologies"]
    C --> D["Service Dependency Mapping"]
    D --> E["Tier-0 Blast Radius Isolation"]
```

### Directory Contents
1. **[Operational Architecture & Operating Models](operational-architecture.md)** — System operating models, tiered service classifications, SLA/OLA alignments, and handover governance.
2. **[Service Dependency Mapping & Blast Radius](service-dependency-mapping.md)** — Upstream/downstream topological discovery, hard vs soft dependencies, graceful fallback boundaries, and Tier-0 criticality.
