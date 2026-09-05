# Kubernetes RBAC & Service Account Governance

## Executive Summary

Kubernetes Role-Based Access Control (RBAC) regulates which users and service accounts can perform actions (`get`, `list`, `watch`, `create`, `update`, `delete`) on cluster resources.

---

## 1. Architectural Guardrails
1. **Ban Wildcards**: Never permit `verbs: ["*"]` or `resources: ["*"]` in Role specifications.
2. **Disable Automatic Token Mounting**: Configure `automountServiceAccountToken: false` on pods that do not interact with the Kubernetes API server.
3. **Namespace-Scoped Roles**: Use `Role` and `RoleBinding` bound to specific application namespaces; restrict `ClusterRoleBinding` strictly to platform-level operators.
