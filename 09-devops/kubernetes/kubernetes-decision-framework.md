# Kubernetes Decision Framework: Should We Use Kubernetes?

Kubernetes is often adopted by default due to industry hype, resulting in immense operational overhead for simple workloads. An architect must evaluate alternatives before adopting Kubernetes.

## 1. When Kubernetes is UNNECESSARY (Anti-Patterns)
- You have fewer than 10 microservices.
- Your engineering team has no dedicated SRE/Platform engineers to manage cluster upgrades, CNI networking, and etcd backups.
- Your application can run cleanly on PaaS (Heroku, Render) or Managed Containers (AWS ECS, Google Cloud Run, Azure Container Apps).
- Your workload consists of static frontend sites or simple scheduled cron jobs.

## 2. When Kubernetes is GENUINELY REQUIRED
- You need deep cross-cloud or on-premises workload portability.
- You operate a complex microservices mesh with dynamic service discovery, fine-grained autoscaling, and sophisticated traffic engineering (canaries, mTLS service mesh).
- You manage custom controllers and complex stateful distributed operators (e.g., managing a self-hosted Kafka cluster or ML training cluster).
- You are building an Internal Developer Platform (IDP) hosting thousands of services across multiple product teams.

## 3. The Architecture Decision Matrix

```
Workload & Organizational Complexity
     ▲
High │   [MANAGED CONTAINERS]     │   [KUBERNETES / EKS / GKE]
     │   (AWS ECS / Cloud Run)    │   High Scale, Complex Topology,
     │   Fast Time-to-Market      │   Internal Platform Foundation
     ├────────────────────────────┼─────────────────────────────
Low  │   [SERVERLESS / PAAS]      │   [VIRTUAL MACHINES]
     │   (AWS Lambda / Vercel)    │   (EC2 / Compute Engine)
     │   Low Ops, Pure Pay/Use    │   Legacy Monoliths, Specialized HW
     └────────────────────────────┴─────────────────────────────►
         Low                      High
                    Team DevOps Maturity & Scale
```

## Related Resources
- [Container Decisions](../docker/container-architecture-decisions.md)
- [Production Cluster Architecture](./production-cluster-architecture.md)
