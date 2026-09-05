# Architecture Review Board (ARB) Packet: [PROJECT NAME]

---
**Metadata**:
```yaml
review_id: "ARB-REV-[YEAR]-[NUMBER]"
project_name: "[Project Name]"
presenter: "[Lead Solution Architect Name <email>]"
arb_chair: "[Chief Architect / ARB Chair Name]"
review_date: "YYYY-MM-DD"
status: "Pending Review" # Pending Review | Approved | Approved with Conditions | Rework Required | Rejected
related_documents:
  - "SAD: [SAD-001](../02-sad/template.md)"
  - "HLD: [HLD-001](../03-hld/template.md)"
  - "ADRs: [ADR-0001, ADR-0002]"
```
---

## 1. Review Objective & Scope
* What specific architecture milestone is being evaluated (Initial Blueprint, Major Evolution, Pre-Implementation)?
* What approvals or concessions are being requested from the ARB?

## 2. Architecture Summary & Strategic Alignment
* High-level summary of the business capability and technical approach.
* Alignment with enterprise architecture principles (e.g., Cloud-First, API-Led, Zero Trust).

## 3. Key Architectural Decisions (ADRs Under Review)
| ADR ID | Decision Summary | Alternatives Rejected | Key Trade-off Accepted |
|---|---|---|---|
| ADR-001 | CockroachDB for multi-region ledger | PostgreSQL with async replication | Higher cross-region write latency for RPO=0 |
| ADR-002 | Kafka for asynchronous event ingestion | RabbitMQ, AWS SQS | Operational complexity for 30-day event replay |

## 4. Domain Deep-Dives
* **Security & Compliance**: Status of threat modeling, PII redaction, and compliance sign-offs.
* **Data Architecture**: Consistency model, schema migration strategy, and backup retention.
* **Resilience & DR**: Target RTO/RPO and multi-region failover automation.
* **Cost & FinOps**: Estimated monthly cloud run-rate and annual licensing commitments.

## 5. Formal ARB Decision Record
*(Completed during the ARB session)*

* **Decision Outcome**:
  - [ ] **Approved** (Proceed to implementation without reservation).
  - [ ] **Approved with Conditions** (Proceed to implementation; conditions must be closed before PRR).
  - [ ] **Rework Required** (Substantial architectural gaps; must re-present at ARB).
  - [ ] **Rejected** (Architecture unviable; project redirected).
  - [ ] **Deferred** (Awaiting external dependency or feasibility spike).

### Conditions & Required Action Items
| Item # | Required Action | Assigned Owner | Due Date | Verification Gate |
|---|---|---|---|---|
| 1 | Conduct load test verifying p99 latency < 250ms at 15,000 TPS | Lead Engineer | YYYY-MM-DD | LLD Review |
| 2 | Complete STRIDE threat model with Information Security team | SecArch | YYYY-MM-DD | Pre-Implementation |

### Signatures & Approvals
* **ARB Chair**: ___________________________ Date: _________
* **Chief Information Security Officer (CISO)**: ___________________________ Date: _________
* **Head of Infrastructure & Cloud**: ___________________________ Date: _________
