# Policy as Code & Automated Guardrails

Policy as Code programmatically verifies that infrastructure, pipelines, and container configurations adhere to enterprise security and architectural standards before deployment.

## 1. The Policy Enforcement Spectrum

```
┌─────────────────────────────────────────────────────────────┐
│ 1. PRE-COMMIT & CI TIME (Static Shift-Left)                 │
│ - Checkov / tfsec: Scans Terraform manifests in PRs         │
│ - Conftest / OPA: Verifies JSON/YAML configs against Rego   │
├─────────────────────────────────────────────────────────────┤
│ 2. ADMISSION CONTROL TIME (Cluster Boundary Gate)           │
│ - OPA Gatekeeper / Kyverno: Validates K8s API requests      │
│ - Rejects pods running as root or pulling from untrusted hub│
├─────────────────────────────────────────────────────────────┤
│ 3. RUNTIME AUDIT (Continuous Verification)                  │
│ - Falco: Detects anomalous kernel syscalls in running pods  │
└─────────────────────────────────────────────────────────────┘
```

## 2. Concrete Enterprise Guardrail Examples
- `Rule 1`: No S3 bucket can be created without SSE-KMS encryption and public access block enabled.
- `Rule 2`: No container can run with `securityContext.privileged: true`.
- `Rule 3`: All cloud resources must have mandatory tags: `Owner`, `Environment`, `CostCenter`.

## Related Resources
- [DevSecOps Architecture](../devsecops/README.md)
- [Terraform Governance](../terraform/terraform-enterprise-governance.md)
