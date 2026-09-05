# Application Architecture: Multi-Tenant Context & Isolation

## 1. Tenant Context Propagation
1. Incoming HTTP request presents JWT: `{"sub":"user_123", "tenant_id":"tenant_acme_corp"}`.
2. API Gateway validates JWT signature and injects `X-Tenant-ID` internal header.
3. Backend service framework extracts `tenant_id` into a thread-local or asynchronous context (`TenantContextHolder`).
4. Every database query, cache key (`acme:users:101`), and background event automatically inherits the active tenant context.

---

## 2. Noisy Neighbor Throttling
- Employs **Token Bucket Rate Limiting** with per-tenant bucket keys:
  - Free/Starter Tier: 20 requests/sec.
  - Business Tier: 100 requests/sec.
  - Enterprise Tier: 1,000 requests/sec with dedicated bursting headroom.
