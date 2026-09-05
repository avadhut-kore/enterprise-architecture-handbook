# Resource-Based Authorization & Multi-Tenant Isolation

## Executive Summary

Broken Object Level Authorization (BOLA / IDOR) is the #1 vulnerability on the OWASP API Top 10. It occurs when an endpoint verifies that a user is authenticated, but fails to verify that the user actually owns or has permission to access the specific resource requested in the URI (e.g., `GET /api/v1/invoices/9842`).

---

## 1. Architectural Mitigations for BOLA

1. **Mandatory Tenant Context Injection**:
   - The API Gateway validates the incoming JWT and injects the verified `X-Tenant-ID` into the internal request headers.
   - Downstream microservices must never accept a tenant ID passed in a query parameter or body payload.
2. **Database Row-Level Security (RLS)**:
   - Enforce multi-tenancy at the database engine level (PostgreSQL RLS):
   ```sql
   CREATE POLICY tenant_isolation_policy ON invoices
   FOR ALL
   USING (tenant_id = CURRENT_SETTING('app.current_tenant_id'));
   ```
3. **Randomized UUID Resource Identifiers**:
   - Never expose auto-incrementing sequential integers (`/orders/1`, `/orders/2`) in public APIs.
   - Use UUIDv4 or ULID identifiers (`/orders/01H8Z9C4B7W...`) to make blind resource enumeration computationally impossible.
