# Helm Architecture and Chart Governance

Helm parameterizes raw Kubernetes manifests, enabling reproducible deployments across heterogeneous environments (Dev, Staging, Production).

## 1. Chart Structure & Values Hierarchy

```
my-service/
├── Chart.yaml              # Chart metadata & version
├── values.yaml             # Default configuration values
├── values-dev.yaml         # Dev environment overrides (small replicas)
├── values-prod.yaml        # Prod environment overrides (high replicas, strict PDB)
└── templates/
    ├── deployment.yaml
    ├── service.yaml
    ├── hpa.yaml
    └── _helpers.tpl        # Reusable Go template helper functions
```

## 2. Helm vs Kustomize: Architectural Trade-Off
- **Helm**: Parameterized templating with logic (`if`, `range`, functions). Ideal for third-party packaged software and complex variable substitution.
- **Kustomize**: Pure template-free declarative patching. Ideal for internal application configuration overlays without learning Go templating.
- **Hybrid Best Practice**: Use Helm to package application charts; use Kustomize / ArgoCD to apply environment-specific patches without modifying the base chart.

## Related Resources
- [Kubernetes Workloads](../kubernetes/workload-abstractions-architecture.md)
- [GitOps Architecture](../gitops/README.md)
