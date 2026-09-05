# Configuration Versioning & GitOps

## 1. GitOps for Configuration
Manage configuration repos separately from application code (e.g., in a central `infra-config` repo managed by ArgoCD or Flux). Every configuration change produces a Git commit hash, enabling instant rollbacks.
