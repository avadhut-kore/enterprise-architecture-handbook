# Authorization Paradigms (RBAC vs ABAC vs ReBAC vs PBAC)

## Executive Summary

Choosing the correct authorization paradigm is a foundational architectural decision that impacts database design, cacheability, API latency, and organizational scalability.

---

## 1. Paradigm Comparison

```mermaid
flowchart TD
    subgraph RBAC ["1. Role-Based Access Control (RBAC)"]
        U1["User"] --> R1["Role (e.g. BillingAdmin)"]
        R1 --> P1["Permission (e.g. invoices:read)"]
    end
    subgraph ABAC ["2. Attribute-Based Access Control (ABAC)"]
        U2["User (Attributes: Dept, Title)"] --> POL["Policy Rule: If Dept==Finance AND Time<18:00"]
        POL --> R2["Resource (Attributes: Classification==Confidential)"]
    end
    subgraph ReBAC ["3. Relationship-Based Access Control (ReBAC)"]
        U3["User"] -->|Member of| G1["Team"]
        G1 -->|Owner of| D1["Document"]
    end
```

---

## 2. Multi-Dimensional Comparison Matrix

| Dimension | RBAC | ABAC | ReBAC (Zanzibar) | PBAC (Policy-as-Code) |
| :--- | :--- | :--- | :--- | :--- |
| **Model Concept** | User $\rightarrow$ Roles $\rightarrow$ Permissions | Policies over subject/resource attributes | Graph traversal over object relationships | Decoupled declarative policy engine (OPA) |
| **Complexity** | Low | High | High | Moderate |
| **Granularity** | Coarse | Extreme | Fine (Hierarchical) | Fine |
| **Latency Overhead** | Sub-millisecond (Bitmap check) | 2–10 ms (Attribute retrieval) | 5–25 ms (Graph query) | 1–5 ms (In-memory Rego evaluation) |
| **Role Explosion Risk**| **Severe** (Thousands of ad-hoc roles) | None | None | None |
| **Recommended Use** | Simple enterprise apps with fixed roles | Highly regulated systems with contextual rules | Collaborative SaaS tools (Google Drive, Notion) | Microservices, Kubernetes, Cloud IAM |
