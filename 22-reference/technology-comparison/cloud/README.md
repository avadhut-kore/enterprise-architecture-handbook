# Cloud Technology Trade-Off Comparisons (`22-reference/technology-comparison/cloud/`)

## Overview

This directory provides multidimensional comparative decision matrices evaluating competing architectural choices in enterprise cloud computing.

---

## Comparative Matrices

| Decision Domain | Comparison Document | Primary Architectural Trade-off |
| :--- | :--- | :--- |
| **Cloud Provider Selection** | [`cloud-providers-tradeoff-matrix.md`](cloud-providers-tradeoff-matrix.md) | AWS (microservices breadth) vs Azure (enterprise licensing) vs GCP (data & K8s) |
| **Cloud Strategy** | [`cloud-strategy-tradeoff-matrix.md`](cloud-strategy-tradeoff-matrix.md) | Single-Cloud Specialization vs Multi-Cloud Diversification |
| **Compute Execution Model** | [`compute-platforms-tradeoff-matrix.md`](compute-platforms-tradeoff-matrix.md) | VMs vs Containers on K8s vs Serverless Containers vs FaaS |
| **Database Hosting** | [`database-hosting-tradeoff-matrix.md`](database-hosting-tradeoff-matrix.md) | Managed Cloud Database (Aurora/Cloud SQL) vs Self-Managed on IaaS |
| **High Availability Topology** | [`high-availability-tradeoff-matrix.md`](high-availability-tradeoff-matrix.md) | Active-Passive (Warm Standby) vs Active-Active (Bi-Directional) |
| **Infrastructure as Code** | [`infrastructure-as-code-tradeoff-matrix.md`](infrastructure-as-code-tradeoff-matrix.md) | Terraform / OpenTofu vs Cloud-Native IaC (Bicep / CloudFormation) |
| **Cloud Migration Strategy** | [`migration-pathways-tradeoff-matrix.md`](migration-pathways-tradeoff-matrix.md) | Rehost (Lift & Shift) vs Replatform (Lift & Reshape) vs Refactor (Rewrite) |
| **Platform Operating Model** | [`platform-operating-models-tradeoff-matrix.md`](platform-operating-models-tradeoff-matrix.md) | Centralized Platform (Golden Paths) vs Team-Owned Decentralized Infra |
| **Regional Resiliency** | [`regional-resiliency-tradeoff-matrix.md`](regional-resiliency-tradeoff-matrix.md) | Single Region Multi-AZ vs Multi-Region Active-Passive vs Active-Active |
| **Storage Paradigms** | [`storage-paradigms-tradeoff-matrix.md`](storage-paradigms-tradeoff-matrix.md) | Block Storage (EBS) vs File Storage (EFS) vs Object Storage (S3/Blob) |
