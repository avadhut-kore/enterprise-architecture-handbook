# Edge Authorization & Policy Enforcement

## 1. RBAC vs. ABAC at the Perimeter
* **Role-Based Access Control (RBAC)**: Validates static roles (`ADMIN`, `CUSTOMER`).
* **Attribute-Based Access Control (ABAC)**: Evaluates contextual attributes:
  $$\text{Allow If: } \text{Role} == \text{"MANAGER"} \land \text{Region} == \text{"EMEA"} \land \text{Time} \in [08:00, 18:00]$$

---

## 2. Open Policy Agent (OPA) Integration

```mermaid
flowchart LR
    Gateway[API Gateway / Envoy] -->|Query Rego Policy Engine| OPA[Open Policy Agent (Sidecar)]
    OPA -->|Allow: true / false| Gateway
```

* Decouples authorization rules from application code; security policies are declared in **Rego** and version-controlled in Git.
