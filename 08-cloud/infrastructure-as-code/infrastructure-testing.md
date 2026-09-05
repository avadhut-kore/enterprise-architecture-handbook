# Infrastructure Testing: Static Analysis, Unit & Integration Testing

## Executive Summary

Treating infrastructure as software requires applying modern software testing methodologies to cloud infrastructure definitions.

---

## 1. The Infrastructure Testing Pyramid

```mermaid
graph TD
    Static[1. Static Analysis & Linting: tflint, terraform fmt, yamllint - FASTEST / SECONDS]
    Sec[2. Security & Compliance Scanning: Checkov, tfsec, Trivy - SUB-MINUTE]
    Unit[3. Contract Testing: Dry-run Plan Validation against Mock State]
    Integration[4. Integration Testing: Terratest / Ephemeral Sandbox Provision & Destroy - MINUTES]

    Static --> Sec --> Unit --> Integration
```

---

## 2. Integration Testing with Terratest (Go)

- **Terratest**: Automates spinning up real infrastructure in an isolated sandbox cloud account, running HTTP/database health queries to verify functionality, and executing `terraform destroy` upon completion.
- **Enterprise Guardrail**: Run Terratest suites in nightly regression pipelines rather than on every commit to manage cloud sandbox costs.
