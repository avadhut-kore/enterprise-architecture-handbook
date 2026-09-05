# Cloud Shared Responsibility Model Deep Dive

## Executive Summary

Understanding the boundary between the Cloud Service Provider (CSP) and the Customer is essential for audit attestation and security control implementation.

---

## Responsibility Matrix Across Service Models

| Layer | On-Premises | IaaS (EC2/VMs) | CaaS (EKS/AKS) | PaaS (App Services) | Serverless (Lambda) | SaaS (Salesforce) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Data & Classification** | Customer | Customer | Customer | Customer | Customer | Customer |
| **Identity & IAM** | Customer | Customer | Customer | Customer | Customer | Customer |
| **Application Code** | Customer | Customer | Customer | Customer | Customer | CSP |
| **Container Runtime** | Customer | Customer | Customer | CSP | CSP | CSP |
| **Operating System** | Customer | Customer | CSP (Managed) | CSP | CSP | CSP |
| **Virtualization / Hypervisor**| Customer | CSP | CSP | CSP | CSP | CSP |
| **Physical Datacenter** | Customer | CSP | CSP | CSP | CSP | CSP |
