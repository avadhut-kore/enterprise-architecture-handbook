# Envelope Encryption Architecture

## Executive Summary

Encrypting large volumes of data directly using a central KMS key creates severe network bottlenecks and hits KMS API rate limits. **Envelope Encryption** solves this by encrypting data locally with an ephemeral Data Encryption Key (DEK).

---

## 1. Envelope Encryption Workflow

```mermaid
sequenceDiagram
    autonumber
    participant App as Application Service
    participant KMS as Key Management Service (KMS)
    participant Storage as Database / S3 Storage

    Note over App: 1. Request Data Encryption Key
    App->>KMS: GenerateDataKey(KeyId="kms-master-kek")
    KMS-->>App: Returns: Plaintext DEK + Encrypted DEK
    
    Note over App: 2. Encrypt Data locally in memory
    App->>App: Ciphertext = AES-256-GCM(Plaintext Data, Plaintext DEK)
    Note over App: 3. Wipe Plaintext DEK from RAM immediately!
    
    App->>Storage: Writes {Ciphertext, Encrypted DEK, IV, AuthTag}
```
