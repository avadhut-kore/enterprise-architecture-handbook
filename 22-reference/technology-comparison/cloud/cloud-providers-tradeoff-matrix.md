# Technology Comparison: Cloud Providers Trade-Off Matrix

## Executive Summary
This reference matrix evaluates the architectural trade-offs between aws vs azure vs gcp.

---

## Architectural Comparison Matrix

| Dimension | Amazon Web Services (AWS) | Microsoft Azure | Google Cloud Platform (GCP) |
| :--- | :--- | :--- | :--- |
| **Enterprise Sweet Spot** | Deepest microservices & broad IaaS | Windows/SQL licensing & Entra ID | Big Data (BigQuery) & K8s (GKE) |
| **Networking Topology** | Regional VPCs with Transit Gateway | Regional VNets with Virtual WAN | Natively Global VPC across all regions |
| **Container Gold Standard**| EKS + Karpenter | AKS + Azure CNI Overlay | GKE Autopilot (Zero-node management) |
| **Cost Optimization** | Graviton ARM64 (40% discount) | Azure Hybrid Benefit (EA discounts) | Custom VM sizing & GCS Autoclass |
