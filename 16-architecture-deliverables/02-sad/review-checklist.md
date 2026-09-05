# Solution Architecture Document Review Checklist

Use this 25-point checklist during Architecture Review Board (ARB) sessions.

---

## 1. Strategic Alignment & Requirements
- [ ] Business capabilities and drivers are explicitly documented.
- [ ] In-Scope and Out-of-Scope boundaries are unambiguous.
- [ ] Functional requirements trace directly to business objectives.
- [ ] Non-Functional Requirements (NFRs) are quantified with testable thresholds.

## 2. Architectural Modeling & Visuals
- [ ] C4 System Context diagram (Level 1) clearly identifies all external actors and dependencies.
- [ ] C4 Container diagram (Level 2) illustrates all deployable units, databases, and brokers.
- [ ] Network protocols and payload formats are labeled on every interaction arrow.

## 3. Data & Persistence
- [ ] Source of truth is defined for each domain aggregate.
- [ ] Consistency model (ACID vs Eventual) is explicitly justified.
- [ ] Data retention, archival, and GDPR/privacy policies are documented.

## 4. Security & Compliance
- [ ] Trust boundaries and identity perimeters are mapped.
- [ ] Authentication (OIDC) and authorization (RBAC/ABAC) mechanisms are specified.
- [ ] Data encryption in transit (TLS 1.3) and at rest (AES-256) is mandated.
- [ ] Threat modeling has been conducted and mitigations documented.

## 5. Resilience & Disaster Recovery
- [ ] RTO and RPO targets are documented and validated against business requirements.
- [ ] Single points of failure (SPOFs) have been identified and mitigated.
- [ ] Failure cascades are prevented via circuit breakers, timeouts, and fallbacks.

## 6. Operations, Observability & Cost
- [ ] Distributed tracing, structured logging, and metrics aggregation are defined.
- [ ] SRE on-call model and critical runbooks are identified.
- [ ] Cloud infrastructure TCO estimate is completed and approved by FinOps.
- [ ] All critical architectural decisions reference approved ADRs.
