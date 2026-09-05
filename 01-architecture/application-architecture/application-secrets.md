# Application Secrets Management

## 1. Secret Architecture Invariants

1. **Zero Hardcoded Secrets**: Secrets must never be committed to source code repositories, Dockerfiles, or Git history.
2. **Ephemeral In-Memory Exposure**: Secrets fetched from Vault/KMS should exist in process memory only as long as needed; clear strings from memory buffers if supported by runtime.
3. **Automated Rotation**: Applications must support hot-reloading of updated credentials without requiring a container restart or pod eviction.
4. **Least-Privilege Secret Scoping**: An order service must only receive permissions to decrypt order database credentials, never billing or customer secrets.
