# Architecture Review Board (ARB) Formal Submission Checklist

Use this 50-point master checklist before submitting high-level designs to the Architecture Review Board.

## 1. Executive Summary & Business Intent
- [ ] Business problem statement and value drivers articulated clearly.
- [ ] System Context (C4 L1) diagram included with primary personas.
- [ ] Key Non-Functional Requirements (NFRs) defined with quantitative targets (TPS, p99 latency, availability).

## 2. Technical Architecture & Topologies
- [ ] Container (C4 L2) diagram showing all runtime applications and databases.
- [ ] Deployment topology showing multi-AZ infrastructure, VPCs, and subnets.
- [ ] Primary database engine choice supported with trade-off analysis.

## 3. Security, Compliance & Governance
- [ ] Trust boundaries visually demarcated in architecture diagrams.
- [ ] Zero Trust and mTLS enforced for internal communication.
- [ ] PII/PCI classification and encryption at rest/in transit documented.
- [ ] STRIDE threat model completed and reviewed with Infosec.

## 4. Resilience, Operations & Disaster Recovery
- [ ] Single points of failure eliminated across compute, networking, and data tiers.
- [ ] Disaster recovery RTO and RPO targets validated against business requirements.
- [ ] OpenTelemetry distributed tracing and structured JSON logging configured.
- [ ] Blue-Green or Canary progressive deployment strategy defined.
