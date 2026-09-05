# Tenant Security & Encryption

## 1. Per-Tenant Cryptographic Keys (BYOK)
Enterprise clients require **Bring Your Own Key (BYOK)** governance:
* Each tenant possesses a dedicated Customer Master Key (CMK) in AWS KMS or HashiCorp Vault.
* If a tenant terminates their contract, cryptographically shredding their CMK renders all historical backups and database records instantaneously unrecoverable.
