# DevOps in Regulated Environments (SOC2, PCI-DSS, HIPAA, DORA)

Operating continuous delivery in banking, healthcare, and critical infrastructure without violating regulatory mandates.

## 1. Key Regulatory Pillars & Automated Evidence

| Regulation | Mandatory Control | Modern Automated DevOps Architecture |
| :--- | :--- | :--- |
| **SOC 2 Type II** | Separation of Duties | Developer who authors a PR cannot approve their own PR (enforced by branch rulesets). |
| **PCI-DSS v4.0** | Vulnerability remediation & MFA | Automated SCA scanning in CI; multi-factor authentication for all platform access. |
| **HIPAA** | Cryptographic audit logs | All deployment and access events streamed to WORM immutable storage. |
| **DORA (EU Banking)**| Operational resilience & DR | Automated cross-region failover testing and disaster recovery metrics. |

## 2. Compliance as Code
Compliance is not a binder of paper screenshots reviewed by auditors once a year. In modern DevOps, compliance is continuous: every Git commit, build log, security scan, and deployment approval is cryptographically logged and exportable via automated compliance APIs.

## Related Resources
- [Pipeline Governance](../ci-cd/pipeline-governance/pipeline-governance-and-standards.md)
- [Regulated Enterprise Architecture](../../10-architect-mastery/regulated-enterprise/README.md)
