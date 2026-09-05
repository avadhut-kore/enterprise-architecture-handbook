# Enterprise Secrets Management Architecture

Hardcoded credentials, long-lived API tokens, and secrets checked into Git are the leading causes of enterprise cloud breaches.

## 1. The Secrets Hierarchy & Storage Archetypes

```
┌─────────────────────────────────────────────────────────────┐
│                ENTERPRISE SECRET STORE                      │
│             (HashiCorp Vault / AWS Secrets Mgr)             │
├──────────────────────────────┬──────────────────────────────┤
│ CI/CD SECRETS (Build Time)   │ RUNTIME SECRETS (Pods/VMs)   │
│ - Ephemeral OIDC federation  │ - Injected into memory via   │
│ - Short-lived token grants   │   External Secrets Operator  │
│ - Scoped per environment     │ - Dynamic Vault DB leasing   │
└──────────────────────────────┴──────────────────────────────┘
```

## 2. Dynamic Secret Leases (Vault Architecture)
Instead of static database passwords that never change:
1. Application requests database credentials from Vault.
2. Vault dynamically creates a unique temporary PostgreSQL user with a 60-minute TTL.
3. If an attacker exfiltrates the password, it self-destructs within the hour!

## 3. Secret Leak Prevention Protocol
- Mandatory pre-commit hooks running Gitleaks.
- GitHub Secret Scanning with automated push protection.
- Automated secret revocation webhooks if credentials are inadvertently exposed.

## Related Resources
- [DevSecOps Architecture](../devsecops/README.md)
- [Security Architecture](../../10-security/README.md)
