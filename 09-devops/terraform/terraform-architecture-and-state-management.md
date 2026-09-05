# Terraform Architecture and State Management

Terraform relies on state files to map declarative resource definitions to real-world cloud API entities. State management is the single most critical architectural concern in Terraform.

## 1. State Storage & Locking Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                TERRAFORM CI/CD EXECUTION                    │
│           (GitHub Actions / Terraform Cloud)                │
└──────────────────────────────┬──────────────────────────────┘
                               │
            ┌──────────────────┴──────────────────┐
            │ 1. Acquire Distributed Mutex Lock   │
            ▼                                     ▼
┌──────────────────────────────┐       ┌──────────────────────┐
│ AWS DYNAMODB LOCK TABLE      │       │ S3 ENCRYPTED BUCKET  │
│ (Prevents concurrent applies)│       │ (Encrypted with KMS, │
│                              │       │  versioning enabled) │
└──────────────────────────────┘       └──────────────────────┘
```

## 2. Reducing State Blast Radius
- **Anti-Pattern**: Storing an entire enterprise datacenter or AWS account in a single `terraform.tfstate` file. An apply error or corrupted state locks out the entire organization.
- **Architectural Solution**: Decompose state by Lifecycle and Blast Radius:
  - `01-networking/` (VPCs, Subnets, Transit Gateways — Changes quarterly)
  - `02-data/` (RDS, Kafka, OpenSearch — Changes monthly)
  - `03-compute/` (EKS Clusters, AutoScaling Groups — Changes weekly)
  - `04-apps/` (Service-specific IAM, SQS queues — Changes daily)

## Related Resources
- [Terraform Enterprise Governance](./terraform-enterprise-governance.md)
- [Infrastructure as Code](../infrastructure-as-code/README.md)
