# Enterprise Cloud Architecture Anti-Patterns

## Executive Summary

This section documents the most pervasive and damaging architectural anti-patterns observed in enterprise cloud implementations. Each anti-pattern provides root-cause analysis, business impact, and actionable remediation runbooks.

---

## The Catalog of Cloud Anti-Patterns

| Anti-Pattern | Core Manifestation | Primary Risk & Impact |
| :--- | :--- | :--- |
| **[Kubernetes Everywhere](kubernetes-everywhere.md)** | Mandating K8s for simple websites and APIs | Crippling operational complexity, cognitive burnout, high SRE costs |
| **[Blind Multi-Cloud](blind-multi-cloud.md)** | Multi-cloud without business justification | Lowest common denominator, high egress fees, split-brain outages |
| **[Single-Region Critical Workloads](single-region-critical-workloads.md)**| Tier-1 core banking deployed to 1 region | Catastrophic business failure during regional datacenter outages |
| **[Public Cloud Databases](public-cloud-databases.md)** | RDS/Cosmos DB assigned public IP addresses | Immediate risk of automated internet brute-force data breaches |
| **[Over-Permissioned IAM](over-permissioned-iam.md)** | Wildcard `*` permissions, shared service keys | Massive lateral movement following a single application compromise |
| **[Snowflake Manual Infrastructure](snowflake-manual-infrastructure.md)**| Hand-crafted console configurations | Irreproducible environments, catastrophic recovery delays |
| **[Lift-and-Shift Forever](lift-and-shift-forever.md)** | Rehosting to VMs without post-migration modernization| Exploding cloud invoices with zero developer agility gains |
| **[Untested Disaster Recovery](untested-disaster-recovery.md)** | Maintaining paper DR plans without game day drills| DR failover fails in production during a real disaster |
| **[No Cost Ownership & Tagging](no-cost-ownership-and-tagging.md)**| Unallocated cloud invoices without cost centers | Uncontrolled budget overruns; tragedy of the commons |
| **[Shared Production Accounts](shared-production-accounts.md)** | Multiple applications sharing 1 cloud account | Enormous blast radius; compliance audit failure |
| **[Secrets in Source Control](secrets-in-source-control.md)** | Hardcoding API keys and passwords in Git | Automated secret scraping and total environment compromise |
| **[Premature Cloud-Native Refactoring](premature-cloud-native-refactoring.md)**| Rewriting stable monoliths into 50 microservices| Distributed transaction failures, team velocity collapse |
