# Infrastructure as Code (IaC) Security Scanning

## Executive Summary

IaC security scanners (Checkov, tfsec) evaluate Terraform, CloudFormation, and Bicep code during pull requests to detect misconfigurations before cloud resources are provisioned.

---

## 1. High-Impact IaC Blocking Rules
- Block security group ingress allowing `0.0.0.0/0` on ports other than 80/443.
- Block S3 bucket creation without server-side encryption or public access blocks.
- Block database creation without multi-AZ replication or automated backups.
- Block unencrypted EBS, EFS, or Managed Disk volumes.
