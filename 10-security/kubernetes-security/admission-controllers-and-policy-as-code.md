# Validating Admission Controllers: Kyverno vs OPA Gatekeeper

## Executive Summary

Validating Admission Webhooks act as the gatekeeper for the Kubernetes API server, inspecting and rejecting non-compliant YAML manifests before they are persisted to etcd.

---

## 1. Comparison: Kyverno vs OPA Gatekeeper

| Dimension | Kyverno | OPA Gatekeeper |
| :--- | :--- | :--- |
| **Policy Language** | Pure Kubernetes YAML (Zero learning curve) | Rego (Domain-specific language) |
| **Mutation & Generation** | Native YAML mutation and resource generation | Supported via Assign/Modify CRDs |
| **Cross-Platform Fit** | Kubernetes-only | Universal (Cloud, CI/CD, Terraform, APIs) |
| **Enterprise Standard** | Ideal for Kubernetes-focused platform teams | Ideal for multi-layer enterprise policy governance |
