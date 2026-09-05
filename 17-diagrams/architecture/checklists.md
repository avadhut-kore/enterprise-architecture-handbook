# Architecture Review Board (ARB) Review Checklist

This checklist provides a structured 30-point evaluation standard for Architecture Review Boards (ARB) and Chief Architects evaluating solution designs.

## 1. Business Alignment & Scope
- [ ] Are business drivers and non-functional requirements (NFRs) clearly articulated and prioritized?
- [ ] Does the design satisfy defined throughput (TPS), latency (p99), and availability (99.9x%) targets?
- [ ] Are system boundaries and bounded contexts cleanly segregated without circular dependencies?

## 2. Security & Compliance
- [ ] Are trust boundaries explicitly visualized in diagrams?
- [ ] Is Zero Trust enforced: are all inter-service communications authenticated via mTLS and authorized via token claims?
- [ ] Are sensitive customer data and credentials encrypted both in transit (TLS 1.3) and at rest (KMS envelope encryption)?
- [ ] Does the architecture satisfy GDPR, HIPAA, or PCI-DSS regulatory constraints?

## 3. Reliability, Resilience & Scalability
- [ ] Are there single points of failure (SPOFs) in any compute, networking, or persistence tiers?
- [ ] Are circuit breakers, retries with exponential backoff, and fallbacks configured on all external calls?
- [ ] Is horizontal auto-scaling configured based on real-time utilization metrics?
- [ ] Are cross-region disaster recovery (DR) RTO and RPO targets validated with operational failover mechanisms?

## 4. Observability & Operability
- [ ] Are distributed tracing (W3C Trace Context), structured JSON logging, and Prometheus metrics incorporated across all services?
- [ ] Are health check endpoints (`/livez`, `/readyz`) decoupled and implemented across all microservices?
- [ ] Is an automated deployment strategy (Blue/Green or Canary) defined with automated rollback metrics?

## 5. Architectural Integrity & Evolution
- [ ] Have major architectural decisions been captured in formal Architecture Decision Records (ADRs)?
- [ ] Have trade-offs between competing design alternatives been quantified and reviewed?
- [ ] Has technical debt introduced by temporary shortcuts been documented with scheduled remediation?
