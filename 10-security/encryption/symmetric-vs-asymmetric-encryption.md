# Symmetric vs Asymmetric Cryptography

## Executive Summary

| Dimension | Symmetric Cryptography | Asymmetric Cryptography |
| :--- | :--- | :--- |
| **Keys** | Single shared secret key | Public key / Private key pair |
| **Speed** | **Blazing Fast** (Hardware AES-NI acceleration) | Slow (Computationally intensive math) |
| **Approved Algorithms**| **AES-256-GCM**, ChaCha20-Poly1305 | **RSA-4096**, **ECDSA P-384**, **Ed25519** |
| **Primary Use Case** | Bulk data encryption (Databases, files, disks) | Identity assertions, digital signatures, key exchange |
