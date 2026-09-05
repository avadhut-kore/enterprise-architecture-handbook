# Architecture Review Board (ARB) Quality Checklist

This checklist is used by Enterprise and Solution Architects during formal Architecture Review Board (ARB) sessions to gate technical designs prior to engineering commitment.

---

## 1. Strategic & Business Alignment
* [ ] **Business Outcome Mapped**: Does the architecture clearly map to specific business KPIs (revenue, cost savings, compliance, customer experience)?
* [ ] **Architecture Principles Adherence**: Does the design adhere to the [15 Architecture Principles](../../ARCHITECTURE-PRINCIPLES.md)? Any deviations documented in an ADR?
* [ ] **Total Cost of Ownership (TCO)**: Has a 3-year FinOps model (compute, storage, egress, licensing, support) been approved by engineering leadership?
* [ ] **Technology Radar Compliance**: Are all chosen runtimes, databases, and frameworks in the `ADOPT` or `TRIAL` rings of the [Technology Radar](../../TECHNOLOGY-RADAR.md)?

---

## 2. Requirements & Boundary Integrity
* [ ] **NFR Quantification**: Are all Non-Functional Requirements numerically quantified (p95/p99 latency, throughput RPS, availability nines, RPO, RTO)?
* [ ] **Domain Separation (DDD)**: Are bounded contexts clearly delineated with no shared database tables across service boundaries?
* [ ] **Modular vs. Distributed Justification**: Has the team justified why a modular monolith is insufficient if proposing distributed microservices?
* [ ] **ADR Completeness**: Are all major trade-offs captured in formally committed ADRs with documented alternatives and consequences?

---

## 3. Resilience, Fault Tolerance & Scalability
* [ ] **Single Point of Failure (SPOF)**: Has every SPOF (database master, message queue, external gateway) been identified with automated failover?
* [ ] **Cascading Failure Mitigation**: Are circuit breakers, request timeouts, and exponential retry backoff with jitter configured on all network boundaries?
* [ ] **Load Shedding & Rate Limiting**: Is traffic throttled at the ingress/API Gateway to protect backend services from burst saturation?
* [ ] **Horizontal Scaling Limits**: Has the database read/write ceiling been calculated, and is there a sharding or caching strategy to surpass it?

---

## 4. Security & Compliance
* [ ] **Zero Trust Baseline**: Is east-west internal network traffic authenticated and encrypted (mTLS via service mesh)?
* [ ] **Identity & Token Validation**: Are API endpoints guarded by standard OAuth2/OIDC claims validation with short-lived tokens?
* [ ] **Secret Management**: Are credentials and encryption keys dynamically provisioned (HashiCorp Vault / Cloud KMS) with zero hardcoded values?
* [ ] **STRIDE Threat Model**: Has a formal STRIDE threat model been conducted with documented mitigations?
* [ ] **Regulatory Compliance**: Does the data architecture satisfy relevant standards (GDPR, PCI-DSS, HIPAA, SOC 2)?

---

## 5. Observability & Operations
* [ ] **Distributed Tracing**: Is OpenTelemetry W3C trace context (`traceparent`) propagated across all HTTP, gRPC, and messaging boundaries?
* [ ] **Telemetry Golden Signals**: Are latency, traffic, errors, and saturation (RED/USE metrics) exposed via standardized Prometheus endpoints?
* [ ] **Structured Logging**: Are application logs output as structured JSON with mandatory trace ID and correlation ID fields?
* [ ] **SLO Burn Rate Alerting**: Are multi-window alerts configured for critical user journeys rather than noisy threshold alerts?
* [ ] **Runbooks & Rollback**: Does a documented zero-downtime deployment (canary/blue-green) and automated rollback plan exist?

---

## Verdict & Sign-off
* **Review Date**: [YYYY-MM-DD]
* **ARB Decision**: [ ] Approved  [ ] Conditionally Approved  [ ] Resubmit Required
* **ARB Chair Signature**: ___________________________________________
