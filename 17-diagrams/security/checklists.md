# Security Architecture Review Checklist

This checklist provides a structured 40-point verification framework for Technical Architects, Solution Architects, and the Architecture Review Board (ARB) to ensure security rigor across system designs.

## 1. Identity, Authentication & Federation
- [ ] Is an enterprise identity provider (IdP) used as the sole source of truth (no local application user databases)?
- [ ] Is multi-factor authentication (MFA) mandatory for all user interactions, with phishing-resistant FIDO2 passkeys for privileged users?
- [ ] Is OAuth 2.0 Authorization Code Flow with PKCE enforced for all web and mobile clients?
- [ ] Are Implicit Flow and Resource Owner Password Credentials (ROPC) strictly banned?
- [ ] Are JSON Web Tokens (JWT) signed asymmetrically (RS256/ES256) and validated using dynamic JWKS endpoints?
- [ ] Is algorithm none (`alg: "none"`) explicitly rejected by all token parsers?
- [ ] Are token lifetimes appropriately bounded (Access Token <= 15 minutes, Refresh Token with rotation)?
- [ ] Is automated SCIM 2.0 provisioning and instant deprovisioning integrated with HRIS lifecycle events?

## 2. Authorization & Least Privilege
- [ ] Is authorization decoupled from business logic using policy engines (e.g., Open Policy Agent / Rego)?
- [ ] Are access policies evaluated on every request (Never Trust, Always Verify)?
- [ ] Is Broken Object Level Authorization (BOLA / IDOR) mitigated through explicit tenant and ownership validation?
- [ ] Is administrative access governed by Just-in-Time (JIT) elevation with automated session expiration?
- [ ] Are separation of duties (SoD) enforced between deployment roles and operational governance roles?

## 3. Network & Perimeter Defense
- [ ] Are all security trust boundaries explicitly defined and visualized in architecture diagrams?
- [ ] Are public internet ingress paths protected by cloud-edge DDoS scrubbing and a Web Application Firewall (WAF)?
- [ ] Is East-West network micro-segmentation enforced via default-deny Kubernetes NetworkPolicies or security groups?
- [ ] Is egress traffic from private subnets routed through an inspecting egress proxy to prevent data exfiltration?
- [ ] Are legacy protocols (FTP, Telnet, HTTP, unencrypted LDAP) explicitly blocked at firewall perimeters?

## 4. Cryptography & Data Protection
- [ ] Is TLS 1.3 mandated for all public and internal communications (with TLS 1.2 as a minimum fallback; TLS 1.0/1.1 disabled)?
- [ ] Are weak cipher suites (RC4, 3DES, CBC mode ciphers) disabled across all load balancers?
- [ ] Is envelope encryption implemented for sensitive data at rest using Customer Managed Keys (CMKs) in KMS/HSM?
- [ ] Are plaintext Data Encryption Keys (DEKs) wiped from volatile memory immediately after cryptographic operations?
- [ ] Is data classified into standard tiers (Public, Internal, Confidential, Restricted) with automated DLP tagging?
- [ ] Is Restricted data (PCI, PII, PHI) field-level encrypted or tokenized before entering relational storage?

## 5. Secrets Management
- [ ] Are all static credentials, API keys, and certificates banned from source code and Docker images?
- [ ] Are application secrets dynamically leased and injected in-memory (`tmpfs`) at container runtime?
- [ ] Is automated rotation configured for all database passwords and third-party API credentials?
- [ ] Are secret access operations fully audited and forwarded to SIEM in real time?

## 6. Software Supply Chain & DevSecOps
- [ ] Are pre-commit hooks configured to detect secrets, leaked keys, and misconfigurations locally?
- [ ] Are static application security testing (SAST) and software composition analysis (SCA) automated in CI/CD?
- [ ] Are container images scanned for CVEs and cryptographically signed (Cosign/Sigstore) before registry upload?
- [ ] Is an automated Software Bill of Materials (SBOM) generated in SPDX or CycloneDX format for each release?
- [ ] Do Kubernetes admission controllers reject unsigned container images or images containing critical vulnerabilities?

## 7. Threat Modeling & Operations
- [ ] Has a formal STRIDE threat model been completed, reviewed, and signed off for the architecture?
- [ ] Are all security audit events, authentication attempts, and authorization failures streamed to a centralized SIEM?
- [ ] Are audit logs stored in write-once-read-many (WORM) storage with legal hold protection?
- [ ] Are automated SOAR playbooks configured for high-confidence security incidents (e.g., auto-contain compromised IP)?
- [ ] Has an incident response and disaster recovery plan been documented with defined RTO and RPO metrics?
