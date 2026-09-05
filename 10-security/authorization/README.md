# Authorization Systems Architecture (`authorization/`)

## Executive Summary

While authentication verifies identity, authorization answers: **"Is this authenticated identity permitted to execute action $A$ on resource $R$ under environment context $C$?"**

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`authorization-paradigms.md`](authorization-paradigms.md) | Paradigms | RBAC vs ABAC vs ReBAC vs PBAC |
| [`fine-grained-authorization.md`](fine-grained-authorization.md) | Policy as Code | Open Policy Agent (OPA), Google Zanzibar, Cedar |
| [`resource-based-authorization.md`](resource-based-authorization.md) | Resource Scoping | Multi-tenant isolation, row-level security, tenant ACLs |
