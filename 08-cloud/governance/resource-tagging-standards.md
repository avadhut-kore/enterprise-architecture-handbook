# Enterprise Resource Tagging & Metadata Standards

## Executive Summary

Without consistent resource tagging, FinOps cost allocation, security ownership attribution, and automated patching are impossible.

---

## 1. The Four Mandatory Tag Categories

| Tag Key | Example Values | Enforcement Mechanism | Purpose |
| :--- | :--- | :--- | :--- |
| **`Environment`** | `production`, `staging`, `dev` | SCP / Azure Policy Deny | Isolates production resources; drives patching cycles |
| **`CostCenter`** | `cc-finance-402`, `cc-retail-108` | Automated CI/CD Linting | Allocates cloud invoices back to business unit P&Ls |
| **`OwnerEmail`** | `sre-payments@company.com` | SCP / Azure Policy Deny | Identifies on-call owner for security incident alerts |
| **`DataClassification`**| `public`, `internal`, `confidential`, `restricted`| Automated Policy Block | Restricts automated backups and encryption standards |

---

## 2. Programmatic Tag Enforcement (SCP)
```json
{
  "Effect": "Deny",
  "Action": ["ec2:RunInstances", "rds:CreateDBInstance", "s3:CreateBucket"],
  "Resource": "*",
  "Condition": {
    "Null": {
      "aws:RequestTag/CostCenter": "true",
      "aws:RequestTag/Environment": "true"
    }
  }
}
```
*Any attempt to provision a resource without mandatory tags is immediately rejected at the cloud API level.*
