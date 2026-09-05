# Tokenization Architectures in Regulated Integrations

## 1. Tokenization vs. Encryption
- **Encryption**: Reversible mathematical transformation using a cryptographic key. Possession of the key allows decryption anywhere. If keys leak, all data is compromised.
- **Tokenization**: Replaces sensitive data with a mathematically unrelated, surrogate value (a "token") using a secure centralized Token Vault. Outside the vault, the token has zero cryptographic or mathematical relationship to the original plaintext.

## 2. Format-Preserving Tokenization (FPT)
Format-Preserving Encryption / Tokenization retains the length, structure, and character set of the original sensitive string (e.g., a 16-digit credit card PAN or a 9-digit SSN):

```
Original PAN:   4111 2222 3333 4444  (Visa, 16 digits)
Tokenized PAN:  4999 8172 6381 4444  (Retains 4-prefix and last 4 digits for receipt printing)
```

## 3. De-tokenization Service Integration Pattern

```
[Untrusted Integration Layer] ──> Passes Token: 4999-8172-6381-4444
                                         │
[Secure Detokenizer (Vault Boundary)] ──┤ (Checks caller authorization via mTLS + OIDC)
                                         ▼
[Token Database (HSM Encrypted)] ──> Returns Plaintext PAN: 4111-2222-3333-4444
                                         │
                                         ▼ Directly transmitted to payment acquirer
```

## 4. Scope Reduction Benefits
Using tokenization at the ingress API gateway removes downstream event brokers, analytical data lakes, and microservices from the scope of PCI-DSS and HIPAA audits, dramatically lowering compliance costs.
