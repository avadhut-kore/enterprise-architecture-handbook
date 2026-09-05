# Security, Tenant Encryption & SOC 2 Type II

## 1. Bring-Your-Own-Key (BYOK) Encryption
- Enterprise tier tenants can supply their own AWS KMS or Azure Key Vault Customer Managed Keys (CMK).
- All tenant database storage volumes and backups are encrypted under their specific CMK.

---

## 2. Cryptographic Data Shredding on Tenant Churn
When a tenant cancels their contract, rather than executing expensive database purges across petabytes of historical backups, the tenant's individual KMS master encryption key is destroyed. All historical backups encrypted under that key are rendered permanently unrecoverable in compliance with SOC 2 / GDPR requirements.
