# Security, Privacy & Compliance Architecture: CRM

## 1. Field-Level Encryption & RBAC
- **Field-Level Encryption (Envelope Encryption)**: Sensitive fields (Customer Tax IDs, Credit Card tokens, Personal Mobile Numbers) are encrypted at rest using individual data encryption keys (DEKs) wrapped by an enterprise HSM KMS master key.
- **Hierarchical Role-Based Access Control (RBAC)**: Sales reps only see accounts within their assigned territory; regional managers see all accounts in their jurisdiction.

---

## 2. GDPR & CCPA Compliance Architecture
- **Right to be Forgotten**: Triggering an account erasure orchestrates a cryptographic purge: the customer's DEK in the key vault is destroyed, rendering all historical encrypted PII mathematically unrecoverable across all database backups.
- **Consent Ledger**: Immutable tracking of opt-in/opt-out status for marketing emails and data processing.
