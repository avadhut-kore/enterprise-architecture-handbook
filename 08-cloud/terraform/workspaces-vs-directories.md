# Terraform Workspaces vs Directory-per-Environment

## Executive Summary

Terraform natively supports "Workspaces" to share identical code across environments. In enterprise production architecture, **Directory-per-Environment is the required standard**.

---

## 1. Workspaces vs Directory-per-Environment Comparison

| Dimension | Terraform Workspaces | Directory-per-Environment |
| :--- | :--- | :--- |
| **Code Structure** | Single codebase; state partitioned by workspace name (`dev`, `prod`). | Independent directory hierarchies (`live/dev`, `live/prod`). |
| **Backend Isolation** | Single shared backend bucket. | **Dedicated isolated backend per environment / cloud account.** |
| **Blast Radius** | High: An accidental `terraform destroy` in the wrong workspace destroys prod. | **Low: Zero possibility of impacting prod from dev directory.** |
| **Version Drift** | Impossible to test new module versions in dev without impacting prod. | **Trivial: Dev can pin module v2.0 while Prod remains pinned to v1.4.** |
| **Enterprise Verdict** | **PROHIBITED FOR PRODUCTION** | **MANDATORY ENTERPRISE STANDARD** |
