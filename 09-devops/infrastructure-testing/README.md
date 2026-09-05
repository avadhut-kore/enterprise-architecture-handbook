# Infrastructure Testing & Validation

Testing infrastructure code is just as vital as testing application software. Untested IaC introduces silent outages and security holes.

## 1. The Infrastructure Testing Pyramid

```
                /  End-to-End & Chaos Tests                 /  (Unannounced DR failover)                 /--------------------------------             /   Integration Tests (Terratest)              /  (Spin up real AWS infra & assert)            /--------------------------------------          /     Static Linting & Security Scans             /     (tflint, checkov, terraform validate)        /--------------------------------------------```

## 2. Terratest in Practice (Go)
- Terratest compiles Go code that provisions real cloud resources via Terraform, asserts HTTP/network reachability, and calls `terraform destroy` during cleanup.

## Related Resources
- [Infrastructure as Code Hub](../infrastructure-as-code/README.md)
- [Policy as Code](../policy-as-code/README.md)
