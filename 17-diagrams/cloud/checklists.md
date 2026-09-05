# Enterprise Cloud Architecture Review Checklist

This checklist provides a structured 25-point evaluation for enterprise cloud architectures, multi-account structures, and landing zone governance.

## 1. Multi-Account & Landing Zone Governance
- [ ] Are workloads separated into distinct cloud accounts/subscriptions by environment (Prod, Staging, Dev)?
- [ ] Are centralized Service Control Policies (SCPs) or Azure Policies enforced to prevent risky actions?
- [ ] Is root account access strictly secured with hardware MFA and prohibited from operational usage?
- [ ] Is automated infrastructure provisioning enforced using Infrastructure-as-Code (Terraform / Bicep)?

## 2. Networking, Ingress & Egress
- [ ] Is a centralized Hub-and-Spoke or Transit Gateway topology implemented for network inspection?
- [ ] Are all direct internet egress routes from private subnets routed through NAT gateways or egress firewalls?
- [ ] Are private endpoints (AWS PrivateLink / Azure Private Endpoints) used for cloud PaaS services?
- [ ] Is CIDR IP address allocation planned to prevent overlapping subnets across hybrid on-prem connections?

## 3. Security, Encryption & IAM
- [ ] Is single sign-on (SSO) integrated with the enterprise identity provider using temporary STS credentials?
- [ ] Are all storage volumes, object stores, and databases encrypted at rest using Customer-Managed Keys (KMS)?
- [ ] Are all public S3 buckets / blob containers globally blocked at the organization policy level?
- [ ] Are cloud security posture management (CSPM) and threat detection (GuardDuty / Defender) enabled?

## 4. Cost Optimization & Operability
- [ ] Are mandatory cost allocation tags enforced via policy on all provisioned cloud resources?
- [ ] Are compute savings plans or reserved instances aligned with predictable baseline utilization?
- [ ] Are automated lifecycle management rules configured on object storage to transition cold data to Glacier/Archive?
