# Terraform Enterprise Architecture

This module establishes architecture standards for Terraform providers, state management, module design, multi-account governance, and CI/CD execution.

## Contents

- [Terraform Architecture and State Management](./terraform-architecture-and-state-management.md) — Providers, state file security, remote locking (S3/DynamoDB), workspaces, and blast radius reduction.
- [Terraform Enterprise Governance](./terraform-enterprise-governance.md) — Module registries, landing zones, tagging standards, cost allocation, and drift detection automation.

## Core Rule
Never store Terraform state locally or in Git. State files contain sensitive plaintext credentials and must be stored in encrypted remote backends with strict IAM locks.
