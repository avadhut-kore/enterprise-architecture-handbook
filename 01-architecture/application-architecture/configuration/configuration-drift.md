# Configuration Drift Detection & Prevention

## 1. Root Causes
Drift occurs when operators make manual hotfix changes directly in cloud portals or container shells without updating source Git repositories.

## 2. Mitigations
- Enforce strict read-only production environments.
- Use Infrastructure-as-Code (Terraform) drift detection in scheduled CI pipelines.
