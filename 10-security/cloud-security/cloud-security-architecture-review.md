# Cloud Security Architecture Review Specification

## Executive Summary

This formal review gate must be completed and ratified by the Cloud Security Architect before any workload deploys to enterprise cloud production.

---

## Review Gate Evaluation Categories

### 1. Identity & Access Guardrails
- [ ] Root accounts locked with hardware FIDO2 keys; zero standing root API keys.
- [ ] Workload Identity Federation (EKS Pod Identity / Azure Workload Identity) used for 100% of compute pods.
- [ ] Service Control Policies (SCPs) enforce preventative guardrails across all accounts.

### 2. Network Isolation & Perimeter
- [ ] Zero databases, caches, or internal APIs assigned public IP addresses.
- [ ] Centralized inspection VPC handles all outbound internet egress via next-gen firewalls.
- [ ] PrivateLink / VPC Endpoints used for all cloud service interactions (S3, KMS, Secrets Manager).

### 3. Data Protection & Cryptography
- [ ] 100% of block storage volumes (EBS) encrypted by default with KMS CMKs.
- [ ] Database backups replicated to a secondary isolated region with immutable WORM locks.
- [ ] Key rotation automated every 365 days via KMS.
