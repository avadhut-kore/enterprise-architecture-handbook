# Identity Architecture (`10-security/identity/`)

## Executive Summary

Identity is the foundational control plane of modern enterprise architecture. In a perimeterless Zero Trust world, cryptographic identity answers the primary question: **"Who or what is making this request, and how is that identity mathematically proven?"**

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`identity-architecture.md`](identity-architecture.md) | Universal Identity | Human, machine, workload, and service identity |
| [`identity-lifecycle-management.md`](identity-lifecycle-management.md) | Lifecycle & Governance | Provisioning, deprovisioning, SCIM 2.0, audit reconciliation |
| [`workload-identity-federation.md`](workload-identity-federation.md) | Cloud & Workload Identity | Short-lived OIDC tokens replacing static cloud API keys |
| [`privileged-identity-management.md`](privileged-identity-management.md) | PIM & PAM | Just-in-Time (JIT) access, time-bound elevation, break-glass |
| [`directory-services-and-idps.md`](directory-services-and-idps.md) | Centralized IdPs | Entra ID, Okta, Ping, Keycloak enterprise topologies |
