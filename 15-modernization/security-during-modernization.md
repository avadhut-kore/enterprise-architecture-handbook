# Security Architecture During System Modernization

## 1. Security Risks in Hybrid Transition Architectures
During modernization, security posture is at its most vulnerable. Attackers exploit gaps between legacy perimeter defenses and modern zero-trust environments.

```
       Legacy Zone (Perimeter Security)                 Modern Cloud Zone (Zero Trust)
┌──────────────────────────────────────────────┐  ┌──────────────────────────────────────────────┐
│  - Static DB passwords in config files       │  │  - Ephemeral tokens & HashiCorp Vault        │
│  - Unencrypted intra-datacenter HTTP         │  │  - Mutual TLS (mTLS 1.3) Everywhere         │
│  - Broad IP-based network trust              │  │  - Fine-grained IAM & Least Privilege        │
└──────────────────────┬───────────────────────┘  └──────────────────────┬───────────────────────┘
                       │                                                 │
                       └───────────── [SECURE TRANSITION BRIDGE] ────────┘
                                      - Token Exchange (SAML -> OAuth2)
                                      - Transit Encryption (mTLS IPSec VPN)
                                      - Dual-Sided Audit Logging
```

---

## 2. Identity Federation and Token Translation
Legacy applications typically rely on Active Directory LDAP, Kerberos, or session cookies, while modern microservices require OAuth 2.0 / OIDC JWTs.
- Deploy an **Identity Broker / Token Exchange Gateway** at the boundary.
- Translate validated legacy session cookies into short-lived, audience-restricted JWTs (`aud: https://orders.modern.internal`).
- Never pass raw legacy database credentials to cloud microservices.

---

## 3. Network Segmentation & Zero-Trust Ingress
- Never open direct database ports (TCP 1521 for Oracle, TCP 1433 for MSSQL) across the public internet between on-premise and cloud.
- Establish dedicated private interconnects (AWS Direct Connect, Azure ExpressRoute) with IPSec encryption.
- Enforce strict microsegmentation using Kubernetes NetworkPolicies and cloud security groups, whitelisting only designated IP ranges and ports.
