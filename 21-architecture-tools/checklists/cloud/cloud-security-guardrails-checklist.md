# Cloud Security Guardrails Checklist

- [ ] Account-level S3 Block Public Access enforced via SCP across all workload accounts.
- [ ] Default-deny NetworkPolicies and Pod Security Standards (`restricted`) enforced on all Kubernetes clusters.
- [ ] Pre-commit secret scanning (Trufflehog / Gitleaks) integrated into all developer workflows.
- [ ] Agentless Cloud Security Posture Management (CSPM) active with automated remediation for open security groups.
- [ ] Interactive administrative access governed by Just-in-Time (JIT) Privileged Identity Management (PIM).
