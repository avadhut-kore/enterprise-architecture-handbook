# Cryptographic Architecture (`encryption/`)

## Executive Summary

Cryptography protects data confidentiality, integrity, and authenticity across all computing domains. This directory defines architectural standards for ciphers, envelope encryption, and TLS 1.3.

---

## Key Guides in this Directory

| Guide | Scope | Core Pattern |
| :--- | :--- | :--- |
| [`encryption-architecture.md`](encryption-architecture.md) | Cryptography Lifecycles | At-rest, in-transit, in-use (Confidential Computing) |
| [`symmetric-vs-asymmetric-encryption.md`](symmetric-vs-asymmetric-encryption.md) | Cipher Selection | AES-256-GCM vs ChaCha20-Poly1305 vs RSA vs ECC |
| [`envelope-encryption-deep-dive.md`](envelope-encryption-deep-dive.md) | Key Hierarchies | Data Encryption Keys (DEKs) and Key Encryption Keys (KEKs) |
| [`tls-1-3-and-certificate-management.md`](tls-1-3-and-certificate-management.md) | Transport Security | TLS 1.3 handshakes, forward secrecy, automated renewal |
