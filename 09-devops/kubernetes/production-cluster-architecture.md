# Production Kubernetes Cluster Architecture

Designing a mission-critical, enterprise-grade Kubernetes cluster for multi-zone resilience, security, and autoscaling.

## 1. The Production Baseline Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    MULTI-AZ KUBERNETES TOPOLOGY             │
├──────────────────────────────┬──────────────────────────────┤
│ AZ-1 (Virginia)              │ AZ-2 (Virginia)              │
│ - Control Plane Node 1 (etcd)│ - Control Plane Node 2 (etcd)│
│ - Worker Node Pool A         │ - Worker Node Pool B         │
│ - Ingress Controller Pod 1   │ - Ingress Controller Pod 2   │
├──────────────────────────────┴──────────────────────────────┤
│ AZ-3 (Virginia - Quorum Node)                               │
│ - Control Plane Node 3 (etcd) / Worker Node Pool C          │
└─────────────────────────────────────────────────────────────┘
```

## 2. Critical Production Guardrails
1. **Pod Disruption Budgets (PDB)**: Enforce minimum available pods during cluster upgrades (`minAvailable: 1` or `maxUnavailable: 25%`).
2. **Resource Requests & Limits**: Never deploy pods without memory/CPU requests and limits. Set `memory requests == memory limits` to prevent unpredictable OOM eviction.
3. **Autoscaling (Karpenter / KEDA)**: Use event-driven autoscaling (KEDA) based on queue depth rather than CPU thresholds alone. Leverage Karpenter for rapid (sub-minute) node provisioning.
4. **Network Policies**: Default-deny all inter-namespace traffic; explicitly whitelist legitimate service-to-service communication.

## Related Resources
- [Multi-Cluster Architecture](./multi-cluster-architecture.md)
- [Kubernetes Decision Framework](./kubernetes-decision-framework.md)
