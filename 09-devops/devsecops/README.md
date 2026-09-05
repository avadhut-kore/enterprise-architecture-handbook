# DevSecOps Architecture & Shift-Left Security

DevSecOps embeds automated security controls, compliance validations, and vulnerability governance into every stage of the software delivery lifecycle.

## 1. The DevSecOps Security Spectrum

```
┌─────────────────────────────────────────────────────────────┐
│ 1. CODE & COMMIT TIME (Developer Workstation)               │
│ - Pre-commit hooks (Gitleaks) to block credential commits   │
│ - IDE real-time vulnerability feedback (Snyk / SonarLint)   │
├─────────────────────────────────────────────────────────────┤
│ 2. CI PIPELINE TIME (Build & Test Gate)                     │
│ - SAST (Static Application Security Testing): Semgrep/CodeQL│
│ - SCA (Software Composition Analysis): OWASP Dependency-Check│
│ - Container Scanning: Trivy / Grype                         │
│ - IaC Scanning: Checkov / tfsec                             │
├─────────────────────────────────────────────────────────────┤
│ 3. REGISTRY TIME (Artifact Storage)                         │
│ - Continuous asynchronous CVE scanning of stored images     │
│ - Cryptographic image signing & attestation (Cosign)        │
├─────────────────────────────────────────────────────────────┤
│ 4. DEPLOY TIME (Admission Control)                          │
│ - Kyverno / OPA: Block unsigned images or high CVEs         │
├─────────────────────────────────────────────────────────────┤
│ 5. RUNTIME (Production Operation)                           │
│ - DAST (Dynamic Application Security Testing): OWASP ZAP    │
│ - Runtime threat detection: Falco kernel eBPF monitoring    │
└─────────────────────────────────────────────────────────────┘
```

## 2. Risk-Based Security Gates (Avoiding Developer Paralysis)
- **Anti-Pattern**: "Block every PR that contains any CVE." This paralyzes delivery because thousands of low/medium vulnerabilities exist in upstream libraries that cannot be remediated immediately.
- **Architectural Policy**:
  - **Critical / High with Known Exploits (EPSS > 0.5)**: Hard build failure (`exit 1`).
  - **Medium / Low without Exploits**: Soft warning with 30-day Jira remediation ticket automatically filed.

## Related Resources
- [Software Supply Chain](../software-supply-chain/README.md)
- [Secrets Management](../secrets-management/README.md)
- [Security Architecture](../../10-security/README.md)
