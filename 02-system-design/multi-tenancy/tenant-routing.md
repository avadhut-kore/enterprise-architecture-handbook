# Tenant Routing Architecture

## 1. Identifying the Tenant at Ingress
* **Subdomain / Host Header**: `acme.saas.enterprise.com` $\rightarrow$ Gateway extracts `acme`.
* **Path Prefix**: `api.enterprise.com/v1/tenants/acme/orders`
* **JWT Claim**: Client submits Bearer token; gateway extracts `claims["tenant_id"]`.
* **Custom Header**: `X-Tenant-Id: 9b1deb4d` (Enterprise B2B API integrations).
