# DevOps Reference Architectures (REF-DEV-01 to REF-DEV-20)

This directory contains the capstone library of 20 enterprise DevOps reference architectures, structured across standardized 16-section blueprints.

## Catalog Index

| ID | Title | Domain Focus | Link |
| :--- | :--- | :--- | :--- |
| **REF-DEV-01** | Standard Enterprise CI/CD Platform | Unified delivery pipeline with multi-stage quality gates and immutable OCI promotion. | [ref-dev-01-enterprise-cicd.md](./ref-dev-01-enterprise-cicd.md) |
| **REF-DEV-02** | Cloud-Native Serverless CI/CD Pipeline | Event-driven serverless delivery utilizing AWS Step Functions, CodeDeploy canaries, and Lambda. | [ref-dev-02-serverless-cicd.md](./ref-dev-02-serverless-cicd.md) |
| **REF-DEV-03** | Kubernetes GitOps Delivery Platform (ArgoCD) | Pull-based declarative reconciliation, multi-repo synchronization, and self-healing drift mitigation. | [ref-dev-03-kubernetes-gitops.md](./ref-dev-03-kubernetes-gitops.md) |
| **REF-DEV-04** | Multi-Cluster Progressive Delivery Platform | Canary traffic shifting with automated metric analysis via Argo Rollouts, Prometheus, and Envoy. | [ref-dev-04-progressive-delivery.md](./ref-dev-04-progressive-delivery.md) |
| **REF-DEV-05** | Enterprise DevSecOps Pipeline & Security Gates | Shift-left integration of SAST, SCA, Trivy container scanning, and Cosign keyless image signing. | [ref-dev-05-enterprise-devsecops.md](./ref-dev-05-enterprise-devsecops.md) |
| **REF-DEV-06** | Global OCI Artifact & Container Registry Platform | Cross-region geo-replicated container registry with immutable retention and vulnerability caching. | [ref-dev-06-global-artifact-registry.md](./ref-dev-06-global-artifact-registry.md) |
| **REF-DEV-07** | Enterprise Container Platform (Hardened Base Images) | Automated base image factory building distroless, non-root, CVE-remediated golden containers. | [ref-dev-07-hardened-container-platform.md](./ref-dev-07-hardened-container-platform.md) |
| **REF-DEV-08** | Internal Developer Platform (Backstage + Golden Paths) | Self-service developer portal with automated microservice scaffolding and platform APIs. | [ref-dev-08-internal-developer-platform.md](./ref-dev-08-internal-developer-platform.md) |
| **REF-DEV-09** | Multi-Team Federated Platform Engineering Topology | Central platform team providing core primitives; federated domain teams owning golden workflows. | [ref-dev-09-federated-platform-topology.md](./ref-dev-09-federated-platform-topology.md) |
| **REF-DEV-10** | Multi-Cloud DevOps & IaC Automation Platform | Terraform and GitHub Actions pipeline orchestrating workloads across AWS, Azure, and GCP. | [ref-dev-10-multicloud-devops-platform.md](./ref-dev-10-multicloud-devops-platform.md) |
| **REF-DEV-11** | Regulated Banking & FinTech CI/CD Platform (DORA/PCI) | Separation of duties, cryptographic WORM audit logs, automated compliance, and dual approvals. | [ref-dev-11-regulated-banking-cicd.md](./ref-dev-11-regulated-banking-cicd.md) |
| **REF-DEV-12** | Global Active-Active Deployment Pipeline | Synchronized progressive rollouts across 3 continental regions with automated health circuit breaking. | [ref-dev-12-global-active-active-pipeline.md](./ref-dev-12-global-active-active-pipeline.md) |
| **REF-DEV-13** | Enterprise Monorepo CI/CD Platform (Nx/Turborepo) | Affected project graph calculation, remote build caching, and sharded parallel test execution. | [ref-dev-13-monorepo-cicd-platform.md](./ref-dev-13-monorepo-cicd-platform.md) |
| **REF-DEV-14** | Microservices Polyrepo Delivery Platform | Centralized reusable pipeline inheritance across 500+ microservice repositories. | [ref-dev-14-polyrepo-microservices-delivery.md](./ref-dev-14-polyrepo-microservices-delivery.md) |
| **REF-DEV-15** | Event-Driven & Streaming Pipeline Deployment Mesh | Schema registry validation in CI/CD, backward compatibility gates, and Kafka stream deployment. | [ref-dev-15-event-driven-streaming-delivery.md](./ref-dev-15-event-driven-streaming-delivery.md) |
| **REF-DEV-16** | Modular Monolith Delivery & Extraction Pipeline | Enforcing strict compile-time module boundary tests (ArchUnit) with zero-downtime blue/green deployment. | [ref-dev-16-modular-monolith-delivery.md](./ref-dev-16-modular-monolith-delivery.md) |
| **REF-DEV-17** | Serverless Micro-Frontend Delivery Fabric | Independent frontend deployment using Cloudflare Workers / AWS CloudFront edge routing. | [ref-dev-17-serverless-microfrontend-fabric.md](./ref-dev-17-serverless-microfrontend-fabric.md) |
| **REF-DEV-18** | Enterprise MLOps & Feature Store Delivery Mesh | Continuous training (CT) pipeline, DVC data versioning, MLflow registry, and Triton model serving. | [ref-dev-18-enterprise-mlops-mesh.md](./ref-dev-18-enterprise-mlops-mesh.md) |
| **REF-DEV-19** | Enterprise Terraform Cloud Landing Zone Engine | Multi-account AWS Landing Zone automation with automated OPA policy checks and state locking. | [ref-dev-19-terraform-landing-zone-engine.md](./ref-dev-19-terraform-landing-zone-engine.md) |
| **REF-DEV-20** | Disaster-Resilient Self-Healing DevOps Infrastructure | High-availability Git mirrors, registry cross-replication, and automated cluster disaster recovery. | [ref-dev-20-resilient-devops-platform.md](./ref-dev-20-resilient-devops-platform.md) |
