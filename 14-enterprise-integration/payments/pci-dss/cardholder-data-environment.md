# Cardholder Data Environment (CDE) Architecture

## 1. CDE Isolation Blueprint

```
                      [Public Internet]
                             │
            ═════════════════▼═════════════════  [WAF / Edge DMZ]
                      [API Gateway]
                             │
     ┌───────────────────────┴───────────────────────┐
     ▼                                               ▼
[Non-CDE Microservices]                    [CDE Bastion Proxy]
(Orders, Catalog, Users)                             │
                                  ═══════════════════▼═══════════════════  [CDE Firewall]
                                             [Card Vault / HSM]
                                             ├── AES-256 Storage
                                             └── Zero External Internet Access
```

## 2. Hardening Requirements for CDE
- Dual-homed architectures are prohibited.
- Ingress permitted exclusively via dedicated API proxies with mTLS and strict payload inspection.
- Outbound internet access from CDE databases is blocked via network firewalls and default-deny egress security groups.
