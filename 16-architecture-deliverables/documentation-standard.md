# Architecture Documentation Standard

## 1. Core Principles

Every deliverable created in this library must adhere to three foundational engineering rules:

1. **Single Source of Truth**: Every architectural fact belongs in exactly one document. Do not copy database schemas into an HLD or security threat models into a PRD. Reference canonical documents using relative links.
2. **Measurable and Testable**: Vague aspirations (*"the system must be scalable and fast"*) are strictly prohibited. Non-functional attributes must be quantified (*"p99 latency < 120ms under 15,000 requests/sec with a max 1.5% CPU throttling rate"*).
3. **Decisions Over Descriptions**: Architecture documents exist to capture why a particular design was chosen over viable alternatives, including costs, risks, and trade-offs.

---

## 2. Mandatory Metadata Schema

Every architecture deliverable MUST begin with the canonical YAML metadata block:

```yaml
---
title: "Solution Architecture Document — Global Payment Gateway"
document_id: "SAD-PAY-001"
version: "1.0.0"
status: "Approved" # Draft | In Review | Approved | Implemented | Superseded | Deprecated | Archived
classification: "Confidential - Internal Engineering"
owner: "Jane Doe <jane.doe@enterprise.com>"
authors:
  - "Jane Doe (Principal Solution Architect)"
  - "John Smith (Staff Platform Engineer)"
reviewers:
  - "Security Review: Alice Wong (Staff Security Architect)"
  - "Data Review: Bob Taylor (Principal Data Architect)"
  - "ARB Sign-Off: Enterprise Architecture Board"
created_date: "2026-03-15"
last_updated: "2026-09-01"
next_review_date: "2027-03-15"
supersedes: "" # Document ID if replacing an existing artifact
superseded_by: "" # Populated only when status transitions to Superseded
repository_link: "https://github.com/enterprise/payment-platform"
related_adrs:
  - "ADR-0042: Database Selection for Ledger Immutability"
  - "ADR-0045: gRPC over REST for Inter-Service Orchestration"
---
```

---

## 3. Canonical Architecture Mapping (Source of Truth)

| Architectural Fact | Canonical Home | Prohibited Redundant Home |
|---|---|---|
| Single architectural decision & trade-offs | [01-adr/](01-adr/README.md) | Inlined inside HLD or README |
| End-to-end multi-view system structure | [02-sad/](02-sad/README.md) | Fragmented across wiki pages |
| Component boundaries & service interactions | [03-hld/](03-hld/README.md) | Class-level LLD specs |
| In-depth class, module, and sequence logic | [04-lld/](04-lld/README.md) | High-level architecture docs |
| HTTP / RPC contract schemas and endpoints | [05-api-design/](05-api-design/README.md) | Prose descriptions in HLD |
| Schema tables, partition keys, ER diagrams | [06-data-design/](06-data-design/README.md) | Application deployment files |
| Enterprise messaging & ETL orchestration | [07-integration-design/](07-integration-design/README.md) | Generic system design docs |
| Threat models, cryptographic key lifecycles | [08-security-design/](08-security-design/README.md) | Copied boilerplate security text |
| Subnets, K8s manifests, autoscaling policies | [09-deployment-design/](09-deployment-design/README.md) | Application logic specs |
| Architectural uncertainty and blast radius | [11-risk-register/](11-risk-register/README.md) | Buried in meeting notes |
| Disaster recovery RTO/RPO and failover steps | [18-disaster-recovery/](18-disaster-recovery/README.md) | Informal on-call wikis |

---

## 4. Architecture Documentation Anti-Patterns

Avoid these 18 critical anti-patterns when authoring deliverables:

1. **Post-Implementation Documentation**: Writing the architecture document after the software has already been written to satisfy a bureaucratic compliance gate.
2. **Diagrams Without Decisions**: Including beautiful box-and-arrow diagrams without detailing component responsibilities, failure handling, or trade-offs.
3. **ADRs Without Context**: Stating *"We chose Postgres"* without recording the problem, constraints, evaluated alternatives (e.g., CockroachDB, MySQL), and operational downsides.
4. **HLD Masquerading as LLD**: Bloating an HLD with Java/Go method signatures, ORM annotations, and internal loops.
5. **LLD Without Implementation Guidance**: High-level hand-waving that leaves engineers guessing on transaction boundaries, concurrency locks, and idempotency keys.
6. **Unquantified NFRs**: Using subjective adjectives like *"fast"*, *"scalable"*, *"resilient"*, or *"user-friendly"*.
7. **Boilerplate Security Sections**: Copy-pasting *"All data is encrypted in transit and at rest"* without threat models, key rotation procedures, or trust boundaries.
8. **Zombie Architecture Documents**: Documents abandoned immediately after initial release with no assigned owner, review cadence, or deprecation notice.
9. **Contradictory Sources of Truth**: Maintaining conflicting diagrams or data schemas across three different project wikis.
10. **Architecture in Vacuum**: Specifying systems without calculating financial infrastructure costs, compute budgets, or license liabilities.
11. **No Failure Analysis**: Assuming sunny-day scenarios where networks never drop, databases never lock, and downstream APIs never time out.
12. **Vendor Lock-in Obfuscation**: Camouflaging proprietary cloud dependencies without documenting exit costs or portability trade-offs.
13. **Missing Rollback Strategies**: Formulating database migrations or cutovers with no automated or manual rollback runbook.
14. **Unassigned Action Items**: Architecture reviews ending with vague recommendations rather than assigned tickets, owners, and hard deadlines.
15. **Over-Engineering Bureaucracy**: Forcing a 50-page SAD on a 2-day microservice tweak.
16. **Undocumented Assumptions**: Assuming downstream systems support infinite throughput or sub-millisecond latencies without verification.
17. **Dead Diagram Links**: Referencing PNGs on private cloud buckets or local drives rather than repository-managed diagrams in [17-diagrams/](../17-diagrams/README.md).
18. **Unchecked Placeholders**: Leaving `<TBD>`, `<Insert diagram here>`, or `<Owner>` in documents marked as `Approved`.
