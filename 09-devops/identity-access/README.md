# Identity & Access Management in DevOps

Modern DevOps architectures eliminate long-lived static credentials in favor of short-lived federated workload identities.

## 1. Workload Identity Federation (OIDC)

```
[CI Runner (GitHub Actions)]
            │
            ▼ 1. Presents Signed OpenID Connect (OIDC) JWT Token
[Cloud IAM (AWS IAM Role / Azure Managed Identity / GCP Workload Identity)]
            │
            ▼ 2. Validates JWT Signature & Repository Claims:
                 `repo:org/billing-service:ref:refs/heads/main`
            │
            ▼ 3. Issues Temporary STS Session Token (Valid for 15 minutes)
[CI Runner Executes Deployment with Zero Static Secrets!]
```

## 2. Least Privilege & Break-Glass Access
- CI/CD runners only hold deployment rights for their specific application namespace.
- Human engineers have zero direct write access to production clusters. Break-glass emergency access requires dual-authorization and triggers automatic session recording.

## Related Resources
- [Pipeline Security](../ci-cd/pipeline-security/pipeline-security-and-hardening.md)
- [Security Architecture](../../10-security/README.md)
