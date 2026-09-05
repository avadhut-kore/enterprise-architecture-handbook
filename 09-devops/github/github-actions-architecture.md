# GitHub Actions Architecture & Self-Hosted Runners

GitHub Actions is the default CI/CD orchestration engine for many modern enterprises. Designing an enterprise runner infrastructure is critical for performance, security, and cost.

## 1. Runner Archetypes Comparison

| Dimension | GitHub-Hosted Runners | Self-Hosted Runners (ARC on K8s) |
| :--- | :--- | :--- |
| **Network Access** | Public Internet (Cannot reach private VPCs without reverse proxies). | Native access to private corporate VPCs, databases, and internal registries. |
| **Security Isolation** | Ephemeral, clean VM per job (Zero cross-job pollution). | Ephemeral pods via Actions Runner Controller (ARC); pod recreated after every job. |
| **Cost Profile** | Pay-per-minute consumption pricing (Can be expensive at scale). | Fixed Kubernetes cluster compute cost; significantly cheaper for massive CI volumes. |
| **Hardware Customization** | Standard CPU/RAM tiers. | Custom GPU nodes, ARM64 Graviton instances, and high-memory configurations. |

## 2. Hardening Best Practices
- **Never Run Self-Hosted Runners on Public Repositories**: Untrusted PRs can execute arbitrary code inside internal corporate networks.
- **Pin Action SHAs**: Never use mutable tags like `@v3`; pin to immutable full SHAs (`actions/checkout@b4ffde65f46336ab88eb53be808477a3936bae11`).
- **OIDC Workload Identity**: Use `id-token: write` to exchange short-lived JWTs with AWS STS / GCP / Azure AD for zero-credential deployments.

## Related Resources
- [Branch Protection and Environments](./branch-protection-and-environments.md)
- [Pipeline Security](../ci-cd/pipeline-security/pipeline-security-and-hardening.md)
