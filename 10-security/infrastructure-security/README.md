# Infrastructure Security Architecture (`infrastructure-security/`)

## Executive Summary

Infrastructure security enforces deterministic configuration baselines, automated policy scanning across Infrastructure as Code (IaC), and zero standing administrative access across servers, hypervisors, and cloud fabrics.

---

## Key Guides in this Directory

| Guide | Scope | Core Focus |
| :--- | :--- | :--- |
| [`infrastructure-hardening-baselines.md`](infrastructure-hardening-baselines.md) | OS Hardening | CIS Benchmarks, immutable golden images, HashiCorp Packer |
| [`iac-security-scanning.md`](iac-security-scanning.md) | Shift-Left IaC | Checkov, tfsec, Terrascan in CI/CD pipelines |
| [`policy-as-code-infrastructure.md`](policy-as-code-infrastructure.md) | Policy Governance | OPA Conftest, HashiCorp Sentinel guardrails |
| [`bastion-hosts-and-zero-standing-access.md`](bastion-hosts-and-zero-standing-access.md) | Admin Access | AWS SSM Session Manager, Teleport, boundary proxies |
