# Banking-Grade Security: HSMs and Network Isolation

## 1. Hardware Security Module (HSM) Integration
Core banking PIN translation, CVV verification, and private key operations must occur strictly inside FIPS 140-2 Level 3 Hardware Security Modules (Thales payShield, AWS CloudHSM). Application code never handles plaintext PIN blocks or master keys.

```
[ATM / POS Terminal] ──(Encrypted PIN Block under Zone Master Key)──> [API Gateway]
                                                                            │
                                   ┌────────────────────────────────────────┘
                                   ▼
              [HSM: FIPS 140-2 Level 3 Appliance]
              ├── Decrypts PIN Block using Zone Master Key (ZMK)
              ├── Translates PIN Block to Terminal Master Key (TMK)
              └── Verifies PIN Offset against Core CVV/PVV tables
```

## 2. Microsegmentation and Bastion Architecture
Core banking subnets must be completely isolated from corporate user networks, accessible exclusively through hardened API proxies with mTLS and dedicated jumped bastion hosts.
