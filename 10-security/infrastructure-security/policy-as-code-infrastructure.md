# Policy as Code for Infrastructure Governance

## Executive Summary

Policy as Code (PaC) treats organizational security rules as software, testing Terraform execution plans against programmatic compliance guardrails.

---

## 1. OPA / Conftest Example Rule (Rego)
```rego
package terraform.security

deny[msg] {
    resource := input.resource_changes[_]
    resource.type == "aws_s3_bucket"
    not resource.change.after.server_side_encryption_configuration
    msg := sprintf("S3 Bucket '%v' must have server-side encryption enabled.", [resource.address])
}
```
