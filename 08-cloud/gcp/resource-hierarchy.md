# GCP Resource Hierarchy: Organizations, Folders & Projects

## Executive Summary

Google Cloud organizes all resources in a strict tree hierarchy: **Organization $\rightarrow$ Folders $\rightarrow$ Projects $\rightarrow$ Resources**. In enterprise GCP architecture, the **Project** is the fundamental boundary for billing, IAM permissions, network attachment, and quota allocation.

---

## 1. Enterprise Resource Hierarchy Blueprint

```mermaid
graph TD
    Org[Organization: company.com] --> CoreFolder[Folder: Core Infrastructure]
    Org --> BU1[Folder: Retail Banking]
    Org --> BU2[Folder: Wealth Management]

    CoreFolder --> NetProj[Project: Shared VPC Host Prod]
    CoreFolder --> SecProj[Project: Central Security & SIEM]
    CoreFolder --> LogProj[Project: Central Log Sink]

    BU1 --> BU1Prod[Folder: Production]
    BU1 --> BU1NonProd[Folder: Non-Production]

    BU1Prod --> App1Proj[Project: Payments Service Prod]
    BU1Prod --> App2Proj[Project: Account Service Prod]
```

---

## 2. Inheritance & Policy Architecture

- **IAM Policy Inheritance**: IAM permissions flow strictly downwards. An IAM binding applied at the Organization or Folder level cannot be revoked at the Project level.
- **Organization Policy Service**: Enforce guardrails across the entire tree:
  - `constraints/compute.restrictPublicIp`: Denies public IP allocation across all VM instances.
  - `constraints/gcp.resourceLocations`: Restricts resource creation to approved geographic boundaries (e.g., `in:eu-locations` for GDPR).
  - `constraints/iam.disableServiceAccountKeyCreation`: Prohibits downloading exported JSON service account keys.
