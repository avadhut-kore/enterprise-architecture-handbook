# Workload Abstractions Architecture

Mapping enterprise business requirements to the correct Kubernetes workload primitives.

## 1. Workload Primitives Selection Guide

| Primitive | Primary Purpose | Lifecycle Semantics | Statefulness |
| :--- | :--- | :--- | :--- |
| **Deployment** | Stateless web services and APIs. | Rolling updates, declarative replica scaling. | Stateless (Replaced freely). |
| **StatefulSet** | Databases, Kafka brokers, Elasticsearch nodes. | Stable network IDs (`pod-0, pod-1`), ordered graceful rollout/down. | Stateful (Dedicated PersistentVolume per pod). |
| **DaemonSet** | Node-level agents (Logging, Monitoring, Security, CNI).| Exactly one pod per matching node in the cluster. | Node-bound. |
| **Job / CronJob** | Batch processing, database migrations, scheduled cleanups. | Runs to completion (`exit 0`); terminates. | Ephemeral. |

## 2. Ingress vs Gateway API
- **Ingress**: Legacy HTTP(S) routing specification; limited support for advanced traffic splitting, header rewrites, and multi-team ownership.
- **Gateway API**: Modern role-oriented routing specification separating Infrastructure Providers, Cluster Operators (`Gateway`), and Application Developers (`HTTPRoute`).

## Related Resources
- [Kubernetes Control Plane](./kubernetes-architecture-and-control-plane.md)
- [Helm Architecture](../helm/README.md)
