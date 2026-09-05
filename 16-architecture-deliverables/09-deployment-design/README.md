# 09-DEPLOYMENT-DESIGN: Runtime Infrastructure & Deployment Architecture

## 1. Overview & Purpose
This directory provides production-grade templates, runtime specifications, and review checklists for designing enterprise cloud and infrastructure deployments.

Deployment design bridges application software architectures and platform engineering. It details how containers, virtual machines, serverless runtimes, network perimeters, data stores, secrets, and autoscaling policies instantiate in production.

---

## 2. Directory Contents
* **[template.md](template.md)**: Master Deployment Design template (18 runtime sections).
* **Infrastructure & Compute**:
  - [environment-strategy.md](environment-strategy.md) — Multi-environment lifecycle (Dev, Staging, Prod).
  - [compute.md](compute.md) — CPU/Memory sizing and VM instance families.
  - [networking.md](networking.md) — VPC topology, CIDR allocations, and routing.
  - [containers.md](containers.md) — Container base images, security, and registries.
  - [kubernetes.md](kubernetes.md) — Pod specs, namespaces, ingress, and network policies.
  - [serverless.md](serverless.md) — Lambda / Cloud Run event-driven execution.
* **Storage & Platform Services**:
  - [storage.md](storage.md) — Block, object (S3), and shared file systems (EFS).
  - [database.md](database.md) — RDS/Aurora clustering, read replicas, and connection pooling.
  - [load-balancing.md](load-balancing.md) — Ingress ALB/NLB, TLS termination, and health checks.
  - [autoscaling.md](autoscaling.md) — Horizontal Pod Autoscaling (HPA) and Karpenter node scaling.
* **Security, Ops & Release**:
  - [configuration.md](configuration.md) — ConfigMaps and external configuration stores.
  - [secrets.md](secrets.md) — Vault / AWS Secrets Manager injection.
  - [observability.md](observability.md) — Prometheus node exporters and Fluentbit log collectors.
  - [backup.md](backup.md) — Automated snapshots and restore test schedules.
  - [disaster-recovery.md](disaster-recovery.md) — Multi-region failover and DNS routing.
  - [multi-region.md](multi-region.md) — Active-Active vs Active-Passive cross-region topology.
  - [deployment-strategy.md](deployment-strategy.md) — Canary, Blue/Green, and Rolling updates.
  - [rollback.md](rollback.md) — Automated failure detection and instant rollback runbooks.
* **Governance**:
  - [review-checklist.md](review-checklist.md) — 20-Point Deployment Design Review Checklist.
  - [examples/multi-region-k8s-deployment.md](examples/multi-region-k8s-deployment.md) — Multi-Region Kubernetes Deployment Design.
