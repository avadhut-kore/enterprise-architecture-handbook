# Architecture Reference (`22-reference/`)

## Executive Summary

The `22-reference/` directory contains curated dictionaries, acronym definitions, technology comparison matrices, and architectural trade-off evaluations across enterprise computing disciplines.

---

## 1. Glossaries & Terminology
* [`glossaries/architecture-glossary.md`](glossaries/architecture-glossary.md) - Comprehensive terminology definitions for enterprise, system, and cloud architecture.
* [`acronyms/architecture-acronyms.md`](acronyms/architecture-acronyms.md) - Standard industry acronym definitions (ADR, CCOE, CSPM, CNI, CSI, Egress, FinOps, IdP, RTO, RPO, SCP, VPC, vWAN).

---

## 2. Technology & Architectural Trade-off Matrices (`technology-comparison/`)

Rigorous, multidimensional comparative analysis evaluating competing platforms, architectures, and design approaches.

### Cloud & Infrastructure Comparisons (`technology-comparison/cloud/`)
* [`cloud-providers-tradeoff-matrix.md`](technology-comparison/cloud/cloud-providers-tradeoff-matrix.md) - AWS vs Azure vs GCP across enterprise strengths, networking, and pricing models.
* [`cloud-strategy-tradeoff-matrix.md`](technology-comparison/cloud/cloud-strategy-tradeoff-matrix.md) - Single-Cloud Specialization vs Multi-Cloud Diversification.
* [`compute-platforms-tradeoff-matrix.md`](technology-comparison/cloud/compute-platforms-tradeoff-matrix.md) - VMs vs Kubernetes vs Serverless Containers vs FaaS.
* [`database-hosting-tradeoff-matrix.md`](technology-comparison/cloud/database-hosting-tradeoff-matrix.md) - Managed Cloud Databases (Aurora, Cloud SQL) vs Self-Managed on IaaS.
* [`high-availability-tradeoff-matrix.md`](technology-comparison/cloud/high-availability-tradeoff-matrix.md) - Active-Passive (Warm Standby) vs Active-Active (Bi-Directional).
* [`infrastructure-as-code-tradeoff-matrix.md`](technology-comparison/cloud/infrastructure-as-code-tradeoff-matrix.md) - Terraform / OpenTofu vs Cloud-Native IaC (Bicep, CloudFormation).
* [`migration-pathways-tradeoff-matrix.md`](technology-comparison/cloud/migration-pathways-tradeoff-matrix.md) - Rehost (Lift & Shift) vs Replatform (Lift & Reshape) vs Refactor (Cloud-Native Rewrite).
* [`platform-operating-models-tradeoff-matrix.md`](technology-comparison/cloud/platform-operating-models-tradeoff-matrix.md) - Centralized Platform (Golden Paths) vs Team-Owned Infrastructure.
* [`regional-resiliency-tradeoff-matrix.md`](technology-comparison/cloud/regional-resiliency-tradeoff-matrix.md) - Single Region Multi-AZ vs Multi-Region Active-Passive vs Multi-Region Active-Active.
* [`storage-paradigms-tradeoff-matrix.md`](technology-comparison/cloud/storage-paradigms-tradeoff-matrix.md) - Block Storage vs File Storage vs Object Storage.

### Data & Integration Comparisons (`technology-comparison/data-integration/`)
* Comparative matrices for [Database Engines](technology-comparison/data-integration/database-engines-comparison.md), [Messaging & Streaming](technology-comparison/data-integration/messaging-and-streaming-comparison.md), [API Protocols](technology-comparison/data-integration/api-protocols-comparison.md), [Data Platforms](technology-comparison/data-integration/data-platforms-comparison.md), [Integration Topologies](technology-comparison/data-integration/enterprise-integration-topologies-comparison.md), and [Reconciliation Approaches](technology-comparison/data-integration/financial-reconciliation-approaches-comparison.md).

### Application Architecture Comparisons (`technology-comparison/application-architecture/`)
* Comparative matrices for [Backend Frameworks](technology-comparison/application-architecture/backend-frameworks-comparison.md), [Frontend Frameworks](technology-comparison/application-architecture/frontend-frameworks-comparison.md), [Mobile Frameworks](technology-comparison/application-architecture/mobile-frameworks-comparison.md), [State Management](technology-comparison/application-architecture/state-management-comparison.md), [ORM/Data Access](technology-comparison/application-architecture/orm-data-access-comparison.md), and [Testing Frameworks](technology-comparison/application-architecture/testing-frameworks-comparison.md).
