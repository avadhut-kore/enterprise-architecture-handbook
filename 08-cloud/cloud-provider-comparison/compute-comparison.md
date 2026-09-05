# Compute & Container Architecture Comparison: AWS vs Azure vs GCP

## Executive Summary

Compute represents the primary execution engine and the largest line-item in enterprise cloud budgets. This document compares virtual machines, serverless containers, managed Kubernetes, and Function-as-a-Service (FaaS) across AWS, Azure, and GCP.

---

## 1. Virtual Machines (IaaS)

| Capability / Metric | AWS (EC2) | Microsoft Azure (VM) | Google Cloud (GCE) |
| :--- | :--- | :--- | :--- |
| **Hypervisor Engine** | AWS Nitro System (Dedicated ASIC/Card) | Azure Hyper-V / Custom DPU Offload | KVM on Google Borg Hardware |
| **ARM64 Processor** | AWS Graviton (Graviton2, Graviton3, Graviton4) | Ampere Altra ARM Processors | Tau T2A (Ampere Altra ARM) |
| **Machine Sizing** | Strict predefined instance families | Strict predefined instance sizes | **Custom Machine Types** (Mix any vCPU & RAM ratio) |
| **Temporary Compute** | Spot Instances (2-min notice) | Spot VMs (30-sec notice) | Spot VMs (30-sec notice) |
| **Architectural Verdict**| Industry benchmark for depth, Graviton price/performance, and specialized accelerators. | Seamless Windows Server & SQL Server licensing portability (Azure Hybrid Benefit). | Superior flexibility with custom sizing; fastest VM provisioning time. |

---

## 2. Serverless Containers & Managed PaaS

| Capability / Metric | AWS (ECS + Fargate) | Microsoft Azure (App Service) | Google Cloud (Cloud Run) |
| :--- | :--- | :--- | :--- |
| **Underlying Engine** | Firecracker MicroVMs on AWS Fargate | Azure Web Apps / App Service Plan | Knative on Google Borg |
| **Concurrency Model** | 1 Task = 1 Request/Job execution | Thread-based within fixed App Service Plan | **Up to 250 concurrent requests per single container** |
| **Cold Start Latency** | 30–60 seconds | Near-zero in pre-warmed tiers | 2–5 seconds from zero |
| **Scale to Zero** | Yes (via Service Application Auto Scaling) | Only in Consumption/Serverless tiers | **Native, instantaneous scale to zero** |
| **Architectural Verdict**| High enterprise stability; deep IAM and VPC integration. | Ideal for standard enterprise .NET/Java enterprise portals. | **Market leader in developer ergonomics, concurrency, and cold start performance.** |

---

## 3. Managed Kubernetes (EKS vs AKS vs GKE)

| Capability / Metric | Amazon EKS | Azure Kubernetes Service (AKS) | Google Kubernetes Engine (GKE) |
| :--- | :--- | :--- | :--- |
| **Control Plane SLA** | 99.95% ($0.10/hour per cluster) | 99.95% ($0.10/hour with SLA tier) | 99.95% ($0.10/hour, 1 free cluster per billing acct) |
| **Autopilot / Zero-Node**| None (Must manage node groups / Karpenter) | Limited preview / Virtual Nodes | **GKE Autopilot** (Gold standard automated node management) |
| **Node Autoscaler** | **Karpenter** (High-speed node binpacking) | Cluster Autoscaler / KEDA | GKE Cluster Autoscaler / Nap (Node Auto Provisioning) |
| **Networking Plugin** | AWS VPC CNI (IP allocation per ENI) | Azure CNI Overlay | GKE Dataplane V2 (eBPF Cilium native) |
| **Release Velocity** | Conservative; lags upstream Kubernetes | Fast; strong focus on enterprise tooling | **Fastest; upstream Kubernetes creators** |
