# Pipeline Security and Hardening

The CI/CD pipeline is the most privileged execution environment in an enterprise. A compromised pipeline grants attackers direct production write access.

## 1. The Threat Matrix

| Threat Vector | Attack Mechanism | Architectural Defense |
| :--- | :--- | :--- |
| **Poisoned Pipeline Execution (PPE)** | Attacker modifies `.github/workflows/ci.yml` in a PR to exfiltrate production secrets. | Require approval for PR workflows from first-time contributors; isolate environment secrets to protected branches. |
| **Supply Chain Dependency Injection** | Attacker publishes malicious typosquatted package into npm/PyPI. | Use strict lockfiles (`package-lock.json`), private caching proxy (Artifactory), and automated SCA scanners. |
| **Compromised Runner Host** | Persistent runner disk stores uncleaned credentials from previous jobs. | Use strictly ephemeral runners (ARC on Kubernetes) that terminate and re-create after each job. |
| **Long-Lived Credential Leak** | AWS IAM Access Keys stored in repository secrets are dumped to build logs. | Enforce OIDC federated authentication; eliminate all permanent static access keys. |

## 2. OIDC Token Exchange Architecture
```
[GitHub Actions Runner] ──► Request OIDC JWT from GitHub Token Authority
                                      │
                                      ▼
[Cloud Provider (AWS/Azure/GCP)] ◄── Exchange JWT for Short-Lived Ephemeral Token (15 min)
```

## Related Resources
- [Secrets Management](../../secrets-management/README.md)
- [Software Supply Chain](../../software-supply-chain/README.md)
