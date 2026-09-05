# Enterprise Architecture Review Checklist

## Overview

This checklist is the standard evaluation tool utilized by reviewers, Enterprise Architects, and the Architecture Review Board (ARB). Every proposed solution architecture must be evaluated against these verification checkpoints prior to formal ratification.

---

## 1. Business Alignment & Scope
- [ ] **Problem Articulation**: Is the business problem stated clearly in measurable terms rather than pure technology desires?
- [ ] **Capability Mapping**: Are the system's components mapped to approved Level 2/Level 3 Enterprise Business Capabilities?
- [ ] **Capability Sprawl**: Does this solution duplicate an existing enterprise platform (e.g., building custom chat when Slack/Teams exists)?
- [ ] **Scope Boundaries**: Are in-scope and explicitly out-of-scope boundaries clearly demarcated?

## 2. Architecture Styles & Modularity
- [ ] **Bounded Contexts**: Are domain boundaries established using Domain-Driven Design (DDD) principles?
- [ ] **Style Selection Justified**: Is the choice of architecture style (Modular Monolith, Microservices, Serverless, EDA) defended in an ADR?
- [ ] **Coupling & Cohesion**: Are components decoupled temporally and spatially? Are circular service dependencies eliminated?
- [ ] **Paved-Road Conformance**: Does the stack utilize enterprise-approved languages and frameworks (Technology Radar: Adopt)?

## 3. Data Architecture & Persistence
- [ ] **Data Ownership**: Does each bounded context / microservice own its own data? Are cross-boundary SQL joins strictly forbidden?
- [ ] **Storage Engine Selection**: Is the database paradigm (Relational, Document, Key-Value, Search) matched to empirical access patterns?
- [ ] **Partitioning & Shard Keys**: If partitioned, is the shard key evaluated for high cardinality and hot-spot prevention?
- [ ] **Data Retention & Purging**: Are automated lifecycle rules defined to transition aged data to cold archive storage?
- [ ] **GDPR / Privacy Compliance**: Is customer PII identified, tokenized, and prepared for cryptographic erasure (crypto-shredding)?

## 4. Security & Compliance
- [ ] **Zero Trust Perimeter**: Is every request authenticated and authorized at the API Gateway and internal service boundaries?
- [ ] **Identity & Protocols**: Are OAuth 2.0 / OpenID Connect with short-lived JWTs enforced?
- [ ] **Encryption in Transit**: Is TLS 1.3 enforced for public ingress and mTLS enforced for internal microservice RPC?
- [ ] **Encryption at Rest**: Are all databases, disks, and object buckets encrypted using AES-256 with KMS Customer Managed Keys (CMKs)?
- [ ] **STRIDE Threat Modeling**: Has a formal data-flow threat model been conducted with documented mitigations?
- [ ] **Secrets Management**: Are credentials dynamically fetched from Vault/KMS? Zero hardcoded secrets in repositories or Docker images.

## 5. Reliability, Availability & Disaster Recovery
- [ ] **Single Point of Failure (SPOF)**: Has every SPOF (DNS, Load Balancers, Databases, NAT Gateways) been eliminated?
- [ ] **Multi-AZ Redundancy**: Are stateless compute and managed databases distributed across at least 3 Availability Zones?
- [ ] **Resilience Patterns**: Are circuit breakers, timeouts, retries with exponential jitter, and bulkheads implemented for all external calls?
- [ ] **RPO & RTO Targets**: Are Recovery Point Objective (RPO) and Recovery Time Objective (RTO) explicitly documented and testable?
- [ ] **Backup Immutability**: Are database snapshots streamed continuously to WORM (Write Once Read Many) offsite storage?

## 6. Scalability & Performance
- [ ] **Empirical Scale Projections**: Are peak read QPS, peak write TPS, and 5-year storage growth mathematically calculated?
- [ ] **Stateless Compute**: Are application worker pods strictly stateless, allowing horizontal pod auto-scaling (HPA)?
- [ ] **Caching Architecture**: Is multi-tier caching (CDN edge + L2 Redis) implemented for read-heavy workloads?
- [ ] **Connection Pooling**: Are database connection pools sized via Little's Law with intermediate poolers (PgBouncer/RDS Proxy)?

## 7. Observability & Operations
- [ ] **Distributed Tracing**: Does the architecture propagate W3C TraceContext headers across all HTTP, gRPC, and Kafka hops?
- [ ] **Structured Logging**: Do all services emit structured JSON logs with embedded `trace_id` and `span_id`?
- [ ] **Standard Metrics (RED/USE)**: Do services expose standardized Prometheus/OpenTelemetry metrics for Rate, Errors, and Duration?
- [ ] **Health Probes**: Are distinct Liveness and Readiness probes configured for all container orchestrators?

## 8. FinOps & Cost Efficiency
- [ ] **Total Cost of Ownership (TCO)**: Is a 3-year cloud infrastructure expenditure model formulated at 1x, 5x, and 10x scale?
- [ ] **Unit Economics**: Is the Cost per Transaction calculated and validated against gross product margins?
- [ ] **Resource Tagging**: Are mandatory cloud tags (`CostCenter`, `Owner`, `Environment`, `ServiceId`) enforced in IaC scripts?
- [ ] **Commitment Strategy**: Has baseline compute been modeled for Reserved Instances (RI) or Savings Plans?
