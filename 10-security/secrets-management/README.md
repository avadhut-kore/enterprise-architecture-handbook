# Secrets Management Architecture (`secrets-management/`)

## Executive Summary

Secrets management governs the storage, dynamic injection, and automated rotation of operational credentials (database passwords, API tokens, TLS certificates).

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`secrets-management-architecture.md`](secrets-management-architecture.md) | Secrets Strategy | Centralized secret stores vs distributed configuration |
| [`hashicorp-vault-architecture.md`](hashicorp-vault-architecture.md) | Enterprise Vault | Dynamic database credentials, AppRole, Kubernetes auth |
| [`external-secrets-operator-eso.md`](external-secrets-operator-eso.md) | K8s Synchronization | Syncing cloud secrets to Kubernetes in-memory secrets |
| [`secrets-anti-patterns.md`](secrets-anti-patterns.md) | Anti-Patterns | Secrets in Git, hardcoded tokens, container env leakage |
