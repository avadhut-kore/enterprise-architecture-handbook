# Payload and Transport Encryption in Enterprise Integration

## 1. Transport vs. Message-Level Encryption

```
Transport Layer Security (TLS 1.3)
[Client Application]  ═════════════════════════════════════>  [API Gateway]
   (Encrypted in transit over the wire, but in plain text inside RAM/proxies)

Message-Level Envelope Encryption (JWE / CMS)
[Client Application]  ------------------------------------->  [Core Vault Database]
   { "ciphertext": "a8F91...2D", "encrypted_key": "k39...X" }
   (Encrypted end-to-end; intermediate queues, proxies, and loggers cannot read data)
```

## 2. Envelope Encryption Strategy
In financial, healthcare, and multi-tenant platforms, data must remain encrypted at rest inside message brokers (Kafka, RabbitMQ, SQS). Envelope encryption uses a two-tier key hierarchy:
1. **Data Encryption Key (DEK)**: A symmetric AES-256-GCM key generated locally per message.
2. **Key Encryption Key (KEK)**: An asymmetric or master key stored in a Hardware Security Module (HSM) or cloud KMS used to encrypt the DEK.

```json
{
  "encrypted_dek": "AQEBAHj8X91...3sM=",
  "kek_key_id": "arn:aws:kms:us-east-1:123456789:key/enterprise-master-kek",
  "algorithm": "AES-256-GCM",
  "iv": "v8k92M1L8xO=",
  "tag": "j9F19Mx81QkL29==",
  "ciphertext": "k9102Nx0912Mx81..."
}
```

## 3. Cryptographic Standards Matrix
- **Cipher Suite**: TLS 1.3 `TLS_AES_256_GCM_SHA384` or `TLS_CHACHA20_POLY1305_SHA256`.
- **Symmetric Data Encryption**: AES-256-GCM (provides authenticated encryption with associated data).
- **Asymmetric Key Exchange**: RSA 4096-bit or Elliptic Curve (ECDH with Curve25519 or NIST P-384).
- **Hashing & Signatures**: SHA-256 / SHA-512 with HMAC or RSA-PSS.
