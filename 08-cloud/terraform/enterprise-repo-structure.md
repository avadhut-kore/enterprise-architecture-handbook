# Enterprise Terraform Repository Structure

## Executive Summary

The directory layout of enterprise Terraform codebases dictates team blast radius, deployment velocity, and blast radius isolation.

---

## 1. Recommended Enterprise Directory Blueprint

```text
terraform-enterprise/
├── modules/                         # Shared, versioned child modules
│   ├── networking/
│   │   ├── main.tf
│   │   ├── variables.tf
│   │   └── outputs.tf
│   ├── compute-eks/
│   └── database-aurora/
│
└── live/                            # Root execution environments
    ├── core-shared/                 # Transit gateway, centralized logging
    │   ├── main.tf
    │   └── backend.tf
    ├── dev/
    │   ├── networking/
    │   ├── compute/
    │   └── data/
    └── prod/
        ├── networking/
        ├── compute/
        └── data/
```

---

## 2. Why Monolithic State Files Are Prohibited
- Packing networking, compute, and databases into a single `main.tf` creates a single massive state file.
- Running `terraform apply` on a 5,000-resource state takes 45 minutes of API querying and creates a catastrophic blast radius: a typo in an IAM policy could destroy the production database.
- **Rule**: Deconstruct environments into distinct functional stacks (Networking $\rightarrow$ Compute $\rightarrow$ Data) with independent remote state backends.
