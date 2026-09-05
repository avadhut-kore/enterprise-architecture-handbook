# ADR-0047: Compute Runtime Standardization on Serverless Containers and EKS

## Metadata
```yaml
id: ADR-0047
title: Compute Runtime Standardization on Serverless Containers and EKS
status: accepted
decision_type: architectural
scope: enterprise-cloud-infrastructure
owners: enterprise-architecture-board
date: 2026-09-05
review_cadence: annual
```

---

## 1. Context & Problem Statement
Engineering teams were deploying bespoke combinations of raw EC2 virtual machines, standalone Docker hosts, and unmanaged Kubernetes clusters.

---

## 2. Decision
We standardize enterprise compute runtimes into two tiers: Tier A: Serverless Containers (AWS ECS Fargate) as the default Golden Path for 80% of microservices; Tier B: Amazon EKS for complex distributed platforms requiring custom operators.

---

## 3. Positive Consequences
- Eliminates OS patching toil for 80% of workloads.
- Reduces compute baseline costs via automated container packing.
- Standardizes CI/CD pipelines around OCI container images.

---

## 4. Negative Consequences & Trade-offs
- Requires application engineering to containerize legacy services and externalize state.

---

## 5. Alternatives Considered & Rejected
- **Virtual Machines (EC2) Everywhere**: Rejected due to high maintenance overhead and slow autoscaling.
- **Kubernetes Everywhere**: Rejected due to excessive operational tax on small engineering teams.
