# Automated Key Rotation & Crypto-Shredding

## Executive Summary

- **Annual Automated Rotation**: Cloud KMS rotates Key Encryption Keys (KEKs) every 365 days without re-encrypting existing data. KMS retains previous key versions strictly for decryption.
- **Crypto-Shredding**: Destroying the KMS key renders all corresponding ciphertext irrecoverable, providing instantaneous compliance with data sanitization mandates (DoD 5220.22-M).
