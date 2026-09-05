# Architecture Documentation Quality Checklist

Use this 30-point universal quality checklist during peer reviews, Architecture Review Board (ARB) evaluations, and pre-release audits.

---

## 1. Document Identity & Governance

- [ ] **Standard Metadata Present**: Document contains valid YAML header (Title, ID, Version, Status, Owner, Reviewers, Dates).
- [ ] **Explicit Status Defined**: Status is one of `Draft`, `In Review`, `Approved`, `Implemented`, `Superseded`, `Deprecated`, or `Archived`.
- [ ] **Single Ownership Assigned**: A named architect or technical lead is designated as accountable for document currency.
- [ ] **Periodic Review Cadence Specified**: A `next_review_date` is scheduled within 6 to 12 months.
- [ ] **Zero Unresolved Placeholders**: No occurrences of `<TBD>`, `TODO`, or placeholder text remain in documents submitted for approval.

---

## 2. Business Context & Scope

- [ ] **Problem Statement Articulated**: Clearly details the business friction, capability gap, or regulatory mandate being solved.
- [ ] **Scope Boundaries Demarcated**: Both **In Scope** and **Out of Scope** boundaries are explicitly enumerated.
- [ ] **Key Stakeholders Identified**: Business sponsors, engineering leads, security officers, and operations leads are listed with contact information.
- [ ] **Assumptions Documented**: Critical operational or business assumptions are stated alongside validation criteria.
- [ ] **External Dependencies Cataloged**: Downstream APIs, vendor SaaS systems, third-party libraries, and shared platforms are identified.

---

## 3. Requirements & Measurable NFRs

- [ ] **Requirements Traceability**: Functional requirements map directly to business drivers and subsequent design components.
- [ ] **Quantified Performance SLOs**: Latency (p50, p95, p99), throughput (RPS), and concurrency are defined under specific loads.
- [ ] **Availability & SLA Defined**: Availability targets (e.g., 99.95%) specify excluded maintenance windows and measurement mechanisms.
- [ ] **RTO and RPO Targets Established**: Maximum permissible downtime (RTO) and data loss (RPO) are quantified for disaster scenarios.
- [ ] **Scalability Limits Defined**: Peak headroom, auto-scale thresholds, and horizontal capacity ceiling are quantified.

---

## 4. Architecture & Technical Design

- [ ] **Architecture Style Justified**: Design style (microservices, modular monolith, event-driven, batch) aligns with documented constraints.
- [ ] **Canonical Diagrams Referenced**: Standard visual models reference canonical formats from [17-diagrams/](../17-diagrams/README.md) (C4 Context/Container, Sequence).
- [ ] **Single Source of Truth Respected**: Specialized details (API endpoints, database tables, network subnets) are linked to dedicated design docs.
- [ ] **Architectural Trade-Offs Analyzed**: Clear documentation of what was sacrificed (e.g., latency vs consistency, complexity vs cost).
- [ ] **ADRs Linked**: Significant architectural decisions link directly to formal [01-adr/](01-adr/README.md) records.

---

## 5. Security & Data Protection

- [ ] **Trust Boundaries Identified**: Network perimeters, VPC boundaries, public/private subnets, and authentication barriers are diagrammed.
- [ ] **Threat Modeling Completed**: STRIDE or attack vector analysis identifies threats and countermeasures.
- [ ] **Authentication & Authorization Defined**: Identity provider (OIDC/SAML), token exchange (OAuth2/JWT), and RBAC/ABAC models are specified.
- [ ] **Data Protection in Transit & Rest**: TLS versions, cipher suites, envelope encryption, and KMS key rotation policies are documented.
- [ ] **PII & Compliance Controls**: Data classification (PII, PCI-DSS, HIPAA, GDPR), retention rules, and redaction practices are established.

---

## 6. Resilience, Operations & Cost

- [ ] **Failure Modes Analyzed**: Downstream timeouts, network splits, database failovers, and cascading failure mitigations (circuit breakers, fallbacks) are specified.
- [ ] **Observability Strategy Specified**: Metrics (RED/USE), structured logging formats, correlation tracing IDs, and alert thresholds are defined.
- [ ] **Deployment & Rollback Strategy**: Deployment pattern (Canary, Blue/Green, Rolling) and automated rollback triggers are documented.
- [ ] **Operational Runbooks Linked**: PagerDuty/incident response runbooks, backup verification, and manual failover procedures are referenced.
- [ ] **Total Cost of Ownership (TCO) Estimated**: Monthly cloud infrastructure run rates, compute/storage costs, and licensing fees are documented.
