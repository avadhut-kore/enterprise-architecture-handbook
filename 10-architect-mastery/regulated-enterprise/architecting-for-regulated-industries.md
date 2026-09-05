# Architecting for Regulated Industries

Regulated software systems must be designed for continuous auditability, deterministic traceability, and regulatory survival (DORA, HIPAA, PCI-DSS v4.0).

## 1. The Core Compliance Pillars

```
┌─────────────────────────────────────────────────────────────┐
│ 1. IMMUTABLE AUDIT TRAILS & PROVENANCE                      │
│ Every read, write, and privilege elevation written to WORM  │
│ (Write Once, Read Many) S3 Object Lock storage with tamper- │
│ evident SHA-256 cryptographic hash chaining.                │
├─────────────────────────────────────────────────────────────┤
│ 2. SEPARATION OF DUTIES & ZERO-TRUST PRIVILEGE              │
│ Developers have zero direct production database access.     │
│ Break-glass access requires dual-operator authorization and │
│ auto-terminates after 60 minutes with full session replay.  │
├─────────────────────────────────────────────────────────────┤
│ 3. CRYPTOGRAPHIC ENVELOPE ENCRYPTION                        │
│ Data encrypted at rest using AES-256-GCM with customer-     │
│ managed keys (BYOK) rotated automatically every 365 days.   │
├─────────────────────────────────────────────────────────────┤
│ 4. DISASTER RESILIENCE & DORA OPERATIONAL TESTING           │
│ Strict RPO <= 1 min, RTO <= 15 min with automated monthly   │
│ cross-region unannounced failover drills.                   │
└─────────────────────────────────────────────────────────────┘
```

## Related Modules
- [Global Architecture](file:///d:/company/products/enterprise-architecture-handbook/10-architect-mastery/global-architecture/README.md)
- [Security Architecture](../../10-security/README.md)
