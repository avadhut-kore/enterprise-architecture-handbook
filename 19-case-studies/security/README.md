# Security Architecture Forensic Case Studies

## 1. Domain Overview & Architectural Scope
Modern enterprise security failures are rarely caused by brute-force password guessing or esoteric zero-day kernel exploits. Instead, they stem from architectural vulnerabilities: Broken Object-Level Authorization (BOLA/IDOR) in REST APIs, Server-Side Request Forgery (SSRF) bypassing perimeter defenses to exfiltrate cloud metadata credentials, compromised dependencies in the CI/CD software supply chain, symmetrically signed JWT tokens with hardcoded HMAC secrets, unauthenticated Kubernetes API ports exposed to the public internet, and missing multi-tenant row-level data isolation.

This category presents deep, blameless forensic post-mortems of critical architectural security breaches, analyzing the chain of latent vulnerabilities and establishing automated zero-trust guardrails.

---

## 2. Case Study Portfolio Index

| Case Study ID | Title | Primary Security Vulnerability | Systemic Consequence |
| :--- | :--- | :--- | :--- |
| **[`cs-sec-01`](cs-sec-01-broken-object-level-authorization-bola.md)** | **Broken Object-Level Authorization (BOLA)** | Sequential database IDs exposed in REST API without ownership checks | 3.5M Banking customer records, statements, and SSNs exfiltrated |
| **[`cs-sec-02`](cs-sec-02-ssrf-cloud-metadata-credential-exfiltration.md)** | **SSRF Cloud Metadata IAM Credential Exfiltration** | Webhook URL validator vulnerable to SSRF accessing AWS IMDSv1 | Attacker exfiltrated IAM role credentials; 120 TB customer S3 data stolen |
| **[`cs-sec-03`](cs-sec-03-supply-chain-malicious-dependency.md)** | **Software Supply Chain Malicious Dependency** | Typosquatted NPM package injected into build pipeline | Production AWS credentials exfiltrated during CI build; $1.8M ransomware |
| **[`cs-sec-04`](cs-sec-04-hardcoded-jwt-signing-secret-forge.md)** | **Hardcoded JWT Secret Token Forgery** | Symmetric HS256 JWT signing secret hardcoded in open repo | Attackers forged admin JWTs, accessing 450,000 healthcare patient records |
| **[`cs-sec-05`](cs-sec-05-kubernetes-api-misconfiguration-cryptomining.md)** | **Unauthenticated K8s API Port 10250 Exploit** | Kubelet unauthenticated read-write port exposed to internet | Attacker launched 4,000 Monero cryptomining DaemonSets; $350k AWS bill |
| **[`cs-sec-06`](cs-sec-06-multi-tenant-cross-tenant-data-leak.md)** | **SaaS Cross-Tenant Data Leak via Missing Filter** | ORM repository missing `tenant_id` filter on bulk API | Competitor accessed 18 enterprise client payroll databases; SEC audit |
