# JWT Signing Algorithms: RS256 vs ES256 vs EdDSA vs HS256

## Executive Summary

Selecting the cryptographic signing algorithm dictates key management overhead, CPU verification costs, and vulnerability exposure.

---

## 1. Algorithm Comparison Matrix

| Algorithm | Type | Security Strength | Performance (Verification) | Enterprise Recommendation |
| :--- | :--- | :--- | :--- | :--- |
| **HS256** (HMAC-SHA256) | Symmetric (Shared Secret) | 128-bit | **Ultra-Fast** | **Prohibited for distributed APIs**. If any microservice is compromised, the attacker can forge tokens for *all* services. |
| **RS256** (RSA-SHA256) | Asymmetric (Public/Private) | 112-bit (2048-bit key) | Fast | **Legacy Enterprise Baseline**. Supported universally by all libraries; higher key size. |
| **ES256** (ECDSA P-256) | Asymmetric (Elliptic Curve) | 128-bit (256-bit key) | **Fast & Compact** | **Recommended Standard**. Smaller key size, lower bandwidth, robust security. |
| **EdDSA** (Ed25519) | Asymmetric (Edwards Curve) | 128-bit | **Blazing Fast** | **Modern Gold Standard**. Immune to timing attacks; rapid adoption across modern runtimes. |
