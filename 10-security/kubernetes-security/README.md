# Kubernetes Security Architecture (`kubernetes-security/`)

## Executive Summary

Kubernetes security encompasses control plane hardening, worker node isolation, RBAC least privilege, declarative network policies, admission control, and runtime workload protection.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`kubernetes-security-architecture.md`](kubernetes-security-architecture.md) | Platform Hardening | Control plane API server flags, etcd encryption at rest |
| [`kubernetes-rbac-and-service-accounts.md`](kubernetes-rbac-and-service-accounts.md) | RBAC Governance | Least-privilege roles, banning cluster-admin, namespace scoping |
| [`pod-security-standards-pss.md`](pod-security-standards-pss.md) | Pod Standards | Privileged vs Baseline vs Restricted standards |
| [`kubernetes-network-policies.md`](kubernetes-network-policies.md) | East-West Isolation | Default deny-all ingress/egress, Cilium eBPF policies |
| [`admission-controllers-and-policy-as-code.md`](admission-controllers-and-policy-as-code.md) | Policy as Code | Kyverno and OPA Gatekeeper validating admission webhooks |
| [`secrets-in-kubernetes.md`](secrets-in-kubernetes.md) | K8s Secrets | External Secrets Operator (ESO), HashiCorp Vault Agent |
