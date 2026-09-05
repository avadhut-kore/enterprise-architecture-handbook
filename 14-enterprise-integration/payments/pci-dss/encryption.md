# Strong Cryptography and Key Management (Requirement 3 & 4)

## 1. Cryptographic Storage Standards
- **Primary Account Numbers (PAN)**: Must be rendered unreadable using strong cryptography (AES-256-GCM), format-preserving encryption, or irreversible cryptographic hashing.
- **Sensitive Authentication Data (SAD)**: CVV2/CVC2, full track data, and PIN blocks must **NEVER be stored** after authorization.

## 2. Key Management Lifecycle
- Cryptographic keys must be generated inside FIPS 140-2 Level 3 HSMs.
- Key-encrypting keys (KEK) must be separate from data-encrypting keys (DEK).
- Split knowledge and dual control required for manual key management procedures.
