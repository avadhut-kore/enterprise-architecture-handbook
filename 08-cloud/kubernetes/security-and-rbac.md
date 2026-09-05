# Kubernetes Multi-Tenant Security & RBAC Hardening

## Executive Summary

Kubernetes was not originally designed for untrusted multi-tenancy. Hardening enterprise clusters requires a defense-in-depth architecture spanning **RBAC**, **NetworkPolicies**, and **Pod Security Standards**.

---

## 1. Defense-in-Depth Security Matrix

```mermaid
graph TD
    Req[Kubernetes API Request] --> AuthN[1. Authentication: OIDC / Entra ID]
    AuthN --> AuthZ[2. Authorization: RBAC RoleBindings]
    AuthZ --> Admission[3. Admission Control: Kyverno / OPA Gatekeeper]
    Admission --> DataPlane[Data Plane Runtime Security]
    DataPlane --> NetPol[4. NetworkPolicies: Default-Deny East-West]
    DataPlane --> PSS[5. Pod Security Standards: Restricted Profile]
```

---

## 2. Non-Negotiable Hardening Baselines

1. **Default-Deny Network Policies**:
   - By default, Kubernetes networking is flat: any pod in any namespace can communicate with any other pod in any namespace.
   - Enforce a **Default-Deny Ingress and Egress NetworkPolicy** in every namespace, requiring application teams to explicitly whitelist authorized internal microservice communication paths.
2. **Pod Security Standards (Restricted Baseline)**:
   - Enforce the `restricted` Pod Security Standard across all production namespaces:
     - Disallow running as root (`runAsNonRoot: true`).
     - Disallow privilege escalation (`allowPrivilegeEscalation: false`).
     - Disallow host namespaces (`hostPID: false`, `hostNetwork: false`).
