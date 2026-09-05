# PII Protection and Compliance in Integration Architectures

## 1. Personally Identifiable Information (PII) Taxonomy
PII encompasses any information that can be used to distinguish or trace an individual's identity:
- **Direct Identifiers**: National ID, Passport Number, Full Name, Email, Phone Number, Biometrics.
- **Indirect / Quasi-Identifiers**: Postal Code, Gender, Date of Birth, IP Address, Device Fingerprint.

## 2. Architectural Controls for PII in Integration

```
[Ingress Gateway] ──> [PII Inspection Engine (DLP)] ──> [Field Tokenizer]
                               │                               │
                      Detected Unencrypted SSN         Tokenized Payload:
                               │                       { "customer_id": "TOK-81729" }
                               ▼                               │
                       [Quarantine Alert]                      ▼
                                                        [Message Queue]
```

## 3. Compliance Matrix: GDPR, CCPA, and Cross-Border Transfer
- **Right to Erasure (GDPR Art. 17)**: Event brokers (Kafka) are immutable. Never write raw PII into immutable topics; instead, write a pseudonymized key (`customer_id`) and store PII in a mutable lookup store that can be purged upon deletion request.
- **Cross-Border Restrictions**: Ensure integration payloads originating in the EU/UK do not leave local cloud regions without appropriate Standard Contractual Clauses (SCCs) and encryption.
