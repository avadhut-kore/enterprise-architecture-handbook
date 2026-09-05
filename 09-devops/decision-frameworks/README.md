# Master Catalog of 21 DevOps Decision Frameworks

Objective, multi-criteria trade-off evaluations for high-consequence enterprise DevOps choices.

---

### 1. Kubernetes vs Managed Containers (AWS ECS / Cloud Run)
- Choose **Managed Containers** if team size is < 20 engineers and workloads are standard HTTP APIs.
- Choose **Kubernetes** if building an internal platform, requiring cross-cloud portability, or operating complex custom operators.

### 2. Kubernetes vs Serverless (AWS Lambda)
- Choose **Serverless** for event-driven, spiky, or low-frequency batch execution with zero baseline compute cost.
- Choose **Kubernetes** for steady-state, high-throughput, memory-intensive, or multi-tenant workloads.

### 3. Container vs Virtual Machine (VM)
- Choose **Containers** for cloud-native microservices, fast autoscaling, and high-density bin packing.
- Choose **VMs** for legacy stateful monoliths, custom kernel drivers, or compliance requiring strict hardware virtualization.

### 4. Terraform vs Native Cloud IaC (CloudFormation / Bicep)
- Choose **Terraform** for multi-cloud parity, open ecosystem modules, and unified enterprise governance.
- Choose **Native Cloud IaC** if operating exclusively in a single cloud with Day-0 support for newest cloud services.

### 5. Terraform vs Ansible
- Use **Terraform** for provisioning cloud API infrastructure (declarative, state-tracked).
- Use **Ansible** for in-guest OS configuration, package installation, and network device management.

### 6. GitHub Enterprise vs GitLab Ultimate
- Choose **GitHub** for developer ecosystem adoption, modern Actions marketplace, and best-of-breed toolchains.
- Choose **GitLab** for self-hosted sovereign air-gapped environments and unified single-pane compliance.

### 7. Monorepo vs Polyrepo
- Choose **Monorepo** for tightly coupled services, shared TypeScript types, and atomic cross-service refactorings.
- Choose **Polyrepo** for autonomous cross-functional squads operating polyglot stacks with decoupled release cycles.

### 8. GitFlow vs Trunk-Based Development
- Choose **Trunk-Based** for Continuous Delivery, microservices, and high-frequency deployment cultures.
- Choose **GitFlow** for packaged software supporting multiple active release versions simultaneously.

### 9. Push vs Pull Deployment
- Choose **Pull (GitOps)** for Kubernetes clusters to eliminate external cluster admin keys and enforce drift correction.
- Choose **Push** for serverless functions, static CDNs, and simple single-VM deployments.

### 10. GitOps vs Traditional CI/CD
- Choose **GitOps** for declarative infrastructure and multi-cluster Kubernetes synchronization.
- Choose **Traditional CI/CD** for non-Kubernetes workloads or workflows requiring imperative step orchestrations.

### 11. Blue/Green vs Canary Deployment
- Choose **Blue/Green** when rollbacks must be instantaneous (< 5s) and database schemas tolerate version coexistence.
- Choose **Canary** for high-volume traffic where small sample blast radiuses reveal latent production anomalies.

### 12. Self-Hosted CI vs Managed Cloud CI
- Choose **Self-Hosted (ARC on K8s)** when accessing private VPC databases or managing massive CI compute volume.
- Choose **Managed Cloud CI** for low operational maintenance and zero infrastructure overhead.

### 13. Central CI Platform vs Team-Owned Pipelines
- Choose **Central Golden Platform** with parameterized inheritance to enforce corporate security standards.

### 14. Centralized Platform Team vs Decentralized DevOps
- Choose **Central Platform + Embedded Champions** for optimal balance of corporate consistency and local autonomy.

### 15. Platform Engineering vs Traditional DevOps
- Adopt **Platform Engineering** when organization exceeds 100 engineers to eliminate ticket queues via self-service APIs.

### 16. Build vs Buy Developer Portal (Backstage vs Commercial SaaS)
- Choose **Backstage (Build/Extend)** for deep enterprise customization and private cloud integration.
- Choose **Commercial SaaS (Port / Cortex)** for rapid 30-day time to value without managing a TypeScript portal codebase.

### 17. Central Artifact Registry vs Distributed Multi-Region Registries
- Use a **Central Registry with Local Read-Through Caching Mirrors** to eliminate cross-region egress costs.

### 18. Shared Multi-Tenant Cluster vs Dedicated Cluster per Team
- Use **Dedicated Clusters per Environment (Dev, Stage, Prod)** and **Shared Multi-Tenant Clusters with strict namespaces/quotas per domain**.

### 19. Single Cluster vs Multi-Cluster
- Avoid single mega-clusters for production enterprise; use multi-cluster topologies to isolate failure blast radius.

### 20. Single-Region vs Multi-Region Delivery
- Use **Single-Region Multi-AZ** for standard enterprise workloads; use **Multi-Region Active-Active** only for mission-critical disaster resilience.

### 21. Immutable Infrastructure vs Mutable In-Place Patching
- Always enforce **Immutable Infrastructure** in the cloud: deploy fresh AMIs/containers and decommission old ones.

## Related Resources
- [DevOps Anti-Patterns](../devops-anti-patterns/README.md)
- [Reference Architectures](../reference-architectures/README.md)
