# GCP Kubernetes Architecture: Google Kubernetes Engine (GKE)

## Executive Summary

Google Kubernetes Engine (GKE) is the industry benchmark for managed Kubernetes. At enterprise scale, **GKE Autopilot** eliminates node-level maintenance by managing node provisioning, hardening, and scaling automatically.

---

## 1. GKE Autopilot vs GKE Standard

| Architectural Dimension | GKE Autopilot (Recommended Standard) | GKE Standard |
| :--- | :--- | :--- |
| **Node Management** | Fully managed by Google SRE; no worker nodes in customer view | Customer provisions and patches node pools |
| **Security Hardening** | Pre-hardened according to CIS benchmarks; Pod Security Standards enforced | Customer responsible for OS hardening, kernel patches, and CIS compliance |
| **Billing Model** | Pay exclusively for CPU, memory, and storage requested by running pods | Pay for underlying physical GCE virtual machine capacity |
| **Node Autoscaling** | Automatic, seamless pod-level bin-packing | Requires tuning Cluster Autoscaler or open-source autoscalers |

---

## 2. Multi-Cluster Ingress & Fleet Management

Enterprise GKE architectures organize clusters into **Fleets**:
- **Multi-Cluster Services (MCS)**: Cross-cluster service discovery allowing pods in `cluster-us` to call pods in `cluster-eu` via private internal DNS names (`myservice.mynamespace.svc.clusterset.local`).
- **Multi-Cluster Ingress (MCI)**: Deploys a global Cloud Load Balancer that routes external traffic across multiple GKE clusters worldwide based on geographic proximity and backend capacity.
