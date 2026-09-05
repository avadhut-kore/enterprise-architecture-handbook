# Technology Comparison: Compute Platforms Trade-Off Matrix

## Executive Summary
This reference matrix evaluates the architectural trade-offs between vms vs containers on k8s vs serverless containers vs faas.

---

## Architectural Comparison Matrix

| Dimension | Virtual Machines | Kubernetes | Serverless Containers | Serverless FaaS |
| :--- | :--- | :--- | :--- | :--- |
| **Startup Time** | 30–90s | Sub-second (pre-warmed) | 2–5s | 50ms–5s (cold start) |
| **Runtime Control** | Full Root/Kernel | Pod Specs / Capabilities | Container Filesystem | Vendor Sandbox |
| **Scaling Speed** | Minutes | Seconds | Seconds | Milliseconds |
| **Cost at Idle** | High (24/7 VM) | Moderate (Worker nodes) | Zero (Scale to zero) | Zero |
| **Cost at Hyper-Scale** | Lowest per unit | Low (Spot/Binpacking) | Moderate | Highest per unit |
| **Ops Overhead** | High (OS Patching) | Extreme (K8s SRE) | Minimal | Minimal |
