# Enterprise Security Architecture Diagrams

This directory provides standardized, copy-pasteable architectural diagrams and modeling patterns for enterprise security architectures, identity federation, zero trust segmentation, cryptographic lifecycles, and threat modeling.

## Security Diagram Catalog

| Diagram Specification | Primary Focus | Key Standards / Protocols |
|:----------------------|:--------------|:--------------------------|
| [Zero Trust Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/zero-trust.md) | Identity-aware micro-segmentation & PDP/PEP | NIST SP 800-207, BeyondCorp |
| [Identity Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/identity-flow.md) | Cross-domain enterprise identity lifecycle | SAML 2.0, SCIM 2.0, LDAP |
| [OAuth 2.0 Authorization](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/oauth2.md) | Grant types, token exchange, authorization server | RFC 6749, RFC 7636 (PKCE), RFC 8693 |
| [OpenID Connect (OIDC)](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/oidc.md) | Identity verification & federated claims | OIDC Core 1.0, Discovery, UserInfo |
| [JWT Architecture & Lifecycle](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/jwt.md) | Signing, validation, JWKS rotation, revocation | RFC 7519, RFC 7517, RFC 7515 (JWS) |
| [Enterprise Authentication](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/authentication.md) | MFA, adaptive risk engine, passwordless | FIDO2 / WebAuthn, TOTP, Biometrics |
| [Enterprise Authorization](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/authorization.md) | RBAC, ABAC, ReBAC policy enforcement | XACML, Open Policy Agent (OPA) / Rego |
| [IAM Reference Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/iam.md) | Identity governance, directory sync, federation | Active Directory, Azure AD/Entra, Okta |
| [API Security Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/api-security.md) | Gateway enforcement, rate limiting, mTLS | OWASP API Top 10, OAuth2, Mutual TLS |
| [Secrets Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/secrets-management.md) | Dynamic secrets injection, HSM leasing, rotation | HashiCorp Vault, AWS Secrets Manager |
| [Data Encryption Lifecycle](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/encryption.md) | At-rest, in-transit, and in-use cryptographic flows | TLS 1.3, AES-256-GCM, Envelope Cryptography |
| [Key Management Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/key-management.md) | Root CA, KMS, envelope encryption, rotation | FIPS 140-2/3 Level 3 HSM, PKCS#11 |
| [Network Security Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/network-security.md) | Ingress filtering, micro-segmentation, egress proxy | Next-Gen Firewall (NGFW), IDS/IPS, VPC CNI |
| [WAF & DDoS Mitigation](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/waf.md) | L7 inspection, bot management, rate throttling | OWASP ModSecurity, Cloudflare, AWS WAF |
| [Threat Modeling Diagrams](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/threat-model.md) | STRIDE, DREAD, attack trees, vulnerability surface | Microsoft Threat Modeling, MITRE ATT&CK |
| [Trust Boundaries](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/trust-boundaries.md) | Zone isolation, untrusted ingest, privilege tiers | Defense-in-depth, Security Zones 0-4 |
| [Data Classification & Flow](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/data-classification.md) | Public vs Internal vs Confidential vs Restricted | GDPR, HIPAA, PCI-DSS Data Scoping |
| [Privileged Access Management](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/privileged-access.md) | Just-in-Time (JIT) elevation, session recording | CyberArk, BeyondTrust, Teleport |
| [Security Operations & SIEM](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/security-monitoring.md) | Telemetry ingestion, SOAR orchestration, alert triage | Splunk, Microsoft Sentinel, Cortex XSOAR |
| [Supply Chain & DevSecOps](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/supply-chain.md) | SAST, DAST, SCA, SBOM signing, SLSA Provenance | Sigstore/Cosign, Trivy, SLSA Level 3 |
| [AI Security Architecture](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/ai-security.md) | Prompt guardrails, model poisoning, output sanitizing | OWASP Top 10 for LLM, NeMo Guardrails |
| [Security Diagram Template](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/template.md) | Standardized trust boundary & auth flow skeleton | Architecture Blueprint Standard |
| [Security Review Checklist](file:///d:/company/products/enterprise-architecture-handbook/17-diagrams/security/checklists.md) | ARB / Infosec architectural sign-off review | 40-point Security Architecture Audit |

## Visual Modeling Conventions
1. **Trust Boundaries**: Always use distinct dashed subgraphs (`style boundary stroke-dasharray: 5 5`) to demarcate crossing of security perimeters (e.g., Public Internet, DMZ, Application Zone, Restricted Data Vault).
2. **Encrypted Channels**: Explicitly label wire protocols (`mTLS 1.3`, `HTTPS / TLS 1.3`, `IPsec Tunnel`) directly on connection paths.
3. **Authentication vs Authorization**: Clearly distinguish identity assertion tokens (`ID Token`, `Client Certificate`) from capability/access tokens (`Bearer Access Token`, `RBAC Role Claim`).
