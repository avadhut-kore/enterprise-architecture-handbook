# Infrastructure as Code (IaC) Architecture

Infrastructure as Code treats infrastructure specifications as software: version-controlled, modular, testable, and automated.

## 1. Core IaC Paradigms

```
┌─────────────────────────────────────────────────────────────┐
│ DECLARATIVE (What you want) vs IMPERATIVE (How to build it) │
├──────────────────────────────┬──────────────────────────────┤
│ DECLARATIVE (Terraform, K8s) │ IMPERATIVE (Bash, AWS CLI)   │
│ - Specify target end state   │ - Specify sequence of steps  │
│ - Idempotent by design       │ - Must manage error states   │
│ - Engine handles state diff  │ - Hard to rollback cleanly   │
└──────────────────────────────┴──────────────────────────────┘
```

## 2. The Four Pillars of Enterprise IaC
1. **Idempotency**: Running the same IaC code multiple times produces the exact same target state with zero unintended changes.
2. **Immutability**: Avoid modifying existing running servers in-place. Replace them with newly provisioned, tested instances.
3. **Automated State Tracking**: Maintain a single cryptographic record of real-world infrastructure mappings.
4. **Policy-as-Code Guardrails**: Enforce enterprise security rules (no unencrypted storage, no 0.0.0.0/0 security groups) prior to execution.

## Related Resources
- [Terraform Architecture](../terraform/README.md)
- [Ansible Architecture](../ansible/README.md)
- [Policy as Code](../policy-as-code/README.md)
