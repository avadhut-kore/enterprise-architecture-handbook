# Mobile Security Architecture & Hardware Enclaves

## Executive Summary

Sensitive data on mobile devices (biometric keys, refresh tokens, private signing keys) must never be stored in plaintext shared storage (`SharedPreferences` or `UserDefaults`).

---

## Hardware-Backed Key Storage
- **iOS Keychain & Secure Enclave**: Keys are generated and stored within an isolated coprocessor. Private keys never enter application memory; cryptographic signing operations occur entirely within the hardware enclave.
- **Android KeyStore & StrongBox**: Hardware security module enforcing cryptographic operations outside the main Android OS kernel.
