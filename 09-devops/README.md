# DevOps Architecture & Engineering

Welcome to the **DevOps Architecture & Engineering** operating system of the Enterprise Architecture Handbook.

This knowledge domain treats DevOps not as a collection of disjointed tools (Docker, Kubernetes, Jenkins), but as a holistic socio-technical capability:

$$\text{DevOps} = \text{People} + \text{Process} + \text{Technology} + \text{Automation} + \text{Security} + \text{Operations} + \text{Governance} + \text{Measurement}$$

The central thesis of enterprise DevOps is:
> **"DevOps is a system for delivering and operating software safely, repeatedly, quickly, and sustainably."**

Architecture decisions must always flow from business objectives down to technical execution:
$$\text{Business Needs} \to \text{Delivery Needs} \to \text{Operational Needs} \to \text{Security Mandates} \to \text{Constraints} \to \text{Options} \to \text{Decision} \to \text{Implementation} \to \text{Operations}$$

---

## 1. Domain Navigation Index

| Domain Area | Key Focus Areas | Subdirectory Link |
| :--- | :--- | :--- |
| **Foundations & Maturity** | What DevOps is/isn't, Dev vs Ops, CALMS, Lifecycle, Capability Taxonomy, 6-Level Maturity Model | [devops-foundations/](./devops-foundations/), [devops-maturity/](./devops-maturity/) |
| **Source Control & Git** | Git internals, Trunk-Based vs GitFlow, Monorepo vs Polyrepo, GitHub Enterprise, GitLab, Governance | [git/](./git/), [github/](./github/), [gitlab/](./gitlab/), [source-control-governance/](./source-control-governance/) |
| **CI/CD Architecture** | Pipeline orchestration, caching, reusable workflows, golden pipelines, 10 language reference pipelines | [ci-cd/](./ci-cd/) |
| **Release & Deployments** | Release trains, SemVer, 9 deployment strategies (Blue/Green, Canary, Progressive), Environments, Artifacts | [release-engineering/](./release-engineering/), [deployment-strategies/](./deployment-strategies/), [artifact-management/](./artifact-management/) |
| **Containers & Orchestration**| Docker multi-stage & distroless, Kubernetes production architecture, multi-cluster, Helm governance | [docker/](./docker/), [kubernetes/](./kubernetes/), [helm/](./helm/) |
| **IaC, GitOps & Automation** | Terraform state & enterprise modules, Ansible, GitOps (ArgoCD/Flux), Policy as Code (OPA), IaC Testing | [infrastructure-as-code/](./infrastructure-as-code/), [terraform/](./terraform/), [ansible/](./ansible/), [gitops/](./gitops/), [policy-as-code/](./policy-as-code/) |
| **DevSecOps & Supply Chain** | Shift-left security gates, Vault secrets, SLSA Framework, SBOM, OIDC workload identity, Compliance | [devsecops/](./devsecops/), [secrets-management/](./secrets-management/), [software-supply-chain/](./software-supply-chain/), [compliance/](./compliance/) |
| **Platform Engineering** | Platform as a Product, Internal Developer Platform (IDP / Backstage), Golden Paths, DevEx, Economics | [platform-engineering/](./platform-engineering/), [developer-experience/](./developer-experience/), [platform-economics/](./platform-economics/) |
| **Specialized Delivery** | Mobile CI/CD (Fastlane), Database DevOps (zero-downtime migrations), MLOps, LLMOps/AIOps | [mobile-devops/](./mobile-devops/), [database-devops/](./database-devops/), [mlops/](./mlops/), [aiops/](./aiops/) |
| **Operations & Resilience** | DORA metrics, DevOps FinOps, 15 failure modes post-mortems, Red-teaming, DevOps platform DR | [devops-metrics/](./devops-metrics/), [devops-economics/](./devops-economics/), [failure-engineering/](./failure-engineering/), [disaster-recovery/](./disaster-recovery/) |
| **Catalogs & Checklists** | 30+ Anti-Patterns, 21 Decision Matrices, 20 Reference Architectures, 20 Case Studies, 20 Checklists | [devops-anti-patterns/](./devops-anti-patterns/), [decision-frameworks/](./decision-frameworks/), [reference-architectures/](./reference-architectures/), [case-studies/](./case-studies/), [checklists/](./checklists/) |

---

## 2. Core Architectural Tenets

1. **No Technology-First Dogma**: We do not start with *"Use Kubernetes"* or *"Use Microservices"*. We analyze constraints, scale, and team capabilities first.
2. **Build Once, Promote Everywhere**: Binaries and container images are built exactly once, cryptographically signed, and promoted through immutable staging gates.
3. **Paved Roads, Not Paved Prisons**: Platforms provide friction-free golden paths with self-service autonomy, allowing specialized opt-outs when business context dictates.
4. **Resilience Over Velocity**: Speed without automated verification, canary progression, and instant rollback capability is recklessness.
5. **Observability and Feedback**: Continuous production telemetry feeds directly back into developer backlogs and architectural fitness functions.

---

## 3. Cross-Phase Integration

- [Phase 3: System Design & Distributed Systems](../02-system-design/README.md) — Scalability, reliability, and failure mitigation.
- [Phase 4: Application Engineering](../03-backend/README.md) — Polyglot runtimes (.NET, Java, Python, Node, Frontend, Mobile).
- [Phase 5: Data & Integration Architecture](../06-data/README.md) — Database migrations, streaming pipelines, and messaging fabrics.
- [Phase 6: Cloud Architecture & FinOps](../08-cloud/README.md) — Multi-cloud infrastructure, networking, and cloud unit economics.
- [Phase 7: Security & Zero Trust Architecture](../10-security/README.md) — Threat modeling, IAM, encryption, and vulnerability management.
- [Phase 8: AI & Modern Architecture](../12-ai/README.md) — MLOps, LLMOps, vector mesh, and agentic workflows.
- [Phase 9: Enterprise Architecture](../09-enterprise-architecture/README.md) — Business capability mapping, portfolio management, and IT governance.
- [Phase 10: Architect Mastery](../10-architect-mastery/README.md) — Executive communication, trade-offs, and master decision frameworks.
- [Phase 11: Observability & SRE](../11-observability/README.md) — SLOs, Error budgets, incident command, and telemetry.
