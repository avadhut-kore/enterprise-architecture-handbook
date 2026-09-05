# Offline Mobile Data Security & Local Encryption

## Executive Summary

For enterprise mobile applications operating in offline-first mode (e.g., healthcare field workers, logistics):
1. **Encrypted Local Datastores**: Mandate **SQLCipher** for local SQLite databases using 256-bit AES encryption.
2. **Biometric Key Derivation**: The database encryption key must be derived dynamically from the device hardware enclave using biometric authentication (Face ID / Fingerprint). The key is wiped from RAM whenever the app transitions to the background.
