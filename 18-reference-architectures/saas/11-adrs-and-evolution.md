# Architecture Decision Records & Evolution Roadmap: SaaS

## 1. Canonical Architecture Decision Records

### ADR-001: Adoption of Hybrid Multi-Tenancy (Pool for Standard, Silo for Enterprise)
- **Status**: Accepted
- **Context**: Siloed databases for all 5,000 tenants would cost over $300k/month in idle database overhead. A purely pooled database is rejected by Fortune 500 enterprise customers demanding physical isolation.
- **Decision**: Implement a hybrid model: Standard and Pro tenants share a pooled PostgreSQL database with Row-Level Security; Enterprise tier customers are provisioned dedicated, isolated RDS database instances.
- **Consequences**: Minimizes base infrastructure costs while closing enterprise deals; requires database router middleware.

---

## 2. Evolution Roadmap (1x to 100x Scale)
- **Stage 1 (1x)**: Pure pooled single-database multi-tenancy with tenant_id column filtering.
- **Stage 2 (10x)**: PostgreSQL Row-Level Security; SAML/OIDC enterprise SSO; token bucket rate limiting.
- **Stage 3 (100x)**: Hybrid Silo/Pool architecture; multi-region tenant residency routing; BYOK customer managed keys.
