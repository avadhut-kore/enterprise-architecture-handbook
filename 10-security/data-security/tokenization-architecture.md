# Tokenization Architecture (Vaulted vs Vaultless)

## Executive Summary

Tokenization replaces sensitive data (e.g., credit card Primary Account Numbers) with a non-sensitive surrogate value (token) that has zero exploitable value.

---

## 1. Vaulted vs Vaultless Tokenization

| Dimension | Vaulted Tokenization | Vaultless Tokenization (FPE) |
| :--- | :--- | :--- |
| **Mechanism** | Random token mapped to ciphertext in encrypted database | Format-Preserving Encryption (AES-FFX) using a master key |
| **Scalability** | Database scales with number of tokens ($O(N)$ storage) | Pure computational scaling ($O(1)$ storage) |
| **PCI-DSS Scope**| Isolates PCI scope strictly to the Token Vault | Cryptographic key remains within PCI boundary |
| **Latency** | 5–15 ms database lookup | Sub-millisecond CPU encryption |
