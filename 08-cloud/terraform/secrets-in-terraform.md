# Secrets Management in Terraform State Files

## Executive Summary

> **CRITICAL SECURITY FACT**: Terraform state files store resource attributes in **plaintext JSON**, including database passwords, TLS private keys, and API tokens.

---

## 1. How Plaintext Secrets Leak into State

```mermaid
graph TD
    TFCode[HCL: resource 'random_password' 'db_pass'] --> StateFile[terraform.tfstate: Plaintext JSON!]
    StateFile --> Leak["db_password": "superSecretPassword123" <== VISIBLE IN PLAINTEXT!]
```

---

## 2. Enterprise Mitigation Architecture

1. **Never Generate Passwords in Terraform**:
   - Do not use `random_password` in Terraform. Provision databases with temporary passwords and immediately rotate them via AWS Secrets Manager or HashiCorp Vault.
2. **OpenTofu State Encryption**:
   - OpenTofu (open-source Terraform fork) supports native **State Encryption at Rest**, encrypting sensitive attributes directly inside the state file using AES-GCM before writing to the remote backend.
