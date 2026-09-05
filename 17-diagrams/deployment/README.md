# Deployment Topologies & Infrastructure Diagrams

Deployment diagrams visualize **physical and cloud infrastructure topology**, showing where software containers, processes, and data stores run, how they scale across Availability Zones and Regions, and how redundancy is achieved.

## Core Deployment Topologies Covered
1. **Single-Server & Simple 3-Tier**: Monoliths, load balancers, and relational read replicas.
2. **Virtual Machine (VM) Infrastructure**: Auto-scaling groups, bastion hosts, and private subnets.
3. **Container Orchestration**: Kubernetes (EKS/GKE/AKS), node pools, Ingress, and pod replica distributions.
4. **Serverless Architectures**: Event-driven serverless functions, managed gateways, and NoSQL engines.
5. **Hybrid Cloud & Edge**: DirectConnect/ExpressRoute, local edge compute, and Cloudflare Workers.
6. **High Availability & Disaster Recovery**: Multi-Region Active-Active, Active-Passive warm standby, and Pilot Light failover.
7. **Specialized Compute Fabrics**: Mobile notification backends and GPU-accelerated AI model inference clusters.

---

## Directory Contents
- [`single-server.md`](./single-server.md) — Single node / low-complexity baseline topology.
- [`three-tier.md`](./three-tier.md) — Classic web, application, and database tier separation.
- [`vm-based.md`](./vm-based.md) — Multi-AZ Auto-Scaling Group with private database subnets.
- [`containerized.md`](./containerized.md) — Managed container runtimes (AWS ECS / Google Cloud Run).
- [`kubernetes.md`](./kubernetes.md) — Production Kubernetes cluster topology across Availability Zones.
- [`serverless.md`](./serverless.md) — Pure serverless event-driven architecture.
- [`hybrid-cloud.md`](./hybrid-cloud.md) — On-premises data center to cloud private connectivity.
- [`multi-region.md`](./multi-region.md) — Global multi-region routing with Anycast DNS.
- [`active-active.md`](./active-active.md) — Multi-region Active-Active data synchronization and conflict resolution.
- [`active-passive.md`](./active-passive.md) — Warm standby failover topology.
- [`disaster-recovery.md`](./disaster-recovery.md) — Pilot Light and cold backup recovery topologies.
- [`edge.md`](./edge.md) — Edge compute, CDN caching, and local termination.
- [`mobile-backend.md`](./mobile-backend.md) — Mobile API gateway, push notification hubs, and sync services.
- [`ai-platform.md`](./ai-platform.md) — GPU inference node pools, model artifact stores, and vector search nodes.
- [`template.md`](./template.md) — Copy-pasteable deployment starter templates.
- [`checklists.md`](./checklists.md) — Production deployment review checklist.
