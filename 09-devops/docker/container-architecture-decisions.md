# Container Architecture Decision Framework

Architectural evaluation for container deployment, runtime selection, and image archetypes.

## 1. Container vs VM vs Serverless

| Dimension | Virtual Machines (VMs) | Containers (Docker/K8s) | Serverless (Lambda/Cloud Run) |
| :--- | :--- | :--- | :--- |
| **Isolation Level** | Hardware / Hypervisor (Highest security) | OS Kernel Namespaces (Shared kernel) | MicroVM / Sandboxed Container |
| **Startup Time** | 30 - 120 seconds | 0.5 - 3 seconds | 0.05 - 0.5 seconds (Cold starts) |
| **Operational Overhead**| High (OS patching, kernel upgrades) | Moderate (Base image updates, K8s ops)| Minimal (Cloud vendor manages infrastructure) |
| **Stateful Workloads** | Native & Simple | Moderate (CSI / PersistentVolumes) | Unsuitable (Stateless ephemeral compute) |
| **Cost Profile** | Continuous fixed cost | Elastic node pool / fixed baseline | Pure pay-per-execution consumption |

## 2. Distroless vs Alpine vs Full OS (Debian/Ubuntu)
- **Distroless**: Highest security, zero package managers, difficult to debug interactively in dev.
- **Alpine**: Extremely small (~5MB), but uses `musl libc` instead of `glibc`, which can introduce cryptic memory allocation bugs in C-extensions (Python/Node).
- **Slim Debian/Ubuntu**: Safest general compatibility, larger image size (~70MB), requires active CVE scanning.

## Related Resources
- [Kubernetes Decision Framework](../kubernetes/kubernetes-decision-framework.md)
- [Docker Hub](./README.md)
