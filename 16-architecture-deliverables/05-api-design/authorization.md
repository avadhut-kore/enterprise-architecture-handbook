# API Authorization Standards

## 1. Scope & Claim Enforcement
* APIs must enforce fine-grained OAuth2 scopes formatted as `<domain>:<action>` (e.g., `invoices:read`, `invoices:write`, `invoices:admin`).
* Attribute-Based Access Control (ABAC) must be verified inside the service to ensure tenant isolation (e.g., confirming `tenant_id` in token matches requested resource).
