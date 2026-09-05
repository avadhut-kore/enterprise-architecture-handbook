# GitOps Architecture and Reconciliation

Traditional CI/CD uses "Push Deployment": a CI runner with cluster admin credentials connects directly to Kubernetes and executes `kubectl apply`. GitOps inverts this paradigm to "Pull-Based Reconciliation".

## 1. Push vs Pull Deployment Models

```
TRADITIONAL PUSH DEPLOYMENT:
[Git Commit] ──► [CI Server] ──► (Holds Cluster Admin Keys) ──► PUSH to K8s Cluster
Risk: CI server compromise grants full cluster root access; external drifts overwritten or ignored.

GITOPS PULL DEPLOYMENT:
[Git Commit] ◄────── RECONCILIATION LOOP ──────► [GitOps Controller (ArgoCD)]
(Source of Truth)                                 (Runs INSIDE K8s Cluster)
                                                           │
                                                           ▼
                                                Synchronizes Actual Cluster State
Advantage: Zero cluster credentials stored outside; automated drift detection and self-healing.
```

## 2. Core GitOps Invariants
1. **Declarative Target State**: Entire environment described declaratively (YAML/Kustomize/Helm) in Git.
2. **Automated State Pulling**: The cluster operator continually compares desired Git state against actual live cluster state.
3. **Self-Healing Drift Mitigation**: If an operator manually edits a deployment via `kubectl edit`, the GitOps controller immediately detects the drift and reverts it back to Git state.

## Related Resources
- [Kubernetes Architecture](../kubernetes/README.md)
- [Helm Architecture](../helm/README.md)
