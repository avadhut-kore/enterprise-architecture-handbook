# ADR-0055: Establishment of Platform Engineering Team & Golden Paths

## Metadata
```yaml
id: ADR-0055
title: Establishment of Platform Engineering Team & Golden Paths
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Application developers spent 40% of their working hours wrestling with raw Terraform, Kubernetes manifests, and IAM policies, paralyzing business feature delivery.

---

## 2. Decision
We establish a dedicated Platform Engineering Team to build an Internal Developer Platform (IDP) providing self-service Golden Paths for common application architectures.

---

## 3. Positive Consequences
- Reduces developer onboarding and microservice provisioning from weeks to minutes.
- Enforces compliance, security, and tagging standards by default.
- Drastically reduces developer cognitive load.

---

## 4. Negative Consequences & Trade-offs
- Requires dedicated ongoing platform engineering investment ($$$).
- Risk of building an ivory-tower platform if developer feedback is ignored.

---

## 5. Alternatives Considered & Rejected
- **Centralized IT Ticketing Gatekeepers**: Rejected due to crippling 4-week delivery delays.
- **Decentralized Chaos (Every Team Builds Own Infra)**: Rejected due to fractured standards and security vulnerabilities.
