# Serverless Containers: Cloud Run, Fargate & Container Apps

## Executive Summary

Serverless Containers bridge the gap between traditional FaaS and full Kubernetes orchestration. They execute standard Docker containers on demand without requiring virtual machine or cluster management.

---

## 1. Comparative Matrix

| Platform | Provider | Concurrency per Instance | Scale to Zero | Max Execution Duration |
| :--- | :--- | :---: | :---: | :--- |
| **Google Cloud Run** | Google Cloud | **Up to 250 requests** | **Yes** | Up to 60 minutes |
| **AWS Fargate** | AWS (ECS/EKS) | Task-level (Multi-thread) | Via Auto-Scaling | Unlimited (Runs as long as needed) |
| **Azure Container Apps** | Azure | Dynamic (KEDA-driven) | **Yes** | Unlimited (Background workers supported) |

---

## 2. The Architectural Winner: Serverless Containers

For 80% of modern enterprise microservices, **Serverless Containers represent the sweet spot**:
- **Zero Cluster Upgrades**: No etcd, CNI, or Kubernetes control plane lifecycles to manage.
- **High Concurrency**: A single Cloud Run container handles hundreds of concurrent connections, eliminating cold-start churn.
- **Standard Tooling**: Developers write standard Dockerfiles and test locally using Docker Desktop.
